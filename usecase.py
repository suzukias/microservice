# this file shows an example of how to send request to get random number.
import requests


url = 'https://szkasm.pythonanywhere.com/'

params = {'max_num': 100}  # You can change this maximum number as needed
response = requests.get(url, params=params)
data = response.json()
random_number = data['random_number']
print(f"Received random number is {random_number}")
