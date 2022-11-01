import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5577")

# send name of the food
toSend = "dogfood"
print("sending: " + toSend + "...")
socket.send(toSend.encode("utf-8"))

time.sleep(1)

print("Waiting to receive...")
# print the returned nutrients information
print(socket.recv().decode("utf-8"))
