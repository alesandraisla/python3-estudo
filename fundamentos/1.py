def analisar_texto():
    """
    Pede ao usuário um texto e exibe uma análise detalhada:
    número de palavras, vogais, consoantes e a palavra mais longa.
    """
    print("--- Analisador de Texto ---")
    texto_original = input("Digite seu texto: ")

    # 1. Pré-processamento do texto
    # Converte para minúsculas para facilitar a contagem de vogais/consoantes
    # Remove caracteres que não são letras ou espaços (ex: pontuação) para contagem de palavras mais precisa
    texto_processado = ''.join(char.lower() for char in texto_original if char.isalpha() or char.isspace())

    # 2. Contar palavras
    # Usa .split() para dividir o texto em uma lista de palavras
    # Filtra palavras vazias que podem surgir de múltiplos espaços
    palavras = [palavra for palavra in texto_processado.split() if palavra]
    numero_palavras = len(palavras)

    # 3. Contar vogais e consoantes
    vogais = "aeiouáàãâéêíóôõúü" # Inclui vogais acentuadas para uma contagem mais precisa
    contador_vogais = 0
    contador_consoantes = 0

    for char in texto_processado:
        if char.isalpha(): # Verifica se é uma letra
            if char in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1

    # 4. Encontrar a palavra mais longa
    palavra_mais_longa = ""
    if palavras: # Verifica se há palavras na lista para evitar erro em texto vazio
        # Usa a função max() com a chave len para encontrar a palavra com o maior comprimento
        palavra_mais_longa = max(palavras, key=len)

    # 5. Exibir resultados
    print("\n--- Resultados da Análise ---")
    print(f"Texto original: \"{texto_original}\"")
    print(f"Número total de caracteres (incluindo espaços e pontuação): {len(texto_original)}")
    print(f"Número de palavras: {numero_palavras}")
    print(f"Número de vogais: {contador_vogais}")
    print(f"Número de consoantes: {contador_consoantes}")
    print(f"Palavra mais longa: \"{palavra_mais_longa}\" (com {len(palavra_mais_longa)} caracteres)")

# Chama a função para executar o analisador
analisar_texto()