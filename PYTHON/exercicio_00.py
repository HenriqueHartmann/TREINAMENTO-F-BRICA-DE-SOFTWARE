# -*- coding: utf-8 -*-
def preco_aluguel_carro(dias,km):
    ''' Recebe uma quantidade de dias que o carro foi alugado e a 
    quantidade de kilometros rodados, e retorna o valor a ser pago.
    1 dia: 60 reais mais R$ 0,15 por km rodado.
    Dica: use round() para arrendondar o resultado'''
    d = 60
    k = 0.15
    total_dias = d * dias
    total_km = k * km
    total_pagar = total_dias + total_km
    return total_pagar

def dias_para_segundos(dias,horas,minutos,segundos):
    ''' Recebe uma data em dias com horas,minutos,segundos, e retorna 
    a data em segundos'''
    total_horas = horas + (dias * 24)
    total_minutos = minutos + (total_horas * 60)
    total_segundos = segundos + (total_minutos * 60)
    return total_segundos

def salario(dinheiro_horas,horas_mensais):
    ''' Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto'''
    salario_bruto = dinheiro_horas * horas_mensais
    salario_cem = salario_bruto / 100
    desc_INSS = salario_cem * 8
    desc_IR = salario_cem * 11
    desc_Sindicato = salario_cem * 5
    desc_total = desc_INSS + desc_IR + desc_Sindicato
    salario_liquido = salario_bruto - desc_total
    return round(salario_liquido)

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
        print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
            repr(obtido)))

def main():

    print('Preco a pagar pelo aluguel do carro:')
    test(preco_aluguel_carro(10,100), 615.00)
    test(preco_aluguel_carro(13,133), 799.95)
    test(preco_aluguel_carro(1,0), 60.00)
    test(preco_aluguel_carro(3,79), 191.85)

    print('Dias,horas,minutos e segundos para segundos:')
    test(dias_para_segundos(0,0,0,1), 1)
    test(dias_para_segundos(0,0,1,0), 60)
    test(dias_para_segundos(0,0,1,1), 61)
    test(dias_para_segundos(0,1,0,0), 3600)
    test(dias_para_segundos(0,1,1,0), 3660)
    test(dias_para_segundos(0,1,1,1), 3661)
    test(dias_para_segundos(1,0,0,0), 86400)
    test(dias_para_segundos(0,23,59,59), 86399)
    test(dias_para_segundos(1,1,1,1), 90061)
    test(dias_para_segundos(10,20,59,1), 939541)

    print('Salário líquido:')
    test(salario(10,80), 608)
    test(salario(100,30), 2280)
    test(salario(2.5,300), 570)
    test(salario(5,120), 456)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")