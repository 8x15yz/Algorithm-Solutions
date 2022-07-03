# Binary Search
I solved using **binary search** with **recursion**
## the concept about binary search is .. 
We are gived target value and list. and we have to find the index that the value would be located. list is sorted list and it is odd or even also.<br>
to searching, we have to get the index which is the middle one about the list. let's call this "middle index". there is way to carculate middle index, it's same for both list odd and even. <br>following code is used to get middle index.<br>
```
middle_index = ((end-start)//2) + start

# The initial setting about start value and end value is:
# start = 0
# end = len(list)-1
```
with using this index, we can compare with target value. and maybe it will occer two situations:<br>
1. target value > middle one
<br>or
2. target value < middle one<br>
<br>
if target value is bigger than middle one, the range will be reset to "middle ~ end"<br> 
and if target value is smaller than middle one, the range will be reset to "start ~ middle"<br><br>
that is the end of binary search !! now we just need to repeat these process.<br>
<br>
okey, now I'm ready to solve this part. <br>
<br>
<br>

## solving problems
[35. Search Insert Position](./35)<br>
