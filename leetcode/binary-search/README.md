# 35. Search Insert Position
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

## explain my solution 
my solution is [here](./leetcode-35.py), and you can see my code together as you reading this page.<br>
<br>

### line 3 ~ 4
I make the function for recursion, its input value is:
```
nums (input list)
terget (input value)
fs (start index)
ed (end index)
```
the next line, I writed the code that can calculate middle index.
and we jump to line 14 ...
### line 14 ~ 17

there are two situations we have, 
