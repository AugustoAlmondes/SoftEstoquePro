import bcrypt

# Senha inserida pelo usuário (pode ser obtida via input)
senha = "play2233"
print(senha)
# Gerar um hash para a senha
senha_codificada = senha.encode('utf-8')  # Codificar a senha para bytes
hashed = bcrypt.hashpw(senha_codificada, bcrypt.gensalt())

# Exibir o hash gerado
print("Senha criptografada:", hashed)

# Verificar se a senha fornecida corresponde ao hash (para fins de autenticação, por exemplo)
senha_informada = "play2233"
senha_informada_codificada = senha_informada.encode('utf-8')
print(senha_informada_codificada)
# b'$2b$12$a/AvPX7TEQGgfGHnKF3p2uY89EQtBotZRAL8mfM3VVxTz0L1RtHn2'

# Verificar se a senha informada corresponde ao hash gerado
if bcrypt.checkpw(senha_informada_codificada, hashed):
    print("Senha correta. Acesso concedido!")
else:
    print("Senha incorreta. Acesso negado.")

# def verificar_casas_decimais(numero, casas_decimais):
#     # Arredonda o número para a quantidade desejada de casas decimais
#     numero_arredondado = round(numero, casas_decimais)
    
#     # Verifica se o número original é igual ao número arredondado
#     if numero == numero_arredondado:
#         return f"O número {numero} já possui {casas_decimais} casas decimais."
#     else:
#         return f"O número {numero} não possui {casas_decimais} casas decimais e foi arredondado para {numero_arredondado}."

# # Exemplo de uso
# numero = 3.14159
# casas_decimais_desejadas = 3

# resultado = verificar_casas_decimais(numero, casas_decimais_desejadas)
# print(resultado)
