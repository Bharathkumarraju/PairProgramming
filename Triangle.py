#  File: Triangle.py
#  Description: Use algorithms to find the greatest path sum of a triangle
#  Student's Name: Matthew Frangos
#  Student's UT EID: msf955
#  Partner's Name: Braeden Conrad
#  Partner's UT EID: bsc875
#  Course Name: CS 313E
#  Unique Number: 51335
#  Date Created: 3/7/2018
#  Date Last Modified:
import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
  sum_list=[]
  sum_list=sum_exhaustive(grid, grid[0][0], 0, 0, sum_list)
  return max(sum_list)

def sum_exhaustive(grid, partial, row, position, sum_list):
  hi = len(grid)
  if (row+1 == hi):
    sum_list.append(partial)
  else:
    c = partial
    partial+=grid[row+1][position]
    c+=grid[row+1][position+1]
    sum_exhaustive (grid, partial, row+1, position, sum_list)
    sum_exhaustive (grid, c, row+1, position+1, sum_list)
  return sum_list

# returns the greatest path sum using greedy approach
def greedy (grid):
  return

def conquer (grid,row,index):
  if (row+1 == len(grid)):
      return grid[row][index]
  else:
      return grid[row][index] + max(conquer(grid,row+1,index),conquer(grid,row+1,index+1))

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return conquer(grid,0,0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  return

def main ():
  # read triangular grid from file
  in_file= open('triangle.txt', 'r')
   # read the number of rows
  line = in_file.readline()
  line = line.strip()
  num_rows = int(line)

  # create empty list of rows
  row_list = []

  # read the list of rows from file
  for i in range (num_rows):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for i in range (len(row)):
      row[i] = int (row[i])
    row_list.append (row)
  print(row_list)
  print()

  ti = time.time()
  # output greatest path from exhaustive search
  great_sum=exhaustive_search(row_list)
  print("The greatest path sum through exhaustive search is "+ str(great_sum) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search
  print('The time taken for exhaustive search is '+str(del_t)+'seconds.')
  print()
  ti = time.time()
  # output greatest path from greedy approach
  great_sum=greedy(row_list)
  print("The greatest path sum through greedy search is "+ str(great_sum) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach
  print('The time taken for greedy search is '+str(del_t)+'seconds.')
  print()
  ti = time.time()
  # output greates path from divide-and-conquer approach
  great_sum=rec_search(row_list)
  print("The greatest path sum through recursive search is "+ str(great_sum) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  print('The time taken for recursive search is '+str(del_t)+'seconds.')
  print()
  ti = time.time()
  # output greates path from dynamic programming
  great_sum=dynamic_prog(row_list)
  print("The greatest path sum through dynamic programming is "+ str(great_sum) + '.')
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  print('The time taken for dynamic programming is '+str(del_t)+'seconds.')
if __name__ == "__main__":
  main()
