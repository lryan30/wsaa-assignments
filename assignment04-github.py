




from github import Github
from config import githubkey as cfg
import requests

# API key for authorization
g = Github(cfg)

# Access the repository: 
repo = g.get_repo("lryan30/wsaa-assignments")  

# file path:
file_path = "file.txt"  

# Get the file content
file_content = repo.get_contents(file_path)

#get url of the file
url = file_content.download_url
print(url)

# Get the file content using requests
response = requests.get(url)

file_data = response.text
print(file_data)

# replace Andrew with Louise
file_data = file_data.replace("Andrew", "Louise")
print(file_data)

# Update the file in the repository
repo.update_file(file_path, "Updated file", file_data, file_content.sha)
print("File updated successfully!")









