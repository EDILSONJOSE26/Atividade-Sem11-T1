carro = float(input().strip())
poupanca = 10000
rende = 0.007
taxa = 0.004
mes = 0

while poupanca <= carro: 
    poupanca = poupanca + poupanca * rende 
    carro = carro + carro * taxa 
    mes += 1

print(mes)
