# global variables
hostAddress = 'localhost'
portNo = 9999
databaseFileName = "data.txt"

def findCustomer(keyToSearch):
    # print(customers.items())
    # searchedRecord = next(item for item in customers.items() if item[0] == keyToSearch)
    for key, value in customers.items():
        name = key
        age, address, phoneNo = value
        searchedRecord = ''
        if name == keyToSearch:
            searchedRecord = "\nName:" + str(name).strip() + " -Age:" + str(age).strip() + " -Address:" + str(address).strip() + " -PhoneNo:" + str(phoneNo).strip()
            break
        else:
            continue

    if searchedRecord == '':
        searchedRecord = "customer not found"
    # print(searchedRecord)
    return  searchedRecord

def add_customer(name, age, address, phoneNo):
    addMessage = ''
    if name not in customers.keys():
        customers[name] = [age, address, phoneNo]
        addMessage = "customer added successfully"
    else:
        addMessage = "customer already exists"
    return addMessage

def delete_customer(name):
    deleteMessage = ''
    if name in customers:
        del customers[name]
        deleteMessage = 'customer record is deleted'
    else:
        deleteMessage = 'customer of given name does not exist'
    return deleteMessage

updateMessage = ''
def update_customer_age(nameToUpdate, newAge):
    if nameToUpdate in customers:
        # print(customers[nameToUpdate])
        age, address, phoneNo = customers.get(nameToUpdate)
        age = newAge
        customers[nameToUpdate] = [age, address, phoneNo]
        # print(customers[nameToUpdate])
        updateMessage = 'customer age updated successfully'
    else:
        updateMessage = 'customer of given name not found'
    return updateMessage

def update_customer_address(nameToUpdate, newAddress):
    if nameToUpdate in customers:
        # print(customers[nameToUpdate])
        age, address, phoneNo = customers.get(nameToUpdate)
        address = newAddress
        customers[nameToUpdate] = [age, address, phoneNo]
        # print(customers[nameToUpdate])
        updateMessage = 'customer address updated successfully'
    else:
        updateMessage = 'customer of given name not found'
    return updateMessage

def update_customer_phone_number(nameToUpdate, newPhoneNo):
    if nameToUpdate in customers:
        # print(customers[nameToUpdate])
        age, address, phoneNo = customers.get(nameToUpdate)
        phoneNo = newPhoneNo
        customers[nameToUpdate] = [age, address, phoneNo]
        # print(customers[nameToUpdate])
        updateMessage = 'customer phone number updated successfully'
    else:
        updateMessage = 'customer of given name not found'
    return updateMessage

def loadRecords():
    database = open(databaseFileName, 'r')
    # print(database)
    customers = {}
    for record in database.readlines():
        name, age, address, phoneNo = record.split('|')
        str(name).strip()
        if name == '' or name == ' ':
            continue
        else:
            customers[name] = [age, address, phoneNo]
        # customers[name] = [age, address, phoneNo]
    database.close()
    return customers

def sendDataReport(customers):
    sortedCustomers = sorted(customers.items(), key = lambda x:x[0].lower())
    records = ''
    dataDictionary = dict(sortedCustomers)

    for key,value in dataDictionary.items():
        name = key
        age,address,phoneNo = value
        # if key == '' or name == '':
        #     continue
        # else:
        records = records + "\nName:" + str(name).strip() + " -Age:" + str(age).strip() + " -Address:" + str(address).strip() + " -PhoneNo:" + str(phoneNo).strip()
    return records


#Main Program
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostAddress, portNo))
server.listen(5)
print('Server started... waiting for client...')
customers = loadRecords()
print("Data is loaded from file...")
while True:
    conn, addr = server.accept()
    print('client is connected by ' + str(addr) + ' address...')
    # customers = loadRecords()
    # print("Data is loaded from file...")
    while True:
        data = conn.recv(4096)
        if not data: break
        data = data.decode().strip()
        print('choice from client : ' + data)
        if(data == '1'):
            key = conn.recv(4096).decode().strip()
            result = str(findCustomer(key))
            conn.send(result.encode())
        elif(data == '2'):
            newData = conn.recv(4096).decode().split('*')
            newName = newData[0].strip()
            newAge = newData[1].strip()
            newAddress = newData[2].strip()
            newPhoneNo = newData[3].strip()
            result = str(add_customer(newName, newAge, newAddress, newPhoneNo))
            conn.send(result.encode())
        elif(data == '3'):
            nameToDeleteRecord = conn.recv(4096).decode().strip()
            result = str(delete_customer(nameToDeleteRecord))
            conn.send(result.encode())
        elif(data == '4'):
            newData = conn.recv(4096).decode().split('*')
            newName = newData[0].strip()
            newAge = newData[1].strip()
            result = str(update_customer_age(newName, newAge))
            conn.send(result.encode())
        elif (data == '5'):
            newData = conn.recv(4096).decode().split('*')
            newName = newData[0].strip()
            newAddress = newData[1].strip()
            result = str(update_customer_address(newName, newAddress))
            conn.send(result.encode())
        elif (data == '6'):
            newData = conn.recv(4096).decode().split('*')
            newName = newData[0].strip()
            newPhoneNo = newData[1].strip()
            result = str(update_customer_phone_number(newName, newPhoneNo))
            conn.send(result.encode())
        elif(data == '7'):
            result = str(sendDataReport(customers))
            # print(result)
            conn.send(result.encode())
        elif(data == '8'):
            conn.send("Good Bye!".encode())
            # conn.close()
            print('client disconnected')
            print('**************************************************************************************')
        else:
            print('no valid data to send')