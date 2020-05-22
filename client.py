# global variables
hostAddress = 'localhost'
portNo = 9999
databaseFileName = "data.txt"

def printDBOptions():
    print("\nPython DB Menu\n1.Find customer\n2.Add customer\n3.Delete customer\n4.Update custmer age\n5.Update custmer address\n6.Update custmer phone\n7.Print report\n8.Exit")



#Main Code
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hostAddress, portNo))

print("Client is connected to Server.")

while(True):
    printDBOptions()
    choice = input("Enter your choice from option 1 to 8 : ")
    if(choice == '1'):
        client.send(choice.encode())
        name = input("Enter name to search customer : ").strip()
        while (name == '' or name == ' '):
            name = input("Name cannot be blank. Enter name to add customer : ").strip()
        client.send(name.encode())
    elif (choice == '2'):
        client.send(choice.encode())
        name = input("Enter name to add customer : ").strip()
        while(name == '' or name == ' '):
            name = input("Name cannot be blank. Enter name to add customer : ").strip()

        while(True):
            try:
                age = input("Enter age to add customer : ").strip()
                if(age == ''):
                    break
                else:
                    age = int(age)
                    break
            except:
                print("Age should be in Number.")
                pass

        address = input("Enter address to add customer : ")
        phoneNo = input("Enter phone number to add customer : ")
        # client.send(name.encode())
        # client.send(str(age).encode())
        # client.send(address.encode())
        # client.send(phoneNo.encode())
        data = name + "*" + str(age) + "*" + address + "*" + phoneNo
        # print(data)
        client.send(data.encode())
    elif (choice == '3'):
        client.send(choice.encode())
        name = input("Enter customer's name to delete record : ").strip()
        while (name == '' or name == ' '):
            name = input("Name cannot be blank. Enter name to add customer : ").strip()
        client.send(name.encode())
    elif (choice == '4'):
        client.send(choice.encode())
        name = input("To update age of customer, Enter name : ").strip()
        while (name == '' or name == ' '):
            name = input("Name cannot be blank. Enter name to update customer : ").strip()
        while (True):
            try:
                age = input("Enter new age to update : ").strip()
                if (age == ''):
                    break
                else:
                    age = int(age)
                    break
            except:
                print("Age should be in Number.")
                pass
        data = name + "*" + str(age)
        client.send(data.encode())
        # print('choice is 4')
    elif (choice == '5'):
        client.send(choice.encode())
        name = input("To update address of customer, Enter name : ").strip()
        while (name == ''):
            name = input("Name cannot be blank. Enter name to update customer : ").strip()
        address = input("Enter new address to update : ").strip()
        data = name + "*" + address
        client.send(data.encode())
        # print('choice is 5')
    elif (choice == '6'):
        client.send(choice.encode())
        name = input("To update phone_number of customer, enter Name : ").strip()
        while (name == ''):
            name = input("Name cannot be blank. Enter name to update customer : ").strip()
        phoneNo = input("Enter new phone number to update : ").strip()
        data = name + "*" + phoneNo
        client.send(data.encode())
        # print('choice is 6')
    elif (choice == '7'):
        # print(choice)
        client.send(choice.encode())
    elif (choice == '8'):
        client.send(choice.encode())
        break
    else:
        print('No valid choice. Please enter your choice again : ')
        continue

    from_server = client.recv(4096)
    print("Message from server : " + from_server.decode())
print("Message from server : " + client.recv(4096).decode())
client.close()