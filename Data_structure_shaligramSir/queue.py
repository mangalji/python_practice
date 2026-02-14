queue = []

queue.append("a")
queue.append("b")
queue.append("c")

print("queue: ",queue)

frontElement = queue[0]
print("frontElement: ",frontElement)

poppedElement = queue.pop(0)
print("poppedElement: ",poppedElement)
print("queue after dequeue: ",queue)

if len(queue) >= 0:
	print("queue is empty? : ",False)
else:
	print("queue is empty? : ",True)

print("size: ",len(queue))