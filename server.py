import zmq
import service

PORT = 1738

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{PORT}")
    print("Server ready.")

    while True:
        message = socket.recv().decode()
        print(f"Recieved message: {message}")

        output = service.service(message)
        print(f"Sending output: {output}")
        socket.send(output.encode())
        print()
