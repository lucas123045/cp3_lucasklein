temperaturas = [
    [28, 31, 34, 33], #sala1
    [25, 27, 29, 28], #sala2
    [32, 35, 36, 34], #sala3
    [24, 26, 25, 27]  #sala4
]

sala_maior_risco = None
max_criticos = -1

for i, sala in enumerate(temperaturas):
    numero_sala = i + 1
    media = sum(sala) / len(sala)
    criticos = sum(1 for temp in sala if temp >= 33)

    print ("--------------------------------")
    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {criticos}")
    print("---------------------------------")

    if criticos > max_criticos:
        max_criticos = criticos
        sala_maior_risco = numero_sala

print(f"Sala com maior risco: Sala {sala_maior_risco}")