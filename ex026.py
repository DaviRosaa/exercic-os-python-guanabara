frase=input("Digite uma frase: ").strip()
letra_a=frase.upper().count("A")
print(f"A letra a aparece {letra_a} vezes")
letra_a_b=frase.upper().find("A")+1
print(f"A posição que ela primeiro aparece é {letra_a_b}")
letra_a_c=frase.upper()
print(f"A posição que ela aparece pela ultima vez é {letra_a_c.rfind("A")+1}")


