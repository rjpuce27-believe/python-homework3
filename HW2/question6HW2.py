# Bowling Night Challenge
"""
You and your friends go out one night to bowl three games.
Write a Pyhton script that evaluates how successful your bowling night
was based on your three scores. 
""" 
## Function
def bowling_night(game_1, game_2, game_3, goal_score):

# Validate scores

    if game_1 < 0 or game_1 > 300:
        print('Invalid Score')
        return
    if game_2 < 0 or game_2 > 300:
        print('Invalid Score')
        return
    if game_3 < 0 or game_3 > 300:
            print('Invalid Score')
            return
    if goal_score < 0 or goal_score > 300:
            print('Invalid Score')
            return

# Calculate average and total score

    total_score = game_1 + game_2 + game_3
    average_score = total_score / 3

# Compare the games scores with your goal score for the night

    games_at_goal_score = 0

    if game_1 >= goal_score:
          games_at_goal_score = games_at_goal_score + 1

    if game_2 >= goal_score:
              games_at_goal_score = games_at_goal_score + 1

    if game_3 >= goal_score:
              games_at_goal_score = games_at_goal_score + 1

# Check if you improved and the overall performance

    if game_3 > game_1:
           print("Your score improved over the night.")
    elif game_3 == game_1:
           print("Your score stayed the same over the night ")
    else:
        print("Your score decreased over the night.")

    if games_at_goal_score == 3:
           print("Amazing night bowling!")
    if games_at_goal_score == 1 or games_at_goal_score == 2:
           print("Solid bowling night!")
    else:
        print("Keep working:)")

    print("Total Score:", total_score)
    print("Average Score:", average_score)
    print("Games at or above your goal:", games_at_goal_score)

if __name__ == "__main__":
    goal_score = int(input("What is your goal score? "))
    game_1 = int(input("What did you score in game 1? "))
    game_2 = int(input("What did you score in game 2? "))
    game_3 = int(input("What did you score in game 3? "))

    bowling_night(game_1, game_2, game_3, goal_score)