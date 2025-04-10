# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = 3 
# n = 3 Done

# nums1 = [1]
# nums2 = []
# m = 1 
# n = 0 done 

nums1 = [0]
nums2 = [1]
m = 0 
n = 1

def merge(list1, list2 , n , m):
     first_list = list1[:m]
     second_list = list2[:n]
     result = sorted(first_list + second_list)
     print(result)
merge(nums1 , nums2, n , m)

