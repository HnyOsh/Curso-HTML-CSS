times = []

while True:
    
    jogador = {}
    partidas = []

    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))

    for c in range(tot):
        partidas.append(int(input(f'   Quantos gols na partidas {c + 1}? ')))
    print('-=' * 30)

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    times.append(jogador.copy)

    while True:
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
        

print(partidas)
print(jogador)
print(times)