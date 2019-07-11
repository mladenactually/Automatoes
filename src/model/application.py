class Application:
    def __init__(self, smart_home, user):
        self.smart_home = smart_home
        self.user = user
        self.user_data = {}

    def login(self, username, password):
        if username in self.user_data:
            if self.user_data[username] == password:
                return
            else:
                print("Invalid password")
        else:
            print("Username doesn't exist")

    def logout(self):
        pass

    def load_user_data(self):
        file = open('user_data', 'r')
        line = file.readline()
        while line != "":
            tokens = line.split("|")
            username = tokens[0]
            password = tokens[1]
            self.user_data[username] = password
            line = file.readline()
        file.close()
