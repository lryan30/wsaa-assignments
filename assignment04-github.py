from github import Github
from config import githubkey as cfg
import base64

# API key for authorization
g = Github(cfg)

# Access the repository: 
repo = g.get_repo("lryan30/wsaa-assignments")  

# file path:
file_path = "file.txt"  

# Get the file content
file = repo.get_contents(file_path)

# decoded content
decoded_content = base64.b64decode(file.content).decode("utf-8")
print(decoded_content)

# replace Andrew with Louise
updated_content = decoded_content.replace("Andrew", "Louise")
print(updated_content)

# Update the file in the repository
repo.update_file(file_path, "Updated file.txt", updated_content, file.sha)

print("File updated successfully!")






