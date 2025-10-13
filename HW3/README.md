# Homework 3 --- PROBLEM DESCRIPTIONS

# Problem 1 ---> Modify "AStarMaze" for A* and Greedy BFS
For this problem, and **Problem 2**, we are going to take one of the existing files from the course GitHub with a new maze similar to that of the images in the "Homework 3" assignment.
I decided to use the same exact shape, but have the start and goal positions be on opposite sides of the barrier, to get some new paths different than that of the homework images. The maze structure is shown below:

  <img width="654" height="654" alt="image" src="https://github.com/user-attachments/assets/40b987ff-470a-4931-9483-cadc8a6ed4ff" />

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

  <img width="655" height="652" alt="image" src="https://github.com/user-attachments/assets/a404f4a8-4325-4223-b3b3-d9ae62e5e34b" />

The path, as expected, goes all the way down instead of going into the outcrop, taking into account both g(n) and h(n). We get a completely different path when we look at Greedy BFS.

## Greedy BFS --- h(n) exlcusive
Greedy BFS only takes into account h(n) and not g(n). Like A* above, it utilizes the Manhatten Distance for h(n). With that being said, some changes to the **find_path** function needed to be made, since for A* it uses g(n). The biggest change is ensuring we don't visit cells that have already been used and thus, disregarded. This is so we don't have an extrememly long path going up and down the maze when necessary. After these lines of code, in the _if_ statement,

  <img width="804" height="170" alt="image" src="https://github.com/user-attachments/assets/3151ac8a-164c-4e4a-ab95-7542152486f9" />

we will add th3 following lines of code to implement the Greedy BFS algorithm:

  ```
    neighbor = self.cells[new_pos[0][new_pos[1]]

    if new_pos not in visited:
      neighbor.h = self.heuristic(new_pos)
      neighbor.f = neighbor.h
      neighbor.parent = current_cell
      open_set.put((neighbor.f, new_pos))
  ```

What this section of code does is it asigns a new position to neighbor (in my case, from the starting position, it will check the cell above it). If it is in the grid and/or not in a wall, it will check to see if the new cell, or the neighbor, has been visited. If it isn't, we get the heuristic from the cell, assign it to **_f_** for the neighbor, set the parent for the neighbor cell to be the current cell (this way we can create the path), and lastly we add the cell and the respective heuristic to the P.Q. Once every direction is checked, the P.Q will then spit out the next cell that had the lowest heuristic. This cycle will rinse and repeat until the goal state is met. To ensure we don't go to previously visited nodes, at the beginning of the **_while_** loop, we have this if statement.

**ADD VISITED NODE AND INCLUDE EVERY POSITION**
  ```
    if current_pos in visited:
      continue
    visited.add(current_pos)
  ```
This will ensure no previously visited node is visited more than once, to ensure a single long path. If the node has been visited, we skip the code in the **_while_** loop and go to the next one in the P.Q. Now, when we run this program, we get the path below:

  <img width="651" height="655" alt="image" src="https://github.com/user-attachments/assets/4cd43cc5-d5fc-4414-b90d-e653ec9bf8a4" />

When just using h(n), the path will move according to the lowest value of h(n), disregarding walls until a wall is met. We can see this at the top of the maze, where the path goes until it gets to the cell in the upper inside corner of the structure, where h(n) = 40. However, the path gets met with a wall, so it must follow the next smallest h(n) value, which is down at h(n) = 50. It continues down until it can't go down OR right, at which point it begins to move left. Then we see if syncs up to around where the **A*** algoirthm is and from there it's a similar path to the goal position.

# Problem 2 ---> Utilizing Euclidean Distance 
Now, this problem follows the same practice as **Problem 1**, but instead of using the Manhattan Distance for our heuristic we will use the Euclidean Distance. With using the Euclidean Distance, the values of h(n) for every cell will be different than those in the previous problem that used the Manhattan Distance, since they are two completely different functions. 

  - When multiplying the heuristic by 10, I would get long decimals. So for the Euclidean Distance heuristic, we won't multiply every value by 10. Just a heads up.

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

  <img width="650" height="655" alt="image" src="https://github.com/user-attachments/assets/0289402c-e776-43d7-a2bd-f10dbdd2941c" />

From viewing the image, we can see the effect that using the Euclidean Distance has compared to that of the Manhattan Distance in **Problem 1**. We can clearly see where the diagonal moves come into effect. Instead of going straight down, the A* algorithm takes a couple diagonal moves in to the right, then a couple diagonal moves to the left once at the middle of the structure. Once at the bottom, it goes until reaching the far bottom-right side, goes up two diagonals, and then goes straight up to the goal position. So we can clearly see that using a different heuristic results in a slightly different path to the goal position.

## Euclidean Distance w/ Greedy BFS

Now we will use the Euclidean Distance for the Greedy GFS. We will use the same code changes and use the code we used in **Problem 1** for **Greedy BFS**. When we run the program, we get the path below:

  <img width="655" height="646" alt="image" src="https://github.com/user-attachments/assets/98eb6233-b81f-430f-af4e-79653a76164e" />

Now, from an immediate look, it's obvious that this is the worst path out of the four we have seen. There are twice as many cells in the path and it looks to be much longer than any of the previous three. While it may _look_ wrong, it is still correct. When using the Euclidean Distance AND **Greedy BFS**, we have twice as many cells to look at. Thus, there are twice as many cells that can qualify to have the lowest heristic value, and thus, be the next cell in hte P.Q after each cell. I will illustrate the path that was taken to show what happened, because there is a lot:

  <img width="652" height="653" alt="image" src="https://github.com/user-attachments/assets/491bdc5d-aad1-4abd-b6bd-5016205c8a22" />

# Problem 3 ---> Different Weighted Versions of A*




