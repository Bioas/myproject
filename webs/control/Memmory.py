
class PathFile:
    def __init__(self, filename):
        # print(".......................................................................................................")
        # print("Path File")
        self.M_file = filename
        # print("Name path :", self.M_file)

    def set_file(self, file_name):
        self.M_file = file_name
        # print("N path :", self.M_file)

    def get_file(self):
        return self.M_file
