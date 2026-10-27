import time

# Palavra-chave secreta para liberar o acesso
senha = "boxxx"

# Solicita a entrada inicial do usuário
keyword = input("Digite o nome de usuário para acessar a biblioteca: ")

# Laço de repetição: continua pedindo enquanto a senha estiver errada
while keyword != senha:
    print("Usuário incorreto")
    keyword = input("Digite o nome de usuário para acessar a biblioteca: ")

# Assim que o usuário acerta, a lista personalizada de jogos é liberada
lista = [
    "The Witcher 3: Wild Hunt", 
    "God of War Ragnarök", 
    "Hades II",
    "Cyberpunk 2077", 
    "Spider-Man 2", 
    "Elden Ring",
    "Alan Wake 2", 
    "Baldur's Gate 3", 
    "Resident Evil 4 Remake"
]

print("\nAcesso liberado! Carregando biblioteca de jogos...\n")

# Percorre e exibe cada item da lista com um pequeno atraso temporal
for item in lista:
    print(item)
    time.sleep(0.5)