#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: BobAnkh
Github: https://github.com/BobAnkh
Date: 2020-07-25 10:50:35
LastEditors: BobAnkh
LastEditTime: 2020-08-02 22:36:19
FilePath: /LinuxBeginner/scripts/auto_project.py
Description: Script to add new pull request to project
Copyright 2020 BobAnkh
'''
import re
import sys

from github import Github

ACCESS_TOKEN = ''
REPO_NAME = 'BobAnkh/LinuxBeginner'
PROJECT_NAME_1 = 'Linux command'
CONDITION_1 = 'LinuxCommand/'
PROJECT_NAME_2 = 'Linux tool'
CONDITION_2 = 'LinuxTool/'
COLUMN_NAME = 'In progress'
ACCESS_TOKEN = sys.argv[1]

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
projects = repo.get_projects()
pulls = repo.get_pulls(state='open', sort='created')

for project in projects:
    if project.name == PROJECT_NAME_1:
        columns_1 = project.get_columns()
        for pr in pulls:
            if not re.match(CONDITION_1, pr.head.ref):
                print(pr.head.ref, 'does not match', CONDITION_1)
                continue
            id = pr.id
            already_have_it = 0
            for column in columns_1:
                cards = column.get_cards()
                for card in cards:
                    if pr.issue_url == card.content_url:
                        print('PR', pr.number, 'is already in', project.name,
                              'column', column.name)
                        already_have_it = 1
                        break
                if already_have_it == 1:
                    break
            if already_have_it == 0:
                for column in columns_1:
                    if column.name == COLUMN_NAME:
                        column.create_card(content_id=id,
                                           content_type='PullRequest')
                        print('Add PR', pr.number, 'to', project.name,
                              'column', COLUMN_NAME)
    elif project.name == PROJECT_NAME_2:
        columns_2 = project.get_columns()
        for pr in pulls:
            if not re.match(CONDITION_2, pr.head.ref):
                print(pr.head.ref, 'does not match', CONDITION_2)
                continue
            id = pr.id
            already_have_it = 0
            for column in columns_2:
                cards = column.get_cards()
                for card in cards:
                    if pr.issue_url == card.content_url:
                        print('PR', pr.number, 'is already in', project.name,
                              'column', column.name)
                        already_have_it = 1
                        break
                if already_have_it == 1:
                    break
            if already_have_it == 0:
                for column in columns_2:
                    if column.name == COLUMN_NAME:
                        column.create_card(content_id=id,
                                           content_type='PullRequest')
                        print('Add PR', pr.number, 'to', project.name,
                              'column', COLUMN_NAME)
    else:
        pass
