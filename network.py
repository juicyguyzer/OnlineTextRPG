import socket
import json

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.130"
        self.port = 5000
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
n = Network()

config = {}
def reload_config():
    with open("conf.json", "r") as f:
        global config
        config = json.load(f)
    print("Reloaded Config!")

reload_config()

while 1:
    i = input("> ")
    n.send(config["username"] + ": " + i)
