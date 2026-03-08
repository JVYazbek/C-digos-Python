"""a) Implemente uma função para calcular a amplitude do dia. 
A função deverá receber uma tupla (data, tmin, tmax) e retornar a amplitude térmica do dia (tmax – tmin).

b) Implemente uma função que receba a lista de tuplas e retorne uma lista de tuplas
 no formato (data, media_dia, amplitude), onde media_dia = (tmin + tmax)/2.

c) Implemente uma função que receba a lista do de tuplas no formato
 (data, media_dia, amplitude) e retorne a data em que houve a maior amplitude registrada."""

lista = []
dias = int(input("digite quantos dias serão comparados -->"))
for i in range (dias):
    data = input("DATA -->")
    temp_minima = float(input("temp_min-->"))
    temp_max = float(input("temp_max-->"))  
    amplitude = temp_max - temp_minima  
    lista.append({"DATA": data, "temperatura minima": temp_minima, "temperatura maxima": temp_max, "Amplitude térmica": amplitude})
print(lista)

lista2 = []
for i in range(dias):
    media_dia = (temp_minima + temp_max)/2
    lista2.append({"DATA": data,"temperatura média":media_dia, "Amplitude térmica": amplitude})
print(lista2)
