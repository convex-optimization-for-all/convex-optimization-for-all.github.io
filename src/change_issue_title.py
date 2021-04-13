import os
import requests


if __name__ == "__main__":
    token = os.environ["GITHUB_TOKEN"]
    issue_number = os.environ["ISSUE_NUMBER"]
    owner = "convex-optimization-for-all"
    repo = "convex-optimization-for-all.github.io"

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    original_title = requests.get(url, auth=("username", token)).json()["title"]
    payload = {
        "title": "[Closed] " + original_title.split("·", maxsplit=1)[0]
    }
    requests.patch(url, auth=("username", token), json=payload)
