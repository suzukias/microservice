# microservice
This microservice returns a random number between 1 and a number sent with the request.

How to programmatically REQUEST data:
Make a HTTP GET request to the following endpoint.
Endpoint: 'https://your-microservice-url.com/get_random_num'
Include the max_num parameter in the URL query string to specify the maximum number for the random number generation.

Example call:
```
import requests


url = 'https://szkasm.pythonanywhere.com/'

params = {'max_num': 100}  # You can change this maximum number as needed
response = requests.get(url, params=params)
data = response.json()
random_number = data['random_number']
print(f"Received random number is {random_number}")
```
