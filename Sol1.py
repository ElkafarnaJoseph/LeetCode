nums = [2, 7, 11,15]
target = 9

def check_value( arr , target):
    for i in range(len(arr)):
        for j in range(i , len(arr)):
            if (arr[i] + arr[j]) == target:
                return i , j
            
print(check_value(nums , target))


def twoSum(self, nums, target): # We define a new function named 'twoSum' that takes two inputs: 'nums' (a list of numbers) and 'target' (a single number)
    num_map = {} # Here, we create an empty dictionary called 'num_map'. Think of it as a backpack where we can store and look up numbers quickly.
    for i in range(len(nums)): # This starts a loop that goes through each number in the 'nums' list, using 'i' as the index (like your position in the list)
        difference = target - nums[i] # We calculate 'difference' by subtracting the current number (nums[i]) from 'target'
        if nums[i] in num_map: # We check if the current number (nums[i]) is already in our 'num_map' dictionary
            return [num_map[nums[i]], i] # If it is, that means we found the pair! We return the indices of those two numbers as a list
        num_map[difference] = i # If not, we store the 'difference' as the key in 'num_map' and set its value to the current index 'i'
