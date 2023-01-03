def intersect(lst1, lst2):
    new_lst=[]
    for i in lst1:
        if i in lst2:
            new_lst.append(i)
    return new_lst

def intersect2(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1 & set2)

def difference(lst1, lst2):
    new_lst=[]
    for i in lst1:
        if i not in lst2:
            new_lst.append(i)
    return new_lst

def difference2(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1 - set2)

lst1=[1,2,3,4,5,6,7,8,9,0]
lst2=[2,4,6,8,0,12,14,16]

print(intersect(lst1,lst2))
print(intersect2(lst1,lst2))
print(difference(lst1,lst2))
print(difference2(lst1,lst2))

def char_counter(my_str):
    counter={}
    for char in my_str:
        if char in counter.keys():
            counter[char]+=1
        else:
            counter[char]=1
    return counter

print(char_counter("abcddcaafta"))

def maxi(lst):
    import sys
    max = -sys.maxsize - 1
    max_index=-1
    for index, number in enumerate(lst):
        if number>max:
            max=number
            max_index=index
    return (max_index, max)

lst=[7,77,88,99,44,55,66,8888,777,222,333,444,5555]
print(maxi(lst))

def max_consecutive_sum(lst):
    max_sum = 0
    current_sum = 0
    for num in lst:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

my_list1=[1, 2, 3, -1, 8, 9, 10, -10, 4]
my_list2=[-1, -2, -3, -4, -5]
my_list3=[1, 2, 3, 4, 5]
print(max_consecutive_sum(my_list1))
print(max_consecutive_sum(my_list2))
print(max_consecutive_sum(my_list3))

def strong_letter(my_str):
    my_s_dict={}
    abc="abcdefghijklmnopqrstuvwxyz"
    for letter in my_str:
        if letter in my_s_dict.keys():
            my_s_dict[letter]+=1
        else:
            my_s_dict[letter]=1
    for i in reversed(range(26)):
        if my_s_dict.get(abc[i].upper(),0)>0 and my_s_dict.get(abc[i].lower(),0)>0:
            return abc[i].upper()
    return "NO"

string1="abcdeEfg"
string2="asdfGHJKLqwerZXCvBnM"
string3="AaZuUrtp"

print(strong_letter(string1))
print(strong_letter(string2))
print(strong_letter(string3))

def strong_password(password):
    if len(password)<8:
        return False
    digit=False
    special=False
    upper=False
    lower=False
    abc="abcdefghijklmnopqrstuvwxyz"
    chars="!@#$%^&*()"
    for char in password:
        if char==" ":
            return False
        if char.isdigit():
            digit=True
        if char in abc:
            lower=True
        if char in abc.upper():
            upper=True
        if char in chars:
            special=True
    return digit and lower and upper and special

password1="ohAd2023!"
password2="@@P pr0gramming"
password3="Rt1@asd"

print(strong_password(password3))
print(strong_password(password2))
print(strong_password(password1))