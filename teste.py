import bcrypt

senha = 'augusto'

senha_crip = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())

print(senha)
print(senha_crip)