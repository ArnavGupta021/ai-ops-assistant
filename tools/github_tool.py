import requests


def search_repos(query: str, limit: int = 2):

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    headers = {
        "Accept": "application/vnd.github+json"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            print("GitHub API Error:", response.status_code, response.text)
            return []

        data = response.json()

        if "items" not in data:
            print("No items found in GitHub response:", data)
            return []

        repos = []
        for item in data["items"][:limit]:
            repos.append({
                "name": item["name"],
                "stars": item["stargazers_count"],
                "url": item["html_url"]
            })

        return repos

    except Exception as e:
        print("GitHub Exception:", str(e))
        return []
