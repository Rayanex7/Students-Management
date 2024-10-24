def client_side():
    import socket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "192.168.1.117"
    port = 65301

    conn = (host, port)

    client.connect(conn)

    print(f"Connected to server at {conn}")
    
    #Receive menu
    message = client.recv(1024).decode('utf-8')
    print(message)

    #Send order to do
    order = input()
    client.send(order.encode('utf-8'))

    #receive instructions
    message = client.recv(1024).decode('utf-8')
    print(message)

    order = input()
    client.send(order.encode('utf-8'))

    #entering First name
    message = client.recv(1024).decode('utf-8')
    print(message)
    Fname = input("")
    client.send(Fname.encode('utf-8'))
    
    #entering Last name
    message = client.recv(1024).decode('utf-8')
    print(message)
    Lname = input("")
    client.send(Lname.encode('utf-8'))

    #entering Age
    message = client.recv(1024).decode('utf-8')
    print(message)
    Age = input("")
    client.send(Age.encode('utf-8'))

    #entering MassarCode
    message = client.recv(1024).decode('utf-8')
    print(message)
    M_code = input("")
    client.send(M_code.encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == "[ERROR] : This Massar code already exist !":
        print(message)
        exit()
    else:
        print(message)
        degree = input("")
        client.send(degree.encode('utf-8'))

    #Inputing sector
    message = client.recv(1024).decode('utf-8')
    print(message)
    sector = input("")
    client.send(sector.encode('utf-8'))

    client.close()


if __name__ == '__main__':
    client_side()
