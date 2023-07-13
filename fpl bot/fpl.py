from players import Forward, Midfield, Player

team = []
def add_player(Player):
    team.append(Player)

lyng = Forward("lyng", 14.0, "forward",5.2,40)
muddern = Midfield("muddern", 9.0, "midfield", 6.1,50)
add_player(lyng)
add_player(muddern)

lyng.update_xp(7.0)

lyng.show_stats()
def find_highest_xp(lst) -> str:
    high_xp = 0
    highest = None
    for obj in lst:
        if high_xp < obj.xp:
            high_xp = obj.xp
            highest = obj
    return highest.name + " med expected points " + str(highest.xp)
print(find_highest_xp(team))
