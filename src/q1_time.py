from typing import List, Tuple
import json
import pandas as pd
from datetime import datetime
from memory_profiler import profile

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))

    df = pd.json_normalize(data)
    
    df['date_only'] = pd.to_datetime(df['date']).dt.date
    
    top_dates = df['date_only'].value_counts().nlargest(10).index
    
    result = []
    for date in top_dates:
        date_df = df[df['date_only'] == date]
        top_user = date_df['user.username'].value_counts().idxmax()
        result.append((date,  top_user))
    
    return result