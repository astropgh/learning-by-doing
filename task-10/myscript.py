import json
import requests
import numpy as np

repos = json.loads(requests.get('https://api.github.com/orgs/astropgh/repos').text)
names = [ repo['name'] for repo in repos ]
# print([repo['name'] for repo in repos])

# lbd = repos[2]
# print(lbd.keys())

def print_creation(name=None):
    if name == None:
        for repo in repos:
            print(repo['name'], 'was created at', repo['created_at'])
    else:
        repo = get_repo(name)
        print(name, 'was created at', repo['created_at'])


def print_max_PR(name=None):
    repo = get_repo(name)
    pulls = json.loads(requests.get(repo['pulls_url'][:-9]).text)
    users = [ pull['user']['login'] for pull in pulls]
    max_user = max(set(users), key=users.count)
    print(max_user, 'has the most PRs with', users.count(max_user))


def get_repo(name):
    return repos[np.where(np.array(names, copy=False)==name)[0][0]]
