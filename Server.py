import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def GetHost():
    return socket.gethostname()
def Connection():
    s.bind((GetHost(),12345))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("dia chi add",addr)
        while True:
            k = input("Hay Nhap Thong tin can gui di:")
            if len(k)>10:
                break
            c.send(k.encode())
            print('Client request',c.recv(1025).decode())
        c.close()
if __name__ == '__main__':
    Connection()