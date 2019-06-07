Python Clearcode intern summer 2019 task

This task is a classic example of the knapsack problem, thus to complete it, I decided to use dynamic programming instead of the brute force method. I considered using a genetic algorithm, but judging by the way the solutions are going to be judged, finding the optimal solution is the priority, as oposed to finding a good solution in a set amout of time (like with using GA).

The dynamic programing approach to this problem involves the creation of a table[n, c], where n is the number of memes(items) and c is the capacity of the usb stick(knapsack). For 0 ≤ i ≤ n and 0 ≤ j ≤ c, table[i,j] will contain the value of the most valuable items from the subset of the first i items that can fit into the knapsack with the capacity of j.

To decide whether an item is worth putting into the knapsack we use the following conditions:

if j < weights[i]:
  Table[i, j] = table[i-1, j] #Cannot fit the ith item
else:
  Table[i, j] = max(table[i-1, j], values[i] + table[i-1, j – values[i],]) #Dont use the ith item / Use the ith item
  
To make life easier, we create table[n+1, c+1] and fill the first row and column with zeros, since both the knapsack with size equal to 0 and a list of items containing no items will make the result 0.
