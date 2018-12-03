import json
import requests
import numpy as np

"""
Q1: Find out which user has submitted the most PRs in astropgh/learning-by-doing
"""
repos = json.loads(requests.get('https://api.github.com/repos/astropgh/learning-by-doing/pulls').text)
prs_users = [repo['user']['login'] for repo in repos]
print(prs_users[np.argmax([prs_users.count(user) for user in prs_users])])

"""
Q2: Find out how many commits have been made to the master branch of numpy/numpy in 2018 October
"""
# TODO: I don't know how to find the number of total pages
n_commits = 0
for page in range(20):
    repos = json.loads(requests.get('https://api.github.com/repos/numpy/numpy/commits', params={'page': page}).text)
    commit_dates = [repo['commit']['author']['date'] for repo in repos]
    n_commits += len([commit_date for commit_date in commit_dates if '2018-10' in commit_date])
print(n_commits)

"""
Q3: (cont'd after 2) Find out how many distinct users made those commits
"""


"""
Q4: List all the branch names in numpy/numpy
"""
