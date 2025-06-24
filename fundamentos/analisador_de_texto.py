def analisar_texto_digitado():
  print("-----------------------------------")
  print("--- Sistema analisador de texto ---")
  print("-----------------------------------")
  
  texto_digitado = input("Digite um texto: ")
  
  if texto_digitado.isnumeric():
    return print(f"Texto digitado: \"{texto_digitado} Sistema não reconhece somente número\"")
  
  converte_para_minusculo = texto_digitado.lower()
  
  palavras = [palavra for palavra  in converte_para_minusculo.split() if palavra]
  quantidadeDePalavras = len(palavras)
  
  vogais = "aeiouáàãâéêíóôõúü"
  numero = "1234567890"
  contador_vogais = 0
  contador_consoante = 0
  contador_numero = 0
  
  for letra in texto_digitado:
      if letra.isdigit():
          contador_numero += 1
      elif letra.isalpha():
          if letra.lower() in vogais: 
              contador_vogais += 1
          else:
              contador_consoante += 1
              
  palavra_mais_longa = ""
  if palavras:
    palavra_mais_longa = max(palavras, key=len)
        
    print("-------------------------------")
    print("\n--- Resultados da Análise ---")
    print("-------------------------------")
    print(f"Texto digitado: \"{texto_digitado}\"")
    print(f"Número total de caracteres (incluindo espaços e pontuação): {len(texto_digitado)}")
    print(f"Número de palavras: {quantidadeDePalavras}")
    print(f"Número de vogais: {contador_vogais}")
    print(f"Quantidade de números: {contador_numero}")
    print(f"Número de consoantes: {contador_consoante}")
    print(f"Palavra mais longa: \"{palavra_mais_longa}\" (com {len(palavra_mais_longa)} caracteres)")
  
analisar_texto_digitado()