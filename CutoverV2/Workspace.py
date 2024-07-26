import pandas as pd

class WorkspaceData:
   
    def set_workspace_columns(self):
   
        columns = ['Id', 'Type', 'Name', 'Short Name', 'Created', 'Updated']
        
        return pd.DataFrame(columns=columns)
        
       
        
                        
    def append_workspace_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Short Name': item['attributes']['key'],
            'Created': item['attributes']['created_at'], 
            'Updated': item['attributes']['updated_at']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




