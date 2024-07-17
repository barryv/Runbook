
import json

# Assuming the JSON data is stored in a string
json_data = '''
{
    "id": "13561",
    "type": "runbook",
    "attributes": {
        "archived": false,
        "auto_start": true,
        "created_at": "2024-07-16T22:28:59Z",
        "custom_fields_values": [
            {"name": "Runbook Country", "value": "US"},
            {"name": "Record Code", "value": "Ben 04-05"},
            {"name": "Use Case", "value": "Infrastructure Release"},
            {"name": "AOCommon]CRQID", "value": "CRQ123456789"}
        ],
        "description": "Test Description",
        "end_actual": null,
        "name": "Runbook Name"
    },
    "relationships": {
        "author": {
            "data": {
                "id": "12441",
                "type": "user"
            },
            "links": {
                "related": "LINKS"
            }
        },
        "workspace": {
            "data": {
                "id": "108",
                "type": "workspace"
            },
            "links": {
                "related": "LINK"
            }
        }
    },
    "links": {
        "self": "LINK"
    },
    "meta": {
        "tasks_count": 7,
        "complete": 0
    }
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Accessing various elements
runbook_id = data['id']
runbook_type = data['type']
archived = data['attributes']['archived']
auto_start = data['attributes']['auto_start']
created_at = data['attributes']['created_at']
custom_fields_values = data['attributes']['custom_fields_values']
description = data['attributes']['description']
end_actual = data['attributes']['end_actual']
name = data['attributes']['name']

# Example: Accessing custom fields values
for field in custom_fields_values:
    print(f"{field['name']}: {field['value']}")

# Accessing relationships
author_id = data['relationships']['author']['data']['id']
workspace_id = data['relationships']['workspace']['data']['id']

# Accessing meta
tasks_count = data['meta']['tasks_count']
complete = data['meta']['complete']

# Example output
print(f"Runbook ID: {runbook_id}, Name: {name}, Author ID: {author_id}, Workspace ID: {workspace_id}")
import requests

class CutoverAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def query_runbooks(self):
        # Query a list of runbooks from the API
        response = requests.get(f"{self.base_url}/runbooks")
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def query_tasks_for_runbook(self, runbook_id):
        # Query a list of tasks based on the runbook ID
        response = requests.get(f"{self.base_url}/tasks?runbookId={runbook_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def query_workspace_for_runbook(self, runbook_id):
        # Query workspace for each runbook listed
        response = requests.get(f"{self.base_url}/workspaces?runbookId={runbook_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return []

def main():
    # Main function to run the application
    api = CutoverAPI("http://example.com/api")
    
    runbooks = api.query_runbooks()
    print("Runbooks:", runbooks)
    
    for runbook in runbooks:
        runbook_id = runbook['id']
        tasks = api.query_tasks_for_runbook(runbook_id)
        workspace = api.query_workspace_for_runbook(runbook_id)
        
        print(f"Tasks for Runbook {runbook_id}:", tasks)
        print(f"Workspace for Runbook {runbook_id}:", workspace)

if __name__ == "__main__":
    main()



class CutoverApplication:
    def __init__(self):
        # Initialize the application
        self.runbooks = []
        self.tasks = []
        self.workspaces = []

    def read_runbooks(self, runbooks_list):
        # Read a list of Cutover Runbooks
        self.runbooks = runbooks_list

    def read_tasks(self, tasks_list):
        # Read a list of Cutover Tasks
        self.tasks = tasks_list

    def read_workspaces(self, workspaces_list):
        # Read a list of Cutover Workspaces
        self.workspaces = workspaces_list

def main():
    # Main function to run the application
    app = CutoverApplication()
    
    # Example data
    runbooks_list = ["Runbook 1", "Runbook 2", "Runbook 3"]
    tasks_list = ["Task 1", "Task 2", "Task 3"]
    workspaces_list = ["Workspace 1", "Workspace 2", "Workspace 3"]
    
    # Reading data
    app.read_runbooks(runbooks_list)
    app.read_tasks(tasks_list)
    app.read_workspaces(workspaces_list)
    
    # Example output
    print("Runbooks:", app.runbooks)
    print("Tasks:", app.tasks)
    print("Workspaces:", app.workspaces)

if __name__ == "__main__":
    main()
