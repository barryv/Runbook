import pandas as pd

class RunbookData:
   
    def set_runbook_columns(self):
   
        columns = ['Id', 'Type', 'Name', 'Description', 'Primary', 'Task Count', 'Task Completed', 
                   'Start Display', 'Start Latest Planned', 'End Display', 'End Latest Planned', 'End Planned']
        
        return pd.DataFrame(columns=columns)
        
       
        
                        
    def append_runbook_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Description': item['attributes']['description'],
            'Primary': item['attributes']['is_primary'], 
            'Task Count': item['meta']['tasks_count'], 
            'Task Complete': item['meta']['completed_tasks_count'], 
            'Start Display': item['attributes']['start_display'], 
            'Start Latest Planned ': item['attributes']['start_latest_planned'], 
            'End Display': item['attributes']['end_display'],    
            'End Latest Planned': item['attributes']['end_latest_planned'], 
            'End Planned': item['attributes']['end_planned']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        
        




