# microservice
**How to Programmatically Request Data:**

Make an HTTP GET request to the following endpoint:

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

**How to Programmatically Receive Data:**

The microservice responds with JSON data containing the generated random number in the following format:
```
{
    "random_number": 12
}
```
Handle the received random number as the example above.

**UML Sequence Diagram:**

![image](https://github.com/suzukias/microservice/assets/114200275/f4d39943-9a71-4c9f-8e10-df68af13be52)
