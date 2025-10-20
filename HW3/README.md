# Homework 3 --- PROBLEM DESCRIPTIONS

# Problem 1 ---> Modify "AStarMaze" for A* and Greedy BFS
For this problem, and **Problem 2**, we are going to take one of the existing files from the course GitHub with a new maze similar to that of the images in the "Homework 3" assignment.
I decided to use the same exact shape, but have the start and goal positions be on opposite sides of the barrier, to get some new paths different than that of the homework images. The maze structure is shown below:

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/40b987ff-470a-4931-9483-cadc8a6ed4ff" />

The starting position will be in the top-left corner and the goal position will be in the top right. We'll first start with A*.

## A* Algorithm --- g(n) & h(n)
The script I am editing already has **A*** implemented. The code changes below are just some adjustments I made to allow for easier understanding:

**EDIT h(n):**
  ```
  def heuristic(self):
    return 10 * (abs(pos[0] - self.goal_pos[0]) + abs(pos[1] - self.goal_pos[1]))
  ```
**EDIT g(n):**
  ```
    new_g = current_cell.g + 10
  ```

After making these changes, the A* algorithm is all good to run. The path generated using it is below:

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/a404f4a8-4325-4223-b3b3-d9ae62e5e34b" />

The path, as expected, goes all the way down instead of going into the outcrop, taking into account both g(n) and h(n). We get a completely different path when we look at Greedy BFS.

## Greedy BFS --- h(n) exlcusive
Greedy BFS only takes into account h(n) and not g(n). Like A* above, it utilizes the Manhatten Distance for h(n). With that being said, some changes to the **find_path** function needed to be made, since for A* it uses g(n). The biggest change is ensuring we don't visit cells that have already been used and thus, disregarded. This is so we don't have an extrememly long path going up and down the maze when necessary. After these lines of code, in the _if_ statement,

  <img width="804" height="170" alt="image" src="https://github.com/user-attachments/assets/3151ac8a-164c-4e4a-ab95-7542152486f9" />

we will add the following lines of code to implement the Greedy BFS algorithm:

  ```
    neighbor = self.cells[new_pos[0][new_pos[1]]

    if new_pos not in visited:
      neighbor.h = self.heuristic(new_pos)
      neighbor.f = neighbor.h
      neighbor.parent = current_cell
      open_set.put((neighbor.f, new_pos))
  ```

What this section of code does is it asigns a new position to neighbor (in my case, from the starting position, it will check the cell above it first). If the new cell is in the grid and/or not a wall, it will check to see if the new cell, or the neighbor, has been visited. If it isn't, we get the heuristic from the cell, assign it to **_f_** for the neighbor, set the parent for the neighbor cell to be the current cell (this way we can create the path), and lastly we add the cell and the respective heuristic to the P.Q. Once every direction is checked, the P.Q will then spit out the next cell, which will the cell that has the lowest heuristic. This cycle will rinse and repeat until the goal state is found. To ensure we don't go to previously visited nodes, at the beginning of the **_while_** loop, we have this if statement.

**ADD VISITED NODE AND INCLUDE EVERY POSITION**
  ```
    if current_pos in visited:
      continue
    visited.add(current_pos)
  ```
This will ensure no previously visited node is visited more than once, to ensure a single long path. If the node has been visited, we skip the code in the **_while_** loop and go to the next one in the P.Q. Now, when we run this program, we get the path below:

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/4cd43cc5-d5fc-4414-b90d-e653ec9bf8a4" />

When just using h(n), the path will move according to the lowest value of h(n), disregarding walls until a wall is met. We can see this at the top of the maze, where the path goes until it gets to the cell in the upper inside corner of the structure, where h(n) = 40. However, the path gets met with a wall, so it must follow the next smallest h(n) value, which is down at h(n) = 50. It continues down until it can't go down OR right, at which point it begins to move left. Then we see if syncs up to around where the **A*** algoirthm is and from there it's a similar path to the goal position.

# Problem 2 ---> Utilizing Euclidean Distance 
Now, this problem follows the same practice as **Problem 1**, but instead of using the Manhattan Distance for our heuristic we will use the Euclidean Distance. With using the Euclidean Distance, the values of h(n) for every cell will be different than those in the previous problem that used the Manhattan Distance, since they are two completely different functions. 

  - NOTE: When multiplying the heuristic by 10, I would get very long decimals for some cells. Therefore, for the Euclidean Distance heuristic, we won't multiply every value by 10.

## Euclidean Distance w/ A*
We'll first look at the A* program and see what the Euclidean distance does to the pathfinding as a result. The same maze structure used in **Problem 1** will also be used for this problem. With the change in heuristic, there will be some code changes too. The code changes are below: 

**CHANGE THE HEURISTIC FUNCTION**
  ```
  def heuristic(self,pos):
    return round(math.sqrt(math.pow(pos[0]-self.goal_pos[0],2) + math.pow(pos[1] - self.goal_pos[1],2)),3)
  ```
**ADD NEW DIRECTIONS (EUCLIDEAN USES DIAGONALS & HORIZONTALS)**
  ```
    #### ADD THE DIAGONAL DIRECTIONS TO BE USED W/ EUCLIDEAN DISTANCE (NE, SE, SW, NW)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1,1),(-1,-1)]:
      new_pos = (current_pos[0] + dx, current_pos[1] + dy)
  ```
After these changes have been made to the A* program, we can run and view the resulting path. The path we get is below: 

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/0289402c-e776-43d7-a2bd-f10dbdd2941c" />

From viewing the image, we can see the effect that using the Euclidean Distance has compared to that of the Manhattan Distance in **Problem 1**. We can clearly see where the diagonal moves come into effect. Instead of going straight down, the A* algorithm takes a couple diagonal moves in to the right, then a couple diagonal moves to the left once at the middle of the structure. Once at the bottom, it goes until reaching the far bottom-right side, goes up two diagonals, and then goes straight up to the goal position. So we can clearly see that using a different heuristic results in a slightly different path to the goal position.

## Euclidean Distance w/ Greedy BFS

Now we will use the Euclidean Distance for the Greedy GFS. We will use the same code changes and use the code we used in **Problem 1** for **Greedy BFS**. When we run the program, we get the path below:

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/98eb6233-b81f-430f-af4e-79653a76164e" />

Now, from an immediate look, it's obvious that this is the worst path out of the four we have seen. There are twice as many cells in the path and it looks to be much longer than any of the previous three. While it may _look_ wrong, it is still correct. When using the Euclidean Distance AND **Greedy BFS**, we have twice as many cells to look at. Thus, there are twice as many cells that can qualify to have the lowest heristic value, and thus, be the next cell in the P.Q after each cell. I will illustrate the path that was taken to show what happened, because there is a lot:

  <img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/491bdc5d-aad1-4abd-b6bd-5016205c8a22" />

So, from these two experiments, we can declare that A* was the best with this given structure. For other's though, one algorithm may prove better than another.

# Problem 3 ---> Different Weighted Versions of A*
For **Problem 3**, we are tasked with explaining how different weights values of α and β affect the weighted version of A* below:

  **f(n) = α * g(n) + β * h(n) , where α,β >= 0** 

The results for different values of α and β are below:

  α | β | Observed Behavior | 
  --------------------------
  1 | 0 | Strictly Dijkstra's algorithm.
  --------------------------
  0 | 1 | Strictly Greedy BFS algorithm.
  --------------------------
  1 | 1 | A* algorithm. Both α and β are even in cost, which means both will have an equal effect on each other.
  --------------------------
  2 | 1 | Both costs are > 0, but more of a Dijkstra's algorithm than an optimal A* algorithm.
  --------------------------
  1 | 2 | Both costs again are > 0, but with a higher β we have more of a Greedy BFS algorithm.
  --------------------------

## Part B. ---> 
Part B. wants us to look at how changing β for the heuristic value affects the algorithm. From running a couple values against a strict alpha value of α = 1, it's obvious that the path does not change if it were a strict Greedy BFS algorithm. The pictures of the path for values of β = 1, 2, and 3 are below, respectively.

  
  <img width="655" height="653" alt="image" src="https://github.com/user-attachments/assets/7f5602c5-c5ae-4081-994f-9ffba2a69dc7" />

  <img width="649" height="650" alt="image" src="https://github.com/user-attachments/assets/17a1028a-4aab-4847-a801-29174e64eee2" />

  <img width="656" height="646" alt="image" src="https://github.com/user-attachments/assets/cfa591fa-6b1e-4436-bb2b-f2479a992f8f" />


From testing these three different values of β, we can see that there is no change in the path from if we simply use the same values of α and β. The heuristic values are just going to be multipled by the scalar value of β. Thus, the path will stay the same of β = 1 and α = 0.

# Problem 4 (Extra Credit) --> Path w/ Minimum Effort #1631
I decided to take a stab at the extra credit for this homework assignment, and went with the first problem in which we needed to use Dijkstra’s Algorithm or A*. For this problem, we are tasked with finding the **minimum** effort from the top-left cell to the bottom-right cell. To do this we use something similar to that of Dijkstra's Algorithm in which we take the absolute value of each effort from one cell to another, get the maximum effort, and then find the minimum effort out of all of them. And since the problem is only looking for the minimun effort, we don't need to track the path at all. We instead will make a new matrix, of the same dimension, and use that to find the minimum effort from one cell to another and return that value once we get to the goal node.

The code begins with initializing everything we need:
  - import the P.Q.
  - get the rows and cols
  - get start and goal position
  - create effort matrix to track the minimum effort to get to each cell.
  - directions list
  - set the starting position to 0 (no effort needed)
  - set the only value in the P.Q to be the starting position (0,0) and the starting effort (0)
  - empty visited() set, to track cells that have already been visited (don't need to do this but I did)

Now, while the P.Q is not empty (which it doesn't to begin with), all values will be popped into respective values:

  - curr_effort = 0
  - curr_pos = (0,0)

We check two things after getting the next effort and position in the P.Q. We check if the position has already been visited and check to see if the current position is the goal position. If the cell has already been visited, we go to the next respective effort and position in the P.Q. If the goal positon has been reached, then we return the current effort we have, which will be the minimum effort to get from the starting position to the goal position.

Now the _for_ loop. For each direction in the _directions_ list, we will get a new position. For my code, and from starting at the position node, the first position we will look at is (1,0), which is a valid position within the _heights_ matrix. We will then get a new effort, which is the absolute maximum effort between the two cells. Once we have this _new_effort_, we will see if it is less than the effort in the _efforts_ matrix in that respective cell at the current position in the _heights_ matrix. If it is, we replace the effort in that cell with the _new_effort_ we just got. We then do this for the other 3 directions and every cell in the _heights_ matrix until

After going through every cell, we will return the current minimum effort, which will be the minimum effort for a certain path.

  ```
  class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        from queue import PriorityQueue
        
        rows, cols = len(heights), len(heights[0]) # NUMBER OF ROWS AND COLUMNS
        start_pos, goal_pos = (0,0), (rows-1, cols-1) # START POSITION
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # CAN GO NORTH, SOUTH, EAST, OR WEST.

        efforts = [[float('inf')] * cols for eff in range(rows)] # MAKE MATRIX, OF SAME DIMENSION, AND USE IT TO STORE EFFORTS (ALL INF TO BEGIN)
        efforts[0][0] = 0 # SINCE WE START IN THE TOP LEFT CELL, THERE IS NO EFFORT. MAKE IT 0.

        pq = PriorityQueue() # INITIALIZE THE PRIORITY QUEUE
        pq.put((0, start_pos[0], start_pos[1])) # ADD THE CURRENT VALUE OF EFFORT AND THE X,Y OF THE CURRENT CELL;
        visited = set()

        while not pq.empty(): # WHILE P.Q NOT EMPTY

            effort, pos_x, pos_y = pq.get() # GET THE VALUES
            curr_pos = (pos_x, pos_y) # CONDENSE THE COORDINATES

            if curr_pos in visited: # CHECK IF THE CURRENT POSITION HAS BEEN VISITED
                continue
            visited.add(curr_pos) # ADD POSITION TO VISITED

            if pos_x == goal_pos[0] and pos_y == goal_pos[1]: # CHECK IF CURRENT POSITION IS THE GOAL POSITION
                return effort
            
            for x, y in directions:
                new_x, new_y = pos_x + x , pos_y + y

                if 0 <= new_x < rows and 0 <= new_y < cols: # CHECK IF POSITION IS VALID (WE ARE IN A CELL)
                    new_effort = max(effort, abs(heights[new_x][new_y] - heights[pos_x][pos_y])) # GET NEW M

                    if new_effort < efforts[new_x][new_y]:
                        efforts[new_x][new_y] = new_effort
                        pq.put((new_effort, new_x, new_y))
  ```

Submission acceptance below:

  <img width="683" height="442" alt="image" src="https://github.com/user-attachments/assets/0c1c59c5-1cdd-4d16-a452-4068720650ad" />










  
