from yapf.yapflib.yapf_api import FormatCode
from github import Github
import sys
import re
import base64

ACCESS_TOKEN = []
REPO_NAME = []
WORKING_PATH = []
ACCESS_TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]
WORKING_PATH = sys.argv[3]

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
contents = repo.get_contents(WORKING_PATH)

pyscripts = []
for content_file in contents:
    if re.search(r'.py$', content_file.name) is not None:
        pyscripts.append(content_file)

for pyscript in pyscripts:
    py_content = repo.get_contents(pyscript.path).content
    py_content = base64.b64decode(py_content).decode('utf-8')
    py_content = FormatCode(py_content)
    if py_content[1]:
        message = ("style(" + pyscript.name + "): format "
                   "python script with yapf")
        repo.update_file(pyscript.path, message, py_content[0], pyscript.sha)
