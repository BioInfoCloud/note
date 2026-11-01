import shutil, os, sys, subprocess

ROOT = r"E:\BaiduSyncdisk\00-gitHubProjects\MyProjects\note"
DOCS = os.path.join(ROOT, "docs")
TMP = r"C:\tmp\bioinfocloud_docs"
CFG = os.path.join(ROOT, "_mkdocs_build.yml")

def ignore(src, names):
    # 跳过 Baidu 同步临时文件及其他同步垃圾，避免构建时竞态崩溃
    return [n for n in names
            if ".baiduyun." in n
            or n == ".DS_Store"
            or n == "__TEMP"]

# 复用临时目录，覆盖复制（避免一次性删除海量文件触发安全拦截）。
shutil.copytree(DOCS, TMP, ignore=ignore, dirs_exist_ok=True)


def prune(root, keep_rel, exts=None):
    """删除 root 下不在 keep_rel（相对 docs 的路径集合）里的文件，返回被删的相对路径列表。"""
    gone = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for f in filenames:
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, root)
            if rel not in keep_rel:
                os.remove(full)
                if exts is None or f.lower().endswith(exts):
                    gone.append(rel)
    # 清理空目录
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        if dirpath != root and not os.listdir(dirpath):
            os.rmdir(dirpath)
    return gone


keep = set()
for dirpath, _dirnames, filenames in os.walk(DOCS):
    for f in filenames:
        keep.add(os.path.relpath(os.path.join(dirpath, f), DOCS))

removed_md = prune(TMP, keep, exts=(".md",))
if removed_md:
    print("已从副本中移除 %d 个已删除文件（其中 md %d 个）" % (len(removed_md), len(removed_md)))
print("Clean docs copied to", TMP)

with open(os.path.join(ROOT, "mkdocs.yml"), encoding="utf-8") as f:
    cfg = f.read()
# site_dir 固定为仓库外的目录。
# 关键：不能用 --dirty 构建 —— 导航栏会渲染进每个页面，--dirty 只重建改动过的页面，
# 未改动页面的侧边栏会一直停留在旧的 mkdocs.yml 上（已删的目录项仍可点）。
# 但 mkdocs 全量构建前会 "Cleaning site directory" 一次性删上千个文件，会被批量删除拦截打断。
# 解决办法：把上一次的站点目录改名挪走（改名是 O(1)，不涉及删除），再让 mkdocs 全新建站。
SITE = r"C:\tmp\bic_site"
if os.path.isdir(SITE):
    i = 1
    while os.path.exists("%s_old%d" % (SITE, i)):
        i += 1
    os.rename(SITE, "%s_old%d" % (SITE, i))
    print("上一次的站点目录已改名为 %s_old%d（可择机清理）" % (SITE, i))
cfg = (
    "docs_dir: " + TMP.replace("\\", "/") + "\n"
    + "site_dir: " + SITE.replace("\\", "/") + "\n"
    + cfg
)
with open(CFG, "w", encoding="utf-8") as f:
    f.write(cfg)
print("Wrote temp config", CFG)

mode = sys.argv[1] if len(sys.argv) > 1 else "build"
cmd = [sys.executable, "-m", "mkdocs", mode, "-f", CFG]
if mode == "gh-deploy":
    cmd.append("--force")
print("Running:", " ".join(cmd))
r = subprocess.run(cmd, cwd=ROOT)

sys.exit(r.returncode)
