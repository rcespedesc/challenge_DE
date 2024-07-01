from typing import List, Tuple
from collections import Counter
import emoji
import pandas as pd
import json


def q2_time(file_path: str) -> List[Tuple[str, int]]:

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    
    # Create a DataFrame from the JSON data
    df = pd.json_normalize(data)
    
    # Extract content and count emojis
    all_emojis = []
    for content in df['content']:
        all_emojis.extend([char for char in content if char in emoji.UNICODE_EMOJI_ENGLISH])
    
    # Get the top 10 most common emojis
    emoji_counts = Counter(all_emojis).most_common(10)
    
    return emoji_counts