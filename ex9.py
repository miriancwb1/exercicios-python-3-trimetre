# Programa para converter minutos em horas e minutos
minutos = int(input("Digite a quantidade de minutos: "))
horas = minutos // 60
restante_minutos = minutos % 60
print(f"{minutos} minutos são equivalentes a {horas} horas e {restante_minutos} minutos.")
