luckyNum = [2, 7, 11, 31, 37]
friends = ["Lee", "KK", "Nec", "Azu", "Anubis"]
friends.append("Xi")            # adding item to the list
print(friends)

friends.insert(2, "Zhou")
print(friends)

friends.pop()           # remove the last item of the list
print(friends)

print(friends.index("KK"))

friends.sort()
print(friends)

friends.reverse()
print(friends)

luckyNum.reverse()          # large to small
print(luckyNum)

luckyNum.sort()         # small to large (or alphabetical order)
print(luckyNum)

friendsCpy = friends.copy()
print(friendsCpy)