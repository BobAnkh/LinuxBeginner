from github import Github
import sys
ACCESS_TOKEN = ''
REPO_NAME = ''
PROJECT_NAME = ''
COLUMN_NAME = ''
ACCESS_TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]
PROJECT_NAME = sys.argv[3]
COLUMN_NAME = sys.argv[4]


g=Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
projects = repo.get_projects()
pulls = repo.get_pulls(state='open', sort='created')

for project in projects:
    if project.name == PROJECT_NAME:
        columns = project.get_columns()

for pr in pulls:
    id = pr.id
    already_have_it = 0
    for column in columns:
        cards = column.get_cards()
        for card in cards: 
            if pr.issue_url == card.content_url:
                print('PR', pr.number, 'is already in column', column.name)
                already_have_it = 1
                break
        if already_have_it == 1:
            break
    if already_have_it == 0:
        for column in columns:
            if column.name == COLUMN_NAME:
                column.create_card(content_id=id, content_type='PullRequest')
                print('Add PR', pr.number, 'to column', COLUMN_NAME)
