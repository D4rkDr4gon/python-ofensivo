import socket

# Define the IP address and port range to scan
ip_address = input("dame el ip: ")
port_range = range(1, 1025)

# Loop through the ports and check if they are open or closed
for port in port_range:
    try:
        # Create a new socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        
        # Attempt to connect to the port
        result = s.connect_ex((ip_address, port))
        
        # Check if the port is open or closed
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket
        s.close()
    except:
        pass
