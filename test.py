import asyncio
async def func():
    print("A")
    await asyncio.sleep(1)
    print("B")
async def  main():
    await asyncio.gather(func(), func())
    print("C")
print("R")
asyncio.run(main())
print("D")