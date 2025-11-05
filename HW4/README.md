# HOMEWORK 4 -- PROBLEM DESCRIPTIONS

## PROBLEM 1 --> NIMA + ALGORITHMS
For **Problem 1**, we will talk about **Nim** and using the **Minimax** algorithm and **Alpha-Beta Pruning**.

**A. Game Description:** The rules to play **Nim** are below:
  1. Two players take turns removing objects from a pre-determined number of piles/bins.
  2. In these distinct bins, there are a select number of objects within each bin.
  3. Players take turns choosing any bin and any number of objects from said bin, but they _must_ take at least one object.
  4. The player who removes the very last object wins.
  5. **NOTE** You can only take as many objects as there are in a single bin. For example, lets say there are two bins as described in **Part B** with 2 objects in each bin (1 & 2), respectively. You can only take 'x' number of objects from one bin. You can't take one from bin 1 and another from bin 2. Also, for our example, you can take up to 2 objects from bin 1 and 2 from bin 2.

**B. Game Tree:** Now that we know the rules of **Nim**, we can create a simple game tree. We will create a tree for a simple case of Nim, in which there are two heaps with containing two and two objects, respectively. The tree will show _all_ possible moves and each player's outcome. This game tree will look similar to the Tic-Tac-Toe example we were introduced to in class. While there are only two bins and less than five objects, this game tree will be very small. The picture of the tree is shown below:

  <img width="539" height="302" alt="image" src="https://github.com/user-attachments/assets/3a8b6156-3cca-466a-bbaa-a7cc569f791d" />

You can see the many different ways that player 1 (who would go first) can begin the game. He could take one or two objects from bin 1, and the same amounts from the other bin. After any of those four moves, player 2 has more than twice as many options to make (depending of course on what move player 1 makes prior). 

**C. Minimax Algorithm** We now have our **Nim** game tree. We will now apply the **Minimax Algorithm** to our game tree. From the image above, we will cut the tree off at a depth of 2, since we are now dealing with a 2-ply game. Now comes applying the algorithm. I will be using a simple evaluation function:
  - 1 --> Winning Position for the current player
  - -1 --> Losing Position for the current player
  - 0 --> Current Player wins.

Below is the 2-Ply Game Tree above with the Minimax Algorithm applied:




## PROBLEM 2 --> OPTIMIZATION AND H() EVALUATION

For Problem 2, we will be looking at potential different ways to optimize the **Minimax** algorithm AND develop a heuristic function to estimate the value of the game states in **Nim**. We will also 
