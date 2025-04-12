# Write a program in python that will read a file from a repository, 

# The program should then replace all the instances of the text "Andrew" with your name. 

# The program should then commit those changes and push the file back to the repository


import os
from git import Repo
import requests
import config as cfg

# Define the repository URL and the file path

