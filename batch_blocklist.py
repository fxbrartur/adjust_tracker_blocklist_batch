import requests
import json
import csv
from tqdm import tqdm
from time import sleep

# Set up the endpoint URL
url = 'https://api.adjust.com/dashboard/api/trackers/{}/blacklist'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': {API_TOKEN}
}

# Open the CSV file and read in the tokens
with open('tokens.csv', 'r') as f:
    reader = csv.reader(f)
    tokens = [row[0] for i, row in enumerate(reader) if i != 0]  # skip header row

# Set up the progress bar
pbar = tqdm(total=len(tokens))

# Iterate over the tokens and make a POST request for each one
with open('responses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Status', 'Response'])

    for token in tokens:
        # Make the POST request
        response = requests.post(url.format(token), headers=headers)

        # Write the response to the CSV file
        writer.writerow([response.status_code, response.content.decode()])

        # Update the progress bar
        pbar.update(1)

        # Sleep for 3 seconds before making the next request
        sleep(2)

# Close the progress bar
pbar.close()
