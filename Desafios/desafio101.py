def voto(anonasc):
    idade = 2019 - anonasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    if idade >= 65 or idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))
