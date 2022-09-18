database = [
    {"name":"Trunks", "human":True, "Hero":True, "Movie":True , "Original":False, "Inventor":False, "Mexican":False, "Saiyan":True, "Assasin":False, "Hero-King":False, "Messiah":False, "Laguz":False},

    {"name": "Marth", "human": True, "Hero": True, "Movie": False, "original":False, "inventor":False,"Mexican": False, "Saiyan":False, "Assasin":False, "Hero-King":True, "Messiah":False, "Laguz":False},

    {"name": "Aleph", "human": True, "Hero": True, "Movie": False, "original": False, "inventor":True,"Mexican": True, "Saiyan":False, "Assasin":False, "Hero-King":False, "Messiah":True, "Laguz":False},

    {"name": "Ezio Auditore", "human": True, "Hero": True, "Movie": False, "original": False, "inventor": False,"Mexican": False, "Saiyan":False, "Assasin":True, "Hero-King":False, "Messiah":False, "Laguz":False},

    {"name": "Sonic The Hedgehog", "human": False, "Hero": True, "Movie": True, "original":False, "inventor": False,"Mexican": False, "Saiyan":False, "Assasin":False, "Hero-King":False, "Messiah":False, "Laguz":False},

    {"name": "Link", "human": True, "Hero": True, "Movie": False, "original": False, "inventor": False,"Mexican":False, "Saiyan":False, "Assasin":False, "Hero-King":False, "Messiah":False, "Laguz":False},

    {"name": "Tibarn", "human": False, "Hero": False, "Movie": False, "original": False, "inventor":False,"Mexican": False, "Saiyan":False, "Assasin":False, "Hero-King":False, "Messiah":False, "Laguz":True},
]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("Tu personaje es "+database[0]["name"])
        quit()


ans = input("Tu personaje es humano?(y,n)")
take_chance(ans, "human")


ans = input("Tu personaje es un héroe?(y,n)")
take_chance(ans, "Hero")

ans = input("Tu personaje aparece en una película?(y,n)")
take_chance(ans,"Movie")

ans = input("Tu personaje es original?(y,n)")
take_chance(ans,"original")

ans = input("Tu personaje es un inventor?(y,n)")
take_chance(ans,"inventor")

ans = input("Tu personaje es mexicano?(y,n)")
take_chance(ans,"Mexican")

ans = input("Tu personaje es un sayayin?(y,n)")
take_chance(ans,"Saiyan")

ans = input("Tu personaje es un Asesino?(y,n)")
take_chance(ans,"Assasin")

ans = input("Tu personaje es un Héroe-Rey?(y,n)")
take_chance(ans,"Hero-King")

ans = input("Tu personaje es un Mesías?(y,n)")
take_chance(ans,"Messiah")

ans = input("Tu personaje es un Laguz?(y,n)")
take_chance(ans,"Laguz")