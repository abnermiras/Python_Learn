import random

# A Matriz começa no Zero!
#          0      1     2     3       4     5       6    
pessoa = ["Je", "Tu", "Il" ,"Elle", "On", "Vous", "Ils"]
#          0          1       2         3         4      
verbo = ["Aller", "Aimer", "Sauter", "Courir", "Voler", "Étudier", "Jouer", "Travailler"]
#   5         6          7
 
#          0       1       2       3     
aluno = ["Jose","Maria","Pedro","João"]
questao = str

def randomiza():
#indice do pessoa (inicio e fim)
    indPessoa = random.randint(0,6)
#indice do verbo (inicio e fim)
    indVerbo = random.randint(0,7)
#indice do Aluno (inicio e fim)
    indAluno = random.randint(0,3)
   
#comando para limpar a tela e ir para primeira linha
    print("\x1b[2J\x1b[1;1H", end="")

  #texto que vai ser impresso para ser lido
    print('Pronome Pessoal: ' + pessoa[indPessoa] + '\n' + '          Verbo: ' + verbo[indVerbo] + '\n     para aluno: ' + aluno[indAluno])
    print('\n')
  #pergunta para finalziar o programa
    return input('Continua S/N? : ')
     
#chama a funcao pela primeira vez
questao = randomiza()

#condicao de loop para pergunta de finalizacao
while(questao =='s'):
    questao = randomiza()
    


