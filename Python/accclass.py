class PartyAnimal:
    __x = 0
    name = ''
    def acc(self,x):
        self.__x=x
        return self.__x
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        print(self.name,'party count',self.__x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')
qq=q.acc(100)
print(qq)