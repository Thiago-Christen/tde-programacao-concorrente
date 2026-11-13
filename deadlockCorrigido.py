import threading, time


# Regra global: sempre adquirir LOCK_A antes de LOCK_B,
# em TODAS as threads.
 
# Thread 1 e Thread 2:
#   adquirir(LOCK_A)
#     adquirir(LOCK_B)
#       // secao critica
#     liberar(LOCK_B)
#   liberar(LOCK_A)



LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def thread1():
    LOCK_A.acquire()
    print('thread 1 PEGOU A')

    try:
        time.sleep(0.05)
        print('thread 1 TENTANDO pegar B')
        LOCK_B.acquire()
        print('thread 1 PEGOU B')
        try:
            print('Thread 1 concluiu')
        finally:
            LOCK_B.release()
            print('thread 1 SOLTOU B')
    finally:
        LOCK_A.release()
        print('thread 1 SOLTOU A')


def thread2():
    LOCK_A.acquire()
    print('thread 2 PEGOU A')
    try:
        time.sleep(0.05)
        print('thread 2 TENTANDO pegar B')
        LOCK_B.acquire()
        print('thread 2 PEGOU B')
        try:
            print('Thread 2 concluiu')
        finally:
            LOCK_B.release()
            print('thread 2 SOLTOU B')
    finally:
        LOCK_A.release()
        print('thread 2 SOLTOU A')


t1 = threading.Thread(target=thread1, daemon=True)
t2 = threading.Thread(target=thread2, daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()