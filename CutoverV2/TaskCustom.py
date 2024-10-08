import pandas as pd


class TaskCustom:
        
    def set_taskcustom_columns(self):
        columns = ['Runbook Id', 'Task Id', 'Tool', 'Task', 'Action', 'IStatus', 'PStatus',
                   'BStatus', 'GStatus', 'Requested', 'Coordinated', 'Job', 'Path',
                  'Host', 'Env', 'CRQ', 'INC', 'Ratio', 'TID']
        
        return pd.DataFrame(columns=columns)
        
    def process_task_custom(self, rbid: str, item: list, df: pd.DataFrame):
       
        
        if item['attributes']['custom_field_values'] != {}:
           newRow = self.create_new_taskcustom()
           customFields = item['attributes']['custom_field_values']
           for field in customFields:
               newRow = self.add_taskcustom_value(newRow, field)
               
        if newRow['Tool'] != 'none':
            newRow['Runbook Id'] = rbid
            newRow['Task Id'] = item['id']
            df = self.append_taskcustom_data(newRow, df)
            
        return df
        
    def append_taskcustom_data(self, newRow: dict, df: pd.DataFrame):
             
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)

    def add_taskcustom_value(newRow: dict, field: list):
        
        if field['name'] == '[AOBlade]TaskTechnologyTool':
            newRow['Tool'] = field['value']
        elif field['name'] == '[AOBlade]TaskName':
            newRow['Task'] = field['value']
        elif field['name'] == '[AOSearchlight]Action':
            newRow['Action'] = field['value']
        elif field['name'] == '[Integration]Status':
            newRow['IStatus'] = field['value']
        elif field['name'] == 'Polling status':
            newRow['PStatus'] = field['value']
        elif field['name'] == 'Orchestrator via Polling: Orchestrator - BladeLogic: Polling status':
            newRow['BStatus'] = field['value']
        elif field['name'] == 'Orchestrator via Polling: Orchestrator - Greenlight: Polling status':
            newRow['GStatus'] = field['value']
        elif field['name'] == '[AOBlade]RequestedBy':
            newRow['Requested'] = field['value']
        elif field['name'] == '[AOBlade]CoordinatedBy':
            newRow['Coordinated'] = field['value']
        elif field['name'] == 'AOBlade]JobName':
            newRow['Job'] = field['value']
        elif field['name'] == '[AOBlade]JobPath':
            newRow['Path'] = field['value']
        elif field['name'] == '[AOBlade]HostName':
            newRow['Host'] = field['value']
        elif field['name'] == '[AOBlade]Environment': 
            newRow['Env'] = field['value']
        elif field['name'] == '[AOBlade]CRQID':
            newRow['CRQ'] = field['value']
        elif field['name'] == '[AOBlade]INCID':
            newRow['INC'] = field['value']
        elif field['name'] == '[AOSearchlight]Ratio':
            newRow['Ratio'] = field['value']
        elif field['name'] == '[AOAnsible]TemplateID':
            newRow['TID'] = field['value']
            
        return newRow
            
    def create_new_taskcustom(self):
        
        none = 'none'
        newRow = {
            'Runbook Id': '',
            'Task Id': '', 
            'Tool': none,
            'Task': '',
            'Action': '',
            'IStatus': '',
            'PStatus': '',
            'BStatus': '',
            'GStatus': '',
            'Requested': '',
            'Coordinated': '',
            'Job': '',
            'Path': '',
            'Host': '',
            'Env': '',
            'CRQ': '',
            'INC': '',
            'Ratio': '',
            'TID': ''
        }    
        return newRow



