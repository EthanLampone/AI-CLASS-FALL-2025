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
                      pq.put((new_effort, new_x, new_y))_