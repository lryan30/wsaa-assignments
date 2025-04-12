import requests
from github import Github
import base64
from config import githubkey as cfg

# API key for authorization
g = Github(cfg)

# Access the repository: 
repo = g.get_repo("lryan30/wsaa-assignments")  

# file path:
file_path = "test.txt"  

# Get the file content
file = repo.get_contents(file_path)


