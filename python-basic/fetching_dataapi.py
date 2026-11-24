import httpx
import json

try:
 endpoint = "https://jsonplaceholder.typicode.com/users/1"
 response = httpx.get(endpoint,timeout=10.0)
 response.raise_for_status()

 user_data = response.json()

 with open ("user_data.json","w") as file:
  json.dump(user_data,file,indent=4)
  

except httpx.HTTPStatusError as error:
 print(f"HTTP ERROR: {error}")

except httpx.RequestError as error:
    print(f"CONNECTION ERROR: {error}")
