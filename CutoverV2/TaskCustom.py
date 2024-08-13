import pandas as pd


class TaskCustom:
        
    def set_taskcustom_columns(self):
   
        columns = ['Runbook Id', 'Task Id', 'Pid', 'Name', 'Value']
        
        return pd.DataFrame(columns=columns)
        
    def process_task_custom(self, rbid: str, item: list, df: pd.DataFrame):
       
        pid=0
        if ('attributes' in item and 
           'custom_field_values' in item['attributes'] and
           not item['attributes']['custom_field_values']):
           customFields = item['attributes']['custom_field_values']
           for field in customFields: 
               df = self.append_taskcustom_data(rbid, item['id'], str(pid), field, df) 
        
        return df
        
    def append_taskcustom_data(self, rbid: str, tid: str, pid: str, field: list, df: pd.DataFrame):
            
           
        newRow = {
            'Runbook Id': rbid,'
            'Task Id': tid, 
            'Pid': pid,
            'Name': field['name'], 
            'Value': field['value']
            }
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)




