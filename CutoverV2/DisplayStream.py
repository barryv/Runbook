import pandas as pd

class DisplayStream:
        def __init__(self, api_service: APIService):
        self.api_service = api_service
   
    def set_displaystream_columns(self):
   
        columns = ['Id', 'Parent Id', 'Type', 'Name', 'Description', 'Primary', 'Task Count', 'Task Completed', 
                   'Start Display', 'Start Latest Planned', 'End Display', 
                   'End Latest Planned', 'End Planned', 'Stream', 'Sub']
        
        return pd.DataFrame(columns=columns)
        
    def process_display_stream(self, rbid: str, df: pd.DataFrame):
        
        item = self.api_service.get_stream_rbid(rbid)

        if not isinstance(item['relationships'].get('parent'), dict):
            pid = "Parent"
            pars = item['attributes']['name']
            subs = "-----"
        else:
            pid = ['relationships']['parent']['data']['id']
            par = self.api_service.get_stream_id(pid)
            pars = par['attributes']['name']
            subs = item['attributes']['name']
            
        df = self.append_displaystream_data(item: list, pid: str, pars: str, 
                                            subs: str, df: pd.Dataframe)
       
                        
    def append_displaystream_data(self, item: list, pid: str, pars: str,
                                  subs: str, df: pd.DataFrame):
            
        newRow = {
            'Id': item['id'], 
            'Parent Id': pid,
            'Type': item['type'], 
            'Name': item['attributes']['name'], 
            'Description': item['attributes']['description'],
            'Primary': item['attributes']['is_primary'], 
            'Task Count': item['meta']['tasks_count'], 
            'Task Completed': item['meta']['completed_tasks_count'], 
            'Start Display': item['attributes']['start_display'], 
            'Start Latest Planned ': item['attributes']['start_latest_planned'], 
            'End Display': item['attributes']['end_display'],    
            'End Latest Planned': item['attributes']['end_latest_planned'], 
            'End Planned': item['attributes']['end_planned'],
            'Stream': pars,
            'Sub': subs}
        
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        
        




