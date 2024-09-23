import pandas as pd

class RoleData:
   
    def set_role_columns(self):
   
        columns = ['Id', 'Type', 'Expires', 'Runbook Id', 'Role Type Id', 'User Id']
       
        return pd.DataFrame(columns=columns)
        
                           
    def append_role_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'],
            'Expired': item['attributes']['expires-at'], 
            'Runbook Id': item['relationships']['resource']['data']['id'],       
            'Role Type Id': item['relationships']['role_type']['data']['id'],
            'User Id': item['relationships']['subject']['data']['id']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




