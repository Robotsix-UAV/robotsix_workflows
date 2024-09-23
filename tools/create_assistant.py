import os
import json
import sys
from openai import OpenAI

# Get the repository name from command-line arguments or environment variables
if len(sys.argv) > 1:
    repo_name = sys.argv[1]
else:
    # Attempt to get the repository name from the GITHUB_REPOSITORY environment variable
    repo_full_name = os.getenv('GITHUB_REPOSITORY', 'Unknown/Unknown')
    repo_name = repo_full_name.split('/')[-1]  # Extract the repo name

# Set your OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>")
client = OpenAI(api_key=api_key)

# Define the assistant's name and instructions
name = f"Repository Assistant for {repo_name}"
instructions = """
You are an AI assistant designed to help improve code quality, update documentation, and manage repository tasks.
"""

# Create the assistant
response = client.beta.assistants.create(
    name=name,
    instructions=instructions,
    model="gpt-4o-2024-08-06",
)

# Extract the assistant ID
assistant_id = response.id

# Save the assistant ID to a JSON configuration file
config = {
    "assistant_id": assistant_id
}

with open('assistant_config.json', 'w') as f:
    json.dump(config, f, indent=4)
