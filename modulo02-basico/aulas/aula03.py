frase = "Curso em Vídeo Python"
print(frase[0:5])#Vai de 0 a 5
print(frase[:5])#Também vai de 0 a 5
print(frase[7:])#Inicio em 7 e termina quando a frase termina
print(frase[0:19:2])#Pula de dois em dois
print(frase[::3])
print(frase[9::3])#Começa no nove e vai até o final[9:], depois pula em três e três[:3]
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
frase2 = frase.replace('Python', 'Java')
print(frase2)
dividido = frase.split()
print(dividido[0])

print(""" 
  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
  standard dummy text ever since the 1500s, when an 
  unknown printer took a galley of type and scrambled it to make a type specimen book. It has survive
  
  """)