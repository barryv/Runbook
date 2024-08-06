import pandas as pd
from api_service import APIService


class DisplayFolder:
    def __init__(self, api_service: APIService):
        self.api_service = api_service
        
    def set_displayfolder_columns(self):
   
        columns = ['Id', 'Parent Id', 'Type', 'Name', 'Short Name', 'Created', 
                   'Updated' 'Workspace', 'Group', 'AIT']
        
        return pd.DataFrame(columns=columns)
        
    def process_display_folder(self, wsid: str, rbid: str, item: list, df: pd.DataFrame):
       

        if not isinstance(item['relationships'].get('parent'), dict):
            pid = "Parent"
            parf = item['attributes']['name']
            subf = "-----"
        else:
            pid = ['relationships']['parent']['data']['id']
            parf = self.find_folder_name(wsid,pid)
            subf = item['attributes']['name']
            
        df = self.append_displayfolder_data(item: list, pid: str, parf: str, 
                                            subf: str, df: pd.Dataframe)
            
    def find_folder_name(self, wsid: str, fid: str):
        nfn = "None"
        items = self.get_folders_by_workspaceid(wsid)
        for item in items:
            if item['id'] == fid:
                return item['attributes']['name']
            
        return nfn
            

        
    def append_displayfolder_data(self, item: list, pid: str, parf: str,
                                  subf: str, df: pd.DataFrame):
            
           
        newRow = {
            'Id': item['id'], 
            'Parent Id': pid,
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Short Name': item['attributes']['key'],
            'Created': item['attributes']['created_at'], 
            'Updated': item['attributes']['updated_at'],
            'Workspace': item['relationships']['workspace']['data']['id'],
            'Group': parf,
            'AIT': subf
            }
       
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)