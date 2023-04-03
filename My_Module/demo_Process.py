import multiprocessing
def cal():
    for i in range(10):
        print(i**3)
def cal1(number):
    for i in range(11):
        print(i**4)
if __name__=='__main__':
    print(multiprocessing.cpu_count())
    p1=multiprocessing.Process(target=cal)
    print(p1.name)
    p2=multiprocessing.Process(target=cal1,args=(10,))
    print(p2.name)
    p1.start()
    print(p1.pid)
    p2.start()
    print(p2.pid)