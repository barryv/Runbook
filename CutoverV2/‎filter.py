from datetime import datetime, timedelta
from pickle import TRUE


def filter_runbook(self, item: list, end_date: str, updated: str):
        endDate = datetime(end_date)
        updateDate = datetime(updated)
        today = datetime.now()
        sixMonths = timedelta(days=180)
        threeMonths = timedelta(days=90)
        sixAgo = today - sixMonths
        threeAgo = today - threeMonths
        stage = item['attributes']['stage']
        is_template = item['attributes']['is_template']
        
        if stage == 'completed' and endDate >= sixAgo:
            return TRUE
        if stage != 'completed' and updateDate >= threeAgo:
            return TRUE
        if is_template == "False":
            return TRUE
        if stage != 'cancelled':
            return TRUE
        
        return FALSE
