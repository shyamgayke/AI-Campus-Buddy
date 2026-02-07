import requests

# Test the feedback endpoint
url = 'http://127.0.0.1:5000/feedback'

# Normal text
data = {'text': 'This is a sample assignment text about climate change. It discusses the impact on the environment and suggests solutions.'}
response = requests.post(url, json=data)
print("Normal Text Status Code:", response.status_code)
print("Normal Text Response:", response.json())

# Empty text
data_empty = {'text': ''}
response_empty = requests.post(url, json=data_empty)
print("Empty Text Status Code:", response_empty.status_code)
print("Empty Text Response:", response_empty.json())

# Short text
data_short = {'text': 'Hi'}
response_short = requests.post(url, json=data_short)
print("Short Text Status Code:", response_short.status_code)
print("Short Text Response:", response_short.json())

# Long text
data_long = {'text': 'Climate change is a significant global issue that affects various aspects of our lives. It is caused by human activities such as burning fossil fuels, deforestation, and industrial processes. The consequences include rising temperatures, melting ice caps, sea level rise, and extreme weather events. To mitigate climate change, we need to transition to renewable energy sources, reduce carbon emissions, and promote sustainable practices. Governments, businesses, and individuals all have a role to play in addressing this challenge. Education and awareness are key to fostering a culture of environmental responsibility. By taking action now, we can work towards a more sustainable future for generations to come.'}
response_long = requests.post(url, json=data_long)
print("Long Text Status Code:", response_long.status_code)
print("Long Text Response:", response_long.json())

# Grammatically poor text
data_poor = {'text': 'Climate change bad. We need stop it. Use less car. No more pollution.'}
response_poor = requests.post(url, json=data_poor)
print("Poor Grammar Text Status Code:", response_poor.status_code)
print("Poor Grammar Text Response:", response_poor.json())

# Off-topic text
data_off = {'text': 'I love playing video games. My favorite is Fortnite. It is very fun and exciting.'}
response_off = requests.post(url, json=data_off)
print("Off-Topic Text Status Code:", response_off.status_code)
print("Off-Topic Text Response:", response_off.json())

# Special characters
data_special = {'text': 'Climate change: @#$%^&*()!'}
response_special = requests.post(url, json=data_special)
print("Special Characters Text Status Code:", response_special.status_code)
print("Special Characters Text Response:", response_special.json())
