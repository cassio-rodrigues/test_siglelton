class LazySingletonTeste:

    __instance = None

    def __init__(self) -> None:
        if not LazySingletonTeste.__instance:
            print("chamando metodo __init__")
        else:
            print(f"A instancia já foi criada: {self.get_instance()}")

    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingletonTeste()
        return cls.__instance

s1 = LazySingletonTeste()

print(f"criando objeto: {LazySingletonTeste.get_instance()}")

s2 = LazySingletonTeste()