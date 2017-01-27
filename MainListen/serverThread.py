import socket
import threading
import queue
import dataStudent
import time

class serverThread(threading.Thread):
    def __init__(self, queue, statusQueue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.statusQueue = statusQueue
        self.daemon = True

    def run(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        serversocket.bind(("localhost", 9999))
        serversocket.listen(10)
        while 1:
            client, address = serversocket.accept()
            client.settimeout(30)
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
                                        student.setSignIn(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                                        print(student)
                                        self.queue.put(student)
                                        print(self.queue.qsize())
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