def server_side():        
    import socket

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.1.117"
    port = 65301

    conn = (host, port)

    server.bind(conn)

    server.listen(1)

    print(f"SERVER LISTENING: {conn}")

    client, addr = server.accept()
    print(f"Got connection from : {addr}")

    #Menu
    menu = (
        "********** Abderrahman Ibn Ghazala **********\n"
        "1- Add Student\n"
        "2- Delete Student\n"
        "3- Modify Student\n"
        "4- List Students\n"
        "5- Search Student\n"
        "6- Exit\n"
        "**********************************************"
    )

    client.send(menu.encode('utf-8'))

    order = client.recv(1024).decode('utf-8')

    if (order == "1"):
        level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
        client.send(level.encode('utf-8'))

        choice = client.recv(1024).decode('utf-8')

        if (choice == "1"):
            filepath = "/home/rayane/School/Common_Core"
            client.send("First Name: ".encode('utf-8'))
            Fname = client.recv(1024).decode('utf-8')

            client.send("Last Name: ".encode('utf-8'))
            Lname = client.recv(1024).decode('utf-8')
            
            client.send("Age: ".encode('utf-8'))
            Age = client.recv(1024).decode('utf-8')

            client.send("MassarCode: ".encode('utf-8'))
            M_code = client.recv(1024).decode('utf-8')

            with open(filepath, "r") as fl:
                print(M_code)
                for lines in fl:
                    if M_code in lines:
                        error = "[ERROR] : This Massar code already exist !"
                        client.send(error.encode('utf-8'))
                        exit()
            
                    
            client.send("Past year degree: ".encode('utf-8'))
            Degree = client.recv(1024).decode('utf-8')

            client.send("Sector: ".encode('utf-8'))
            Sec = client.recv(1024).decode('utf-8')

            data = "First name: {Fname}\t Last name: {Lname}\t Age: {Age}\t MassarCode: {M_code}\t\t Past year degree: {Degree:.2f}\t Sector: {Sec}\n"
            
            file = open(filepath, "a")
            file.write(data.format(Fname=Fname, Lname=Lname, Age=Age, M_code=M_code, Degree=float(Degree), Sec=Sec))

            

            client.close()
            server.close()

        elif (choice == "2"):
            filepath = "/home/rayane/School/1st_Bac"
        elif (choice == "3"):
            filepath = "/home/rayane/School/2nd_Bac"
        else:
            print("Error, enter a valid number\n")
            return


    
    
    
    
    
    


if __name__ == '__main__':
    server_side()

