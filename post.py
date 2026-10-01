texto = (input("Digite seu texto: "))
quantidade = len(texto)
if quantidade >3:
    print(f"Excedeu o limite de caracteres ({quantidade})")
else:
    print(f"menos q o limite ({quantidade})")