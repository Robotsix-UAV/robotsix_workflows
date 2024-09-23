import requests

def create_github_branch(repo_owner, repo_name, new_branch_name, base_branch='main', token='your_github_token'):
    """
    Creates a new branch on a GitHub repository.
    
    Args:
    - repo_owner: GitHub username or organization (e.g., 'your_username').
    - repo_name: Name of the repository (e.g., 'your_repo').
    - new_branch_name: Name of the new branch to create.
    - base_branch: Name of the base branch to create the new branch from (default is 'main').
    - token: GitHub personal access token for authentication.
    
    Returns:
    - Response JSON or error message.
    """
    # GitHub API base URL
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git"
    
    # Get the SHA of the latest commit on the base branch
    headers = {'Authorization': f'token {token}'}
    base_branch_url = f"{api_url}/refs/heads/{base_branch}"
    response = requests.get(base_branch_url, headers=headers)
    
    if response.status_code != 200:
        return f"Error: Could not fetch the base branch {base_branch}. Status Code: {response.status_code}, Response: {response.text}"
    
    # Extract the commit SHA from the base branch
    base_commit_sha = response.json()['object']['sha']
    
    # Define the payload to create the new branch
    new_branch_payload = {
        "ref": f"refs/heads/{new_branch_name}",
        "sha": base_commit_sha
    }
    
    # Create the new branch
    create_branch_url = f"{api_url}/refs"
    response = requests.post(create_branch_url, json=new_branch_payload, headers=headers)
    
    if response.status_code == 201:
        return f"Branch '{new_branch_name}' created successfully."
    else:
        return f"Error: Could not create the branch {new_branch_name}. Status Code: {response.status_code}, Response: {response.text}"
