class Cachorro:
    def __init__(self, nome, raça, comida):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.feliz = False
        self.acordado = False
        self.energia = 100  # Inicializando o atributo energia com 100

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado!") 

    def dormir(self):
        self.acordado = False
        self.energia = 100  # Restaurando a energia para 100 quando o cachorro dorme
        print(f"{self.nome} está dormindo e sua energia foi restaurada para {self.energia}!") 

    def comer(self):
        if self.acordado:
            if self.comida > 0:  # Garante que há comida disponível
                self.comida -= 1
                self.energia += 10  # Comendo aumenta a energia
                print(f"{self.nome} comeu e agora tem {self.energia} de energia!")
            else:
                print(f"{self.nome} não tem comida para comer!")
        else:
            print(f"{self.nome} está dormindo e não pode comer!") 

    def latir(self):
        if self.acordado:
            if self.energia > 0:
                self.energia -= 5  # Latindo consome energia
                print(f"{self.nome} está latindo: AU AU AU! Energia restante: {self.energia}")
            else:
                print(f"{self.nome} está muito cansado para latir.")
        else:
            print(f"{self.nome} está dormindo e não está latindo") 

    def brincar(self):
        if self.acordado:
            if self.energia >= 20:  # Verifica se há energia suficiente para brincar (20 ou mais)
                self.feliz = True
                self.energia -= 20  # Brincando gasta 20 de energia
                print(f"{self.nome} está brincando e está feliz! Energia restante: {self.energia}")
            else:
                print(f"{self.nome} está muito cansado para brincar e não tem energia suficiente.")
        else:
            print(f"{self.nome} está dormindo e não pode brincar.")

# Exemplo de uso
cachorro1 = Cachorro("Siena Velho", "Lander", 6)
cachorro1.brincar()  # Tenta brincar sem energia suficiente
cachorro1.comer()
cachorro1.acordar()
cachorro1.latir()
cachorro1.dormir()
cachorro1.brincar()
cachorro1.acordar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.brincar()
cachorro1.dormir()
