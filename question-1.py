def find_max(numbers):
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


def find_position(numbers, target):
    count = 0
    for n in numbers:
        if n == target:
            break
        elif count == len(numbers) - 1:
            count = -1
            break
        else:
            count += 1
    return count


print(find_max([1, 2, 4, 5]))  # should print 5
print(find_max([5, 2, 7, 1, 6]))  # should print 7
print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
# should print 2 (the first one)
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))  # should print -1
