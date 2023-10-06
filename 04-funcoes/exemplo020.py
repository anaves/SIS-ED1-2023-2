def a():
    print('inicio A')
    for i in range(5):
        print(f'A: {i}')
    b()
    print('fim A')
    return None   # None => NADA

def b():
    print('funcao b')
    print('b1 e b2')
    print('fim b')

print('Inicio main')    # main = principal!
a()                     # chamar a funcao a()
#print('invocar a funcao a() novamente')
#a()
print('Fim main')