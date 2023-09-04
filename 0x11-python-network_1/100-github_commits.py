#!/usr/bin/python3
"""
    Python script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 2:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        api_url = 'https://api.github.com'
        request_url = "{}/repos/{}/{}/commits?{}".format(
                api_url, owner_name, repository_name,
                'per_page=10'
                )
        response = requests.get(request_url, headers={'Accept': 'application/vnd.github.v3+json'}
                )
        if response.status_code == 200:
            for commit in response.json():
                commit_sha = commit['sha']
                commit_author = commit['commit']['author']['name']
                print('{}: {}'.format(commit_sha, commit_author))
