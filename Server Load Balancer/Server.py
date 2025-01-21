import serial  
import random

def hrng():
    # ser = serial.Serial("COM3", 9600)  
    # try:
    #     while True:
    #         bs = ser.readline().decode("utf-8").strip()
    #         if bs.isdigit():
    #             print(bs)
    #             return int(bs)
    # finally:
    #     ser.close()  
    return  random.getrandbits(32) #use for testing with System's inbuilt RNG
class Server:
    def __init__(self, name):
        self.name = name

    def handle_request(self):
        return f"Hello from {self.name}"

server_count=int(input("How many servers are required? "))
servers = [Server(f"Server{i + 1}") for i in range(server_count)]

def load_balancer(hrng_value):
    selected_server = servers[hrng_value % len(servers)] 
    return selected_server.handle_request()

def test_load_balancer(request_count):
    responses = []
    for _ in range(request_count):
        random_number = hrng() 
        response = load_balancer(random_number)
        responses.append(response)
        print(response)
    return responses
reqs_count=int(input("How many clients are required? "))
test_load_balancer(reqs_count)