def soma_todos(nome, email, *args):
    return sum(args), nome, email


print(soma_todos('Angelina', 'Jolie'))
print(soma_todos('Angelina', 'Jolie', 1))
print(soma_todos('Angelina', 'Jolie', 2, 3))
print(soma_todos('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos('Angelina', 'Jolie', 3, 4, 5, 6))

print(soma_todos('Angelina', 'Jolie', 23.4, 12.5))
