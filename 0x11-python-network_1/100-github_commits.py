#!/usr/bin/python3
"""
    Python script to list 10 commits of the repository
"""
import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    data = r.json()
    for commit in data[:10]:
        sha = commit['sha']
        name = commit['commit']['author']['name']
        print("{}: {}".format(sha, name))
