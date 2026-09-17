import asyncio

async def func():
    print("T1 started")
    await asyncio.sleep(1)# if sleep(2) is used, then T2 will start after T1 completes
    print("T1 completed")

async def func2():
    print("T2 started")
    await asyncio.sleep(1)
    print("T2 completed")

async def main():
    await asyncio.gather(func(), func2())
asyncio.run(main())


#perameter passing in async function is not possible, so we can use asyncio.create_task() to pass parameters to async function.
import asyncio
async def func3(n):
    print(f"{n} started")
    await asyncio.sleep(1)
    print(f"{n} completed")
async def main2():
    await asyncio.gather(func3("proposal"), func3("accepted"))
asyncio.run(main2())