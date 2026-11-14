N = 5 

garfos = [None] * N
estado = ["com fome"] * N

def garfo_esquerda(p):
    return p

def garfo_direita(p):
    return (p + 1) % N

def jantar(p):
            if estado[p] == "com fome":
                if garfos[garfo_esquerda(p)] is None:
                    garfos[garfo_esquerda(p)] = p
                    print(f"Filósofo {p} pegou o garfo {garfo_esquerda(p)} na esquerda.")
                    estado[p] = "com fome com um garfo"
                    return
                else:
                    print(f"Filósofo {p} não conseguiu pegar o garfo {garfo_esquerda(p)} na esquerda e está esperando.")
                    return
            elif estado[p] == "com fome com um garfo":
                if garfos[garfo_direita(p)] is None:
                    garfos[garfo_direita(p)] = p
                    print(f"Filósofo {p} pegou o garfo {garfo_direita(p)} na direita.")
                    estado[p] = "comendo"
                    return
                else:
                    print(f"Filósofo {p} não conseguiu pegar o garfo {garfo_direita(p)} na direita e está esperando.")
                    return
            elif estado[p] == "comendo":
                garfos[garfo_esquerda(p)] = None
                garfos[garfo_direita(p)] = None
                print(f"Filósofo {p} terminou de comer e liberou os garfos {garfo_esquerda(p)} e {garfo_direita(p)}.")
                estado[p] = "pensando"
                return

for iniciar in range(5):
    for p in range(N):
        jantar(p)

            