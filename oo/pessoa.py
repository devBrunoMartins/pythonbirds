class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    bruno = Pessoa(nome='Bruno')
    gustavo = Pessoa(bruno, nome='Bruno')
    print(Pessoa.cumprimentar(gustavo))
    print(id(gustavo))
    print(gustavo.cumprimentar())
    print(gustavo.nome)
    print(gustavo.idade)
    for filho in gustavo.filhos:
        print(filho.nome)
    del gustavo.filhos
    gustavo.sobrenome = 'Martins'
    print(gustavo.__dict__)
    print(bruno.__dict__)