def penalty(arr):
    numbers_list = []
    for i in range(len(arr)):
        numbers_list.append(min(arr))
        arr.remove(min(arr))
    penalty = "".join(numbers_list)
    print(penalty)

penalty(['45', '30', '50', '1'])
# Should return "1304550"

penalty(['100', '10', '1'])
# Should return "100101"
