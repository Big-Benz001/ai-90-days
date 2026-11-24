import httpx
import asyncio
import json
async def fetch_user(client, user_id):
    endpoint = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = await client.get(endpoint)
    response.raise_for_status()

    user_data = response.json()

    return user_data

async def get_users():
    async with httpx.AsyncClient() as client:
        users = await asyncio.gather(
           fetch_user(client,1), 
           fetch_user(client,2),
           fetch_user(client,3), 
           fetch_user(client,4),
           fetch_user(client,5)
        )
        user_count = -1
    for user in users :
     user_count += 1
     print(users[user_count]["name"])

    with open("users_data.json","w") as file:
                json.dump(users,file,indent=4)
    print(f"Successfully saved {len(users)} users to users_data.json")
asyncio.run(get_users())