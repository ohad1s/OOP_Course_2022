def first_q1(lst1, lst2):
    to_return=[]
    for element in lst1:
        if element in lst2:
            to_return.append(element)
    return to_return


lst1= [1,2,3,4,5,6,7,8,9]
lst2=[2,4,6,8,0]
print(first_q1(lst1,lst2))

def maximum_tup(lst):
    index_max=0
    max=lst[0]
    for index, number in enumerate(lst):
        print(index, number)
        pass

def maximum_tup2(lst):
    max_num=max(lst)
    max_index= lst.index(max_num)
    return (max_index, max_num)


lst3=[1,2,4,6,8,3,77,99,44]
print(maximum_tup2(lst3))


def max_range(lst):
    new_lst=[]
    max_sum=lst[0]
    for i in range(len(lst)):
        new_lst.append(0)
    for i in range(len(lst)):
        for j in range(i+1):
            new_lst[i]+=lst[j]
    for i in range(len(lst)):
        if new_lst[i]>max_sum:
            max_sum=new_lst[i]
    for i in range(len(lst)):
        for j in range(i):
            if new_lst[i]-new_lst[j] > max_sum:
                max_sum= new_lst[i]-new_lst[j]
    return max_sum

my_list4=[1, 2, 3, -1, 8, 9, 10, -10, 4]
my_list5=[-1, -2, -3, -4, -5]
my_list6=[1, 2, 3, 4, 5]

print(max_range(my_list4))
print(max_range(my_list5))
print(max_range(my_list6))

class Line():

    def __init__(self, point1, point2):
        self.point1=point1
        self.point2= point2
        self.__hidden= "abc"


    def __a(self):
        return (self.point1[1]-self.point2[1])/(self.point1[0]-self.point2[0])

    def __b(self):
        b=self.__a()*self.point1[0]-self.point1[1]
        return -b

    def __repr__(self):
        """
            y=ax+b
        """
        return f"Y={self.__a()}X+{self.__b()}"

line1=Line((5,3),(7,2))
print(line1)
print(line1.point1)
# print(line1.hidden)
# print(line1.__a())

import threading
class my_counter():

    def __init__(self):
        self.counter=0
        self.cond= threading.Condition()

    def increment(self):
        with self.cond:
            if self.counter==0:
                self.cond.notify()
            self.counter+=1

    def decrement(self):
        with self.cond:
            if self.counter==0:
                self.cond.wait()
            self.counter-=1

class my_queue():

    def __init__(self):
        self.queue=[]
        self.lock=threading.Lock()


    def get(self):
        self.lock.acquire()
        self.queue.pop(0)
        self.lock.release()


    def insert(self, e):
        with self.lock:
            self.queue.insert(e)

