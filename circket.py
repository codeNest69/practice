#print("-----------CIRCKET SCORE BOARD-----------")

#individual_runs = {}

#while True:
 #   my_input = input("enter your name: and score: (out to quit) ")
  #  if my_input == "out":
   #     break
    #else:
     #    name , score = my_input.split() 
      #   score = int

#         if name in individual_runs:
 #           individual_runs[name] += score
  #       else:
   #         individual_runs [name] = score
#
#print("-----------SCORE BOARD-----------")
#for player, runs in individual_runs.items():
 #      print(f"{player}: {runs}")
print("-----------CRICKET SCORE BOARD-----------")

individual_runs = {}

while True:
    my_input = input("Enter your name and score (type 'out' to quit): ")
    if my_input == "out":
        break
    else:
        name, score = my_input.split()
        score = int(score)  

        if name in individual_runs:
            individual_runs[name] += score
        else:
            individual_runs[name] = score

print("-----------SCORE BOARD-----------")
for player, runs in individual_runs.items():
    print(f"{player}: {runs}")
print("--------TEAM SCORE BOARD---------")

team_runs = sum(individual_runs.values())
print(f"total runs: {team_runs}")

  


          
   
    