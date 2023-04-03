import multiprocessing
result=[]
def cal_square(numbers,q):
    #global result
    for i in numbers:
        q.put(i*i)

def addition(num,q):
    for i in num:
        q.put(2*i)


       # result.append((i*i))
    #print("inside the process"+str(result))
if __name__=='__main__':
    num=[1,2,3,7,8]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(num,q))
    p2=multiprocessing.Process(target=addition,args=(num,q))
    print(p1.name)
    print(p2.name)
    p1.start()
    p2.start()
    p1.join()
    while q.empty() is False:
        print(q.get())
    #print("Print in main process"+str(result))