#whitened (XOR) output
import serial
import matplotlib.pyplot as plt
import random

def hrng():
    ser = serial.Serial("COM7", 9600, timeout=1)
    try:
        while True:
            raw_bytes = ser.readline()
            # print(f"Raw Bytes: {raw_bytes}")  # Debugging output
            bs = raw_bytes.decode("utf-8", errors="ignore").strip()
            
            try:
                value = float(bs)
                mapped_value = int((value / 5.0) * 10)
                print(f"Raw: {value}, Mapped: {mapped_value}")
                return mapped_value
            except ValueError:
                continue
    finally:
        ser.close()

class Server:
    def __init__(self, name):
        self.name = name
        self.request_count = 0

    def handle_request(self):
        self.request_count += 1
        return f"Hello from {self.name}, handled {self.request_count} requests"

server_nos=8
servers = [Server(f"Server{i + 1}") for i in range(server_nos)]

def load_balancer(hrng_value):
    hrng_value=  hrng_value ^ random.randint(0,len(servers)) #WHitened version
    selected_server = servers[hrng_value % len(servers)]
    return selected_server.handle_request()

def test_load_balancer(request_count):
    responses = []
    server_loads = {server.name: 0 for server in servers}
    
    for _ in range(request_count):
        random_number = hrng()
        response = load_balancer(random_number)
        responses.append(response)
        print(response)
        
        selected_server_name = response.split(",")[0].split(" ")[-1]
        server_loads[selected_server_name] += 1
    
    print("\nFinal Load Balancing Statistics:")
    for server in servers:
        print(f"{server.name}: {server.request_count} requests handled")
    
    plt.bar(server_loads.keys(), server_loads.values(), color='skyblue')
    plt.xlabel("Servers")
    plt.ylabel("Requests Handled")
    plt.title("Load Balancing Distribution")
    plt.show()
    
    return responses

test_load_balancer(100)
