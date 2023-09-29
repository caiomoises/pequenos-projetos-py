import math

angulo = float(input('Qual o angulo que deseja verificar: '))
angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f' O ângulo de {angulo} possui SENO de {seno:.2F}\n',
      f'O ângulo de {angulo} possui COSSENO de {cosseno:.2F}\n',
      f'O ângulo de {angulo} possui TANGENTE de {tangente:.2F}')