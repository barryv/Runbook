import pandas as pd

class UserData:
   
    def set_user_columns(self):
   
        columns = ['Id', 'Type', 'First Name', 'Last Name', 'Handle', 'eMail', 'Phone', 'Sign in Count']
       
        return pd.DataFrame(columns=columns)
        
                           
    def append_user_data(self, item: list, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Type': item['type'], 
            'First Name': item['attributes']['first_name'], 
            'Last Name': item['attributes']['last_name'],       
            'Handle': item['attributes']['handle'],
            'eMail': item['attributes']['email'],
            'Phone': item['attributes']['mobile_number'],
            'Sign in Count': item['meta']['sign_in_count']}
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




