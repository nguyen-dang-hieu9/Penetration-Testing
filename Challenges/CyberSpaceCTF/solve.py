import aiohttp
import asyncio

# endpoint to create posts
url = 'http://localhost/user/posts/create'
# get the accesstoken from the cookies upon login
cookies = {
    "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjU2MTMzNDEsImlhdCI6MTcyNTYxMjc0MSwicm9sZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFiIn0.Z4PuNxovMSW22-xWH53FPvxzc2YplSgP-6NmYcSPOCw"
}

# POST Data
post_data = {
    "title": "Race Condition Test",
    "data": "This is the data for the post"
}

async def send_post(session, semaphore):
    async with semaphore:
        async with session.post(url, json=post_data, cookies=cookies) as response:
            text = await response.text()
            print(f"Response: {text}")

async def main():
    concurrency_limit = 100  # Limit the number of concurrent requests
    semaphore = asyncio.Semaphore(concurrency_limit)

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=concurrency_limit)) as session:
        tasks = [send_post(session, semaphore) for _ in range(100)]
        await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())
