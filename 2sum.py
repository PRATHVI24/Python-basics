''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''

def twosum(nums,target):
    prevmap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevmap:
            return(prevmap[diff],i)
        else:
            prevmap[n] = i
    return 

print(twosum([2,7,11,15],9))
