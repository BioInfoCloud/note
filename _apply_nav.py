import io

mk_path = r"E:\BaiduSyncdisk\00-gitHubProjects\MyProjects\note\mkdocs.yml"
nav_path = r"E:\BaiduSyncdisk\00-gitHubProjects\MyProjects\note\_nav_out.txt"

mk = open(mk_path, encoding='utf-8').read()
nav = open(nav_path, encoding='utf-8').read().rstrip('\n')

start = mk.index('\nnav:')
end_marker = '\n# [Extensions]'
end = mk.index(end_marker)

new_mk = mk[:start + 1] + nav + '\n' + mk[end:]
open(mk_path, 'w', encoding='utf-8').write(new_mk)
print("Replaced nav section. start=%d end=%d new_len=%d" % (start, end, len(new_mk)))
