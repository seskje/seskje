from players import Forward, Midfield, Player
import numpy as np

total_money = 100
team = []

def check_total_price(lst: list) -> float:
    total_price = 0
    for obj in lst:
        total_price += obj.price
    return total_price

def add_player(keeg:Player)-> None:
    if keeg.price + check_total_price(team) < total_money:
        team.append(keeg)

    

lyng = Forward("lyng", 14.0, "forward",5.2,40)
muddern = Midfield("muddern", 9.0, "midfield", 6.1,50)
add_player(lyng)
add_player(muddern)

lyng.update_xp(7.0)

lyng.show_stats()
def find_highest_xp(lst: list) -> str:
    high_xp = 0
    highest = None
    for obj in lst:
        if high_xp < obj.xp:
            high_xp = obj.xp
            highest = obj
    return highest.name + " med expected points " + str(highest.xp)
print(find_highest_xp(team))




