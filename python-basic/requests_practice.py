import requests
response = requests.get("http://google.com")
print(f"Status Code : {response.status_code}")
print(f"Successful Code : {response.ok}")
print(f" URL : {response.url}")