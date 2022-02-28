class Produto:
    __id: int
    __nome: str
    __departamento: str
    __codbar: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: int):
        self.__nome = nome

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: int):
        self.__departamento = departamento

    @property
    def codbar(self):
        return self.__codbar

    @codbar.setter
    def codbar(self, codbar: int):
        self.__codbar = codbar

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)