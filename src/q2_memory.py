from typing import List, Tuple
from collections import Counter
import emoji
import json
from memory_profiler import profile

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()
    
    # Process the JSON file line by line
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            emojis_in_content = [char for char in content if char in emoji.UNICODE_EMOJI_ENGLISH]
            emoji_counts.update(emojis_in_content)
    
    # Get the top 10 most common emojis
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis