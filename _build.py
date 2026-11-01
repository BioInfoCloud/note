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

if os.path.exists(TMP):
    shutil.rmtree(TMP)
shutil.copytree(DOCS, TMP, ignore=ignore)
print("Clean docs copied to", TMP)

with open(os.path.join(ROOT, "mkdocs.yml"), encoding="utf-8") as f:
    cfg = f.read()
# 插入 docs_dir 指向干净副本（绝对路径，正斜杠）
cfg = "docs_dir: " + TMP.replace("\\", "/") + "\n" + cfg
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
