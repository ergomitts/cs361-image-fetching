import zmq
import time
import json

def main():
    PORT = 1738
    context = zmq.Context()

    print("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{PORT}")
    print()
    
    while True:
        message = input("Search images of: ")
        if message == "!quit":
            break
        print(f"Sending message: {message}")
        socket.send(message.encode())
        response = socket.recv()
        decoded_response = json.loads(response.decode("utf-8"))
        print(f"Recieved reply: {decoded_response}")
        print()

if __name__ == "__main__":
    main()
