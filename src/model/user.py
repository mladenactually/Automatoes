from src.model.permission import Permission


class Person:
    def __init__(self, pid, first_name, last_name):
        self.pid = pid
        self.first_name = first_name
        self.last_name = last_name


class User:
    def __init__(self, person, permission_table):
        self.person = person
        self.permission_table = permission_table


class Designer(User):
    def __init__(self, person):
        super().__init__(person, Permission(read=True, write=False, repair=True))
        self.tickets = []
        self.designed_homes = []


class Owner(User):
    def __init__(self, person):
        super().__init__(person, Permission(read=True, write=True, repair=False))
        self.tickets = []


class Friend(User):
    def __init__(self, person):
        super().__init__(person, Permission(read=True, write=True, repair=False))


class Guest(User):
    def __init__(self, person):
        super().__init__(person, Permission(read=True, write=False, repair=False))
