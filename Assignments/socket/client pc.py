import socket
import msvcrt as m

def Main():

    host='192.168.1.6' #client ip
    port = 4006

    server = ('192.168.1.6', 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    message = input("-> ")
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__=='__main__':
    Main()