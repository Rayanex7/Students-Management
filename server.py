import socket
import threading

host = "192.168.1.117"
port = 65301

conn = (host, port)

def AddSTD(client):
    level = "In which level the student is in : \n1- Common Core\n2- 1st Baccalaureate\n3- 2nd Baccalaureate"
    client.send(level.encode('utf-8'))

    choice = client.recv(1024).decode('utf-8')

    if (choice == "1"):
        filepath = "/home/rayane/School/Common_Core"
        
    elif (choice == "2"):
        filepath = "/home/rayane/School/1st_Bac"
        
    elif (choice == "3"):
        filepath = "/home/rayane/School/2nd_Bac"
        
    else:
        print("Error, enter a valid number\n")
        return
    
    client.send("First Name: ".encode('utf-8'))
    Fname = client.recv(1024).decode('utf-8')

    client.send("Last Name: ".encode('utf-8'))
    Lname = client.recv(1024).decode('utf-8')
    
    client.send("Age: ".encode('utf-8'))
    Age = client.recv(1024).decode('utf-8')

    client.send("MassarCode: ".encode('utf-8'))
    M_code = client.recv(1024).decode('utf-8')

    with open(filepath, "r") as fl:
        for lines in fl:
            if M_code in lines:
                error = "[ERROR] : This Massar code already exist !"
                client.send(error.encode('utf-8'))
                return
    
            
    client.send("Past year degree: ".encode('utf-8'))
    Degree = client.recv(1024).decode('utf-8')

    client.send("Sector: ".encode('utf-8'))
    Sec = client.recv(1024).decode('utf-8')

    data = "First name: {Fname}\t Last name: {Lname}\t Age: {Age}\t MassarCode: {M_code}\t\t Past year degree: {Degree:.2f}\t Sector: {Sec}\n"
    
    file = open(filepath, "a")
    file.write(data.format(Fname=Fname, Lname=Lname, Age=Age, M_code=M_code, Degree=float(Degree), Sec=Sec))

    client.send("[Success!] Student added successfuly .".encode('utf-8'))
    return

def ListSTD(client):
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    client.send(level.encode('utf-8'))
    lvl = client.recv(1024).decode('utf-8')
    
    if lvl == '1':
        filepath = "/home/rayane/School/Common_Core"
    
    elif lvl == '2':
        filepath = "/home/rayane/School/1st_Bac"
        
    elif lvl == '3':
        filepath = "/home/rayane/School/2nd_Bac"
    
    with open (filepath, "r") as file:
        lines = file.read()
        client.send(lines.encode('utf-8'))
        return
        
def SearchSTD(client):
    code = False
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    client.send(level.encode('utf-8'))
    lvl = client.recv(1024).decode('utf-8')
    Mcode = "MassarCode: "
    client.send(Mcode.encode('utf-8'))
    M_code = client.recv(1024).decode('utf-8')

    if lvl == '1':
        filepath = "/home/rayane/School/Common_Core"   
    
    elif lvl == '2':
        filepath = "/home/rayane/School/1st_Bac"

    elif lvl == '3':
        filepath = "/home/rayane/School/2nd_Bac"
        
    with open (filepath, "r") as file:
        for lines in file:
            if M_code in lines:
                code = True
                client.send(lines.encode('utf-8'))
        if code == False:
            client.send("[ERROR!]: MassarCode Not Found !".encode('utf-8'))
            return
        return            
    
def DelSTD(client):
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    client.send(level.encode('utf-8'))
    lvl = client.recv(1024).decode('utf-8')
    Mcode = "MassarCode: "
    client.send(Mcode.encode('utf-8'))
    M_code = client.recv(1024).decode('utf-8')

    if lvl == '1':
        Massar = False
        filepath = "/home/rayane/School/Common_Core"
        
    
    elif lvl == '2':
        Massar = False
        filepath = "/home/rayane/School/1st_Bac"
        

    elif lvl == '3':
        Massar = False
        filepath = "/home/rayane/School/2nd_Bac"
        
    with open (filepath, "r") as file:
        for lines in file:
            if M_code in lines:
                Massar = True
        if Massar:
            temp = ""
            
            with open (filepath, "r") as file:
                for lines in file:
                    if M_code not in lines:
                        temp += lines

            with open (filepath, "w") as file:
                file.write(temp)
            client.send("Student Deleted Sucessfuly !".encode('utf-8'))
    
        else:
            client.send("[ERROR!]: MassarCode Not Found !".encode('utf-8'))
            return
    return
        
def ModSTD(client):
    code = False
    temp = ""
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    client.send(level.encode('utf-8'))
    lvl = client.recv(1024).decode('utf-8')
    Mcode = "MassarCode: "
    client.send(Mcode.encode('utf-8'))
    M_code = client.recv(1024).decode('utf-8')

    if lvl == '1':
        filepath = "/home/rayane/School/Common_Core"
    
    elif lvl == '2':
        filepath = "/home/rayane/School/1st_Bac"
        

    elif lvl == '3':
        filepath = "/home/rayane/School/2nd_Bac"
    
    with open(filepath, "r") as file:
        for lines in file:
            if M_code not in lines:
                temp += lines

        with open (filepath, "r") as file:
            for lines in file:
                if M_code in lines:
                    client.send(lines.encode('utf-8'))
                    code = True
                    
                

        if code:            
            client.send("First Name: ".encode('utf-8'))
            New_Fname = client.recv(1024).decode('utf-8')
            
            client.send("Last Name: ".encode('utf-8'))
            New_Lname = client.recv(1024).decode('utf-8')
            
            client.send("Age: ".encode('utf-8'))
            New_Age = client.recv(1024).decode('utf-8')

            client.send("MassarCode: ".encode('utf-8'))
            New_M_code = client.recv(1024).decode('utf-8')
            with open(filepath, "r") as file:
                for lines in file:
                    if New_M_code in lines:
                        code = True
                        client.send("[ERROR!] This MassarCode is present: ".encode('utf-8'))
                        return
            
            client.send("Past year degree: ".encode('utf-8'))
            New_Degree = client.recv(1024).decode('utf-8')

            client.send("Sector: ".encode('utf-8'))
            New_Sector = client.recv(1024).decode('utf-8')

            data = "First name: {New_Fname}\t Last name: {New_Lname}\t Age: {New_Age}\t MassarCode: {New_M_code}\t\t Past year degree: {New_Degree:.2f}\t Sector: {New_Sector}\n"

            with open(filepath, "w") as file:
                file.write(temp)
            with open(filepath, "a") as file:
                file.write(data.format(New_Fname=New_Fname, New_Lname=New_Lname, New_Age=New_Age, New_M_code=New_M_code, New_Degree=float(New_Degree), New_Sector=New_Sector))

            client.send("Student Modified successfuly".encode('utf-8'))

        else:
            client.send("[ERROR!]: MassarCode Not Found !".encode('utf-8'))
            return
    return

def SendMenu(client):
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

    if order == '1':
        AddSTD(client)
    elif order == '2':
        DelSTD(client)
    elif order == '3':
        ModSTD(client)
    elif order == '4':
        ListSTD(client)
    elif order == '5':
        SearchSTD(client)
    elif order == '6':
        client.close()
        return False  # Indicate to exit the loop and function
    else:
        client.send("[ERROR!] Enter A Valid Number !".encode('utf-8'))
    return True

def handle_clients(client, addr):
    print(f"[NEW CONNECTION] {addr} Connected.")
    
    while True:
        try:
            if not SendMenu(client):
                break  # Exit loop and disconnect if user chooses to exit
        except Exception as e:
            print(f"[ERROR] Client {addr} encountered an error: {e}")
            break
    print(f"[DISCONNECTED] Client {addr} Disconnected")
    print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 2}")
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((conn))
    server.listen(5)
    print(f"SERVER LISTENING ON PORT {port}")
 
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")

if __name__ == '__main__':
    main()