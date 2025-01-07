import socket
import threading
import ssl
import os
import json
import random
import mysql.connector
from datetime import datetime

unix_to_formatted = lambda x: datetime.fromtimestamp(x).strftime('%Y/%m/%d')
formatted_to_unix = lambda x: int(datetime.strptime(x, '%Y/%m/%d').timestamp())


class protocole:
    def __init__(self, client):
        self.client = client
        
    def Protocole(self, HOST, CLIENT, TYPE, DATA, AUTH_ID=None):
        protocole = {  "FROM"  : f"{HOST}",
                        "TO"   : f"{CLIENT}",
                        "TYPE" : f"{TYPE}",
                        "WHAT" : f"{DATA}",
                        "ID"   : f"{AUTH_ID}"
                        }
        return protocole
    
    def authentication(self, client):
            status = False

            usr_requ = protocole.Protocole(self, IP, get_client_IP(), type("Username: "), str("Username: "))
            json_usr_requ = dic_to_json(usr_requ)
            client.send(json_usr_requ.encode('utf-8'))

            json_user = client.recv(1024).decode('utf-8')
            user = json_to_dic(json_user)

            passwd_requ = protocole.Protocole(self, IP, get_client_IP(), type("Password: "), "Password: ")
            json_passwd_requ = dic_to_json(passwd_requ)
            client.send(json_passwd_requ.encode('utf-8'))

            json_passwd = client.recv(1024).decode('utf-8')
            passwd = json_to_dic(json_passwd)
            
            try:
                with open("authors.json", "x") as file:
                    data = {"Username": "", "Password": ""}
                    json.dump(data, file)
            except FileExistsError:
                pass
            
            with open("authors.json", "r") as file:
                authors = json.load(file)

            for a in authors:
                if a.get("Username") == user["WHAT"] and a.get("Password") == passwd["WHAT"]:
                    user_ID = ID()

                    dic_msg = {"Username": user["WHAT"], "Password": passwd["WHAT"], "ID": str(user_ID)}
                    
                    try:
                        with open("Users_ID.json", "x") as file:
                            txt = {"Username": "","Password": "","ID": ""}
                            json.dump(txt, file, indent=4)
                    except FileExistsError:
                        pass

                    with open("Users_ID.json", "r") as file:
                        data = {"Username":user["WHAT"],"Password":passwd["WHAT"],"ID":user_ID}
                        users = json.load(file)
                    status = True

            if status == True:
                for a in users:
                    if data["Username"] and data["Password"] and data["ID"] in a:
                        continue
                    else:
                        users = [users]
                        users.append(data)
                        with open("Users_ID.json", "w") as file:        
                            json.dump(users, file, indent=4)

                        dic_msg = protocole.Protocole(self, IP, get_client_IP(), type("[WELCOME!]"), "[WELCOME!]", str(user_ID))
                        msg = dic_to_json(dic_msg)
                        client.send(msg.encode('utf-8'))
                        return True
            else:
                data = protocole.Protocole(self, IP, get_client_IP(), type("[AUTHENTICATION FAILED]"), "[AUTHENTICATION FAILED]")
                msg = dic_to_json(data)
                client.send(msg.encode('utf-8'))
                return False                
                  
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
port = 65301

conn = (IP, port)

def dic_to_json(msg):
    new_msg = json.dumps(msg)
    return new_msg

def json_to_dic(msg):
    new_msg = json.loads(msg)
    return new_msg

def AddSTD(client):
    
    if not con.is_connected():
        con.reconnect()


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
    
    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Birthdate (YYYY/MM/DD): "), "Birthdate (YYYY/MM/DD): ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Age = client.recv(1024).decode('utf-8')
    Age = json_to_dic(json_Age)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Massar Code: "), "Massar Code: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    M_code= json_to_dic(json_M_code)

    # I should add Check if Massar code already exists 

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("'M' or 'F' :"), " 'M' or 'F' :")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Gender = client.recv(1024).decode('utf-8')
    Gender = json_to_dic(json_Gender)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Email: "), "Email: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Email = client.recv(1024).decode('utf-8')
    Email = json_to_dic(json_Email)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Country: "), "Country: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Country = client.recv(1024).decode('utf-8')
    Country = json_to_dic(json_Country)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("City: "), "City: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_City = client.recv(1024).decode('utf-8')
    City = json_to_dic(json_City)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Address: "), "Address: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Address = client.recv(1024).decode('utf-8')
    Address = json_to_dic(json_Address)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Phone: "), "Phone: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_Phone = client.recv(1024).decode('utf-8')
    Phone = json_to_dic(json_Phone)

    dic_msg = new_client.Protocole(IP, get_client_IP(), type("Class ID: "), "Class ID: ")
    json_msg = dic_to_json(dic_msg)
    client.send(json_msg.encode('utf-8'))

    json_ClassID = client.recv(1024).decode('utf-8')
    ClassID = json_to_dic(json_ClassID)

    date = formatted_to_unix(Age["WHAT"])

    try:
        cursor.execute('''INSERT INTO Students (Massar_ID, First_name, Last_name, Birthdate, Gender, Email , Country, City, Address, Parent_Phone, Class_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (M_code["WHAT"], Fname["WHAT"], Lname["WHAT"], date, Gender["WHAT"], Email["WHAT"], Country["WHAT"], City["WHAT"], Address["WHAT"], Phone["WHAT"], ClassID["WHAT"]))
        
        con.commit()
        cursor.close()
        con.close()

        dic_msg = new_client.Protocole(IP, get_client_IP(), type("[SUCCESS!]: Student Added Sucessffuly "), "[SUCCESS!]: Student Added Sucessffuly ")
        json_msg = dic_to_json(dic_msg)
        client.send(json_msg.encode('utf-8'))
        return
    except Exception as e:
        print(f"User {addr[0]} ON {addr[1]} Encountred the Following ERROR : {e}")

def ListSTD(client):

    if not con.is_connected():
        con.reconnect()

    cursor.execute("SELECT * FROM Students")
    data =  cursor.fetchall()

    Msg = new_client.Protocole(IP, get_client_IP(), type(data), data)
    msg = dic_to_json(Msg)
    client.send(msg.encode('utf-8'))

    con.commit()
    cursor.close()
    con.close()

def SearchSTD(client):

    Mcode = "MassarCode: "
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    msg = dic_to_json(dic_msg)
    client.send(msg.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    M_code = json_to_dic(json_M_code)
    
    msg = [M_code["WHAT"]]
    cursor.execute('''SELECT * FROM Students WHERE Massar_ID = %s''',msg)
    data = cursor.fetchall()
    
    if data:
        msg = new_client.Protocole(IP, get_client_IP(), type(data), data)
        MSG = dic_to_json(msg)
        client.send(MSG.encode('utf-8'))
    else:
        msg = new_client.Protocole(IP, get_client_IP(), type("[ERROR!]: MassarCode Not Found !"), "[ERROR!]: MassarCode Not Found !")
        MSG = dic_to_json(msg)
        client.send(MSG.encode('utf-8'))
   
def DelSTD(client):

    if not con.is_connected():
        con.reconnect()

    Mcode = "MassarCode: "
    dic_msg = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    msg = dic_to_json(dic_msg)
    client.send(msg.encode('utf-8'))

    m_code = client.recv(1024).decode('utf-8')
    M_code = json_to_dic(m_code)

    cursor.execute('''SELECT * FROM Students WHERE Massar_ID = %s''', (M_code["WHAT"],))
    result = cursor.fetchall()

    if result:    
        cursor.execute('''DELETE FROM Students WHERE Massar_ID = %s''', (M_code["WHAT"],))
        msg = "[SUCCESS!] Student Deleted Successfully"
        odata = new_client.Protocole(IP, get_client_IP(), type(msg), msg)
        data = dic_to_json(odata)
        client.send(data.encode('utf-8'))

        con.commit()
        cursor.close()
        con.close()
    else:
        msg = "[ERROR!]: MassarCode Not Found !"
        odata = new_client.Protocole(IP, get_client_IP(), type(msg), msg)
        data = dic_to_json(odata)
        client.send(data.encode('utf-8'))
        return
    return   

def ModSTD(client):
     
    Mcode = "MassarCode: "
    dic_Mcode = new_client.Protocole(IP, get_client_IP(), type(Mcode), Mcode)
    Mcode = dic_to_json(dic_Mcode)
    client.send(Mcode.encode('utf-8'))

    json_M_code = client.recv(1024).decode('utf-8')
    Origi_M_code = json_to_dic(json_M_code)

    cursor.execute('''SELECT * FROM Students WHERE Massar_ID = %s''', (Origi_M_code["WHAT"],))

    data = cursor.fetchall()

    if data:
        msg = new_client.Protocole(IP, get_client_IP(), type("Change all student data (1) Choose what to change (2)"), "Change all student data (1) Choose what to change (2)")
        Nmsg = dic_to_json(msg)
        client.send(Nmsg.encode('utf-8'))

        data = client.recv(1024).decode('utf-8')
        Ndata = json_to_dic(data)

        
        if Ndata["WHAT"] == "1":
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
            
            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Birthdate (YYYY/MM/DD): "), "Birthdate (YYYY/MM/DD): ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Age = client.recv(1024).decode('utf-8')
            Age = json_to_dic(json_Age)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Massar Code: "), "Massar Code: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_M_code = client.recv(1024).decode('utf-8')
            M_code= json_to_dic(json_M_code)

            # I should add Check if Massar code already exists 

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("'M' or 'F' :"), " 'M' or 'F' :")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Gender = client.recv(1024).decode('utf-8')
            Gender = json_to_dic(json_Gender)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Email: "), "Email: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Email = client.recv(1024).decode('utf-8')
            Email = json_to_dic(json_Email)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Country: "), "Country: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Country = client.recv(1024).decode('utf-8')
            Country = json_to_dic(json_Country)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("City: "), "City: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_City = client.recv(1024).decode('utf-8')
            City = json_to_dic(json_City)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Address: "), "Address: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Address = client.recv(1024).decode('utf-8')
            Address = json_to_dic(json_Address)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Phone: "), "Phone: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_Phone = client.recv(1024).decode('utf-8')
            Phone = json_to_dic(json_Phone)

            dic_msg = new_client.Protocole(IP, get_client_IP(), type("Class ID: "), "Class ID: ")
            json_msg = dic_to_json(dic_msg)
            client.send(json_msg.encode('utf-8'))

            json_ClassID = client.recv(1024).decode('utf-8')
            ClassID = json_to_dic(json_ClassID)

            date = formatted_to_unix(Age["WHAT"])

            cursor.execute('''UPDATE Students
                SET Massar_ID = %s,
                    First_name = %s,
                    Last_name = %s,
                    Birthdate = %s,
                    Gender = %s,
                    Email = %s,
                    Country = %s,
                    City = %s,
                    Address = %s,
                    Parent_Phone = %s,
                    Class_ID = %s
                WHERE Massar_ID = %s;''', (M_code["WHAT"], Fname["WHAT"], Lname["WHAT"], date, Gender["WHAT"], Email["WHAT"], Country["WHAT"], City["WHAT"], Address["WHAT"], Phone["WHAT"], ClassID["WHAT"], Origi_M_code["WHAT"]))
            
            con.commit()
            cursor.close()
            con.close()

            msg = new_client.Protocole(IP, get_client_IP(), type("Update successful"), "Update successful")
            Nmsg = dic_to_json(msg)
            client.send(Nmsg.encode('utf-8'))

        elif Ndata["WHAT"] == "2":
            while True:
                data = """Please select an operation by entering the corresponding number:
        1. Change Massar_ID
        2. Change First_name
        3. Change Last_name
        4. Change Birthdate
        5. Change Gender
        6. Change Email
        7. Change Country
        8. Change City
        9. Change Address
        10. Change Parent_Phone
        11. Change Class_ID
        12. Exit
        """
                msg = new_client.Protocole(IP, get_client_IP(), type(data), data)
                Nmsg = dic_to_json(msg)
                client.send(Nmsg.encode('utf-8'))

                Nmsg = client.recv(2014).decode('utf-8')
                msg = json_to_dic(Nmsg)


                if msg["WHAT"] == "1": #change Massar
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Massar_ID"), "Enter New Massar_ID")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Massar_ID = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Massar_ID updated successfully"), "Massar_ID updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    
                
                elif msg["WHAT"] == "2": #change first name
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New First Name"), "Enter New First Name")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET First_name = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("First name updated successfully"), "First name updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))
                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "3": #change last name
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Last Name"), "Enter New Last Name")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Last_name = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Last name updated successfully"), "Last name updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))
                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "4": #change birthdate
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter Birthdate"), "Enter Birthdate")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    data = json_to_dic(msg)

                    Nmsg = formatted_to_unix(data["WHAT"])

                    try:
                        cursor.execute('''UPDATE Students SET Birthdate = %s WHERE Massar_ID = %s;''', (Nmsg, Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Birthdate updated successfully"), "Birthdate updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "5": #change Gender
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter Gender"), "Enter Gender")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Gender = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Gender updated successfully"), "Gender updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "6": #change Email
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Email"), "Enter New Email")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Email = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Email updated successfully"), "Email updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "7": # Change Country
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Country"), "Enter New Country")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Country = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Country updated successfully"), "Country updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "8":
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New City"), "Enter New City")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET City = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("City updated successfully"), "City updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "9":
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Address"), "Enter New Address")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Address = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Address updated successfully"), "Address updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")


                elif msg["WHAT"] == "10":
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Phone"), "Enter New Phone")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Parent_Phone = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Phone updated successfully"), "Phone updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    

                elif msg["WHAT"] == "11":
                    msg = new_client.Protocole(IP, get_client_IP(), type("Enter New Class ID"), "Enter New Class ID")
                    Nmsg = dic_to_json(msg)
                    client.send(Nmsg.encode('utf-8'))
                    
                    msg = client.recv(1024).decode('utf-8')
                    Nmsg = json_to_dic(msg)

                    try:
                        cursor.execute('''UPDATE Students SET Class_ID = %s WHERE Massar_ID = %s;''', (Nmsg["WHAT"], Origi_M_code["WHAT"]))
                        con.commit()
                        msg = new_client.Protocole(IP, get_client_IP(), type("Class ID updated successfully"), "Class ID updated successfully")
                        Nmsg = dic_to_json(msg)
                        client.send(Nmsg.encode('utf-8'))

                    except Exception as e:
                        Nmsg = new_client.Protocole(IP, assign_ip(), type("Error Applying Changes"), "Error Applying Changes")
                        msg = dic_to_json(Nmsg)
                        client.send(msg.encode('utf-8'))
                        print(f"[ERROR]: {e}")
                    
                
                elif msg["WHAT"] == "12": #exit
                    return False
                    
    else:
        msg = new_client.Protocole(IP, get_client_IP(), type("[ERROR] No Massar Code Found !"), "[ERROR] No Massar Code Found !")
        Nmsg = dic_to_json(msg)
        client.send(Nmsg.encode('utf-8'))
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

def check_ID(client):
    new_client = protocole(client)
    json_msg = client.recv(1024).decode('utf-8')
    msg = json_to_dic(json_msg)
    
    if msg["ID"] != "":
        with open("Users_ID.json", "r") as f:
            json_text = json.load(f)
            for a in json_text:
                if isinstance(a, list):
                    for b in a:
                        if isinstance(b, dict) and msg["ID"] == b.get("ID"):
                            return True
                elif isinstance(a, dict):
                    if msg["ID"] == a.get("ID"):
                        return True
            else:
                return False
    else:
        text = new_client.Protocole(IP, get_client_IP(), type("[ID NOT VERIFIED]"), "[ID NOT VERIFIED]")
        msg = dic_to_json(text)
        client.send(msg.encode('utf-8'))
        return False

def is_auth(client):
    auth = protocole(addr)
    if not check_ID(client):
        try:
            if auth.authentication(client):
                return True
            else:
                return False

        except Exception as e:
            print(f"[ERROR]: {e}")
            return False
    else:
        msg = auth.Protocole(IP, get_client_IP(), type("[ID VERIFIED!]"), "[ID VERIFIED!]")
        text = dic_to_json(msg)
        client.send(text.encode('utf-8'))
        return True
                    
def handle_clients(client, addr):
    print(f"[NEW CONNECTION] {addr} Connected.")
    if is_auth(client):
        while True:
            if not con.is_connected():
                con.reconnect()
            global cursor
            cursor = con.cursor()

            try:
                if not SendMenu(client, addr):
                    break  # Exit loop and disconnect if user chooses to exit
            except Exception as e:
                print(f"[ERROR] Client {addr} encountered an error: {e}")
                break
        print(f"[DISCONNECTED] Client {addr} Disconnected")
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 2}")
        client.close()
    else:
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
    context.load_cert_chain(certfile="/home/rayane/projects/Students-Management/SSL/cert.pem", keyfile="/home/rayane/projects/Students-Management/SSL/key.pem")

    print(f"SERVER LISTENING ON PORT {port}")

    input_threads = threading.Thread(target=END_SERVER)
    input_threads.start()

    global con
    global cursor

    con = mysql.connector.connect (
        host = "127.0.0.1",
        user = "root",
        password = "Meliox7@2013.",
        database = "School"
    )

    cursor = con.cursor()

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

def ID():
    numbers = '0123456789'

    ID = ''.join(random.choices(numbers, k=30))
    return ID

if __name__ == '__main__':
    main()
    