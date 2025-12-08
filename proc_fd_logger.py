'''Here’s a concise but instructive project that blends process management with file-descriptor handling in Python.
It’s small enough for a 1–2 hour lab while giving students real exposure to how UNIX processes and file descriptors work.


---

🗂️ Project: Process Logger with File-Descriptor Tracking

Goal

Create a command-line tool that spawns one or more child processes, logs their output to files, and reports the file descriptors used for standard input/output/error.


---

Core Requirements

1. Command Syntax

python proc_fd_logger.py <command> [args...]

Example:

python proc_fd_logger.py ping -c 4 google.com


2. Spawn a Child Process

Use subprocess.Popen to start the given command.

Redirect the child’s stdout and stderr to separate log files (e.g., stdout.log, stderr.log).

Keep the parent process running until the child exits.



3. File-Descriptor Report

Immediately after starting the child, print a table like:

FD   Target
0    stdin
1    stdout -> stdout.log
2    stderr -> stderr.log

Show the actual file descriptor integers returned by Python (p.stdout.fileno(), etc.).



4. Resource Cleanup

Wait for the child to finish.

Close all file descriptors in the parent process.

Append the child’s exit code to a process_history.json file (append-only).





---

Optional Enhancements

Multiple Children: Add a --parallel N option to run N copies of the same command and track each child’s PIDs and descriptors.

Interactive Input: Allow sending a short message to the child’s stdin and record the descriptor used.

Descriptor Reuse Check: After closing, print whether the descriptor numbers are reused by opening a new file.



---

Implementation Hints

subprocess.Popen with stdout=open("stdout.log","wb"), stderr=open("stderr.log","wb").

fileno() gives the OS-level descriptor number.

os.getpid() and p.pid to track parent and child PIDs.

Use json to append a record like:

{"timestamp": "2025-09-16T10:30Z", "pid": 12345, "exit_code": 0}



---

Example Run

$ python proc_fd_logger.py ls -l
Parent PID: 5678
Child PID : 5682
FD   Target
0    stdin
1    stdout -> stdout.log  (fd=3)
2    stderr -> stderr.log  (fd=4)
Process exited with code 0
History updated in process_history.json


---

Learning Outcomes

Process control: spawning, waiting, capturing output.

File descriptors: understanding 0, 1, 2 and custom descriptor numbers.

Resource management: explicit closing of descriptors.

Logging & JSON: maintaining a lightweight run history.


This compact assignment gives students practical insight into how Python interfaces with the underlying Unix process model and the concept of file descriptors while staying achievable in a short session.'''

import os
import sys
import argparse
import subprocess
import json
import datetime
from multiprocessing import Process


# parser = argparse.ArgumentParser()
# args = parser.parse_args()

# parser.add_argument('ls', )




# tank_to_fish = {
#     "tank_a": "shark, tuna, herring",
#     "tank_b": "cod, flounder",
# }

# parser = argparse.ArgumentParser(description="List fish in aquarium.")
# parser.add_argument("tank", type=str)
# args = parser.parse_args()

# fish = tank_to_fish.get(args.tank)
# print(fish)

# print(sys.argv)

parser = argparse.ArgumentParser("simple_example")
# parser.add_argument("counter", help="An integer will be increased by 1 and printed.",type=int)
parser.add_argument("--product_id", dest='product_id', type=str, help="add product id")
args = parser.parse_args()
print(args.product_id)
# print(args.counter + 1)



