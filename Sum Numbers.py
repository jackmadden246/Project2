def find_max_sum(numbers):
    """function looks through list for largest and second-largest numbers, then adds them.
     If number is largest, number gets assigned to 'largest' variable.
     If not, and is second-largest, number will be assigned to 'second_largest' variable.
     Variables are then added and result returned"""
    largest = 0
    second_largest = 0
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or second_largest < num:
            second_largest = num
    return largest + second_largest

if __name__ == "__main__":
 print(find_max_sum([5, 9, 7, 11]))
 print(find_max_sum([13, 9, 7, 15]))
