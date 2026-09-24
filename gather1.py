# await Promise.all([
#     fetchUsers(),
#     fetchProducts()
#     fetchOrders()
# ])

import asyncio

async def fetch_users():
    return "Users"

async def fetch_products():
    return "Products"

async def fetch_orders():
    return "Orders"

async def main_func():
    result = await asyncio.gather(
        fetch_users(),
        fetch_products(),
        fetch_orders()
    )
    print(result)

asyncio.run(main_func())
