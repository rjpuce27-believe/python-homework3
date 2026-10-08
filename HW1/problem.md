Homework Question: Baseball Raffle Tickets  
Your baseball team has a certain number of raffle tickets that need to be distributed as evenly as 
possible among the players to sell for a fundraiser. Some players volunteered to help organize the 
fundraiser, so if the tickets cannot be divided evenly, they will receive the extra tickets first.  
 
Create a function called distribute_tickets(total_tickets, players, volunteers): 
The inputs are: 
●  total_tickets: the total number of raffle tickets that need to be distributed 
●  players: a list of player names in batting order 
●  volunteers: a list of players who volunteered to help organize the fundraiser, in the order they 
volunteered 
 
Assume that total_tickets is a nonnegative integer, every player name in players is unique, and every 
name in volunteers also appears in players. 
 
The function should determine: 
1.  Divide the tickets up among all the players evenly 
2.  Use the remainder to determine how many extra tickets need to be assigned 
3.  Give the extra tickets to players in the volunteers list first, in order 
4.  If there are still extra tickets left after every volunteer has received one, distribute the remaining 
tickets to the other players in batting order, skipping anyone who has already received an extra 
ticket. 
5.  Each player can receive at most one extra ticket.  
6.  Return a dictionary that maps each player's name to the number of tickets they receive. 
7.  If players is empty, return an error message explaining that tickets cannot be distributed among 
zero players. 
 
Test your function using at least three examples: 
-  one where there is no remainder, 
-  one where the remainder is less than or equal to the number of volunteers 
-  one where the remainder is greater than the number of volunteers. 
 
This problem is meant to assess a student’s ability to combine several Python concepts rather 
than use them separately. It requires functions, lists, parameters, integer division, modular arithmetic, 
loops, conditionals, and dictionaries. Integer division (//) determines how many tickets each player 
receives, while modulo (%) determines how many tickets are left over.  
  The most challenging part is likely to be understanding what the remainder represents and then 
distributing those extra tickets according to a specific priority. The student has to move through the 
volunteer list first and then, if necessary, move through the batting order while making sure that no 
player receives an extra ticket twice. By solving the problem, the student practices breaking a larger 
problem into smaller steps and using several programming tools together to solve a real-world problem.  
 
Answer Key 
Example 1: More extra tickets than volunteers 
{'Alex': 11, 'Ben': 11, 'Chris': 11, 'Dylan': 11, 'Evan': 10, 'Frank': 10} 
Example 2: No extra tickets remaining 
{'Sam': 20, 'Tyler': 20, 'Will': 20} 
Example 3: Fewer extra tickets than volunteers 
{'Aiden': 11, 'Brady': 10, 'Connor': 11, 'Jack': 10, 'Luke': 10}