from github import Github
import requests
from config import githubkey as cfg
import base64

# API key for authorization
g = Github(cfg)

# Access the repository: 
repo = g.get_repo("lryan30/wsaa-assignments")  

# file path:
file_path = "test.txt"  

# Get the file content
file = repo.get_contents(file_path)

# download the file content
url = file.download_url
response = requests.get(url, auth=('token', cfg))






