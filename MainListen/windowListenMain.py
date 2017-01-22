import tkinter as tk
import socket
import threading
import dataStudent

class windowListenMain():
    def __init__(self, parent):
        self.parent = parent
        self.students = []

        self.frameMain = tk.Frame(parent)
        tk.Label(self.frameMain, text="test").pack()

        self.frameMain.pack()

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(("127.0.0.1", 9999))
        self.serversocket.listen(10)
        t = threading.Thread(target=self.server)
        t.daemon = True
        t.start()

    def server(self):
        while 1:
            client, address = self.serversocket.accept()
            client.settimeout(60)
            t = threading.Thread(target=self.dealWithClient, args=(client, address))
            t.daemon = True
            t.start()

    def dealWithClient(self, client, address):
        size = 1024
        while 1:
            try:
                data = client.recv(size).decode("UTF-8")
                print("Data: ", data)
                if data:
                    if data == "ALIVE?":
                        client.send(bytes("ALIVE", "UTF-8"))
                    elif data == "SEND":
                        student = dataStudent.dataStudent()
                        client.send(bytes("200", "UTF-8"))
                        data = client.recv(size).decode("UTF-8")
                        print("Data: ", data)
                        if data:
                            student.setName(data)
                            client.send(bytes("200", "UTF-8"))
                            data = client.recv(size).decode("UTF-8")
                            print("Data: ", data)
                            if data:
                                student.setID(data)
                                client.send(bytes("200", "UTF-8"))
                                data = client.recv(size).decode("UTF-8")
                                print("Data: ", data)
                                if data:
                                    student.setClass(data)
                                    client.send(bytes("200", "UTF-8"))
                                    data = client.recv(size).decode("UTF-8")
                                    print("Data: ", data)
                                    if data:
                                        student.setTeacher(data)
                                        client.send(bytes("200", "UTF-8"))
                                        client.close()
                                        self.students.append(student)
                                        break
                                    else:
                                        raise Exception("No Teacher Received")
                                else:
                                    raise Exception("No Class Received")
                            else:
                                raise Exception("No ID Received")
                        else:
                            raise Exception("No Name Received")
                    else:
                        raise Exception("Client sent invalid data")
                else:
                    raise Exception("Client Disconnected")
            except Exception as e:
                print(e)
                break
                # client.close()
        print(self.students)

