from re import L


def get_index(num):
    nums2=num[:]
    num.sort()
    for i in range(len(nums2)):
        if nums2[i]!=num[i]:
            return i

num = [1,2,4,3]
print(get_index(num))