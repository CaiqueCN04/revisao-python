def calcular_salario():
    salario= float(input('coloque seu salario: '))
    if salario>=2000:
        sp=salario*(7/100)
        sf1=salario+sp
        print(f'seu salario final é {sf1}')
    else:
        sg=salario*(15/100)
        sf2= salario+sg
        print(f'seu salario final é {sf2}')
        
        

