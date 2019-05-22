import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(('127.0.0.1', 65432))
s.listen()

conn, address = s.accept()
print("connesso")
while True:
    dataByte = conn.recv(4096)
    print(dataByte.decode())
    if dataByte.decode() == "":
        break
    stringaDaInviare = input()
    conn.sendall(stringaDaInviare.encode())
    if stringaDaInviare == "":
        break
s.close()
