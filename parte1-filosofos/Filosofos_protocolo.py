N = 5 

garfos = [None] * N
estado = ["com fome"] * N
refeicoes = [0] * N
META = 5
LIMITE = 20

def garfo_esquerda(p):
    return p

def garfo_direita(p):
    return (p + 1) % N


def adquirir(garfo, p):
    if garfos[garfo] is None:
        garfos[garfo] = p
        return True

def liberar(garfo, p):
    if garfos[garfo] != p:
        raise ValueError("O filósofo não possui esse garfo.")
    garfos[garfo] = None


def jantar(p):            
            left = min(garfo_esquerda(p), garfo_direita(p))
            right = max(garfo_esquerda(p), garfo_direita(p))

            if estado[p] == "pensando":
                if refeicoes[p] == META:
                    estado[p] = "finalizado"
                    print(f"Filósofo {p} concluiu suas {META} refeições.")
                else:
                    estado[p] = "com fome"
                    print(f"Filósofo {p} está com fome.")
                return True
        
            if estado[p] == "com fome":
                if not adquirir(left,p):
                    print(f"Filósofo {p} não conseguiu pegar o garfo {left} na esquerda, e continua esperando pois o filósofo {garfos[left]} está utilizando.")
                    return False
                else:
                    estado[p] = "com fome com um garfo"
                    print(f"Filósofo {p} pegou o garfo {left} na esquerda. ")

            if estado[p] == "com fome com um garfo":
                if not adquirir(right,p):
                    print(f"Filósofo {p} não conseguiu pegar o garfo {right} na direita, e continua esperando pois o filósofo {garfos[right]} está utilizando.")
                    return False
                else:
                    print(f"Filósofo {p} pegou o garfo {right} na direita e começou a comer.")
                    estado[p] = "comendo"
                    return
                    
            elif estado[p] == "comendo":
                if garfos[left] != p or garfos[right] != p:
                    raise ValueError("Não pode comer sem os dois garfos.")
                liberar(left, p)
                liberar(right, p)
                refeicoes[p] += 1
                estado[p] = "pensando"
                print(f"Filósofo {p} terminou de comer e liberou os garfos {right} e {left}.")
                return

def executar():
    for iniciar in range(1, LIMITE + 1):
        print(f"\n{iniciar}°Passada\n")
        for p in range(N):
            jantar(p)
        if estado.count("finalizado") == N:
            print("\nRefeições por filósofo:", refeicoes)
            return "concluido"

if __name__ == "__main__":
    executar()


            