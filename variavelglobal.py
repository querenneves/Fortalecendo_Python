#variavel global 
nome_global = 'Lara'


def funcao_local():
    #variavel local
    nome_local = 'João'
    print('Dentro da variável local,'+" o nome local é:", nome_local)



funcao_local()

print('Fora da função, o nome global é:', nome_global)