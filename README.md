## Welcome to nutrients microservice!

This is a food essential nutrients scraper microservice. The communication pipe is socket.
  

### How to REQUEST data from the microservice:

The client needs to send a string of the food name to the microservice. Example:

  
```python
import zmq
import time
 
context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5577")

# send name of the food
toSend = "fish"
print("sending: " + toSend + "...")
socket.send(toSend.encode("utf-8"))

time.sleep(1)
print("Waiting to receive...")

# print the returned nutrients information
print(socket.recv().decode("utf-8"))
```


### How to RECEIVE data from the microservice:

The microservice receives the food name, , and returns the requested essential nutrients, which are protein, calcium and iron, back to the client in json format.
Example:
```json
{"protein": 23.9, "calcium": 12.0, "iron": 0.94}
```
  


Please see the following UML sequence diagram showing how requesting and receiving data work:

![test](https://user-images.githubusercontent.com/25577805/199128097-8e730a70-1a2c-496c-be87-3231ec7402a3.png)
