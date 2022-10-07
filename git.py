
import requests 
import json

def numberReposandCommits(userID):
    url = "https://api.github.com/users/" + userID + "/repos"
    req = requests.get(url)
    content = req.json()
    repositories = []
    for REPO in content:
        repo = "https://api.github.com/repos/" + userID + "/" + REPO["name"] + "/commits"
        req2 = requests.get(repo)
        commits = len(req2.json())
        repositories.append({"Repo":REPO["name"], "Number of commits": commits})
        print("Repo: " + REPO["name"] + " Number of commits: " + str(commits))        
    return REPO

user = "ShivShah202000"
numberReposandCommits(user)