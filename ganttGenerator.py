import requests
import json
import re

# Replace with your GitHub access token
access_token = "PERSONAL_ACCESS_TOKEN"

# Replace with the owner and repository name
owner = "OWNER/ORG"
repo = "REPOSITORY"

# API endpoint for issues
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# API request headers
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github+json"
}

# Send the API request
response = requests.get(url, headers=headers)

# Check for a successful response
if response.status_code != 200:
    print(f"Failed to retrieve issues. Error code: {response.status_code}")
    exit()

# Parse the JSON data
data = json.loads(response.text)

def get_assignee(issue):
    assignee = issue["assignee"]
    if assignee is not None:
        print(f"Assignee: {assignee['login']}")
    else:
        print("Assignee: None")
    return assignee;

def get_milestone(issue):
    milestone = issue["milestone"]
    if milestone is not None:
        print(f"Milestone: {milestone['title']}")
    else:
        print("Milestone: None")
    return milestone;

# Examine the description for the estimated effort, marked by "#TIME:"
def get_time(issue):
    match = re.search("#Time:(\S+)", issue["body"])
    if match:
        return match.group(1)
    else:
        return "Not found"


#todo create gantt chart

# Iterate through the issues
for issue in data:
    print(issue["title"])
    get_assignee(issue)
    print("Time:",get_time(issue))
    get_milestone(issue)
    print("")