# HOMEWORK 4 -- PROBLEM DESCRIPTIONS

## PROBLEM 1 --> NIMA + ALGORITHMS
For **Problem 1**, we will talk about **Nim** and using the **Minimax** algorithm and **Alpha-Beta Pruning**.

**1. Game Description:** The rules to play **Nim** are below:
  A.. Two players take turns removing objects from a pre-determined number of piles/bins.
  B. In these distinct bins, there are a select number of objects within each bin.
  C. Players take turns choosing any bin and any number of objects from said bin, but they _must_ take at least one object.
  D. The player who removes the very last object wins.
  E. **NOTE** You can only take as many objects as there are in a single bin. For example, lets say there are two bins as described in **Part B** with 2 objects in each bin (1 & 2), respectively. You can only take 'x' number of objects from one bin. You can't take one from bin 1 and another from bin 2. Also, for our example, you can take up to 2 objects from bin 1 and 2 from bin 2.

**2. Game Tree:** Now that we know the rules of **Nim**, we can create a simple game tree. We will create a tree for a simple case of Nim, in which there are two heaps with containing two and two objects, respectively. The tree will show _all_ possible moves and each player's outcome. This game tree will look similar to the Tic-Tac-Toe example we were introduced to in class. While there are only two bins and less than five objects, this game tree will be very small. The picture of the tree is shown below:

  <img width="539" height="302" alt="image" src="https://github.com/user-attachments/assets/3a8b6156-3cca-466a-bbaa-a7cc569f791d" />

You can see the many different ways that player 1 (who would go first) can begin the game. He could take one or two objects from bin 1, and the same amounts from the other bin. After any of those four moves, player 2 has more than twice as many options to make (depending of course on what move player 1 makes prior). 

**3. Minimax Algorithm** We now have our **Nim** game tree. We will now apply the **Minimax Algorithm** to our game tree. From the image above, we will cut the tree off at a depth of 2, since we are now dealing with a 2-ply game. Now comes applying the algorithm. I will be using a simple evaluation function:
  - 1 --> Winning Position for the current player
  - -1 --> Losing Position for the current player
Below is a picture of the game tree with both 2-ply and the **Minimax Algorithm**:

  <img width="538" height="308" alt="image" src="https://github.com/user-attachments/assets/087ca887-a009-47d6-8fdd-8b561b793955" />

From the image, we can see the values of each and every node of the game tree. Starting with depth 2, we go from left to right and see if this is either a winning/losing position for P1. If the number of objects is (0,0), then it will automatically be (-1), since this is stating P2 won. After we have the whole entire bottom layer assigned with their correct MV value, we then backtrack through the tree. From the bottom layer to the middle layer, we will be looking to see which value of all the child nodes is the **Min** of all the respective MV's. For the three left nodes connected to (1,2), the value that would go up is (-1). This would happen for the other three middle layer nodes. Then, when we do this for the root node, we will be looking for the **Max** value of the four MV values in the middle layer. This, from the picture, would be (-1). 
This value of (-1) essentially means that Player 1 is ultimately in a losing position given the 2-ply cut off.

**4. Alpha-Beta Pruning** Now we will apply Alpha-Beta Pruning to reduce the number of nodes that need to be evaluated. Of course, we set Alpha and Beta initially to -inf & inf, respectively. Then we will perform DFS starting from the root node. This will take us down to the node (0,2). It's MV value is (+1).

**5. Analysis** After completing steps 1-4, we can come up with some analysis for the game of **Nim**. 

Below is the 2-Ply Game Tree above with the Minimax Algorithm applied:




## PROBLEM 2 --> OPTIMIZATION AND H() EVALUATION

For Problem 2, we will be looking at potential different ways to optimize the **Minimax** algorithm AND develop a heuristic function to estimate the value of the game states in **Nim**. We will also 
