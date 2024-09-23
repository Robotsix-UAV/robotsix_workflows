import os
import json
import sys
from openai import OpenAI

def get_assistant_configuration(config_file='assistant_config.json'):
    """
    Reads the assistant configuration from a JSON file.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(f"Configuration file {config_file} not found.")
        sys.exit(1)
    except KeyError:
        print(f"'assistant_id' not found in {config_file}.")
        sys.exit(1)

def main():
    # Set your OpenAI API key
    api_key = os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>")
    client = OpenAI(api_key=api_key)

    # Get the assistant configuration
    assistant_configuration = get_assistant_configuration()
    assistant_id = assistant_configuration['assistant_id']
    vector_store_id = assistant_configuration['vector_store_id']

    # Update the assistant by adding tools
    response = client.beta.assistants.update(
        assistant_id=assistant_id,
        tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}})

    # Optional: Handle the response as needed
    if response.id == assistant_id:
        print(f"Assistant {assistant_id} has been updated successfully.")
    else:
        print("Failed to update the assistant.")
        sys.exit(1)

if __name__ == "__main__":
    main()
