import aiohttp
import asyncio

async def fetch(session, url, sema):
    async with sema, session.get(url) as response:
        return await response.text()

async def main():
    count = 2
    url = 'http://localhost:8080/api/total/10'
    tasks = []
    sema = asyncio.BoundedSemaphore(value=100)
    async with aiohttp.ClientSession() as session:
        for x in range(1,count):
            tasks.append(fetch(session, url, sema))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            print(html[:1])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("done")