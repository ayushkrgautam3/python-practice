# Print Function

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/python-print/tutorial) tab to know how to to solve.</sub>  
 
The included code stub will read an integer, $n$, from STDIN.

Without using any string methods, try to print the following:  

$123\cdots n$  

Note that "$\dots$" represents the consecutive values in between.

**Example**  
$n = 5$

Print the string $12345$.



**Input Format**

The first line contains an integer $n$.  

**Constraints**

 $1 \le n \le 150$

**Output Format**

Print the list of integers from $1$ through $n$ as a string, without spaces.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T07:07:32.690Z  

```py
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print (i,end='')
        

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-print/problem)