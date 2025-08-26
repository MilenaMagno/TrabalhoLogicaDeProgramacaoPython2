print('Bem-vindo à loja de gelados da Milena Magno')
print('--------------------Cardápio---------------------')
print('-------------------------------------------------')
print('---| Tamanho  |  Cupuacu (CP)  |  Acaí (AC)  |---')
print('---|    P     |    R$  9.00    |  R$ 11.00   |---')
print('---|    M     |    R$ 14.00    |  R$ 16.00   |---')
print('---|    G     |    R$ 18.00    |  R$ 20.00   |---')
print('-------------------------------------------------')

dinheiro = 0
preco1 = 0
preco2 = 0

while True:
    #Verificar sabor (s) e tamanho (s) escolhido (s)
    op = input('Qual o sabor desejado? (CP/AC)') #Selecionar o sabor desejado
    if(op == 'CP'):
      tam = input('Qual o tamanho desejado?(P/M/G)') #Solicitar o tamanho desejado
      if(tam == 'P'):
        preco1 = preco1 + 9
        print(f'Você pediu um cupuacu no tamanho {tam}: R$ {preco1}.')
      elif(tam == 'M'):
          preco1 = preco1 + 14
          print(f'Você pediu um cupuacu no tamanho {tam}: R$ {preco1}.')
      elif(tam == 'G'):
          preco1 = preco1 + 18
          print(f'Você pediu um cupuacu no tamanho {tam}: R$ {preco1}.')
      else:
           print('Tamanho inválido. Tente novamente.')
           continue #Recomecar o loop se o tamanho for inválido
    elif(op == 'AC'):
        tam = input('Qual o tamanho desejado?(P/M/G)') #Solicitar tamanho desejado
        if(tam == 'P'):
          preco2 = preco2 + 11
          print(f'Você pediu um acaí no tamanho {tam}: R$ {preco2}.')
        elif(tam == 'M'):
            preco2 = preco2 + 16
            print(f'Você pediu um acaí no tamanho {tam}: R$ {preco2}.')
        elif(tam == 'G'):
            preco2 = preco2 + 20
            print(f'Você pediu um acaí no tamanho {tam}: R$ {preco2}.')
        else:
            print('Tamanho inválido. Tente novamente.')
            continue

    else:
        print('Sabor inválido. Tente novamente.')
        continue#Recomecar o loop se o sabor for inválido

    x = input('Deseja mais alguma coisa? (S/N)')
    if x == 'S':
        continue
        if x == 'N':
            break #quebrar loop se o usuário não quiser fazer mais escolhas
    #Calcular e informar valor final
    dinheiro += preco1 + preco2
    print(f'O valor total a ser pago é: R$ {dinheiro}.')
    break # encerrar o programa
