import zmq
import time

PORT = 1738
context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://localhost:{PORT}")
print()

message = "Client's string"
print(f"Sending message: {message}")
socket.send(message.encode())
response = socket.recv().decode()
print(f"Recieved reply: {response}")
print()

message = "Client's second string"
print(f"Sending message: {message}")
socket.send(message.encode())
response = socket.recv().decode()
print(f"Recieved reply: {response}")
print()
