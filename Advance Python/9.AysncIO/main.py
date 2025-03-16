import asyncio

async def task1():
    print("Task 1: Started")
    asyncio.sleep(5)  # Simulate delay
    print("Task 1: Completed")

async def task2():
    print("Task 2: Started")
    await asyncio.sleep(1)  # Simulate delay
    print("Task 2: Completed")

async def main():
    await task1()  # Runs first
    await task2()  # Runs only after task1() finishes

asyncio.run(main())

# print("*"*50)

# async def task3():
#     print("Task 3: Started")
#     await asyncio.sleep(10)
#     print("Task 3: Completed")

# async def task4():
#     print("Task 4: Started")
#     await asyncio.sleep(5)
#     print("Task 4: Completed")

# async def main():
#     await asyncio.gather(task3(), task4())  # Run both tasks concurrently

# asyncio.run(main())
