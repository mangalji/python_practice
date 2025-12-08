'''import asyncio
import time

async def my_func():
	start = time.time()
	sleep_func = asyncio.sleep(2)
	print(time.time() - start)
	await sleep_func
	print(time.time() - start)

asyncio.run(my_func)()'''

import asyncio
import random
import time 

async def task(name):
	await asyncio.sleep(random.randint(1,3))
	return f"{name} finished"

async def main():
	tasks = [task(f"Task {i}") for i in range(1,4)]

	start_time = time.time()
	# for coro in asyncio.as_completed(tasks):
	# 	result = await coro
	# 	end_time = time.time()
	# 	print(end_time - start_time, result)

	results = await asyncio.gather(*tasks)
	end_time = time.time()

	print(f"gather look {end_time - start_time}")

	start_printing = time.time()
	for result in results:
		print(time.time() - start_printing, results)
		

	print(f"Total time {time.time() - start_time}")

if __name__ == '__main__':
	asyncio.run(main())