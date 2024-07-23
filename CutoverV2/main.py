
import pandas as pd
from RB import RunbookData 
from Task import TaskData
from Assignees import AssigneeData

     # Sample item to test the get_runbook_data method

def main():

    #input("Start")
    
    test_task = {

      "relationships": {  
          "runbook": {
              "data": {
                  "id": "runbook_123"   
              }
          },
          "stream": {
             "data": {
                 "id": "stream_456"
             }
          },
          "task_type": {
             "data": {
                 "id": "tasktype_789"
             }
          },
          "assignees": {
              "data": [
              {
                 "id": "1",
                 "type": "user",
              },
              {
                 "id": "2",
                 "type": "user",
              },
              {
                 "id": "3",
                 "type": "user",
              }
              ]
          }
      },
      "id": "task_123",
      "type": "task",
      "attributes": {
          "name": "Task Name",
          "comment_count": 5,
          "completion_type": "manual",
          "description": "Task description here.",
          "duration": 120,
          "stage": "planning",
          "created_at": "2023-01-01T00:00:00Z",
          "start_planning": "2023-01-02T00:00:00Z",
          "start_display": "2023-01-03T00:00:00Z",
          "start_fixed": "2023-01-04T00:00:00Z",
          "end_planning": "2023-01-05T00:00:00Z",
          "start_scheduled": "2023-01-06T00:00:00Z",
          "start_actual": "2023-01-07T00:00:00Z",
          "end_actual": "2023-01-08T00:00:00Z",
          "end_display": "2023-01-09T00:00:00Z",
          "end_fixed": "2023-01-10T00:00:00Z",
          "updated_at": "2023-01-11T00:00:00Z"
      }
    }


    test_item = {
        'id': 'rb_123',
        'type': 'runbook',
        'attributes': {
        'description': 'Sample runbook description',
        'status': 'active',
        'name': 'Sample Runbook',
        'run_type': 'manual',
        'stage': 'development',
        'timing_mode': 'standard',
        'created_at': '2023-01-01T00:00:00Z',
        'end_planning': '2023-01-02T00:00:00Z',
        'start_actual': '2023-01-03T00:00:00Z',
        'start_planning': '2023-01-01T00:00:00Z',
        'start_scheduled': '2023-01-02T00:00:00Z',
        'touched_at': '2023-01-03T00:00:00Z',
        'updated_at': '2023-01-04T00:00:00Z',
        'end_actual': '2023-01-05T00:00:00Z',
        'custom_fields_values': [
            {'name': 'Use Case', 'value': 'Example Use Case'},
            {'name': '[AOCommon]CRQID', 'value': 'CRQ123456'},
            {'name': '[AOCommon]INCID', 'value': 'INC654321'},
            {'name': '[AOCommon]CoordinatedBy', 'value': 'Coordinator Name'},
            {'name': '[AOCommon]RequestedBy', 'value': 'Requester Name'} ]
        
        },
        'relationships': {
            'author': {'data': {'id': 'author_123'}},
            'workspace': {'data': {'id': 'workspace_123'}},
            'folder': {'data': {'id': 'folder_123'}},
            'runbook_type': {'data': {'id': 'type_123'}}
            },
        'meta': {
            'tasks_count': 5,
            'complete': 4
            }
    }
    
# Assuming you have an instance of the RunbookData class and an empty DataFrame

    rb_data_instance = RunbookData()
    task_data_instance = TaskData()
    assignee_data_instance = AssigneeData()
    
    rbdf = rb_data_instance.set_runbook_columns()
    taskdf = task_data_instance.set_task_columns()
    assigneedf = assignee_data_instance.set_assignee_columns()
    

# Now, you can call the get_runbook_data method with the test_item
    rbdf = rb_data_instance.append_runbook_data(test_item, rbdf)
    taskdf = task_data_instance.append_task_data(test_task, taskdf)
    assigneedf = assignee_data_instance.append_user_data(taskdf)
    print(rbdf)
    print(taskdf)
    print(assigneedf)
    
   

    
if __name__ == "__main__":
    main()
