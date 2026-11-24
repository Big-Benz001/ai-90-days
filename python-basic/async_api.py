import httpx
import asyncio

async def get_user():
   async with httpx.AsyncClient()as client:
    response = await client.get("https://jsonplaceholder.typicode.com/users/1")
    user_data = response.json()
    print(user_data["name"])

asyncio.run(get_user())

