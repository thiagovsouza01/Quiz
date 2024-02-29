import re

def validar_senha(senha):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,32}$"
    
    if re.match(regex, senha):
        return True
    else:
        return False

senha = input("Digite sua senha: ")
if validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número; e ter de 6 a 32 caracteres. Além disso, não pode ter nenhum caractere de pontuação, acentuação ou espaço.")
