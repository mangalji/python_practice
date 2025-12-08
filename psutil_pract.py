import psutil

# Get overall CPU usage as a percentage
print(psutil.cpu_percent(interval=1))
# Per-CPU usage
print(psutil.cpu_percent(interval=1, percpu=True))

# Number of physical/logical cores
print(psutil.cpu_count(logical=False))
print(psutil.cpu_count(logical=True))

# Virtual memory
print(psutil.virtual_memory())

# Swap memory
print(psutil.swap_memory())

# Disk partitions
print(psutil.disk_partitions())
print('------------------------')
# Disk usage
print(psutil.disk_usage('/'))
print('------------------------')
# Disk I/O
print(psutil.disk_io_counters())

# Network I/O
print(psutil.net_io_counters())
print('----------------------')
# Network interfaces
print(psutil.net_if_addrs())
print('----------------------')
print(psutil.net_if_stats())


# List all process IDs
print(psutil.pids())
print('-----------------')
# Get a specific process
p=''
for pid in psutil.pids():
	p = psutil.Process(pid)

# Common process info
print(p.name())
print('-----------------')
print(p.status())
print('-----------------')
print(p.cpu_percent(interval=1))
print('-----------------')
print(p.memory_info())
print('-----------------')
print(p.open_files())
print('-----------------')
print(p.connections())


# Boot time
print(psutil.boot_time())
print('----------------')
# Logged-in users
print(psutil.users())
