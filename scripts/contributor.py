from github import Github
import sys
import re
import base64

ACCESS_TOKEN = ''
REPO_NAME = 'BobAnkh/LinuxBeginner'
CONTRIB = '### 贡献者\n\n'
CONTRIB_END = '\n\n## 使用许可'
COLUMN_PER_ROW = 6
ACCESS_TOKEN = sys.argv[1]

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
USER = 0
head = '''<table>
<tr>'''
tail = '''
</tr>
</table>'''

contributors = repo.get_contributors()
for contributor in contributors:
    name = contributor.name
    avatar_url = contributor.avatar_url
    html_url = contributor.html_url
    if re.match('https://github.com/apps/', html_url):
        continue
    if name == None:
        name = html_url[19:]
    if USER >= COLUMN_PER_ROW:
        new_tr = '''\n<tr>\n<tr>'''
        head = head + new_tr
    td = f'''
    <td align="center">
        <a href={html_url}>
            <img src={avatar_url} width="100;" alt={name}/>
            <br />
            <sub style="font-size:14px"><b>{name}</b></sub>
        </a>
    </td>'''
    head = head + td
    USER += 1
head = head + tail

contents = repo.get_contents("/README.md")
contents_bkp = repo.get_contents("/docs/README.md")
base = contents.content
base = base.replace('\n', '')
text = base64.b64decode(base).decode('utf-8')
str = text.split(CONTRIB)
end = str[1].split(CONTRIB_END)
if end[0] != head:
    end[0] = head
    text = str[0] + CONTRIB + end[0] + CONTRIB_END + end[1]
    repo.update_file(contents.path, "docs(contrib): update contributors", text,
                     contents.sha)
    repo.update_file(contents_bkp.path, "docs(contrib): update contributors",
                     text, contents_bkp.sha)
else:
    pass
