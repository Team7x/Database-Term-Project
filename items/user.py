class user:
    def __init__(self,nim,name,alamat):
        self.__nim=nim
        self.__name=name
        self.__alamat=alamat

    def nim(self):
        return self.__nim