import socket
import ssl
import json
from tabulate import tabulate
import ast
from datetime import datetime 

class protocole:
    def __init__(self, client):
        self.client = client
        

    def Protocole(self, HOST, CLIENT, TYPE, DATA, AUTH_ID=None):
        protocole = {  "FROM" : f"{HOST}",
                        "TO"   : f"{CLIENT}",
                        "TYPE" : f"{TYPE}",
                        "WHAT" : f"{DATA}",
                        "ID"   : f"{AUTH_ID}"
                        }
        return protocole
    
    def authentication(self):
        
        json_user_requ = conn.client.recv(1024).decode('utf-8')
        user_requ = json_to_dic(json_user_requ)
        print(user_requ["WHAT"])

        user = input()
        user_dic_msg = new_client.Protocole(assign_ip(), conn.host, type(user), user)
        user_msg = dic_to_json(user_dic_msg)
        conn.client.send(user_msg.encode("utf-8"))
        
        json_pass_requ = conn.client.recv(1024).decode('utf-8')
        pass_requ = json_to_dic(json_pass_requ)
        print(pass_requ["WHAT"])
        
        passwd = input()
        passwd_dic_msg = new_client.Protocole(assign_ip(), conn.host, type(passwd), passwd)
        passwd_msg = dic_to_json(passwd_dic_msg)
        conn.client.send(passwd_msg.encode("utf-8"))
        
        msg = conn.client.recv(1024).decode('utf-8')
        d_msg = json_to_dic(msg)  

        
        if d_msg["WHAT"] == "[AUTHENTICATION FAILED]":
            print(d_msg["WHAT"])
            exit()

        else:
            with open("user.json", "w") as file:
                id_data = {"ID": d_msg["ID"]}
                json.dump(id_data, file, indent=4)
                
            print(d_msg["WHAT"])
            return  

class connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def start_client(self):
        sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        context = ssl.create_default_context()

        context.check_hostname = False  # Disable hostname checking
        context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

        host = self.host
        port = self.port

        self.client = context.wrap_socket(sclient, server_hostname=host)

        conn = (host, port)

        self.client.connect(conn)

        print(f"[CONNECTED!] to server at {conn}")

def assign_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"Cannot assign an IPv4 Address: {[e]}")
    finally:
        return ip

new_client = protocole(assign_ip())

conn = connection("192.168.1.117", 65301)


unix_to_formatted = lambda x: datetime.fromtimestamp(x).strftime('%Y/%m/%d')
formatted_to_unix = lambda x: int(datetime.strptime(x, '%Y/%m/%d').timestamp())

def dic_to_json(msg):
    new_msg = json.dumps(msg)
    return new_msg

def json_to_dic(msg):
    new_msg = json.loads(msg)
    return new_msg

def AddSTD():

    #entering First name
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Fname = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Fname), Fname)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))
    
    #entering Last name
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Lname = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Lname), Lname)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #entering Age
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Age = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Age), Age)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #entering MassarCode
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    M_code = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(M_code), M_code)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))
    
    dic_message = conn.client.recv(1024).decode('utf-8')

    #Gender
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Gender = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Gender), Gender)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing Email
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Email = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Email), Email)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing Country
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Country = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Country), Country)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing City
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    City = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(City), City)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing Address
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Address = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Address), Address)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing Phone
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    Phone = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Phone), Phone)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Inputing ClassID
    dic_message = conn.client.recv(1024).decode('utf-8')
    message = json_to_dic(dic_message)
    print("************************")
    print(message["WHAT"])
    
    ClassID = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(ClassID), ClassID)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    #Succes message
    dic_message = conn.client.recv(1024).decode('utf-8')
    msg = json_to_dic(dic_message)
    print("****************************************")
    print(msg["WHAT"])
    print("****************************************")

def DelSTD():

    while True:

        #receive
        json_msg = conn.client.recv(1024).decode('utf-8')
        msg = json_to_dic(json_msg)
        print(msg["WHAT"])

        M_code = input("")
        dic_msg = new_client.Protocole(conn.host, assign_ip(), type(M_code), M_code)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        s_text = conn.client.recv(1024).decode('utf-8')
        text = json_to_dic(s_text)
        print(text["WHAT"].strip())
        return

def ModSTD():

    # Receive msg to enter MassarCode
    json_msg = conn.client.recv(1024).decode('utf-8')
    msg = json_to_dic(json_msg)
    print(msg["WHAT"])

    # Enter MassarCode and send it to server
    M_code = input("")
    dic_msg = new_client.Protocole(conn.host, assign_ip(), type(M_code), M_code)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    Nmsg = conn.client.recv(1024).decode('utf-8')
    msg = json_to_dic(Nmsg)

    if msg["WHAT"] == "[ERROR] No Massar Code Found !":
        print(msg["WHAT"])
        return

    # Receive msg to choose what to change
    print(msg["WHAT"])

    resp = input()
    dic_msg = new_client.Protocole(conn.host, assign_ip(), type(resp), resp)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    if resp == "1":
        # Entering First name
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Fname = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Fname), Fname)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Entering Last name
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Lname = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Lname), Lname)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Entering Age
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Age = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Age), Age)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Entering MassarCode
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        M_code = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(M_code), M_code)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        dic_message = conn.client.recv(1024).decode('utf-8')

        # Gender
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Gender = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Gender), Gender)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing Email
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Email = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Email), Email)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing Country
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Country = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Country), Country)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing City
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        City = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(City), City)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing Address
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Address = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Address), Address)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing Phone
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        Phone = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(Phone), Phone)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Inputing ClassID
        dic_message = conn.client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])

        ClassID = input("")
        dic_msg = new_client.Protocole(assign_ip(), conn.host, type(ClassID), ClassID)
        msg = dic_to_json(dic_msg)
        conn.client.send(msg.encode('utf-8'))

        # Success message
        dic_message = conn.client.recv(1024).decode('utf-8')
        msg = json_to_dic(dic_message)
        print("****************************************")
        print(msg["WHAT"])
        print("****************************************")

    elif resp == "2":
        while True:
            Nmsg = conn.client.recv(1024).decode('utf-8')
            msg = json_to_dic(Nmsg)
            print(msg["WHAT"])

            # Choose Operation
            op = input()

            if op == "1":  # change Massar
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])

                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])

            elif op == "2":  # change first name
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])

                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])

            elif op == "3":  # change last name
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])

                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])

            elif op == "4":  # change birthdate
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])

                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])

            elif op == "5":  # change Gender
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])

                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                
            
            elif op == "6": #change Email
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                

            elif op == "7": #change Country
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                

            elif op == "8": #change City
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                

            elif op == "9": #change Address
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                

            elif op == "10": #change Phone
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                

            elif op == "11": #change Class ID
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))

                Nmsg = conn.client.recv(1024).decode('utf-8')
                msg = json_to_dic(Nmsg)
                print(msg["WHAT"])
                
                new = input()
                Odata = new_client.Protocole(conn.host, assign_ip(), type(new), new)
                data = dic_to_json(Odata)
                conn.client.send(data.encode('utf-8'))

                msg = conn.client.recv(1024).decode('utf-8')
                Nmsg = json_to_dic(msg)
                print(Nmsg["WHAT"])
                
            
            elif op == "12": #exit
                Ndata = new_client.Protocole(conn.host, assign_ip(), type(op), op)
                data = dic_to_json(Ndata)
                conn.client.send(data.encode('utf-8'))
                return False

def ListSTD():
    dic_message = conn.client.recv(1024).decode()
    msg = json_to_dic(dic_message)

    new_msg = msg["WHAT"]
    
    new_data = [new_msg[1:-1]]

    data = ast.literal_eval(new_data[0])

    new_data = []

    for records in data:
        (Massar_ID, First_name, Last_name, Birthdate, Gender, Email, Country, City, Address, Phone, Class_id) = records
        
        date = unix_to_formatted(Birthdate)
        
        up_records = (Massar_ID, First_name, Last_name, date, Gender, Email, Country, City, Address, Phone, Class_id)

        new_data.append(up_records)
        

    headers = ["Massar_ID", "First_name", "Last_name", "Birthdate", "Gender", "Email", "Country", "City", "Address", "Parent_Phone", "Class_ID"]

    print(tabulate(new_data, headers=headers, tablefmt="grid"))

def SearchSTD():

    #receive text to enter masarcode
    json_msg = conn.client.recv(1024).decode('utf-8')
    msg = json_to_dic(json_msg)
    print(msg["WHAT"])

    M_code = input("")
    dic_msg = new_client.Protocole(assign_ip(), conn.host, type(M_code), M_code)
    msg = dic_to_json(dic_msg)
    conn.client.send(msg.encode('utf-8'))

    json_M_code = conn.client.recv(1024).decode('utf-8')
    M_code = json_to_dic(json_M_code)

    if M_code["WHAT"] == "[ERROR!]: MassarCode Not Found !":
        print("[ERROR!]: MassarCode Not Found !")
        return
    else:
    
        data = ast.literal_eval(M_code["WHAT"])
        
        headers = ["Massar_ID", "First_name", "Last_name", "Birthdate", "Gender", "Email", "Country", "City", "Address", "Parent_Phone", "Class_ID"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    
    return

def recv_menu():
    
    #Receive menu
    err_msg = conn.client.recv(1024).decode('utf-8')
    msg = json_to_dic(err_msg)
    print(f'{msg["WHAT"]}')

def check_ID():
    
    status = False
    try:
        with open("user.json", "x") as file:    
            pass
    except FileExistsError:
        pass

    try:
        with open("user.json", "r") as file:
            data = json.load(file)
            id = data["ID"]
            msg = new_client.Protocole(assign_ip(), conn.host, "", "", id)
            text = dic_to_json(msg)
            conn.client.send(text.encode('utf-8'))
            
            text = conn.client.recv(1024).decode('utf-8')
            msg = json_to_dic(text)

            if msg["WHAT"] == "[ID VERIFIED!]":
                return True
            else:
                return False
        status = True
            
    except json.decoder.JSONDecodeError:
        pass
    
    if not status:
        id = ""

        msg = new_client.Protocole(assign_ip(), conn.host, "", "", id)
        text = dic_to_json(msg)
        conn.client.send(text.encode('utf-8'))
        
        text = conn.client.recv(1024).decode('utf-8')
        msg = json_to_dic(text)
        if msg["WHAT"] == "[ID VERIFIED!]":
            return True
        else:
            return False

def client_side():

    conn.start_client()

    auth = protocole(assign_ip())

    if not check_ID():
        auth.authentication()

        while True:

            recv_menu()

            order = input()

            #AddSTD
            if order == '1':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                AddSTD()

            #DelSTD
            elif order == '2':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                DelSTD()

            #ModSTD
            elif order == '3':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                ModSTD()

            #ListSTD
            elif order == '4':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                ListSTD()

            #SearchSTD
            elif order == '5':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                SearchSTD()

            #exit
            elif order == '6':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                print("Have a good time :)")
                exit()
            else:
                conn.client.send(order.encode('utf-8'))
                msg = conn.client.recv(1024).decode('utf-8')
                print(msg) 
    else:
        while True:

            recv_menu()

            #Send order to do
            order = input()
            #AddSTD
            if order == '1':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                AddSTD()

            #DelSTD
            elif order == '2':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                DelSTD()

            #ModSTD
            elif order == '3':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                ModSTD()

            #ListSTD
            elif order == '4':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                ListSTD()

            #SearchSTD
            elif order == '5':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                SearchSTD()

            #exit
            elif order == '6':
                dic_msg = new_client.Protocole(conn.host, assign_ip(), type(order), order)
                msg = dic_to_json(dic_msg)
                conn.client.send(msg.encode('utf-8'))
                print("Have a good time :)")
                exit()
            else:
                conn.client.send(order.encode('utf-8'))
                msg = conn.client.recv(1024).decode('utf-8')
                print(msg) 

if __name__ == '__main__':
    client_side()