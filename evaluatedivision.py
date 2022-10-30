# -----------PROBLEM-----------

# You are given an array of variable pairs equations and an array of real numbers values, 
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
# Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] 
# represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

# Note: The input is always valid. You may assume that evaluating the queries will not result 
# in division by zero and that there is no contradiction.

# ----------SOLUTION------------

# High level idea is to DFS through equations, until we hit the final currency
#   -> keep track of current quotient by multiplying by values[i] (since (a/b) * (b/c) = (a/c))
#   -> we need a visited set to escape cycles in the graph

# Extra details:
#   -> we can use equations backwards, e.g. if we have equations[i] = [Ai, Bi] and Ai / Bi = values[i], then
#       we have, Bi / Ai = 1 / values[i]
#   -> if we ever encounter a variable not in our equations, the equation is invalid -> return -1

def calcEquationWithMemoization(currvar, currval, goal, equations, values, seen, variables):
    if currvar not in variables:
        return -1
    if currvar == goal:
        return currval
    if currvar in seen:
        return -1
    
    seen.add(currvar)
    val = -1
    for equation in range(len(equations)):
        if equations[equation][0] == currvar:
            val = max(val, calcEquationWithMemoization(equations[equation][1], currval * values[equation], goal, equations, values, seen, variables))
    return val
        
def calcEquation(equations, values, queries):
    variables = set()
    
    for equation in range(len(equations)):
        variables.add(equations[equation][0])
        variables.add(equations[equation][1])
        equations.append([equations[equation][1], equations[equation][0]])
        values.append(1 / values[equation])
    
    results = []
    for query in range(len(queries)):
        seen = set()
        results.append(calcEquationWithMemoization(queries[query][0], 1, queries[query][1], equations, values, seen, variables))
    return results

# Example 1:

# Input: 
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

print(calcEquation(equations, values, queries))

# Example 2:

# Input: 
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

print(calcEquation(equations, values, queries))

# Example 3:

# Input: 
equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
print(calcEquation(equations, values, queries))