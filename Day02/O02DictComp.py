
players = {
    'sachin': [190, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 360],
    'sourav': [330, 385, 400, 153, 180],
    'sehwag': [380, 445, 420, 350, 368],
    'yuvraj': [160, 230, 380, 130, 175]
}

print(f"players :{players}")

print("-" *  40)

print(f"sachin :{players['sachin']}")

print("-" *  40)

print(f"sachin :{sum(players['sachin'])}")

runs = {k: sum(v) for k, v in players.items()}
print(f"runs :{runs}")

print("-" *  40)

scores = {k: (lambda scores : sum(scores) / len(scores))(v)
            for k, v in players.items()}
print(f"scores :{scores}")

print("-" *  40)
def avg_scores(score):
    return sum(score) / len(score)

scores = {k :avg_scores(v) for k, v in players.items()}
print(f"scores :{scores}")


players = {
    'sachin': [190, 350, 460, 401, 380],
    'rahul': [230, 410, 185, 275, 360],
    'sourav': [330, 385, 400, 153, 180],
    'sehwag': [380, 445, 420, 350, 368],
    'yuvraj': [160, 230, 380, 130, 175]
}

print("-" *  40)
scores = [score for score in players]
print(f"scores :{scores}")

print("-" *  40)
scores = [score for score in players.values()]
print(f'scores :{scores}')

print("-" *  40)
scores = [scr for score in players.values() for scr in score]
print(f"scores :{scores}")

print("-" *  40)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")

print("-" *  40)

scores = {name :[scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(f"scores :{scores}")
