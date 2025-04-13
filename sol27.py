nums = [3,2,2,3]
val = 3


# def rmv_element(li , v):
#     result = []
#     for i in li :
#         if i != v :
#             result.append(i)
#     return result
# print(rmv_element(nums, val))



# def solution(list , value): 
#     return [i for i in list if i != value]
# print(solution(nums, val)) # we need the index

# Answer
def solution(list , value):
    index = 0
    for i in list :
        if list[i] != value :
            list[index] = list[i]
            index += 1
    return index
print(solution(nums, val))