import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.60.90", 55555))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        message = input('')
        client.send(message.encode("utf-8"))
        
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()