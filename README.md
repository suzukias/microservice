# microservice
This microservice returns a random number between 1 and a number sent with the request.

How to programmatically REQUEST data:
Make a HTTP GET request to the following endpoint.

Endpoint: 'https://szkasm.pythonanywhere.com/'

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

How to programmatically RECEIVE data:

The microservice responds with JSON data containing the generated random number in the following format:
```
{
    "random_number": 42 
}
```
Handle the received random number like the above example.

UML sequence diagram:


![image](https://github.com/suzukias/microservice/assets/114200275/014d4ba1-f602-4540-860b-f498ae0b093c)
