# Pathfinding Starter Code

User Stories:
* “The Random player should generate a randomly generated path which goes from the
start to the exit, but also hits the target at some point between.”
* “I want to see another statistic for each player on the scoreboard.”

Derived Requirements:
* The Random player shall have a randomly assigned path which begins with the start node,
ends with the exit node, and hits the target along the path. The path shall be a valid
traversal such that each sequential pair of nodes in the path are connected by an edge.
* Add a "location" stat for each player

a. random_path code:
    i. Should the player be able to return to the start?
        yes.
    ii. Should the player be able to visit the exit before hitting the target?
        yes.
    iii. Should the player be able to wander back and forth between nodes?
        yes
    iv. What strategies could help avoid infinite loops?
        you could implement a set of visited nodes into your function. however, i wanted to stay true to the randomness and let it be.