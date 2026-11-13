N = 5 

garfos = [None] * N
estado = ["com fome"] * N

def garfo_esquerda(p):
    return p

def garfo_direita(p):
    return (p + 1) % N


def jantar(p):
            left = min(garfo_esquerda(p), garfo_direita(p))
            right = max(garfo_esquerda(p), garfo_direita(p))
        
            if estado[p] == "com fome":
                if garfos[left] is None:
                    garfos[left] = left
                    print(f"Filósofo {p} pegou o garfo {left} na esquerda.")
                    estado[p] = "com fome com um garfo"
                    if garfos[right] is None:
                        garfos[right] = right
                        print(f"Filósofo {p} pegou o garfo {right} na direita e começou a comer.")
                        estado[p] = "comendo"
                        return
                    print(f"Filósofo {p} não conseguiu pegar o garfo {right} na direita e está esperando.")
                    return
                else:
                    print(f"Filósofo {p} não conseguiu pegar o garfo {left} na esquerda e está esperando.")
                    return
            elif estado[p] == "com fome com um garfo":
                if garfos[right] is None:
                    garfos[right] = right
                    print(f"Filósofo {p} pegou o garfo {right} na direita e começou a comer.")
                    estado[p] = "comendo"
                    return
                else:
                    print(f"Filósofo {p} não conseguiu pegar o garfo {right} na direita e está esperando.")
                    return
            elif estado[p] == "comendo":
                garfos[right] = None
                garfos[left] = None
                print(f"Filósofo {p} terminou de comer e liberou os garfos {right} e {left}.")
                estado[p] = "pensando"
                return

for iniciar in range(5):
    for p in range(N):
        jantar(p)

            