class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0

  def Calcula_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media
  
  def mostraDados(self):
    print(f'Nome do(a) aluno(a): {self.nome}')
    print(f'Nota 1: {self.nota1}')
    print(f'Nota 2: {self.nota2}')

  def resultado(self):
    if self.media >= 6.0:
      return 'Aluno(a) aprovado(a)'
    else:
      return 'Aluno(a) reprovado(a)'

aluno1 = Aluno('maria', 7.0, 9.0)
aluno1.mostraDados()

media = aluno1.Calcula_media()
print(f'A média é: ', media)
aluno1.resultado()
resultado = aluno1.resultado()
print(resultado)