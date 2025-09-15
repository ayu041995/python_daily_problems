# list1 = [1,2,3,4,5]

# # for i in list1:
# #     print(i**2)

# # list1[]

square = [i**2 for i in list1]
# square1 = square
# square1[-1] = 30

# print(square)
# print(square1)


# list1 = ['eat','tea','ten','ball']

# o/p : [['eat','tea'],['ten'],['ball']]

def annergam(list1):
    anargam_map = {}
    for i in list1:
        # print(type(i))
        sorted_val = ''.join(sorted(i))
        # print(sorted_val)
        if sorted_val not in anargam_map:
            anargam_map[sorted_val] = []
            
        
        anargam_map[sorted_val].append(i)

    # print(anargam_map)
    return list(anargam_map.values())




print(annergam(['eat','tea','ten','ball']))



