import threading
import time

T = 8
M = 200000

contador = 0
semaforo = threading.Semaphore(1)

# Versão 1 - Sem semáforo
def tarefa_sem_semaforo():
    global contador

    for i in range(M):
        temp = contador
        time.sleep(0)
        contador = temp + 1

# Versão 2 - Com semáforo
def tarefa_com_semaforo():
    global contador

    for i in range(M):
        semaforo.acquire()
        try:
            temp = contador
            time.sleep(0)
            contador = temp + 1
        finally:
            semaforo.release()

def experimento(nome, tarefa):
    global contador

    print(f"{nome}")

    for teste in range(1, 4):
        contador = 0
        threads = []
        inicio = time.perf_counter()

        for i in range(T):
            t = threading.Thread(target=tarefa)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        fim = time.perf_counter()

        esperado = T * M
        perdidos = esperado - contador

        print(f"Teste {teste} esperado: {esperado} obtido: {contador} perdidos: {perdidos} Tempo: {fim - inicio:.4f}s")

experimento("SEM semáforo", tarefa_sem_semaforo)
experimento("COM semáforo", tarefa_com_semaforo)