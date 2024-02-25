

class SigletonTest:

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SigletonTest, cls).__new__(cls)
            print(f"criado o objeto: {cls.instance}")
        return cls.instance
    
    def exibe_teste(self):
        print("Teste Singleton")


s1 = SigletonTest()
print(f"instancia 1: {id(s1)}")
s1.exibe_teste()


s2 = SigletonTest()
print(f"instancia 2: {id(s2)}")
s2.exibe_teste()