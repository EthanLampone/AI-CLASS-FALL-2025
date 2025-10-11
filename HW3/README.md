# Homework 3 ---

## Problem 1 ---> Modify "AStarMaze" for A* and Greedy BFS
For this problem, we are going to take one of the existing files from the course GitHub with a new maze similar to that of the images in the "Homework 3" assignment.
I decided to use the same exact shape, but have the start and goal positions be on opposite sides of the barrier, as shown below:

  <img width="654" height="654" alt="image" src="https://github.com/user-attachments/assets/40b987ff-470a-4931-9483-cadc8a6ed4ff" />

The starting position will be in the top-left corner and the goal position will be in the top right. We'll first start with A*.

## A* Algorithm --- g(n) & h(n)
**EDIT h(n)**
  ```
  def heuristic(self):
    return 10 * (abs(pos[0] - self.goal_pos[0]) + abs(pos[1] - self.goal_pos[1]))
  ```
**EDIT g(n)**
  ```
    new_g = current_cell.g + 10
  ```
The change for g(n) and h(n) isn't necessary, but I did it to make that of the extra credit in the midterm review, and find it better for myself to view the different changes from cell to cell.
After making these changes, the A* algorithm is all good to run. The path generated using it is below:

  <img width="655" height="652" alt="image" src="https://github.com/user-attachments/assets/a404f4a8-4325-4223-b3b3-d9ae62e5e34b" />

The path, as expected, goes all the way down instead of going into the outcrop, taking into account both g(n) and h(n). We get a completely different path when we look at Greedy BFS.

## Greedy BFS --- h(n) exlcusive
Greedy BFS only takes into account h(n) and not g(n). Like A* above, it utilizes the Manhatten Distance for h(n). With that being said, some changes to the **find_path** function needed to be made, since for A* it uses g(n). The biggest change is ensuring we don't visit cells that have already been seen and thus, disregarded. This is so we don't have an extrememly long path going up and down the maze when necessary.

**ADD VISITED NODE AND INCLUDE EVERY POSITION**
  ```
    if current_pos in visited:
      continue
    visited.add(current_pos)
  ```
This will ensure no previously visited node is visited more than once, to ensure a single long path.

  <img width="651" height="655" alt="image" src="https://github.com/user-attachments/assets/4cd43cc5-d5fc-4414-b90d-e653ec9bf8a4" />

When just using h(n), the path will move according to the lowest value of h(n), disregarding walls until a wall is met. We can see this at the top of the maze, where the path goes until it gets to the hell in the upper inside corner, where h(n) = 40. However, the path gets met with a wall, so it must follow the next smallest h(n) value, which is down at h(n) = 50. It continues down 

# Problem 2 ---> Utilizing Euclidean Distance
This problem is basically using the same two programs from problem 1 and editing them to use the Euclidean Distance as the heuristic function and tweaking some of the code as a result. We'll first look at the A* program and see what the Euclidean distance does to the pathfinding as a result. The code changes are below: 

**CHANGE THE HEURISTIC FUNCTION**
  ```
  def heuristic(self,pos):
    return round(math.sqrt(math.pow(pos[0]-self.goal_pos[0],2) + math.pow(pos[1] - self.goal_pos[1],2)),3)
  ```
**ADD NEW DIRECTIONS**
  ```
    #### ADD THE DIAGONAL DIRECTIONS TO BE USED W/ EUCLIDEAN DISTANCE (NE, SE, SW, NW)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1,1),(-1,-1)]:
      new_pos = (current_pos[0] + dx, current_pos[1] + dy)
  ```

