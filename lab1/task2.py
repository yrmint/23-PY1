list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players1, players2 = list_players[0:int(len(list_players) / 2)], \
    list_players[int(len(list_players) / 2):len(list_players) + 1]
print(players1)
print(players2)
