# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
def calcular_area_base ():
    area = 3.14 * (raio * raio)
    return f"a area do círculo é: {area}"

def calcular_volume_cilindro(altura):
    volume = 3.14 * (raio * raio) * altura
    return f"o volume do cilindro é: {volume}"

print ("Digite o raio para calcular a área do círculo e do cilindro  ")

raio = float(input("digite o raio : "))
altura1 = float(input("digite a altura do cilindro para calcular o volume:  "))
volume_cilindro = calcular_volume_cilindro(altura1)
area_raio1 = calcular_area_base()

print(area_raio1)
print(volume_cilindro)


