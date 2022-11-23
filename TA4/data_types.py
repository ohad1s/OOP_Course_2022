# # --------------- list : ----------------------------
mylist= [1, 3 ,5 ,7 ,9 ,11]
# print(mylist)
# mylist.append([2,0])
# print(mylist)
# mylist[0]=2
# print(mylist)
# mylist.insert(2,8)
# print(mylist)
# mylist.extend([99,999,9999])
# print(mylist)
# # mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.index(99)
# print(mylist)
# mylist.remove(9999)
# print(mylist)
# mylist2=["A","b", "c", "d","e"]
# mylist3= mylist+mylist2
# print(mylist3)
# mylist2.clear()
# print(mylist2)
# # --------------- Tuple : ----------------------------
mytup=(7,6,5,3,1,1,1,1,1)
# print(mytup)
# print(mytup[2])
# print(mytup.index(6))
# print(mytup.count(1))
# # mytup[0]=44
# print(len(mytup))
for num in mytup:
    print(num, end=" ")
    # print()
# print()
print(mytup[0:6:2])
tuptup= (10,20,30)
a, b, c = tuptup
# print(a, b ,c)
# print(mytup+tuptup)
# print(tuptup*3)
bdika= list(tuptup)
print(bdika)
# # --------------- Dictionary : ----------------------------
studentA={"name":"ploni", "last":"almoni", "age": 25}
numbers= {0:7, 2:8, 9:2}
letters={"a":7, "b":0,"c":12}
bools={"ohad":True, "dan":False, "yossi":True}
dict_list={"ohad":[1,2,3], "Dan":[4,5,6], "Yossi": (1,2,3)}
dict_free= {True:"ohad", 5:[1,2], "ohad":"opop"}
our_dict={"moshe":777,"amit":666, True:12}
print(studentA["name"])
print(letters["c"])
print(dict_list.keys())
print(dict_list.values())
z= dict_list.popitem()
print(z)
print(dict_list)
print(dict_list.get("ohad"))

dict_list["avg"]=85
dict_list["avg"]=77
dict_list["avg"]+=1
#
print(bools.items())
for x, y in studentA.items():
    print("key is:" ,x, " value is: ", y)
for index, value in enumerate(mylist):
    print(index, "-",value)
mydictbdika={"ohad":8, "ohad":9}
print(mydictbdika)
# print()
# # # -----------------set: ---------------
multi_nums=[1,1,1,2,2,2,3,4,4,3,4,5,5,4,32,11,11]
myset = set(multi_nums)
print(myset)
myset2={1,2,3,41,6,6,6,6,6,66,6,6}
print(myset2)
print(set((7,7,7,7,7,7,7)))
# x=[1,2,3]
# x=(1,2,3)
# x= 7