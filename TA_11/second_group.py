def q1(lst1,lst2):
    new_lst=[]
    for element in lst1:
        if element in lst2:
            new_lst.append(element)
    return new_lst

def char_counter(my_str):
    counter={}
    for char in my_str:
        if char in counter.keys():
            counter[char]+=1
        else:
            counter[char]=1
    return counter

# print(char_counter("aabbababacfggtr"))

def maximum_index(lst):
    maxi=lst[0]
    max_index=0
    for index, element in enumerate(lst): #=>tuple: (index,element)
        if element>maxi:
            maxi=element
            max_index=index
    return (max_index,maxi)

def maxumim_subarray(lst):
    maximum=0
    maximum_curr=0
    for num in lst:
        maximum_curr+=num
        if maximum_curr>maximum:
            maximum=maximum_curr
        elif maximum_curr<=0:
            maximum_curr=0
    return maximum


mylist1=[7,2,-9,5,7,-1]
print(maxumim_subarray(mylist1))

def is_valid(password:str):
    if len(password)<8:
        return False
    digit=False
    special=False
    lower=False
    upper=False
    special_chars="!@#$%^&*()"
    for char in password:
        if char==" ":
            return False
        if char.isdigit():
            digit=True
        if char.isupper():
            upper=True
        if char.islower():
            lower=True
        if char in special_chars:
            special=True
    return digit and lower and upper and special

class Line():

    def __init__(self,p1,p2):
        """
        Constructor
        :param p1: point 1
        :param p2: point 2
        """
        self.p1=p1
        self.p2=p2
        self.__hid="abc"

    def __a(self):
        return (self.p1[1]-self.p2[1])/(self.p1[0]-self.p2[0])

    def __b(self):
        b= self.__a()*self.p1[0]-self.p1[1]
        return -b

    def __repr__(self):
        """
        y=Ax+B
        """
        return f"y={self.__a()}x+{self.__b()}"

import threading
class Safe_Queue():

    def __init__(self):
        self.queue=[]
        self.lock=threading.Lock()

    def get(self):
        with self.lock:
            self.queue.pop(0)


    def insert(self,x):
        self.lock.acquire()
        self.queue.append(x)
        self.lock.release()

class Roy_Counter():

    def __init__(self):
        self.counter=0
        self.lock=threading.Lock()
        self.cond= threading.Condition()

    def increment(self):
        with self.lock:
            if self.counter==0:
                self.cond.notify()
            self.counter += 1

    def decrement(self):
        with self.lock:
            if self.counter==0:
                self.cond.wait()
                self.counter-=1


