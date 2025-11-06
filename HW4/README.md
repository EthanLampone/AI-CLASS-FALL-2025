ETHAN LAMPONE

HOMEWORK 4

CSC 362 - AI

6 NOVEMBER 2025

# HOMEWORK 4 -- PROBLEM DESCRIPTIONS

## PROBLEM 1 --> NIMA + ALGORITHMS
For **Problem 1**, we will talk about **Nim** and using the **Minimax** algorithm and **Alpha-Beta Pruning**.

**1. Game Description:** The rules to play **Nim** are below:
  A.. Two players take turns removing objects from a pre-determined number of piles/bins.
  B. In these distinct bins, there are a select number of objects within each bin.
  C. Players take turns choosing any bin and any number of objects from said bin, but they _must_ take at least one object.
  D. The player who removes the very last object wins.
  E. **NOTE** You can only take as many objects as there are in a single bin. For example, lets say there are two bins as described in **Part B** with 2 objects in each bin (1 & 2), respectively. You can only take 'x' number of objects from one bin. You can't take one from bin 1 and another from bin 2. Also, for our example, you can take up to 2 objects from bin 1 and 2 from bin 2.

**2. Game Tree:** Now that we know the rules of **Nim**, we can create a simple game tree. We will create a tree for a simple case of Nim, in which there are two heaps, each containing two objects. The tree will show _all_ possible moves and each player's outcome. This game tree will look similar to the Tic-Tac-Toe example we were introduced to in class. While there are only two bins and less than five objects, this game tree will be very small. The picture of the tree is shown below:

  <img width="539" height="302" alt="image" src="https://github.com/user-attachments/assets/3a8b6156-3cca-466a-bbaa-a7cc569f791d" />

You can see the many different ways that player 1 (who would go first) can take to start the game. He could take one or two objects from bin 1, and the same amounts from the other bin. After any of those four moves, player 2 has more than twice as many options to make (depending of course on what move player 1 makes prior). 

**3. Minimax Algorithm** We now have our **Nim** game tree. We will now apply the **Minimax Algorithm** to our game tree. From the image above, we will cut the tree off at a depth of 2, since we are now dealing with a 2-ply game. Now comes applying the algorithm. I will be using a standard evaluation function:
  - (+1) --> Winning Position for the current player
  - (-1) --> Losing Position for the current player
Below is a picture of the game tree with both 2-ply and the **Minimax Algorithm**:

  <img width="538" height="308" alt="image" src="https://github.com/user-attachments/assets/087ca887-a009-47d6-8fdd-8b561b793955" />

From the image, we can see the values of each and every node of the game tree. Starting with depth 2, we go from left to right and see if this is either a winning/losing position for P1. If the number of objects is (0,0), then it will automatically be (-1), since this is stating P2 won. After we have the whole entire bottom layer assigned with their correct MV value, we then backtrack through the tree. From the bottom layer to the middle layer, we will be looking to see which value of all the child nodes is the **Min** of all the respective MV's. For the three left nodes connected to (1,2), the value that would go up is (-1). This would happen for the other three middle layer nodes. Then, when we do this for the root node, we will be looking for the **Max** value of the four MV values in the middle layer. This, from the picture, would be (-1). 

This value of (-1) essentially means that Player 1 is ultimately in a losing position given the 2-ply cut off and respective starting number of bins and objects (2,2).

**4. Alpha-Beta Pruning** Now we will apply Alpha-Beta Pruning to reduce the number of nodes that need to be evaluated. Of course, we set Alpha and Beta initially to -inf & inf, respectively. Then we will perform DFS starting from the root node. This will take us down to the node (0,2). It's MV value is (+1). We evaluate this value by bringing it up to the parent node to be evaluated. Since the middle layer is a **Min** layer, we will look to see if α >= β^ANC. α = (+1), which is what we just brought up for evaluation. And β^ANC = inf. Thus, the expression (+1) >= inf is clearly not true. This means we will continue with evaluating all of the child nodes below. We'll look at the last two nodes. The next value, (-1), is then brought up for evaluation. The model will look to see if this value is smaller than the current value (+1). Seeing as this is true, we replace (+1) with (-1). We see that the final value, (+1), is not smaller than (-1), so nothing happens. After we went through _all_ of the child nodes, we will push the new β = -1 up to α. Now, α = (-1). The next two middle layer nodes wont have anything happen to them. While β = -1 <= α^ANC = (-1) is true, its the last child node, so there isn't anything to prune. When we get to the last child node, however, we see that the first node results in β = -1 <= α^ANC = (-1). This is true, so we can prune the last two child nodes. We bring that value up to α and see that (-1) = (-1), so no changes need to be made. 

**Alpha-Beta Pruning** allows us to further see that Player 1 is in a more losing position than winning with the starting number of heaps and objects per heap. The pruning just showed us that more.
The image to the pruned game tree w/ **Minimax Algorithm** is below:

  <img width="837" height="390" alt="image" src="https://github.com/user-attachments/assets/9f6a7dcd-25ea-406a-bd86-cdf934aec0fc" />

We can see that the last two nodes got "prunned" off, since the MV value that was brought up as β was equal to the α^ANC. 

**5. Analysis** After completing steps 1-4, we can come up with some analysis for the _specific_ game of **Nim** we had for this problem. The game itself is very easy to play, and with a bunch of practice can easily be mastered to win no matter what a persons situation may be. For the example that I used, it was clear that the player going first would be unable to win no matter what. Seeing as the other player also plays every move optimally, there is a 0% chance Player 1 can't win _no matter what move they make in the beginning of the game_. If we changed the number of objects in the each heap, (3,3) for example, we could maybe find some ways for Player 1 to actually have a change of winning. The same goes for increasing the number of heaps (2,2,2). 
The **Minimax Algorithm** and **Alpha-Beta Pruning** showed us truly how Player 2 has a better chance, if playing optimally, can guarantee a win no matter what move Player 1 does first

## PROBLEM 2 --> OPTIMIZATION AND H() EVALUATION

For Problem 2, we will be looking at potential different ways to optimize the **Minimax** algorithm AND develop a heuristic function to estimate the MV's of the game states in **Nim** to see if there is any difference from the standard way we did it in Problem 1. 

**1. Optimization Techniques** Iterative Deepening can be used on larger game trees to try and find the best sequence of moves Player 1 can make since they always go first. For this problem, I will use a game tree that is big, but not _too_ big in the sense of 2-ply. We'll use (2,1,2). The 2-ply game tree for this particular game is below:

  <img width="581" height="235" alt="image" src="https://github.com/user-attachments/assets/06f33dec-adf1-4296-a9eb-c3cd285b94c9" />

Now, we can see that even for a 2-ply game tree, there are still _a lot_ more moves that can be made farther down the tree. But, for 2-ply, this will do. However, if we use iterative deepening (depth = 1, 2, ..., k), we can see that at certain depths there are key positions in which, again, Player 1 is at a losing 

**2. Heuristic Evaluation** The last part we will look at doing is creating a new evaluation function for the game states in yet another 2-ply game. For this we need to think about how the many states in a **Nim** game tree can be evaluated. My thinking was collecting all of the winning possible moves and subtracting them from the total number of losing moves a player could make (similar to Tic-Tac_Toe in the lecture). The 2-ply game tree with the new MV values using the _new_ evaluation values is below ((0,0) will result in -1 because that indicates Player 2 wins):

  <img width="523" height="235" alt="image" src="https://github.com/user-attachments/assets/c8e5e178-6a2d-4819-bd7b-4d1cdd81701d" />

From the original **Minimax Algorithm Game Tree**, we see that we get the same result for this specific game tree with the original # of heaps and objects per heap when we use a different evaluation function for the MV values. This can mean that this evaluation function can correctly predict if Player 1 has a positive or negative advantage over Player 2 similar to just a standard **Minimax Algorithm** of (+1) and (-1) in a 2-Ply game. 
