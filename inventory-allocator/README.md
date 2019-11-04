David Zhang (Qixiang)  
qixianz@uci.edu  
Nov 2, 2019  
Deliverr Coding Challenge

#### Problem
The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution).

#### General Approach
**Algorithm**: Greedy - fill the order by iterating through pre-sorted-by-cost warehouses
**Language**: Python 3.6

#### Approach Analysis
**Algorithm in pseudocode**:  
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE}
allocation = []
warehouse_index = 0
N = total number of warehouses
while order is not empty AND warehouse_index < N:
    fill order from warehouse[warehouse_index++]
return (order is empty) ? allocation : []
```
**Correctness**:  
Since the given warehouses are pre-sorted by shipping cost, the order can be filled by iterating through the warehouse list from the cheapest to the most expensive.  

**Input**: `Order`: dict(), `Inventories per warehouses`: list(dict(dict))  
**Output**: `Orders per warehouses`: list(dict(dict))  

###### Test Case Examples  
**Example 1**  
Input: ```{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]```  
Output: ```[{ owd: { apple: 1 } }]```   
Explanation: *Happy Case, exact inventory match!*  

**Example 2**  
Input: ```{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]```    
Output: ```[]```  
Explanation: *Not enough inventory -> no allocations!*  

**Example 3**   
Input: ```{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]```  
Output: ```[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]```  
Explanation: *Should split an item across warehouses if that is the only way to completely ship an item:*

**Other examples**  
(Test on 1000 randomly generated input pairs)


#### Data Consideration (edge cases)
1. Given order is empty or the warehouses are empty -> return an empty list (no allocation)
2. Given order can only be partially filled -> return an empty list (no allocation)

#### Other consideration
The fixed cost for allocation from each warehouses are not considered here.  

For example,

```
    - The order: {apple: 3}
    - Inventories: [
    {name: wh0, inventory: {apple: 1}},
    {name: wh1, inventory: {apple: 1}},
    {name: wh2, inventory: {apple: 1}},
    {name: wh3, inventory: {apple: 3}}]
```
If the total cost of allocating 3 apples from "wh3" is cheaper than the total cost of allocating 3 apples from "wh0", "wh1", "wh2", then the order should be filled from "wh3" only.
