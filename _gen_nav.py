import os, re

DOCS = r"E:\BaiduSyncdisk\00-gitHubProjects\MyProjects\note\docs"
ASSET_DIRS = {'img', 'media', 'images', 'assets'}  # 资源目录，不进入导航

TABS = [
  ('导读与基础', ['getting-started', 'biology', 'bioinformatics-basics']),
  ('生信编程', ['Programming', 'bioinformatics-programming', 'BioInfo/Biopython']),
  ('组学数据分析', ['omics-analysis', 'BioInfo/scRNAseq', 'BioInfo/RNAseq']),
  ('数据库与数据挖掘', ['database-mining', 'BioInfo/TCGA', 'BioInfo/database', 'BioInfo/drugAna', 'BioInfo/immune', 'BioInfo/toolsandsoftware']),
  ('机器学习与深度学习', ['machine-learning', 'deep-learning', 'ML']),
  ('网络药理学', ['network-pharmacology']),
  ('智能体', ['ai-agents']),
  ('可视化', ['visualization']),
  ('文献', ['Literature']),
  ('资源', ['resources', 'WeChatOfficialAccount', 'ABOUT', 'package']),
]

# 目录名 -> 导航里显示的中文分组名（目录已改为英文，但侧边栏要给中文）
LABELS = {
    'Programming/python': 'Python',
    'Programming/python/Matplotlib_visualization': 'Matplotlib 可视化',
    'Programming/vscode-python': 'VSCode 与 Python',
    'BioInfo/scRNAseq': '单细胞（scRNA-seq）',
    'BioInfo/RNAseq': '转录组（RNA-seq）',
    'BioInfo/TCGA': 'TCGA 与 GEO',
    'BioInfo/database': '数据库',
    'BioInfo/drugAna': '药物分析',
    'BioInfo/immune': '免疫分析',
    'BioInfo/toolsandsoftware': '工具与软件',
    'ML': '机器学习',
    'ML/LOGISTIC_REGRESSION': '逻辑回归',
    'ML/knn': 'kNN',
    'ML/knn/knn_py': 'kNN 的 Python 实现',
    'Literature/AI': 'AI 与大模型',
    'Literature/Review': '文献精读',
    'Literature/Ubiquitination': '泛素化',
    'Literature/scRNAseq': '单细胞文献',
    'resources': '站点与前端',
    'WeChatOfficialAccount': '公众号',
    'ABOUT': '关于本站',
    'package': 'R 包文档',
}


def page_title(md_path):
    try:
        t = open(md_path, encoding='utf-8', errors='ignore').read()
    except:
        return None
    m = re.match(r'^---\s*\n(.*?)\n---', t, re.S)
    if m:
        mm = re.search(r'title:\s*(.+)', m.group(1))
        if mm:
            return mm.group(1).strip().strip('"\'')
    m2 = re.search(r'^#\s+(.+)', t, re.M)
    if m2:
        return m2.group(1).strip()
    return None

def section_items(folder_rel):
    folder = os.path.join(DOCS, folder_rel)
    if not os.path.isdir(folder):
        return None
    entries = sorted(os.listdir(folder))
    items = []
    if 'index.md' in entries:
        items.append(os.path.join(folder_rel, 'index.md').replace('\\', '/'))
    for e in entries:
        if e == 'index.md' or e in ASSET_DIRS:
            continue
        ep = os.path.join(folder, e)
        if os.path.isdir(ep):
            sub = section_items(os.path.join(folder_rel, e).replace('\\', '/'))
            title = page_title(os.path.join(ep, 'index.md')) or LABELS.get(
                os.path.join(folder_rel, e).replace('\\', '/'), e)
            if sub:
                items.append({title: sub})
        elif e.endswith('.md'):
            items.append(os.path.join(folder_rel, e).replace('\\', '/'))
    return items

def fmt(items, indent):
    lines = []
    for it in items:
        if isinstance(it, dict):
            for k, v in it.items():
                lines.append(f"{indent}- {k}:")
                lines.append(fmt(v, indent + '  '))
        else:
            lines.append(f"{indent}- {it}")
    return "\n".join(lines)

nav_lines = []
for tab_name, folders in TABS:
    tab_items = []
    if len(folders) == 1:
        si = section_items(folders[0])
        if si:
            tab_items = si
    else:
        for f in folders:
            si = section_items(f)
            if not si:
                continue
            title = page_title(os.path.join(DOCS, f, 'index.md')) or LABELS.get(f, f.split('/')[-1])
            tab_items.append({title: si})
    nav_lines.append(f"  - {tab_name}:")
    nav_lines.append(fmt(tab_items, "    "))

print("nav:\n" + "\n".join(nav_lines))
