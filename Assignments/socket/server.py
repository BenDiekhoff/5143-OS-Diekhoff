import socket

def Main():

    host = '192.168.1.6' #Server ip
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    iplist =[]
    while True:
        data, addr = s.recvfrom(1024)
        if addr not in iplist:
            iplist.append(addr)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        for addr in iplist:
            s.sendto(data.encode('utf-8'), addr)
    s.close()

if __name__=='__main__':
    Main()