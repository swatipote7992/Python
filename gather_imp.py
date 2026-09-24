# Expected Output
# Users
# Orders
# Products

import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
#         try:
#           response.raise_for_status()
#       except httpx.HTTPStatusError as e:
#           print(f"API failed: {e}")
        return response.json()
    

async def main():
    results = await asyncio.gather(
        fetch("https://api.example.com/users"),
        fetch("https://api.example.com/orders"),
        fetch("https://api.example.com/products")
    )

    users,orders,products = results

    print(users)
    print(orders)
    print(products)

asyncio.run(main())

# FastAPI Example
# @app.get("/dashboard")
# async def dashboard():

#     users, orders, products = await asyncio.gather(
#         get_users(), get_orders(), get_products()
#     )

#     return {"users": users, "orders": orders, "products": products}