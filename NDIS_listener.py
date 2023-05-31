import socket
import os 

def listener():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 444)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        data, address = sock.recvfrom(4096)

        print('received {} bytes from {}'.format(
            len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print('sent {} bytes back to {}'.format(
                sent, address))
            

def main():
    listener()

if __name__ == "__main__":
    main()
