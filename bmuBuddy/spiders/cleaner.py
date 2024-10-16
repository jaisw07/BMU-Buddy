import json

# Load the scraped JSON data
with open('bmuData.json', 'r') as f:
    scraped_data = json.load(f)

import re
from w3lib.html import remove_tags

# Function to clean each page's content
def clean_content(content):
    # Remove HTML tags
    content = remove_tags(content)
    
    # Remove extra whitespace and newlines
    content = re.sub(r'\s+', ' ', content).strip()
    
    # Optionally, remove non-ASCII characters
    content = re.sub(r'[^\x00-\x7F]+', '', content)
    
    return content

# Apply cleaning to the data
for page in scraped_data:
    page['title'] = page['title'].strip() if page['title'] else ''
    page['content'] = clean_content(page['content'])

# Save the cleaned data
with open('cleaned_output.json', 'w') as f:
    json.dump(scraped_data, f, indent=4)
