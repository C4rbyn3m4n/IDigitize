import socket

class client():
    def __init__(self, server="127.0.0.1"):
        self.server = server

    def sendStudent(self, student):
        size =1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server, 9999))
        s.send(bytes("ALIVE?", "UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        print("Data: ", data)
        if not data == "ALIVE":
            raise Exception("Server was not alive")
        print(1)
        s.send(bytes("SEND", "UTF-8"))
        print(2)
        if not s.recv(size).decode("UTF-8") == "200":
            raise Exception("Could not send")
        s.send(bytes(student.getName(), "UTF-8"))
        print(student.getName())
        if not s.recv(size).decode("UTF-8") == "200":
            raise Exception("Could not send Name")
        s.send(bytes(student.getID(), "UTF-8"))
        print(student.getID())
        if not s.recv(size).decode("UTF-8") == "200":
            raise Exception("Could not send ID")
        s.send(bytes(student.getClass(), "UTF-8"))
        print(student.getClass())
        if not s.recv(size).decode("UTF-8") == "200":
            raise Exception("Could not send Class")
        s.send(bytes(student.getTeacher(), "UTF-8"))
        print(student.getTeacher())
        if not s.recv(size).decode("UTF-8") == "200":
            raise Exception("Could not send Teacher")
        s.close()




