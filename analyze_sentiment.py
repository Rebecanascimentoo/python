import re

def analyze_sentiment():
    """
    Função que analisa o sentimento de um comentário fornecido pelo usuário.
    
    Retorna:
        Uma string indicando o sentimento do comentário: "Positivo", "Negativo" ou "Neutro".
    """
    # Entrada do usuário
    comentario = input("Digite seu comentário: ")

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Determina o sentimento com base na contagem de palavras
    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Neutro"

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)