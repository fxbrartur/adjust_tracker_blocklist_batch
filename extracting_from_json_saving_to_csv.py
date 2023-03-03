import json
import csv

# Load JSON data
with open('payload.json') as f:
    data = json.load(f)

# Extract tokens
tokens = [tracker['token'] for tracker in data['trackers']]

# Write tokens to CSV
with open('tokens.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['token'])
    writer.writerows([[token] for token in tokens])
