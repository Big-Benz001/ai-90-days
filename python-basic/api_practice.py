import httpx

endpoint = "https://jsonplaceholder.typicode.com/users/1"
response = httpx.get(endpoint)
print (f"Successful Response: {response.status_code}")
user_data = response.json()
print(user_data["name"])
print(user_data["email"])
print(user_data["address"]["city"])
print(user_data["company"]["name"])

