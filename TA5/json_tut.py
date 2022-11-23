import json
from Player import Player
with open("Team.json", "r") as f:
    players = json.load(f)
players_arr= players.get("players")
players_final_arr=[]
for p in players_arr:
    idd=p["identifier"]
    f=p["first_name"]
    l=p["last_name"]
    t=p["team"]
    pos=p["position"]
    im=p["image"]
    players_final_arr.append(Player(idd,f,l,t,pos,im))
for p in players_final_arr:
    print(p)

#
pp=Player(0,"ohad","shirazi","mhfc","striker","blabla")
player= {'identifier': 1003, 'first_name': 'Hector', 'last_name': 'Bellerin', 'team': 'Arsenal', 'position': 'Defender', 'image': 'hectorbellerin.jpg'}
player_json=json.dumps(pp)
print(player_json)