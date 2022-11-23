# -------------- string format-------------------
age = 25
name = "ohad"
# name+str(age)
print("my name is {} and im {} years old".format(name, age))
print("im {:.2f} years old".format(age))
# -------------------------------------------
print(f"name:{name} age:{age}")
# --------------- exceptions ---------------
x = 5
y = 0
try:
    print(x / y)
except(ZeroDivisionError):
    print(" no no no ")
finally:
    print("Ciiii")
# -----------------------
x = input("enter your age")
if x.isdigit():
    print("your age is {}".format(age))
else:
    raise Exception("WTF?!")
# ----------------------------
import traceback

a = 5
b = 0
try:
    print(a / b)
except:
    traceback.print_exc()
finally:
    print("Ciiii")
