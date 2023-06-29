"""
Codifique um algoritmo que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem: 19, 21, 25, 22, 20, 17 e 15°C, de domingo a sábado, respectivamente, o algoritmo deverá exibir:
D: *******************
S: *********************
T: *************************
Q: **********************
Q: ********************
S: *****************
S: *******************
Suponha que as temperaturas sejam todas positivas e que nenhuma seja maior que 80°C.
"""
temperaturas = [19, 21, 25, 22, 20, 17, 15]

for indice, temperatura in enumerate(temperaturas):
    dia_semana = ""
    if indice == 0:
        dia_semana = "D"
    elif indice == 1:
        dia_semana = "S"
    elif indice == 2:
        dia_semana = "T"
    elif indice == 3:
        dia_semana = "Q"
    elif indice == 4:
        dia_semana = "Q"
    elif indice == 5:
        dia_semana = "S"
    elif indice == 6:
        dia_semana = "S"

    # Exibe o dia da semana e o histograma
    print(f"{dia_semana}: {'*' * temperatura}")