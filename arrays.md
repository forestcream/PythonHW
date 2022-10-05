# Arrays

+ [Compress string](#compress-string)

+ [Merge two sorted arrays](#merge-two-sorted-arrays)

+ [Diagonal sum of matrix](#diagonal-sum-of-matrix)
## Compress string

```python

def compress(elems):
    result = []
    current_sum = 0
    if(len(elems))>0:
        result.append(elems[0])
        current_sum = 1
    for i in range(1, len(elems)):
        if elems[i] == elems[i-1]:
            current_sum +=1
        else:
            if current_sum>1:
                result.append(str(current_sum))
                current_sum = 1
            result.append(elems[i])
    if(current_sum>1):
        result.append(str(current_sum))
    return "".join(result)
        
chrs = ["a","b","b","c","c","c"]
chrs2 = ["a","b","c"]
chrs3 = ["c","c","c"]
print(compress(chrs3))

```


## Merge two sorted arrays

``` python

def merge(first, second):
    result = [0] * (len(first)+len(second))
    pA = 0
    pB = 0
    pC = 0
    
    while pA != len(first) and pB != len(second):
        if first[pA] < second[pB]:
            result[pC] =  first[pA]
            pC += 1
            pA += 1
        else:
            result[pC] = second[pB]
            pC += 1
            pB += 1
        while pA != len(first):
            result[pC] = first[pA]
            pC += 1
            pA += 1
        while pB != len(second):
            result[pC] = second[pB]
            pC += 1
            pB += 1
            
    return result
```


##Diagonal sum of matrix

```python

def diagonalSum(mat):
    sum = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if (i==j) or(i==len(mat)-j):
                sum = sum + mat[i][j]
    return sum
```



##SUm of squares

```python
    return sorted(i ** 2 for i in s)


s = [0, 1, 2, 3, 4, 5]
с = [-20, -15, -10, -5]

print(squares(s))
    return sum
```
