# Topic: CSE321 Homework #3
# Owner: Oguzhan Agkus - 161044003

import random

#################### Common Functions - Start ####################

def create_random_list(n, lower = 1, upper = 100): # Creates a random list with size n, each element is between lower and upper bound.
    array = []

    for i in range(n):
        array.append(random.randint(lower, upper))

    return array

#################### Common Functions - End ####################

#################### Quesiton 1 - Start ####################

def algorithm_1(row):
    n = len(row)

    for i in range(1, int(n/2), 2):
         row[i], row[n-1-i] = row[n-1-i], row[i]

def test_algorithm_1(inputs = [7, 8]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 1:\n")
    print("- Testing with random arrays:")

    for n in inputs:
        row = []

        for i in range(n):
            row.append('B') # B represents black

        for i in range(n):
            row.append('W') # W represents white

        print("Before:", row)

        algorithm_1(row)

        print("After: ", row, "\n")

#################### Quesiton 1 - End ####################

#################### Quesiton 2 - Version 1 - Start ####################
# Version note: Fake coin is lighter, we know that.

def algorithm_2_1(coins):
    n = len(coins)
    fake_index = 0

    if(n%2 != 0):
        coins.pop()
        temp = n-1

    left = coins[:n//2] # Split the coins into left and right
    right = coins[n//2:] # Split the coins into left and right

    left_weight = sum(left)
    right_weight = sum(right)

    if(left_weight == right_weight): # It means the coin that has been popped is fake coin
        fake_index = temp

    elif(left_weight < right_weight): # Left side weights less, fake coin should be in there
        fake_index += algorithm_2_1(left)

    else: # Right side weights less, fake coin should be in there
        fake_index += (n/2) + algorithm_2_1(right)

    return int(fake_index)

def test_algorithm_2_1(inputs = [15, 16]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 2 - Version 1:\n")
    print("- Testing with random arrays:")

    for n in inputs:
        fake = 4 # Fake coin weight
        real = 5 # Real coin weight
        coins = []

        for i in range(n-1): # Insert real coins
            coins.append(real)

        index = random.randint(0, n-2)
        coins.insert(index, fake) # Insert a fake coin randomly

        print("My coins:", coins)

        fake_index = algorithm_2_1(coins)

        print("Result =", fake_index, "\n")

#################### Quesiton 2 - Version 1 - End ####################

#################### Quesiton 2 - Version 2 - Start ####################
# Version note: Fake coin can be lighter or heavier, we have no information.

def total_weight(coins, s, e): # Total weight of the coins at index s(start) between e(end)
    sum = 0

    for i in range(s, e+1):
        sum += coins[i]

    return sum

def algorithm_2_2(coins):
    if(len(coins) < 3):
        return "There is insufficient data to detect index of fake coin."

    left_index = 0
    right_index = len(coins)-1

    if(len(coins)%2 != 0):
        right_index -= 1

    end = right_index//2
    left_weight = total_weight(coins, left_index, end)
    right_weight = total_weight(coins, end+1, right_index)

    if(left_weight == right_weight):
        index = len(coins)-1

    else:
        while(left_weight != right_weight):
            left = coins[left_index]
            right = coins[right_index]

            left_index += 1
            right_index -= 1

            left_weight = total_weight(coins, left_index, end)
            right_weight = total_weight(coins, end+1, right_index)

        if(left_index > 1):
            reference = 0

        else:
            reference = right_index

        if(coins[reference] == left):
            index = right_index+1

        elif(coins[reference] == right):
            index = left_index-1

    return index

def test_algorithm_2_2(inputs = [15, 16]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 2 - Version 2:\n")
    print("- Testing with random arrays:")

    for n in inputs:
        coins = []
        real = random.randint(1, 10) # Real coin weight
        fake = random.randint(1, 10) # Fake coin weight

        while(fake == real):
            fake = random.randint(1, 10) # Fake coin weight

        for i in range(n-1): # Insert real coins
            coins.append(real)

        index = random.randint(0, n-2)
        coins.insert(index, fake) # Insert the fake coin randomly

        print("My coins:", coins)
        print("Result = ", end="")

        fake_index = algorithm_2_2(coins)

        print(fake_index, "\n")

#################### Quesiton 2 - Version 2 - End ####################

#################### Quesiton 3 - Start ####################

def insertion_sort(array):
    swap_count = 0

    for i in range(1, len(array)):
        selected = array[i]
        j = i-1

        while(j >= 0):
            if(selected < array[j]):
                array[j+1] = array[j]
                j -= 1
                swap_count += 1

            else:
                break

        array[j+1] = selected

    return swap_count

def partition(array, start, end):
    swap_count = 0

    i = start-1
    pivot = array[end]

    for j in range(start, end):
        if(array[j] < pivot):
            i += 1
            array[i], array[j] = array[j], array[i]

            if(i != j):
                swap_count += 1

    array[i+1], array[end] = array[end], array[i+1]

    if(i+1 != end):
        swap_count += 1

    return i+1, swap_count

def _quick_sort(array, start, end):
    swap_count = 0

    if(start < end):
        p_index, temp = partition(array, start, end)
        swap_count += temp

        swap_count += _quick_sort(array, start, p_index-1)
        swap_count += _quick_sort(array, p_index+1, end)

    return swap_count

def quick_sort(array):
    return _quick_sort(array, 0, len(array)-1)

def test_sort(inputs = [15, 16]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 3:\n")
    print("- Testing with random arrays:")

    for n in inputs:
        temp_array = create_random_list(n)
        temp_array_copy = temp_array.copy()

        print("Unsorted array:", temp_array)

        swap_count_instertion = insertion_sort(temp_array)
        swap_count_quick = quick_sort(temp_array_copy)

        print("Insertion sort result: ", temp_array, ", swap count =", swap_count_instertion)
        print("Quick sort result:     ", temp_array_copy, ", swap count =", swap_count_quick, "\n")

def test_algorithm_3():
    test_sort()

#################### Quesiton 3 - End ####################

#################### Quesiton 4 - Start ####################

def find_median(array): # Using insertion sort algorithm from previous question.
    n = len(array)

    insertion_sort(array) # Firstly sort the array.

    if (n%2 != 0): # If element count is odd, pick the middle element.
        median = array[int(n/2)]

    else: # If element count is even, pick the average of two elements in the middle.
        median = (array[int((n-1)/2)] + array[int(n/2)]) / 2

    return median

def test_algorithm_4(inputs = [15, 16]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 4:\n")
    print("- Testing with random arrays:")

    for n in inputs:
        temp_array = create_random_list(n)

        print("Unsorted array:", temp_array)

        temp_median = find_median(temp_array)

        print("Sorted array:  ", temp_array)
        print("Median =", temp_median, "\n")

#################### Quesiton 4 - End ####################

#################### Quesiton 5 - Start ####################

def lower_bound(array):
    return ((min(array) + max(array)) * len(array) / 4)

def mult(array): # Multiplication of array's all elements
    if(len(array) == 0):
        return 0

    else:
        mul = 1

        for i in range(0, len(array)):
            mul *= array[i]

        return mul

def _sub_array(array, index, subarray): # Generating all possible sub-arrays
    mul = 0
    arr = []

    if(index == len(array)):
        if len(subarray) != 0:
            if(sum(subarray) >= lower_bound(array)):
                mul = mult(subarray)
                arr = subarray.copy()

    else:
        t, temp = _sub_array(array, index+1, subarray)

        if(mul == 0 or mul > t): # If multiplication of generated sub-array's elements smaller than before
            mul = t
            arr = temp

        t, temp = _sub_array(array, index+1, subarray+[array[index]])

        if(mul == 0 or mul > t): # If multiplication of generated sub-array's elements smaller than before
            mul = t
            arr = temp

    return mul, arr

def sub_array(array):
    return _sub_array(array, 0, [])

def test_sub_array(inputs = [7, 8]): # Input is an array of input n's. Random arrays with size n will be generated for each n.
    print("--> Question 5:\n")

    print("- Given test in the pdf:")
    array_1 = [2, 4, 7, 5, 22, 11]
    mult_1, sub_1 = sub_array(array_1)
    print("Array:", array_1, "\nOptimal sub-array:", sub_1, "\n")

    print("- Testing with random arrays:")
    for n in inputs:
        temp_array = create_random_list(n, 1, 20)
        temp_mult, temp_sub = sub_array(temp_array)
        print("Array:", temp_array, "\nOptimal sub-array:", temp_sub, "\n")

def test_algorithm_5():
    test_sub_array()

#################### Quesiton 5 - End ####################
#################### Driver - Start ####################

def driver():
    test_algorithm_1()
    print("-------------------------\n")
    test_algorithm_2_1()
    print("-------------------------\n")
    test_algorithm_2_2()
    print("-------------------------\n")
    test_algorithm_3()
    print("-------------------------\n")
    test_algorithm_4()
    print("-------------------------\n")
    test_algorithm_5()

#################### Driver - End ####################

if __name__ == "__main__":
    driver()
