# student_name: Abilash
# roll_number: 727823tucy021
# project_name: Social Media OSINT Tracker
# date: 2026-03-29

import requests

def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    print("DEBUG: Status Code =", response.status_code)   # 👈 debug line

    if response.status_code == 200:
        data = response.json()
        print("Username:", data["login"])
        print("Followers:", data["followers"])
        print("Public Repos:", data["public_repos"])
    else:
        print("User not found")

username = input("Enter GitHub username: ")
get_github_info(username)
