from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd
from collections import defaultdict, Counter
import time
from memory_profiler import profile

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    date_counts = Counter()
    user_counts = defaultdict(lambda: defaultdict(int))
    
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date_only = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            username = tweet['user']['username']
            
            date_counts[date_only] += 1
            user_counts[date_only][username] += 1
    
    top_dates = date_counts.most_common(10)
    
    result = []
    for date, _ in top_dates:
        top_user = max(user_counts[date], key=user_counts[date].get)
        result.append((date, top_user))
    
    return result