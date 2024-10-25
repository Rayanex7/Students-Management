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
    
    #AddSTD
    if order == '1':
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

    #DelSTD
    elif order == '2':
        #order for search
        client.send(order.encode('utf-8'))
        #receive msg to indicate level
        msg = client.recv(1024).decode('utf-8')
        print(msg)
        lvl = input("")
        client.send(lvl.encode('utf-8'))
        #receive
        msg = client.recv(1024).decode('utf-8')
        print(msg)
        M_code = input("")
        client.send(M_code.encode('utf-8'))
        text = client.recv(1024).decode('utf-8')
        print(text.strip())

    #ModSTD
    elif order == '3':
        #order for search
        client.send(order.encode('utf-8'))
        #receive msg to indicate level
        msg = client.recv(1024).decode('utf-8')
        #In which level the student is in
        print(msg)
        lvl = input("")
        client.send(lvl.encode('utf-8'))
        #receive msg to enter MassarCode
        msg = client.recv(1024).decode('utf-8')
        print(msg)
        M_code = input("")
        client.send(M_code.encode('utf-8'))
        M_code = client.recv(1024).decode('utf-8')
        print(M_code.strip())

    #ListSTD
    elif order == '4':
        client.send(order.encode('utf-8'))
        message = client.recv(1024).decode()
        print(message)
        lvl = input("")
        client.send(lvl.encode('utf-8'))
        list_std = client.recv(1024).decode('utf-8')
        print(list_std)

    #SearchSTD
    elif order == '5':
        #order for search
        client.send(order.encode('utf-8'))
        #receive msg to indicate level
        msg = client.recv(1024).decode('utf-8')
        print(msg)
        lvl = input("")
        client.send(lvl.encode('utf-8'))
        #receive
        msg = client.recv(1024).decode('utf-8')
        print(msg)
        M_code = input("")
        client.send(M_code.encode('utf-8'))
        M_code = client.recv(1024).decode('utf-8')
        print(M_code.strip())
        


if __name__ == '__main__':
    client_side()
