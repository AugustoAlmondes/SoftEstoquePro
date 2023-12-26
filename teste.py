import bcrypt

# Senha inserida pelo usuário (pode ser obtida via input)
senha = "minha_senha_segura"

# Gerar um hash para a senha
senha_codificada = senha.encode('utf-8')  # Codificar a senha para bytes
hashed = bcrypt.hashpw(senha_codificada, bcrypt.gensalt())

# Exibir o hash gerado
print("Senha criptografada:", len(hashed))

# Verificar se a senha fornecida corresponde ao hash (para fins de autenticação, por exemplo)
senha_informada = "minha_senha_segura"
senha_informada_codificada = senha_informada.encode('utf-8')

# Verificar se a senha informada corresponde ao hash gerado
if bcrypt.checkpw(senha_informada_codificada, hashed):
    print("Senha correta. Acesso concedido!")
else:
    print("Senha incorreta. Acesso negado.")
