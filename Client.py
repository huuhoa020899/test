import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host=socket.gethostname()
IP=socket.gethostbyname(Host)
Port=12345
def ConnectServer():
    print('%s'%Host)
    print('%s'%IP)
    s.connect((Host,Port))
    while True:
         print('Server send Messaged',s.recv(1024).decode())
         requerst = input("Hay Nhap thong tin muon gui di:")
         s.send(requerst.encode())
         if len(requerst)>10:
             break
    s.close()
if __name__ == '__main__':
        ConnectServer()