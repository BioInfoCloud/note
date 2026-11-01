import os, re

DOCS = r"E:\BaiduSyncdisk\00-gitHubProjects\MyProjects\note\docs"
ASSET_DIRS = {'img', 'media', 'images', 'assets'}  # 资源目录，不进入导航

TABS = [
  ('导读与基础', ['导读与基础', '生物学基础', '生信基础']),
  ('生信编程', ['Programming', '生信编程', 'BioInfo/Biopython']),
  ('组学数据分析', ['组学分析', 'BioInfo/scRNAseq', 'BioInfo/RNAseq']),
  ('数据库与数据挖掘', ['数据库挖掘', 'BioInfo/TCGA', 'BioInfo/database', 'BioInfo/drugAna', 'BioInfo/immune', 'BioInfo/toolsandsoftware']),
  ('机器学习与深度学习', ['机器学习', '深度学习', 'ML']),
  ('网络药理学', ['网络药理学']),
  ('智能体', ['智能体']),
  ('可视化', ['visualization']),
  ('文献', ['Literature']),
  ('资源', ['资源', 'WeChatOfficialAccount', 'ABOUT', 'package']),
]

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
            title = page_title(os.path.join(ep, 'index.md')) or e
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
            title = page_title(os.path.join(DOCS, f, 'index.md')) or f.split('/')[-1]
            tab_items.append({title: si})
    nav_lines.append(f"  - {tab_name}:")
    nav_lines.append(fmt(tab_items, "    "))

print("nav:\n" + "\n".join(nav_lines))
