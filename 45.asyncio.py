import asyncio
import httpx


async def fetch_users(url):
    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(url)

                if response.status_code in (429, 500, 502, 503, 504):
                    response.raise_for_status()

                return response.json()

        except (httpx.TimeoutException, httpx.HTTPStatusError):
            if attempt == 2:
                raise

            await asyncio.sleep(2**attempt)


fetch_users('http://user.com')