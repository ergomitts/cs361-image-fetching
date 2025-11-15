import zmq
import service
import json

PORT = 1738

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{PORT}")
    print("Server ready.")

    while True:
        message = socket.recv().decode("utf-8")
        print(f"Recieved message: {message}")

        output = service.get_links(message)
        print(f"Sending output: {output}")
        json_output = json.dumps(output)
        socket.send(json_output.encode("utf-8"))
        print()

if __name__ == "__main__":
    main()