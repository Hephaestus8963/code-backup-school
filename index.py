import asyncio, os
from concurrent.futures import ThreadPoolExecutor

current = 1

async def ainput(prompt: str = ''):
    with ThreadPoolExecutor(1, 'ainput') as executor:
        global current
        current = int((await asyncio.get_event_loop().run_in_executor(executor, input, prompt)).rstrip())


async def count(end):
    global current
    while current < end:
        os.system('cls')
        print(f"Current: {current}")
        current += 2
        await asyncio.wait_for(ainput("Relabel?"), 10)


    
    


asyncio.run(count(100))