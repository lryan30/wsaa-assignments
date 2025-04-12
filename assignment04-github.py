# Assignment 04:
# This script uses the GitHub API to access a file in a github repository using an API key.
# It downloads the file from the repository, replaces the name "Andrew" with "Louise",
# and then uploads the edited file back to the repository. 
# Author: LR


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

#get download url of the raw file 
url = file_content.download_url 
print(url)

# Get the file content from the url using requests module
response = requests.get(url)
file_data = response.text
print(file_data)

# replace Andrew with Louise 
file_data = file_data.replace("Andrew", "Louise")
print(file_data)

# Update the file in the repository
repo.update_file(file_path, "Updated file", file_data, file_content.sha)
print("File updated successfully!")



# References: 
# https://pygithub.readthedocs.io/en/stable/examples/Repository.html#update-a-file-in-the-repository
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token
# https://github.com/PyGithub/PyGithub/issues/1343
# https://www.w3schools.com/python/ref_string_replace.asp








