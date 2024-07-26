import pandas as pd

class TaskTypeData:
   
    def set_tasktype_columns(self):
   
        columns = ['Id', 'Type', 'Name', 'Short Name', 'Comms', 'Progression', 'Created', 'Updated']
       
        return pd.DataFrame(columns=columns)
        
                           
    def append_tasktype_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Short Name': item['attributes']['key'],       
            'Comms': item['attributes']['comms'],
            'Progression': item['attributes']['conditional_progression'],
            'Created': item['attributes']['created_at'],
            'Updated': item['attributes']['updated_at']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




