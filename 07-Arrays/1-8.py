computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_games.sort()
ile = len(computer_games)
for i in range(ile):
    print(f'{i+1}- {computer_games[i]}')