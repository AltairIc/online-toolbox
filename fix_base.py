import re
with open(r'C:\Users\Altair\Documents\Codex\2026-07-27\ban\outputs\toolsite\app\templates\base.html', 'r', encoding='utf-8') as f:
    content = f.read()
first_head_end = content.find('</head>')
first_body = content.find('<body', first_head_end)
first_main_end = content.find('main>', first_body) + 5
footer_start = content.find('{% block scripts %}')
head = content[:first_head_end + 7]
body_header = content[first_body:first_main_end]
rest = content[first_main_end:footer_start]
new = head + '\n' + body_header + rest + '\n    {% block scripts %}{% endblock %}\n'
print('Base content rebuilt:', len(new))
with open(r'C:\Users\Altair\Documents\Codex\2026-07-27\ban\outputs\toolsite\app\templates\base.html', 'w', encoding='utf-8') as f:
    f.write(new)
print('Written')
