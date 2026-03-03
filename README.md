
**Name:** Yuvika Shendge  
**UFID:** 61747967

**Instructions to run :**
From the root directory:

```
To run the example test:

python src/cacheEviction.py data/example.in

compare the result to `data/example.out`.
```

**Repository Structure:**
```
src/
    cacheEviction.py

data/
    example.in
    example.out
    example2.in
    file1.in
    file2.in
    file3.in

README 
```

**Assumptions:**

Input format is:

```
k m
r1 r2 r3 ... rm
```

All request IDs are integers.
 The program assumes valid input format.
 The program does not perform additional input validation beyond parsing.

## Written Component

### Q1
| Input File | k | m  | fifo | lru | optff |
|------------|---|----|------|-----|-------|
| file1      | 3 | 80 | 52   | 61  | 32    | |
| file2      | 4 | 63 | 51   | 51  | 29    | |
| file3      | 5 | 55 | 43   | 43  | 23    | | 


In all of the cases OPTFF had the fewest cache misses.
LRU and FIFO were close or tied on Files 2 and 3 , but on File1, LRU actually performed worse than FIFO.
FIFO does not consider usage patterns but for some access patterns this can outperform LRU.
While OPTFF performs best because it uses future knowledge when making eviction decisions.

### Q2

Yes there is a request sequence where OPTFF has fewer misses than LRU or FIFO.

For k = 3, the sequence below shows this:

```
1 2 3 4 1 2 5 1 2 3 4 5

Resulting in:
FIFO  : 9
LRU   : 10
OPTFF : 7
```

#### Explanation
The LRU makes its eviction decisions based
on the past useage. However, this sequence evicts 
the item with the next use furthest in the future.
LRU evicts page 3 when page 5 arrives, because 3 was least recently used,
but page 3 is needed again soon after.
OPTFF avoids this by looking ahead.
So in this case OPTFF would have fewer misses.

### Q3

Let OPTFF be Belady's Farthest-in-Future algorithm.  
Let A be any offline algorithm that knows the full request sequence.  

Assume that A differs from OPTFF at the first eviction decision.

At that step:
- OPTFF evicts the item whose next request occurs farthest in the future.
- A evicts a different item.

Let:
- x = an item evicted by OPTFF
- y= an item evicted by A

OPTFF chooses the item used farthest in the future, so 
the next request to y must be before the next request to x.

Therefore, algorithm A will have a miss on y before OPTFF can have a miss on x.

Then we can modify A so that it evicts x instead of y.
Which does not increase the number of misses.

By repetedly applying this exchange argument, A can be transformed into OPTFF without increasing the number of misses.

Therefore, OPTFF incurs no more misses than any other offline algorithm. **Therfore, OPTFF is optimal**.
