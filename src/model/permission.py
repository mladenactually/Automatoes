class Permission:
    def __init__(self, read=False, write=False, repair=False):
        self.read = read
        self.write = write
        self.repair = repair
