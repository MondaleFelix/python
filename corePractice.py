from random import randint

def dice_roll(roll):
    if (type(roll) != str):
        return

    total = 0

    components = roll.split("d")
    num_rolls = int(components[0])
    num_sides = int(components[1])

    for die_roll in range(0, num_rolls):
        toss = randint(1, num_sides)
        total += toss

    return total

if __name__ == '__main__':
    from sys import argv

    roll = argv[1]
    print(dice_roll(roll))







# def twoSum(numbers, target):
#     results = []
#     filtered = []
#     for number in numbers:
#         if number <= target:
#             filtered.append(number)
#     for i in filtered:
#         for filtered[i+1] in filtered-1:
#             first = filtered[i]
#             second = filtered[i+1]
#             sum = first + second
#             if sum == target:
#                 results += [first, second]
#     return results


#     print(filtered)


# twoSum([1,3,4,5] , 4)
