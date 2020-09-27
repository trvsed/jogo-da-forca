''' 1. Elabore um JOGO de FORCA:
Crie uma lista de palavras e sorteie uma randomicamente uma a cada execução. Pesquise como usar números aleatórios (randômicos)
O programa mostra a forca com os espaços correspondentes às letras da palavra escolhida:
Ex: PERNAMBUCO.

O usuário digita a letra, e se ela fizer parte da palavra sorteada, ela será colocada na posição certa.
A cada tentativa uma parte do boneco será desenhada.
O usuário terá 6 tentativas para acertar a palavra, antes de ser enforcado.
'''

from random import choice #Biblioteca utilizada para sortear as palavras a serem descobertas aleatóriamente.

vocabulario = ["fatec", "aluno", "professor", "programacao", "python"] #Palavras escolhidas para serem sorteadas.
palavra = choice(vocabulario) #Variável de seleção de uma das palavras definidas.

print("Jogo da Forca - FATEC\n")
print("Bem vindo ao Jogo da Forca. Boa sorte!\n")

chances = 6 #Variável definida para limitar o número de chances que o usuário tem para tentar uma palavra antes de completar a forca.
alfabeto = list("abdcefghijklmnopqrstuvwxyz") #Variável definindo as letras que podem ser aceitas dentro do programa, qualquer outra coisa que for digitada e que não esteja dentro dessa variável o programa vai retornar um erro.
tentativas = [] #Lista criada para printar as tentativas realizadas durante o jogo.
erros = 0 #Variável que vai adicionar um valor caso o usuário erre, para que o desenho da forca seja printado durante os erros.

while True:
    print(tentativas)
    print("Chances: ",chances)

    for letra in palavra: #Busca a letra digitada na palavra escolhida pelo programa.
        if letra in tentativas: #Contabiliza a letra se estiver correta na palavra.
            print(letra, end = ' ')
        else: #Continua o espaço vazio caso a letra esteja incorreta.
            print('_', end= ' ')

    palpite = input("\nDigite uma letra(ou a palavra) ou digite 'sair' para encerrar o programa: ").lower()
    if palpite == "sair": #Opção para finalizar o jogo.
        break
    elif palpite not in alfabeto or palpite == '': #Se mais de uma letra ou números ou caractéres especiais forem digitados, serão desconsiderados pelo programa.
        print("Isso não é uma letra!")
        continue
    elif palpite in tentativas: #Caso tenha repetido alguma letra, será desconsiderado pelo programa e você terá uma nova tentativa.
        print("Você já tentou essa letra. Tente outra!")
        continue
    tentativas.append(palpite)
    if palpite in palavra: #Caso acerte uma letra.
        print("Parabéns! Você acertou uma letra!")
    else:
        print("Não há essa letra na palavra escolhida")
        chances-=1
        erros+=1
    if erros == 0: #Condição criada para apresentar o desenho da forca durante as tentativas, durante o acerto ou erro, mas caso haja o erro, um valor é adicionado a variável erros e o programa apresenta parte a parte do desenho da forca.
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |\\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|     \\ ")
        print("_      ")
        print()
    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|   / \\ ")
        print("_      ")
        print()
    if chances == 0:
        print("Game over!!! >:)")
        break
    elif set(palavra).issubset(set(tentativas)): #Caso o usuário consiga acertar decifrar todas as letras, a condição de repetição vai printar a mensagem de vitória.
        print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
        break
