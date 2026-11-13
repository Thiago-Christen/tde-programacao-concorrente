import threading, time


# LOCK_A, LOCK_B = locks distintos
 
# Thread 1:
#   adquirir(LOCK_A)
#     dormir(50ms)              // aumenta a chance do deadlock
#     adquirir(LOCK_B)
#       imprimir "T1 concluiu"
#     liberar(LOCK_B)
#   liberar(LOCK_A)
 
# Thread 2:
#   adquirir(LOCK_B)
#     dormir(50ms)
#     adquirir(LOCK_A)
#       imprimir "T2 concluiu"
#     liberar(LOCK_A)
#   liberar(LOCK_B)


LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def thread1():
    LOCK_A.acquire()
    print('thread 1 PEGOU A')
    try:
        time.sleep(0.05)
        print('thread 1 TENTANDO pegar B')
        LOCK_B.acquire()
        try:
            print('Thread 1 concluiu')
        finally:
            LOCK_B.release()
            print('thread 1 SOLTOU B')
    finally:
        LOCK_A.release()
        print('thread 1 SOLTOU A')


def thread2():
    LOCK_B.acquire()
    print('thread 2 PEGOU B')
    try:
        time.sleep(0.05)
        print('thread 2 TENTANDO pegar A')
        LOCK_A.acquire()
        print('thread 2 PEGOU A')
        try:
            print('Thread 2 concluiu')
        finally:
            LOCK_A.release()
            print('thread 2 SOLTOU A')
    finally:
        LOCK_B.release()
        print('thread 2 SOLTOU B')


t1 = threading.Thread(target=thread1, daemon=True)
t2 = threading.Thread(target=thread2, daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()