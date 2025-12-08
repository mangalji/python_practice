import psutil

while True:
	virt_memory = psutil.virtual_memory()

	virt_disk = psutil.disk_usage('/')

	network_stats = psutil.net_io_counters()

	print("cpu usage in percent: ", psutil.cpu_percent(interval=1))
	print(f"memory usage by programmes, in percent: {virt_memory.percent}, in size: {virt_memory.used//(1024*1024)}MB out of ({virt_memory.total//(1024*1024)})MB")
	print(f"Disk usage in percent: {virt_disk.percent}, in size {virt_disk.used//(1024**3)}GB out of {virt_disk.total//(1024**3) }GB")
	print(f"Network stats: send stats-{network_stats.bytes_sent // (1024*1024)}MB, received stats-{network_stats.bytes_recv//(1024*1024) }GB")