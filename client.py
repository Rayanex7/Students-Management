import socket
import ssl
import json

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

new_client = protocole(assign_ip())

sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context()

context.check_hostname = False  # Disable hostname checking
context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

host = "192.168.1.114"
port = 65300

client = context.wrap_socket(sclient, server_hostname=host)

conn = (host, port)

client.connect(conn)

print(f"[CONNECTED!] to server at {conn}")

def dic_to_json(msg):
    new_msg = json.dumps(msg)
    return new_msg

def json_to_dic(msg):
    new_msg = json.loads(msg)
    return new_msg

def AddSTD():
    #receive instructions
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("**********************************************")
        print(message["WHAT"])
        print("**********************************************")

        order = input()
        dic_msg = new_client.Protocole(assign_ip(), host, type(order), order)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))

        #entering First name
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        Fname = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(Fname), Fname)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))
        
        #entering Last name
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        Lname = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(Lname), Lname)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))

        #entering Age
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        Age = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(Age), Age)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))

        #entering MassarCode
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        M_code = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(M_code), M_code)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))
        
        dic_message = client.recv(1024).decode('utf-8')
        if message == "[ERROR] : This Massar code already exist !":
            print(message)
            exit()
        
        #degree
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        degree = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(degree), degree)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))

        #Inputing sector
        dic_message = client.recv(1024).decode('utf-8')
        message = json_to_dic(dic_message)
        print("************************")
        print(message["WHAT"])
        
        sector = input("")
        dic_msg = new_client.Protocole(assign_ip(), host, type(sector), sector)
        msg = dic_to_json(dic_msg)
        client.send(msg.encode('utf-8'))

        #Succes message
        dic_message = client.recv(1024).decode('utf-8')
        msg = json_to_dic(dic_message)
        print("****************************************")
        print(msg["WHAT"])
        print("****************************************")

def DelSTD():
    #receive msg to indicate level
    json_msg = client.recv(1024).decode('utf-8')
    msg = json_to_dic(json_msg)
    print(msg["WHAT"])
    while True:
        lvl = input("")
        if lvl in ['1','2','3']:
            dic_lvl = new_client.Protocole(host, assign_ip(), type(lvl), lvl)
            lvl = dic_to_json(dic_lvl)
            client.send(lvl.encode('utf-8'))
            
            #receive
            json_msg = client.recv(1024).decode('utf-8')
            msg = json_to_dic(json_msg)
            print(msg["WHAT"])

            M_code = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(M_code), M_code)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            s_text = client.recv(1024).decode('utf-8')
            text = json_to_dic(s_text)
            print(text["WHAT"].strip())
            return
        else:
            print("[ERROR!] Enter A Valid Number !")

def ModSTD():
    #receive msg to indicate level
    lvl_msg = client.recv(1024).decode('utf-8')
    msg = json_to_dic(lvl_msg)
    print(msg["WHAT"])

    while True:
        lvl = input("")
        if lvl in ['1','2','3']:
            dic_lvl = new_client.Protocole(host, assign_ip(), type(lvl), lvl)
            lvl = dic_to_json(dic_lvl)
            client.send(lvl.encode('utf-8'))
            #receive msg to enter MassarCode
            json_msg = client.recv(1024).decode('utf-8')
            msg = json_to_dic(json_msg)
            print(msg["WHAT"])

            #enter MassarCode and send it to server
            M_code = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(M_code), M_code)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            #receive the line with this MassarCodelines
            json_M_code = client.recv(1024).decode('utf-8')
            M_code = json_to_dic(json_M_code)
            if M_code["WHAT"] == "[ERROR!]: MassarCode Not Found !":
                print(M_code["WHAT"].strip())
                return
            
            #Enter new infos
            
            print(M_code["WHAT"])

            #First Name
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            print(line["WHAT"])
            New_Fname = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_Fname), New_Fname)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            
            #Last Name
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            print(line["WHAT"])
            New_Lname = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_Lname), New_Lname)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            
            #Age
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            print(line["WHAT"])
            New_Age = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_Age), New_Age)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            
            #MassarCode
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            print(line["WHAT"])
            New_M_code = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_M_code), New_M_code)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            
            #Degree
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            if line["WHAT"] == "[ERROR!] This MassarCode is present: ":
                print("[ERROR!] This MassarCode is present: ")
                return
            
            print(line["WHAT"])
            New_Degree = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_Degree), New_Degree)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            
            #sector
            json_line = client.recv(1024).decode('utf-8')
            line = json_to_dic(json_line)
            print(line["WHAT"])
            New_Sector = input("")
            dic_msg = new_client.Protocole(host, assign_ip(), type(New_Sector), New_Sector)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            #Final msg
            json_msg = client.recv(1024).decode('utf-8')
            msg = json_to_dic(json_msg)
            print(msg["WHAT"])
            return
        else:
            print("[ERROR!] Enter A Valid Number !")

def ListSTD():
    dic_message = client.recv(1024).decode()
    message = json_to_dic(dic_message)
    print(message["WHAT"])
    while True:
        lvl = input("")
        if lvl in ['1','2','3']:    
            dic_lvl = new_client.Protocole(host, assign_ip(), type(lvl), lvl)
            lvl = dic_to_json(dic_lvl)
            client.send(lvl.encode('utf-8'))
            dic_list_std = client.recv(1024).decode('utf-8')
            list_std = json_to_dic(dic_list_std)
            print(list_std["WHAT"])
            return
        else:
            print("[ERROR!] Enter A Valid Number !")           

def SearchSTD():
    #receive msg to indicate level
    dic_msg = client.recv(1024).decode('utf-8')
    msg = json_to_dic(dic_msg)
    print(msg["WHAT"])

    while True:
        lvl = input("")
        if lvl in ['1','2','3']:
            dic_msg = new_client.Protocole(assign_ip(), host, type(lvl), lvl)
            msg = dic_to_json(dic_msg)    
            client.send(msg.encode('utf-8'))

            #receive
            json_msg = client.recv(1024).decode('utf-8')
            msg = json_to_dic(json_msg)
            print(msg["WHAT"])

            M_code = input("")
            dic_msg = new_client.Protocole(assign_ip(), host, type(M_code), M_code)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))

            json_M_code = client.recv(1024).decode('utf-8')
            M_code = json_to_dic(json_M_code)

            if M_code["WHAT"] == "[ERROR!]: MassarCode Not Found !":
                print("[ERROR!]: MassarCode Not Found !")
                return

            print("************************************")
            print(M_code["WHAT"].strip())
            print("************************************")
            return
        else:
            print("[ERROR!] Enter A valid Number !")

def recv_menu():
    
    #Receive menu
    err_msg = client.recv(1024).decode('utf-8')
    msg = json_to_dic(err_msg)
    print(f"{msg["WHAT"]}")

def client_side():
    
    while True:

        recv_menu()

        #Send order to do
        order = input()
        #AddSTD
        if order == '1':
            dic_msg = new_client.Protocole(host, assign_ip(), type(order), order)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            AddSTD()

        #DelSTD
        elif order == '2':
            dic_msg = new_client.Protocole(host, assign_ip(), type(order), order)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            DelSTD()

        #ModSTD
        elif order == '3':
            dic_msg = new_client.Protocole(host, assign_ip(), type(order), order)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            ModSTD()

        #ListSTD
        elif order == '4':
            dic_msg = new_client.Protocole(host, assign_ip(), type(order), order)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            ListSTD()

        #SearchSTD
        elif order == '5':
            dic_msg = new_client.Protocole(host, assign_ip(), type(order), order)
            msg = dic_to_json(dic_msg)
            client.send(msg.encode('utf-8'))
            SearchSTD()

        #exit
        elif order == '6':
            client.send(order.encode('utf-8'))
            print("Have a good time :)")
            exit()
        else:
            client.send(order.encode('utf-8'))
            msg = client.recv(1024).decode('utf-8')
            print(msg) 


if __name__ == '__main__':
    client_side()