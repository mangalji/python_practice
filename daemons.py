import asyncio

async def prints_quickly():
	while True: 
		await asyncio.sleep(1)
		print("quick!")

async def prints_slowly():
	while True:
		await asyncio.sleep(3)
		print("slow...")

async def main():
	tasks = [asyncio.create_task(prints_quickly(),name="quick"),
			asyncio.create_task(prints_slowly(),name = "slow")]

	# both functions wil run concurently for 7 sec befire cancelling them..
	await asyncio.sleep(7)

	for task in tasks:
		task.cancel()

	await asyncio.wait(tasks)

	print("out!")

if __name__ == "__main__":
	asyncio.run(main()) 