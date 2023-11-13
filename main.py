### funções ### 

#declarar quatro estruturas: palavra-chave def;
# nome da função, que não deve iniciar com números ou símbolos; 
#lista: parâmetros passados para a função;
#corpo: contendo o bloco de comandos para serem executados; 

def exibirMensagem():
  print("Python é fácil!")
print("início")
exibirMensagem()

print("--------------------")

def saudacao(nome):
  print(f"Boa noite,  {nome}, como vai?")
print("início")
saudacao("Cintia")

class Aluno: 

  def __init__(self, nome, matricula, curso):
    self.nome = nome
    self.matricula=matricula
    self.curso = curso 

dados_aluno = Aluno(input("Digite o nome do aluno:"), input("Digite a matrícula do aluno:"), input("Digite o curso do aluno:"))

print("nome:", dados_aluno.nome)
print("matricula:", dados_aluno.matricula)
print("curso:", dados_aluno.curso)