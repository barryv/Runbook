import pandas as pd

class TaskData:
   
    def set_task_columns(self):
    
        columns = ['RunbookId', 'TaskId', 'Type', 'Name', 'CommentCount', 'CompletionType', 
                   'Description', 'Duration', 'Stage', 'StreamId', 'TaskTypeId', 'Assignees', 
                   'Created', 'PlanStart', 'StartDisplay', 'StartFixed', 'PlanEnd', 
                   'ScheduledStart', 'ActualStart',  'ActualEnd','EndDisplay', 
                   'EndFixed', 'LastUpdate']
        
        return pd.DataFrame(columns=columns)
        
    
    def append_task_data(self, item: list, df: pd.DataFrame):
        
        newRow = {
            'RunbookId': item['relationships']['runbook']['data']['id'],
            'TaskId': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'CommentCount': item['attributes']['comment_count'],
            'CompletionType': item['attributes']['completion_type'],
            'Description': item['attributes']['description'],
            'Duration': item['attributes']['duration'],
            'Stage': item['attributes']['stage'],
            'StreamId': item['relationships']['stream']['data']['id'],            
            'TaskTypeId': item['relationships']['task_type']['data']['id'],
            'Assignees': item['relationships']['assignees'],
            'Created': item['attributes']['created_at'], 
            'PlanStart': item['attributes']['start_planning'],
            'StartDisplay': item['attributes']['start_display'],
            'StartFixed': item['attributes']['start_fixed'],
            'PlanEnd': item['attributes']['end_planning'],            
            'ScheduledStart': item['attributes']['start_scheduled'], 
            'ActualStart': item['attributes']['start_actual'],
            'ActualEnd': item['attributes']['end_actual'],
            'EndDisplay': item['attributes']['end_display'],
            'EndFixed': item['attributes']['end_fixed'],
            'LastUpdate': item['attributes']['updated_at']}
       
        taskDf = pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        
        return taskDf
        




