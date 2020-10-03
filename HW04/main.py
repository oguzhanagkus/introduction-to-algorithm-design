# Topic: CSE321 Homework #4
# Owner: Oguzhan Agkus - 161044003

#################### Common Functions - Start ####################

def print_2d_array(array, tab = True):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end="")

            if(tab ):
                print("\t", end="")

            else:
                print(" ", end="")
        print()
    print()

#################### Common Functions - End ####################

#################### Question 1-1 - Start ####################

def check_and_convert(array):
    if(len(array) == 0):
        return "Invalid input!"

    m = len(array)
    n = len(array[0])
    count = 0

    x = 0 # x coordinate
    y = 0 # y coordinate
    x_b = 0 # Backup
    y_b = 0 # Backup

    for i in range(m-1):
        for j in range(n-1):
            if not (array[i][j] + array[i+1][j+1] <= array[i][j+1] + array[i+1][j]):
                count += 1

                if(count > 1):
                    break

                else:
                    x = x_b = j
                    y = y_b = i

                    if(j != 0):
                        x += 1

                    if(i == m-2):
                        y += 1

    if(count == 0):
        return "It is already a special array!"

    elif(count == 1):
        temp = array[y][x] # Backup
        diff = array[y_b][x_b] + array[y_b+1][x_b+1] - array[y_b+1][x_b] - array[y_b][x_b+1]
        array[y][x] += diff

        return f"Coordiantes of changed element: [{y},{x}]\nOld value: {temp}, new value: {array[y][x]}"

    else:
        return "It needs to change more than one element!"

def test_1_1():
    array = [[37,23,22,32],
             [21,6,7,10],
             [53,34,30,31],
             [32,13,9,6],
             [43,21,15,8]]

    print("Question 1 - Part B\n")
    print_2d_array(array)
    print(check_and_convert(array), "\n")

#################### Question 1-1 - End ####################

#################### Question 1-2 - Start ####################

def merge_index(items, evens):
    result = []
    m = len(items)
    n = len(items[0])

    for i in range(m):
        left = evens[i]
        right = -1

        if(i == m-1 and len(evens) == m):
            right = n - 1

        else:
            right = evens[i+1]

        minimum = items[i][left]
        position = left

        for j in range(left, right+1):
            if(items[i][j] < minimum):
                minimum = items[i][j]
                position = j

        result.append(evens[i])
        result.append(position)

    if(len(evens) > m):
        result.append(evens[-1])

    return result

def find_index(array):
    if(len(array) == 1):
        index = 0
        minimum = 2**31-1

        for i in range(len(array[0])):
            if(array[0][i] < minimum):
                minimum = array[0][i]
                index = i

        return [index]

    evens = array[::2]
    even_index = find_index(evens)
    result = merge_index(array[1::2], even_index)

    return result

def test_1_2():
    array = [[23,23,24,32],
             [21,6,7,10],
             [53,34,30,31],
             [32,13,9,6],
             [43,21,15,8]]

    print("Question 1 - Part C\n")
    print_2d_array(array)
    print("Leftmost minimum indexes:", find_index(array), "\n")

#################### Question 1-2 - End ####################

#################### Question 2 - Start ####################

def kth_element(array_1, array_2, k, p_1 = 0, p_2 = 0): # p_1 and p_2 are pointers for array_1 and array_2

    len_1 = len(array_1) # Size of the array_1
    len_2 = len(array_2) # Size of the array_2

    if(p_1 == len_1): # If p_1 reach end of the array_1, return the element that other pointer points
        return array_2[p_2 + k - 1]

    if(p_2 == len_2): # If p_2 reach end of the array_2, return the element that other pointer points
        return array_1[p_1 + k - 1]

    if(k == 0 or k > (len_1 - p_1) + (len_2 - p_2)): # If k has invalid value (zero or bigger than sum of sizes), return -1 (error)
        return -1

    if(k == 1): # Compare first elements, return the smaller
        if (array_1[p_1] < array_2[p_2]):
            return array_1[p_1]

        else:
            return array_2[p_2]

    current = k//2

    if(current - 1 >= len_1 - p_1): # Size of array_1 is less than k/2
        if(array_1[len_1 - 1] < array_2[p_2 + current - 1]): # If last element of array_1 is not kth, directly return (k-len_1)th element in array_2
            return array_2[p_2 + (k - (len_1 - p_1) - 1)]

        else:
            return kth_element(array_1, array_2, k - current, p_1, p_2 + current)

    if(current - 1 >= len_2 - p_2): # Size of array 2 is less than k/2
        if(array_2[len_2 - 1] < array_1[p_1 + current - 1]): # If last element of array_2 is not kth, directly return (k-len_2)th element in array_2
            return array_1[p_1 + (k - (len_2 - p_2) - 1)]

        else:
            return kth_element(array_1, array_2, k - current, p_1 + current, p_2)

    else: # Move pointer of one array k/2 to the right
        if(array_1[current + p_1 - 1] < array_2[current + p_2 - 1]):
            return kth_element(array_1, array_2, k - current, p_1 + current, p_2)

        else:
            return kth_element(array_1, array_2, k - current, p_1, p_2 + current)

def test_2():
    array_1 = [1,3,5,7,9]
    array_2 = [0,2,4,6,8]
    k = 5

    print("Question 2\n")
    print("Array 1:", array_1, "\nArray 2:", array_2, "\nk:", k, "\n")
    print(f"{k}th element is", kth_element(array_1, array_2, k), "\n")

#################### Question 2 - End ####################

#################### Question 3- Start ####################

def maximum_crossing_sum(array, low, medium, high):
	start_index = medium
	end_index = medium

	sum = 0
	left_sum = -(2**31)

	for i in range(medium, low-1, -1):
		sum += array[i]

		if(sum > left_sum):
			left_sum = sum
			start_index = i

	sum = 0
	right_sum = -(2**31)

	for i in range(medium+1, high+1):
		sum += array[i]

		if(sum > right_sum):
			right_sum = sum
			end_index = i

	return (left_sum + right_sum), start_index, end_index

def maximum_subarray_sum(array, low, high) :
	if(low == high):
		return array[low], low, low

	medium = (low + high) // 2

	left_sum, s1, e1 = maximum_subarray_sum(array, low, medium)
	right_sum, s2, e2 = maximum_subarray_sum(array, medium+1, high)
	crossing_sum, s3, e3 = maximum_crossing_sum(array, low, medium, high)

	maximum_sum = max(left_sum, right_sum, crossing_sum)

	if(maximum_sum == left_sum):
		return left_sum, s1, e1

	elif(maximum_sum == right_sum):
		return right_sum, s2, e2

	elif(maximum_sum == crossing_sum):
		return crossing_sum, s3, e3

def maximum_subarray(array):
	max_sum, start_index, end_index = maximum_subarray_sum(array, 0, len(array)-1)
	return array[start_index:end_index+1], max_sum

def test_3():
    array = [5, -6, 6, 7, -6, 7, -4, 3]
    subarray, sum = maximum_subarray(array)

    print("Question 3\n")
    print("Array:", array)
    print("Subarray:", subarray)
    print("Sum:", sum, "\n")

#################### Question 3 - End ####################

#################### Question 4 - Start ####################

class Graph():
    def __init__(self, graph):
        self.vertex_count = len(graph)
        self.graph = graph
        self.colored = [-1 for i in range(self.vertex_count)]

    def can_colored(self, position = 0, color = 1):
        if(self.colored[position] != -1 and self.colored[position] != color):
            return False

        self.colored[position] = color

        answer = True

        for i in range(0, self.vertex_count):
            if(self.graph[position][i]):
                if(self.colored[i] == -1):
                    answer &= self.can_colored(i, 1-color)

                if(self.colored[i] != -1 and self.colored[i] != 1-color):
                    return False

            if not answer:
                return False

        return True

    def is_bipartite(self):
        return self.can_colored()

def test_4():
    test_1 = [[0, 1, 0, 1],
			  [1, 0, 1, 0],
	          [0, 1, 0, 1],
			  [1, 0, 1, 0]]

    test_2 = [[0,0,1,1,1,0],
              [0,0,0,0,0,1],
              [1,0,0,0,1,1],
              [1,0,0,0,0,0],
              [1,0,1,0,0,0],
              [0,1,1,0,0,0]]

    my_graph_1 = Graph(test_1)
    my_graph_2 = Graph(test_2)

    print("Question 4\n")
    print("-> Graph 1:\n")
    print_2d_array(test_1, False)
    print("Is bipartite? :", my_graph_1.is_bipartite(), "\n")
    print("-> Graph 2:\n")
    print_2d_array(test_2, False)
    print("Is bipartite? :", my_graph_2.is_bipartite(), "\n")

#################### Question 4 - End ####################

#################### Question 5 - Start ####################

def best_day(cost, price, low, high):
    if(low == high): # Single element
        return price[low]-cost[low], low

    if(low + 1 == high): # Two elements
        temp_1 = price[low]-cost[low]
        temp_2 = price[high]-cost[high]

        if(temp_1 > temp_2):
            return temp_1, low

        else:
            return temp_2, high

    middle = (low + high) // 2
    left, day_left = best_day(cost, price, low, middle)
    right, day_right = best_day(cost, price, middle+1, high)

    if(left > right):
        return left, day_left

    else: # left <= right
        return right, day_right

def find_best_day(cost, price):
    if(len(cost) == len(price)):
        gain, day = best_day(cost, price, 0, len(cost)-1)
        day += 1 # Because of indexing

        if(gain):
            return f'Best day is {day}th day and gain is {gain} units of money.'

        else: # gain=0
            return "There is no gain during the schedule!"
    else:
        return "Invalid inputs!"

def test_5():
    cost = [5, 11, 2, 21, 5, 7, 8, 12, 13]
    price = [7, 9, 5, 21, 7, 13, 10, 14, 20]

    print("Question 5\n")
    print("Cost:", cost)
    print("Price:", price, "\n")
    print(find_best_day(cost, price), "\n")

#################### Question 5 - End ####################

#################### Driver - Start ####################

def driver():
    print("CSE321 - Homework #4 Test\n")
    print("-------------------------\n")
    test_1_1()
    print("-------------------------\n")
    test_1_2()
    print("-------------------------\n")
    test_2()
    print("-------------------------\n")
    test_3()
    print("-------------------------\n")
    test_4()
    print("-------------------------\n")
    test_5()
    print("-------------------------")

#################### Driver - End ####################

if __name__ == "__main__":
    driver()
