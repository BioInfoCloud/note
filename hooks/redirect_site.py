# -*- coding: utf-8 -*-
"""MkDocs 钩子：构建完成后，为旧地址生成跳转页（meta refresh + JS），

保证目录/文件从中文改名为英文后，老书签与外部链接仍然可访问。

映射表见同目录 redirects.json：
    "旧站点内路径/目录": "新站点内路径/目录"
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MAP_FILE = os.path.join(HERE, "redirects.json")

TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>页面已迁移</title>
<link rel="canonical" href="{target}">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}" + location.hash);</script>
<style>
  body {{ font-family: -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif;
         display: flex; align-items: center; justify-content: center;
         min-height: 80vh; margin: 0; color: #33475b; background: #f7fafc; }}
  .box {{ text-align: center; line-height: 1.9; }}
  a {{ color: #0b7285; }}
</style>
</head>
<body>
<div class="box">
  <p>本页已迁移到新地址，正在跳转…</p>
  <p><a href="{target}">{target}</a></p>
</div>
</body>
</html>
"""


def on_post_build(config, **kwargs):
    if not os.path.isfile(MAP_FILE):
        return
    with open(MAP_FILE, encoding="utf-8") as f:
        mapping = json.load(f)

    site_dir = config["site_dir"]
    written = 0
    for old, new in mapping.items():
        old = old.strip("/")
        new = new.strip("/")
        if not old:
            continue
        # 从 旧目录/index.html 回推到站点根，再进入新目录 —— 与部署路径无关
        depth = old.count("/") + 1
        target = "../" * depth + (new + "/" if new else "")
        html = TEMPLATE.format(target=target)
        out = os.path.join(site_dir, old.replace("/", os.sep), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        written += 1
    print("redirects: 已生成 %d 个旧地址跳转页" % written)
