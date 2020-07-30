from github import Github
import sys
import base64

ACCESS_TOKEN = ''
REPO_NAME = ''
ACCESS_TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

contents = repo.get_contents("/README.md")
contents_bkp = repo.get_contents("/docs/README.md")
base = contents.content
base = base.replace('\n', '')
text = base64.b64decode(base).decode('utf-8')

base_bkp = contents_bkp.content
base_bkp = base_bkp.replace('\n', '')
text_bkp = base64.b64decode(base_bkp).decode('utf-8')
if text != text_bkp:
    repo.update_file(contents_bkp.path,
                     "docs(README): synchronize README files", text,
                     contents_bkp.sha)
else:
    pass
