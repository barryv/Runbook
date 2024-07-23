
import pandas as pd

class RunbookData:
   
    def set_runbook_columns(self):
    
        columns = ['Id', 'Type', 'Name', 'Description', 'Status', 'Run Type', 'Stage', 'Use Case', 'CRQ', 'INC', 
                   'Coordinated', 'Requested', 'AuthorId', 'WorkspaceId', 'FolderId', 'RunTypeId',  'TaskCount',
                   'TaskComplete', 'Timing', 'Created', 'PlanStart', 'PlanEnd', 'ScheduledStart', 'ActualStart', 
                   'ActualEnd', 'LastTouch', 'LastUpdate']
        
        return pd.DataFrame(columns=columns)
        
       
        
                        
    def append_runbook_data(self, item: list, df: pd.DataFrame):
        

        custom_fields_values = item['attributes']['custom_fields_values']
        
        useCase = "Case1"
        CRQId = "CRQ1"
        INCId = "INC1"
        CoordinatedBy = "Coordinator1"
        RequestedBy = "Requester1"
        

        for field in custom_fields_values:
            if ['name'] == 'Use Case':
                useCase = field['value']
            if ['name'] == '[AOCommon]CRQID':
                CRQId = field['value']
            if ['name'] == '[AOCommon]INCID':  
                INCId = field['value']      
            if ['name'] == '[AOCommon]CoordinatedBy':
                CoordinatedBy = field['value']
            if ['name'] == '[AOCommon]RequestedBy':
                RequestedBy = field['value'] 


       
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Description': item['attributes']['description'],
            'Status': item['attributes']['status'], 
            'Run Type': item['attributes']['run_type'],
            'Stage': item['attributes']['stage'], 
            'Use Case': useCase,
            'CRQ': CRQId, 
            'INC': INCId, 
            'Coordinated': CoordinatedBy, 
            'Requested': RequestedBy, 
            'AuthorId': item['relationships']['author']['data']['id'], 
            'WorkspaceId': item['relationships']['workspace']['data']['id'],
            'FolderId': item['relationships']['folder']['data']['id'], 
            'RunTypeId': item['relationships']['runbook_type']['data']['id'],
            'TaskCount': item['meta']['tasks_count'], 
            'TaskComplete': item['meta']['complete'], 
            'Timing': item['attributes']['timing_mode'],
            'Created': item['attributes']['created_at'], 
            'PlanStart': item['attributes']['start_planning'], 
            'PlanEnd': item['attributes']['end_planning'],            
            'ScheduledStart': item['attributes']['start_scheduled'], 
            'ActualStart': item['attributes']['start_actual'],
            'ActualEnd': item['attributes']['end_actual'],        
            'LastTouch': item['attributes']['touched_at'], 
            'LastUpdate': item['attributes']['updated_at']}
        
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        
        