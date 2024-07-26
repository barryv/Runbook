import pandas as pd

class RunTypeData:
   
    def set_runtype_columns(self):
   
        columns = ['Id', 'Type', 'Name', 'Short Name']
       
        return pd.DataFrame(columns=columns)
        
                           
    def append_runtype_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Short Name': item['attributes']['key']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




