import multiprocessing
result=[]
def cal_square(numbers,res):
    for i,n in enumerate(numbers):
        res[i]=n*n
    print(multiprocessing.current_process())
if __name__=='__main__':
    num=[1,2,3,7,8]
    res=multiprocessing.Array('i',5)
    p1=multiprocessing.Process(target=cal_square,args=(num,res))
    print(p1.name)
    p1.start()
    p1.join()
    print(multiprocessing.current_process())
    print(res[:])