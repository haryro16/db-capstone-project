
from github import Github
import os
access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
g = Github(access_token)
owner = 'haryro16'
repo_name = 'db-capstone-project'

repo = g.get_user(owner).get_repo(repo_name)
main_branch = repo.get_branch('main')
file_path = 'https://github.com/haryro16/db-capstone-project.git'
commit_message = 'Delete file'

contents = repo.get_contents(file_path, ref=main_branch.name)
repo.delete_file(contents.path, commit_message, contents.sha, branch=main_branch.name)
