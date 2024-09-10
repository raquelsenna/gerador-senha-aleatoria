import random

def GerarSenha():
  senha = ""
  caractere = "zaqcdevfrbgtnhymjukilop123456789@/#%"

  for i in range(8):
    senha += random.choice(caractere)

  print('='*26)
  print('\tSENHA GERADA')
  print(f'\t{senha}')
  print('='*26)


GerarSenha()
