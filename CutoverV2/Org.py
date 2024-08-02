import pandas as pd

class OrgData:
   
    def set_org_columns(self):
    
        columns = ['UserId', 'Level' 'NetworkId', 'Name', 'ADName', 'Facility', 'Phone', 'eMail', 'MeMail',
                   'TenDot', 'Band', 'LOB', 'SubLOB', 'Division', 'Regulated']
        
        return pd.DataFrame(columns=columns)
    
    def process_org_data(self, item: list, df: pd.DateFrame):

        level = 0
        end = False
        aeMail = 'A@bofa.com'
        eMail = item['attributes']['email']
        
        while (end != True):
            orgItem = self.api.service.get_org_email(eMail)
            df = self.append_org_data(level, item, orgItem, df)
            if (orgItem['WorkEmail'] == aeMail):
                end = True
            else:
                eMail = orgItem['ManagerEmail']
                level +=1
       
        return(df)
    
        
    def append_org_data(self, level: int, item: list, orgitem: list, df: pd.DataFrame):
               
        newRow = {
            'Id': item['id'], 
            'Level': str(level),
            'NetworkID': orgitem['NetworkId'], 
            'Name': orgitem['DisplayName'],
            'ADName': orgitem['AciveDirectoryDisplayName'],
            'Facility': orgitem['FacilityAddress'], 
            'Phone': orgitem['PhoneNumber'],
            'eMail': orgitem['WorkEmail'], 
            'MeMail': orgitem['ManagerEmail'],
            'TenDot' : orgitem['TenDotHiearchy'], 
            'Band': orgitem['HrBand'], 
            'LOB': orgitem['LineOfBusiness'], 
            'SubLOB': orgitem['SubLineOfBusiness'], 
            'Division': orgitem['Division'],
            'Regulated': orgitem('isregulated')
        }
  
        
        return pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        

        



        





