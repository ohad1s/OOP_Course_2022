# --------------------- lambda : -------------------------
x = lambda a: a + 10
y = lambda x: x + x
# why it's good ?
world_cup= [{"name":"Messi", "goals":10, "assists":7},
            {"name":"Ronaldo", "goals":8, "assists":2},
            {"name":"Neymar", "goals":12, "assists":1},
            {"name":"Mbape", "goals":5, "assists":5},
            {"name":"Kane", "goals":6, "assists":4}]

def sort_only_by_goals(player,reverse):
    return player["goals"]

# world_cup.sort() - will not work
# world_cup_sorted= sorted(world_cup,key=lambda player: (player["goals"],player["assists"]),reverse=True)
# print(world_cup_sorted)
# world_cup_sorted2= sorted(world_cup, key=lambda player:player["goals"]+player["assists"],reverse=True)
# world_cup_sorted3=sorted(world_cup,key=sort_only_by_goals,reverse=True)
# print(world_cup_sorted)
# print(world_cup_sorted2)
# print(world_cup_sorted3)
# # --------------------- kargs/kwargs : -------------------------
#
#
def build_a_word(*argv):
    new_word=""
    for arg in argv:
        new_word+=str(arg)[0]
    return new_word

# print(build_a_word())
# print(build_a_word("OMG","hahahaha","amen","double","sdf","fsdf","Fds"))
#
def build_a_word2(arg1, *argv):
    new_word=""
    for arg in argv:
        new_word+=str(arg)[0]
    return new_word+" "+arg1
#
# print(build_a_word2()) # will not work
# print(build_a_word2("Shirazi","OMG","hahahaha","amen","double"))
#
#
def print_them(**kwargs):
    for key, value in kwargs.items():
        print("key: ",key, "value: ",value)
    for value in kwargs.values():
        print(value)
#
#
print_them(Player='Messi', goals=10, assists=8, tup=(1,2,3))
print_them(**{"player":"name"})


def print_them2(arg1, **kwargs):
    for key, value in kwargs.items():
        print("key: ",key, "value: ",value)
        print(arg1)
#
#
# # print_them() will not work
# print_them2('Messi', goals=10, assists=8)
#
def bdika(a,b,c):
    return a+b+c

# print(bdika(a=1,b=2,c=3))



#
def sum(arg1, arg2, arg3):
    print(arg1+arg2+arg3)
#
args = (1,2,3)
sum(*args)
#
kwargs = {"arg1": 1, "arg2":7, "arg3": 2}
sum(**kwargs)
#
#
def the_best(*args, **kwargs):
    to_ret=""
    to_ret+=args[0]+args[1]+args[2]
    to_ret+=kwargs["g"]+kwargs["m"]
    print(to_ret)
#
#
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
the_best('Who ', 'is ', 'the ',g="GOAT? ", m="Messi")
