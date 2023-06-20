import socket
import os 

def listener():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('192.168.1.206', 444)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        data, address = sock.recvfrom(4096)

        print('received {} bytes from {}'.format(
            len(data), address))
        print(data)

        if data:
            # open a new file in current folder to write to the data
            with open("data.txt", "wb") as f:
                f.write(data)
            # close the file
            

            

            

def main():
    listener()

if __name__ == "__main__":
    main()
