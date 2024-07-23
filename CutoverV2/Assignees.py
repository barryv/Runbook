from re import A
import pandas as pd

class AssigneeData:
   
    def set_assignee_columns(self):
    
        columns = ['RunbookId' 'TaskId', 'AssigneeId']
        
        return pd.DataFrame(columns=columns)
        
    
    def append_user_data(self, df: pd.DataFrame):
        
        assignees = {}
        rbId = df['RunbookId']
        taskId = df['TaskId']
        assignees = df['Assignees']
        userDf = pd.DataFrame()
       
        print(assignees)
        
        for assignee in assignees:
            assigneeIds =  assignee['data']
            print("Ids")
            for id in assigneeIds:
                assigneeId = id['id']   
                print(assigneeId)
            print(assigneeIds)
            newRow = { 'RunbookId': rbId, 'TaskId': taskId, 'AssigneeId': assigneeId}
            userDf = pd.concat([userDf, pd.DataFrame([newRow])], ignore_index=True)
        
        return userDf




