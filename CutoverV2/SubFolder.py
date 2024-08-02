import pandas as pd

class SubFolderData:
   
    def set_subfolder_columns(self):
   
        columns = ['Id', 'Parent Id', 'Type', 'Name', 'Short Name', 'Created', 'Updated' 'Workspace']
        
        return pd.DataFrame(columns=columns)
        
                           
    def append_subfolder_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Parent Id': item['relationships']['parent']['data']['Id'],
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Short Name': item['attributes']['key'],
            'Created': item['attributes']['created_at'], 
            'Updated': item['attributes']['updated_at'],
            'Workspace': item['relationships']['workspace']['data']['id']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




