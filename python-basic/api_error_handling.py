import httpx
try:
 endpoint = "https://jsonplaceholder.typicode.com/users/1"
 response = httpx.get(endpoint,timeout=10.0)
 response.raise_for_status()

 user_data = response.json()
 print(user_data["name"])

except httpx.HTTPStatusError as error:
 print(f"HTTP ERROR: {error}")

except httpx.RequestError as error:
    print(f"CONNECTION ERROR: {error}")
