from human_being import human_being
class Person(human_being):
    def __init__(self, age:int=0, name: str=" ", id: str=" ") :
        self.id = id
        self.name = name
        self.age = age
        self.nickname="perrrrsonnn"
        self.__hid="hahahaha catch meeee"

    # def __str__(self) -> str:
    #     return f"name:{self.name} id:{self.id} age:{self.age}"

    def __repr__(self) -> str:
        return f"name:{self.name} id:{self.id} age:{self.age} "

    def __gt__(self, other) -> bool:
        return self.age > other.age
    #
    def __eq__(self, o: object) -> bool:
        return self.id==o.id

    def __add__(self, other):
        return self.age+other.age

    def print_hello(self,msg):
        print(msg)

    def get_gender(self) -> None:
        print("male")
    #
    def hug_sound(self) ->str:
        print("oh oh oh")

    def __hide_func(self):
        print("hahahahah you cant see me")

    def __calcAgePlusFive(self):
        return self.age+5

    def RetPlusFive(self):
        self.__calcAgePlusFive()

    def get_hid(self):
        return self.__hid

    def set_hid(self,new_hid):
        self.__hid=new_hid


if __name__ == "__main__":
    p1=Person(51,"yossi","123456789")
    print(p1)
    p2=Person(name="ohad",id="123456789")
    print(p2)
    p2.name="dani"
    print(p2)
    p3=Person()
    print(p3)
    # # p3=Person("sdfsdf","123456789")
    # # print(p3)
    # p3=Person(16,"Eli","1234567542")
    person_list=[p1,p2,p3]
    print(person_list)
    person_list.sort()
    print(person_list)
    print(p1<p2)
    print(p1+p2)
    # person_tup=(p1,p2)
    # print(person_tup)
    # person_list.sort()
    # print(person_list)
    # print(p1+p2)




