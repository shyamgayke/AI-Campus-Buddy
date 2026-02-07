import requests
import json

# Test the /feedback endpoint
url = 'http://127.0.0.1:5000/feedback'
data = {'text': 'This is a sample assignment text for testing the feedback API.'}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.json()}')
except Exception as e:
    print(f'Error: {e}')
