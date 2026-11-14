# Print Function

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as $0$.

**Input Format**

The first line contains $N$, the number of lines in the XML document. <br>
The next $N$ lines follow containing the XML document.

**Output Format**

Output a single line, the integer value of the maximum level of nesting in the XML document.

**Sample Input**  
```xml
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```
    
**Sample Output**  
```xml  
1
```  

**Explanation**

Here, the root is a *feed* tag, which has depth of $0$. <br>
The tags *title, subtitle, link* and *updated* all have a depth of $1$. <br>

Thus, the maximum depth is $1$.

**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T07:07:36.432Z  

```py
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print (i,end='')
        

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem)