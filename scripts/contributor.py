from github import Github
import sys
import re
import base64

ACCESS_TOKEN = ''
REPO_NAME = ''
CONTRIB = ''
COLUMN_PER_ROW = 6
ACCESS_TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]
CONTRIB = sys.argv[3] + '\n\n'
COLUMN_PER_ROW = int(sys.argv[4])

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
        new_tr = '''\n</tr>\n<tr>'''
        head = head + new_tr
        USER = 0
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
if tail in str[1]:
    end = str[1].split(tail)
    end[0] = end[0] + tail
else:
    end = ['', str[1]]

if end[0] != head:
    end[0] = head
    text = str[0] + CONTRIB + end[0] + end[1]
    repo.update_file(contents.path, "docs(contrib): update contributors", text,
                     contents.sha)
    repo.update_file(contents_bkp.path, "docs(contrib): update contributors",
                     text, contents_bkp.sha)
else:
    base_bkp = contents_bkp.content
    base_bkp = base_bkp.replace('\n', '')
    text_bkp = base64.b64decode(base_bkp).decode('utf-8')
    if text != text_bkp:
        repo.update_file(contents_bkp.path,
                         "docs(README): synchronize README files", text,
                         contents_bkp.sha)
    else:
        pass
