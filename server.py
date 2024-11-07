import socket
import threading
import ssl
import os
import json
import uuid


class protocole:
    def __init__(self, client):
        self.client = client
        

    def Protocole(self, HOST, CLIENT, TYPE, DATA):
        protocole = {  "FROM" : f"{HOST}",
                        "TO"   : f"{CLIENT}",
                        "TYPE" : f"{TYPE}",
                        "WHAT" : f"{DATA}",
                        }
        return protocole
      
def assign_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"Cannot assign an IPv4 Address: {[e]}")
    finally:
        return ip
    
IP = assign_ip()
port = 65300

conn = (IP, port)

def dic_to_json(msg):
    new_msg = json.dumps(msg)
    return new_msg

def json_to_dic(msg):
    new_msg = json.loads(msg)
    return new_msg

def AddSTD(client):
    level = "In which level the student is in : \n1- Common Core\n2- 1st Baccalaureate\n3- 2nd Baccalaureate"
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(level), level)
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_choice = client.recv(1024).decode('utf-8')
    choice = json_to_dic(json_choice)

    if (choice["WHAT"] == "1"):
        filepath = "/home/rayane/School/Common_Core"
        
    elif (choice["WHAT"] == "2"):
        filepath = "/home/rayane/School/1st_Bac"
        
    elif (choice["WHAT"] == "3"):
        filepath = "/home/rayane/School/2nd_Bac"
        
    else:
        print("Error, enter a valid number\n")
        return
    dic_msg = new_client.Protocole(IP, get_client_IP(), type("First Name: "), "First Name: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Fname = client.recv(1024).decode('utf-8')
    Fname = json_to_dic(json_Fname)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Last Name: "), "Last Name: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Lname = client.recv(1024).decode('utf-8')
    Lname = json_to_dic(json_Lname)
    
    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Age: "), "Age: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Age = client.recv(1024).decode('utf-8')
    Age = json_to_dic(json_Age)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Massar Code: "), "Massar Code: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    M_code= json_to_dic(json_M_code)

    with open(filepath, "r") as fl:
        for lines in fl:
            if M_code["WHAT"] in lines:
                error = "[ERROR] : This Massar code already exist !"
                client.send(error.encode('utf-8'))
                return
            else:
                continue
    
            
    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Past Year Degree: "), "Past Year Degree: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Degree = client.recv(1024).decode('utf-8')
    Degree = json_to_dic(json_Degree)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Sector: "), "Sector: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Sec = client.recv(1024).decode('utf-8')
    Sec = json_to_dic(json_Sec)

    data = "First name: {Fname}\t Last name: {Lname}\t Age: {Age}\t MassarCode: {M_code}\t\t Past year degree: {Degree:.2f}\t Sector: {Sec}\n"
    
    file = open(filepath, "a")
    file.write(data.format(Fname=Fname["WHAT"], Lname=Lname["WHAT"], Age=Age["WHAT"], M_code=M_code["WHAT"], Degree=float(Degree["WHAT"]), Sec=Sec["WHAT"]))

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("[SUCCESS!]: Student Added Sucessffuly "), "[SUCCESS!]: Student Added Sucessffuly ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))
    return

def ListSTD(client):
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(level), level)
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))
    json_lvl = client.recv(1024).decode('utf-8')
    lvl = json_to_dic(json_lvl)
    
    if lvl["WHAT"] == '1':
        filepath = "/home/rayane/School/Common_Core"
    
    elif lvl["WHAT"] == '2':
        filepath = "/home/rayane/School/1st_Bac"
        
    elif lvl["WHAT"] == '3':
        filepath = "/home/rayane/School/2nd_Bac"
    
    with open (filepath, "r") as file:
        lines = file.read()
        dic_msg = new_client.Protocole(IP, get_client_IP(), type(lines), lines)
        json_msg = dic_to_json(dic_msg)
        client.send(json_msg.encode('utf-8'))
        return
        
def SearchSTD(client):
    code = False
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(level), level)
    msg = dic_to_json(dic_msg)
    client.send(msg.encode('utf-8'))

    json_lvl = client.recv(1024).decode('utf-8')
    lvl = json_to_dic(json_lvl)

    Mcode = "MassarCode: "
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    msg = dic_to_json(dic_msg)
    client.send(msg.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    M_code = json_to_dic(json_M_code)

    if lvl["WHAT"] == '1':
        filepath = "/home/rayane/School/Common_Core"   
    
    elif lvl["WHAT"] == '2':
        filepath = "/home/rayane/School/1st_Bac"

    elif lvl["WHAT"] == '3':
        filepath = "/home/rayane/School/2nd_Bac"
        
    with open (filepath, "r") as file:
        for lines in file:
            if M_code["WHAT"] in lines:
                code = True
                dic_msg = new_client.Protocole(IP, get_client_IP(), type(lines), lines)
                msg = dic_to_json(dic_msg)
                client.send(msg.encode('utf-8'))
        if code == False:
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("[ERROR!]: MassarCode Not Found !"), "[ERROR!]: MassarCode Not Found !")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            return
        return            
    
def DelSTD(client):
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(level), level)
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_lvl = client.recv(1024).decode('utf-8')
    lvl = json_to_dic(json_lvl)

    Mcode = "MassarCode: "
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    msg = dic_to_json(dic_msg)
    client.send(msg.encode('utf-8'))

    m_code = client.recv(1024).decode('utf-8')
    M_code = json_to_dic(m_code)

    if lvl["WHAT"] == '1':
        Massar = False
        filepath = "/home/rayane/School/Common_Core"
        
    
    elif lvl["WHAT"] == '2':
        Massar = False
        filepath = "/home/rayane/School/1st_Bac"
        

    elif lvl["WHAT"] == '3':
        Massar = False
        filepath = "/home/rayane/School/2nd_Bac"
        
    with open (filepath, "r") as file:
        for lines in file:
            if M_code["WHAT"] in lines:
                Massar = True
        if Massar:
            temp = ""
            
            with open (filepath, "r") as file:
                for lines in file:
                    if M_code["WHAT"] not in lines:
                        temp += lines

            with open (filepath, "w") as file:
                file.write(temp)

            succes_msg = new_client.Protocole(IP, get_client_IP(), type("Student Deleted Sucessfuly !"), "Student Deleted Sucessfuly !")
            json_suc_msg = dic_to_json(succes_msg)
            client.send(json_suc_msg.encode('utf-8'))
    
        else:
            client.send("[ERROR!]: MassarCode Not Found !".encode('utf-8'))
            return
    return   

def ModSTD(client):
    code = False
    temp = ""
    level = "In which level the student is in : 1- Common Core\t2- 1st Baccalaureate\t3- 2nd Baccalaureate"
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(level), level)
    level = dic_to_json(dic_msg)
    client.send(level.encode('utf-8'))

    json_lvl = client.recv(1024).decode('utf-8')
    lvl = json_to_dic(json_lvl)
    Mcode = "MassarCode: "
    dic_Mcode = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    Mcode = dic_to_json(dic_Mcode)
    client.send(Mcode.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    M_code = json_to_dic(json_M_code)

    if lvl["WHAT"] == '1':
        filepath = "/home/rayane/School/Common_Core"
    
    elif lvl["WHAT"] == '2':
        filepath = "/home/rayane/School/1st_Bac"
        
    elif lvl["WHAT"] == '3':
        filepath = "/home/rayane/School/2nd_Bac"
    
    with open(filepath, "r") as file:
        for lines in file:
            if M_code["WHAT"] not in lines:
                temp += lines

        with open (filepath, "r") as file:
            for lines in file:
                if M_code["WHAT"] in lines:
                    dic_msg = new_client.Protocole(IP, get_client_IP(), type(lines), lines)
                    json_msg = dic_to_json(dic_msg)
                    client.send(json_msg.encode('utf-8'))
                    code = True
                    
                

        if code:            
            #FIRST NAME
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("First Name: "), "First Name: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_Fname = client.recv(1024).decode('utf-8')
            New_Fname = json_to_dic(json_New_Fname)
            
            #LAST NAME
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Last Name: "), "Last Name: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_Lname = client.recv(1024).decode('utf-8')
            New_Lname = json_to_dic(json_New_Lname)

            #AGE
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Age: "), "Age: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_Age = client.recv(1024).decode('utf-8')
            New_Age = json_to_dic(json_New_Age)

            #MASSAR_CODE
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("MassarCode: "), "MassarCode: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_M_code = client.recv(1024).decode('utf-8')
            New_M_code = json_to_dic(json_New_M_code)

            with open(filepath, "r") as file:
                for lines in file:
                    if New_M_code["WHAT"] == M_code["WHAT"]:
                        continue
                    elif New_M_code["WHAT"] in lines:
                        code = True
                        dic_msg = new_client.Protocole(IP, get_client_IP(), type("[ERROR!] This MassarCode is present: "), "[ERROR!] This MassarCode is present: ")
                        msg = dic_to_json(dic_msg)
                        client.send(msg.encode('utf-8')) 
                        return
            
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Past Year Degree: "), "Past Year Degree: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_Degree = client.recv(1024).decode('utf-8')
            New_Degree = json_to_dic(json_New_Degree)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Sector: "), "Sector: ")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_New_Sector = client.recv(1024).decode('utf-8')
            New_Sector = json_to_dic(json_New_Sector)

            data = "First name: {New_Fname}\t Last name: {New_Lname}\t Age: {New_Age}\t MassarCode: {New_M_code}\t\t Past year degree: {New_Degree:.2f}\t Sector: {New_Sector}\n"

            with open(filepath, "w") as file:
                file.write(temp)
            with open(filepath, "a") as file:
                file.write(data.format(New_Fname=New_Fname["WHAT"], New_Lname=New_Lname["WHAT"], New_Age=New_Age["WHAT"], New_M_code=New_M_code["WHAT"], New_Degree=float(New_Degree["WHAT"]), New_Sector=New_Sector["WHAT"]))

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Student Modified successfuly"), "Student Modified successfuly")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

        else:
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("[ERROR!]: MassarCode Not Found !"), "[ERROR!]: MassarCode Not Found !")
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            return
    return

def SendMenu(client, addr):
    
    global new_client
    new_client = protocole(client=addr)

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

    dic_msg = new_client.Protocole(IP, addr[0], type(menu), menu)
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_order = client.recv(1024).decode('utf-8')
    order = json_to_dic(json_order)

    if order["WHAT"] == '1':
        AddSTD(client)
    elif order["WHAT"] == '2':
        DelSTD(client)
    elif order["WHAT"] == '3':
        ModSTD(client)
    elif order["WHAT"] == '4':
        ListSTD(client)
    elif order["WHAT"] == '5':
        SearchSTD(client)
    elif order["WHAT"] == '6':
        client.close()
        return False  # Indicate to exit the loop and function
    else:
        dic_error = new_client.Protocole(IP, addr[0], type("[ERROR!] Enter A Valid Number !"), "[ERROR!] Enter A Valid Number !")
        error = dic_to_json(dic_error)
        client.send(error.encode('utf-8'))
    return True

def handle_clients(client, addr):
    print(f"[NEW CONNECTION] {addr} Connected.")
    
    while True:
        try:
            if not SendMenu(client, addr):
                break  # Exit loop and disconnect if user chooses to exit
        except Exception as e:
            print(f"[ERROR] Client {addr} encountered an error: {e}")
            break
    print(f"[DISCONNECTED] Client {addr} Disconnected")
    print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 2}")
    client.close()

def END_SERVER():
    while True:
        end = input()
        if end.lower() == 'exit':
            print("Server is shutting down !")
            os._exit(0)

def main():
    # Standard TCP server setup
    sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sserver.bind(conn)
    sserver.listen(5)
    
    # SSL context setup
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="/home/rayane/School/Students-Management/SSL/cert.pem", keyfile="/home/rayane/School/Students-Management/SSL/key.pem")

    print(f"SERVER LISTENING ON PORT {port}")

    input_threads = threading.Thread(target=END_SERVER)
    input_threads.start()

    while True:
        
        global addr
        # Accept a new client connection
        client, addr = sserver.accept()
        
        # Wrap the client socket with SSL
        client = context.wrap_socket(client, server_side=True)
        
        # Start a new thread for each client
        thread = threading.Thread(target=handle_clients, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 2}")

def get_client_IP():
    CLIENT_IP = addr[0]
    return CLIENT_IP

if __name__ == '__main__':
    main()
    