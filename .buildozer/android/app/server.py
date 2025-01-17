import socket

host = '127.0.0.1'  # Standard loopback interface address (localhost)
port = 8888  # Port to listen on (non-privileged ports are > 1023)
print("Listening to incoming messages:")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)
