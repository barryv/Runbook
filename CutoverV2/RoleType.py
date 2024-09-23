import pandas as pd

class RoleTypeData:
   
    def set_roletype_columns(self):
   
        columns = ['Id', 'Type', 'Description', 'Enabled', 'Key', 'Name']
       
        return pd.DataFrame(columns=columns)
        
                           
    def append_roletype_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'],
            'Description': item['attributes']['description'],
            'Enabled': item['attributes']['enabled'],
            'Key': item['attributes']['key'],
            'Name': item['attributes']['name']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




