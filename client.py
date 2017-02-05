import socket
import pickle

class client():
    def __init__(self, server="127.0.0.1", size=1024):
        self.server = server
        self.size = size

    def sendStudent(self, student):
        s = self.connectToServer()
        s.send(bytes("SEND", "UTF-8"))
        if not s.recv(self.size).decode("UTF-8") == "200":
            raise Exception("Could not send SEND code")
        s.send(bytes(student.getName(), "UTF-8"))
        print(student.getName())
        if not s.recv(self.size).decode("UTF-8") == "200":
            raise Exception("Could not send Name")
        s.send(bytes(student.getID(), "UTF-8"))
        print(student.getID())
        if not s.recv(self.size).decode("UTF-8") == "200":
            raise Exception("Could not send ID")
        s.send(bytes(student.getClass(), "UTF-8"))
        print(student.getClass())
        if not s.recv(self.size).decode("UTF-8") == "200":
            raise Exception("Could not send Class")
        s.send(bytes(student.getTeacher(), "UTF-8"))
        print(student.getTeacher())
        if not s.recv(self.size).decode("UTF-8") == "200":
            raise Exception("Could not send Teacher")
        s.close()

    def connectToServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((self.server, 9999))
        s.send(bytes("ALIVE?", "UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        print("Data: ", data)
        if not data == "ALIVE":
            raise Exception("Server was not alive")
        return s

    def getClassteacherArray(self):
        try:
            s = self.connectToServer()
        except Exception as e:
            print(e)
        s.send(bytes("GET INFO", "UTF-8"))
        data = s.recv(4096)
        return pickle.loads(data)

    def signOut(self, student):
        try:
            s = self.connectToServer()
        except Exception as e:
            print(e)
        s.send(bytes("SIGNOUT", "UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        if not data == "200":
            print("Data: ", data)
            raise Exception("Failed to signout")
        s.send(bytes(str(student), "UTF-8"))
        if not s.recv(1024).decode("UTF-8") == "200":
            print("Data: ", data)
            raise Exception("Failed to send Signout")



