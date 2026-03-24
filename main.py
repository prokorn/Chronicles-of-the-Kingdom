import pandas as pd
import random
class Kingdom:
    def __init__(self, name):
        self.name = name
        self.gold = 100
        self.population = 50
        self.food = 100
        self.turn = 1
        self.history = [] # list to save data

    def record_history(self): # save the history of turn
        data_snap = {
            "Turn": self.turn,
            "Gold": self.gold,
            "Population": self.population,
            "Food": self.food
        }
        self.history.append(data_snap)

    def next_turn(self): # Next turn atributes
        self.record_history()
        self.turn += 1
        self.gold += self.population * 0.5
        self.food -= self.population * 0.2

my_kingdom = Kingdom("Red")
while my_kingdom.food > 0 and my_kingdom.population > 0: # the game logic
    print(f"\n--- Turn {my_kingdom.turn} ---")

    print(f"Gold: {my_kingdom.gold} | Food: {my_kingdom.food} | population: {my_kingdom.population}")

    task = int(input("""1: to buy food (10 gold -> 20 food)
                    2: to let population rest (20 gold + 20 food -> 5 population)
                    3: do nothing 
                    Type your action number: """))
    if task == 1:
        if my_kingdom.gold >= 10:
            my_kingdom.gold -= 10
            my_kingdom.food += 20
            print("For 10 gold you got 20 food")
        else:
            print("Not enough gold")
            continue
    elif task == 2:
        if my_kingdom.food >= 20 and my_kingdom.gold >= 20:
            my_kingdom.gold -= 20
            my_kingdom.food -= 20
            my_kingdom.population += 5
            print("Kingdom grown for 5 population")
        else:
            print("Not enough resources")
            continue
    else:
        continue
    my_kingdom.next_turn()


df = pd.DataFrame(my_kingdom.history) # convert to pandas df
print(df.head())

df.to_csv("kingdom_stats.csv", index=False)
print("📊 Statistics saved at 'kingdom_stats.csv'")

import matplotlib.pyplot as plt

# graph creation
plt.figure(figsize=(10, 6)) # window size

# lines
plt.plot(df['Turn'], df['Gold'], label='Золото', color='gold', marker='o')
plt.plot(df['Turn'], df['Food'], label='Їжа', color='green', marker='s')
plt.plot(df['Turn'], df['Population'], label='Населення', color='blue', marker='^')

# view
plt.title(f"Histrory of kingdom {my_kingdom.name}")
plt.xlabel("Turn")
plt.ylabel("Amount")
plt.legend() # name of lines
plt.grid(True) # add grid

# Вshow the graph
plt.show()









