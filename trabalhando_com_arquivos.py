def le_nome():
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    nome = arquivo.read()
    lista = nome.split('|')
    for n in (lista):
        print(n)

def escreve_nome(nome):
    arquivo = open('meu_nome.txt', 'a', encoding='utf-8')
    arquivo.write(nome)

def entrada_usuario():
    while True:
        nome = input('Digite seu nome: ')
        if nome == '0':
            break
        idade = input('Digite sua idade: ')
        sexo = input('Digite seu sexo: ')
        telefone = input('Digite seu Telefone: ')

        dados = (f'{nome}|{idade}|{sexo}|{telefone}\n')

        escreve_nome(dados)

def main():
    
    entrada_usuario()
    le_nome()

main()
