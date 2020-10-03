# Topic: CSE321 Homework #5
# Owner: Oguzhan Agkuş - 161044003

#################### Question 1 - Start ####################

def find_plan(sequence_1, sequence_2, moving_cost):
    m = len(sequence_1)
    n = len(sequence_2)
    plan = []

    if(m != n):
        print("Mismatching sequences!")
        return

    cost_table = [[0 for i in range(n)] for j in range(2)]

    cost_table[0][0] = sequence_1[0]
    cost_table[1][0] = sequence_2[0]

    for i in range(1, m):
        temp_1 = cost_table[0][i-1] + sequence_1[i]
        temp_2 = cost_table[1][i-1] + sequence_1[i] + moving_cost
        cost_table[0][i] = min(temp_1, temp_2)

        temp_3 = cost_table[0][i-1] + sequence_2[i] + moving_cost
        temp_4 = cost_table[1][i-1] + sequence_2[i]
        cost_table[1][i] = min(temp_3, temp_4)

    i = 0 if(cost_table[0][-1] < cost_table[1][-1]) else 1
    cost = cost_table[i][-1]

    plan.append(i)

    for j in range(m-1, 0, -1):
        if(i == 0):
            if(cost_table[0][j-1] < cost_table[1][j-1] + moving_cost):
                plan.append(i)

            else:
                i = 1
                plan.append(i)

        elif(i == 1):
            if(cost_table[0][j-1] + moving_cost < cost_table[1][j-1]):
                i = 0
                plan.append(i)

            else:
                plan.append(i)

    plan.reverse()

    for i in range(m):
        if(plan[i]):
            plan[i] = "NY"

        else:
            plan[i] = "SF"

    return plan, cost

def test_1():
    print("--> Question 1\n")

    sf_1 = [1, 3, 20, 30]
    ny_1 = [50, 30, 2, 4]
    plan, cost = find_plan(sf_1, ny_1, 10)
    print("Test 1:")
    print("\tSan Francisco: ", sf_1, "\n\tNew York: ", ny_1, sep="")
    print("\tPlan:", plan, "\n\tCost:", cost, "\n")

    sf_2 = [50, 3, 20, 4]
    ny_2 = [1, 30, 2, 30]
    plan, cost = find_plan(sf_2, ny_2, 10)
    print("Test 2:")
    print("\tSan Francisco: ", sf_2, "\n\tNew York: ", ny_2, sep="")
    print("\tPlan:", plan, "\n\tCost:", cost, "\n")

#################### Question 1 - End ####################

#################### Question 2 - Start ####################

class Session(): # Sessions class, it has id, start and end data
    def __init__(self, id, start, end):
        if(start > end or start < 0 or end > 12): # Start time cannot be bigger than end time, I assumed that we have 12 hour schedule (0,12)
            raise Exception()

        self.id = id
        self.start = start
        self.end = end

class Symposium(): # Symposium class, it has session list
    def __init__(self):
        self.sessions = [] # Session list
        self.ordered = False # Its is true if it is ordered according to end times
        self.optimal_list = [] # Save the optimal list to prevent trying to find it again if there is no change

    def add_session(self, id, start, end): # Add session to symposium
        try:
            self.sessions.append(Session(id, start, end))
            self.ordered = False # If it is ordered before, now it is not

        except: # Catch exceptions that occurs because of invalid arguments
            print("Error occured while adding new session! Check your arguments!\n")

    def show_all_sessions(self): # Show all sessions in current order
        print(" Symposium Program:")
        print("--------------------")
        print(" ID\tStart\tEnd")
        print("--------------------")

        for session in self.sessions:
            print(" ", session.id, "\t", session.start, "\t", session.end, sep="")

        print("--------------------\n")

    def show_optimal_sessions(self):
        if not (self.ordered):
            quick_sort(self)

            session_list = []
            i = 0

            session_list.append(self.sessions[i].id)

            for j in range(len(self.sessions)):
                if(self.sessions[j].start >= self.sessions[i].end):
                    session_list.append(self.sessions[j].id)
                    i = j

            self.ordered = True
            self.optimal_list = session_list

        print("Optimal session order:", self.optimal_list, "\n") # Print session ID's in optimal order

# This quick sort algorithm is from HW03 but it is optimized for Symposium objects

def quick_sort(array):
    if(isinstance(array, Symposium)): # If it is not Symposium object, it will not work
        _quick_sort(array.sessions, 0, len(array.sessions)-1)

    else:
        print("Excepted \"Symposium\" class object!\n")
        exit(1)

def _quick_sort(array, start, end):
    if(start < end):
        p_index = partition(array, start, end)
        _quick_sort(array, start, p_index-1)
        _quick_sort(array, p_index+1, end)

def partition(array, start, end):
    i = start-1
    pivot = array[end].end

    for j in range(start, end):
        if(array[j].end < pivot):
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]

    return i+1

def test_2():
    print("--> Question 2\n")
    my_symposium = Symposium()
    my_symposium.add_session(1,1,3)
    my_symposium.add_session(2,5,9)
    my_symposium.add_session(3,11,12)
    my_symposium.add_session(4,0,7)
    my_symposium.add_session(5,3,4)
    my_symposium.add_session(6,8,10)
    my_symposium.add_session(7,2,5)
    my_symposium.show_all_sessions()
    my_symposium.show_optimal_sessions()

#################### Question 2 - End ####################

#################### Question 3 - Start ####################

subsets = []

def find_subsets(array, n, index = 0, sum = 0,  subset = [], dp = []):
    if not(len(dp)):
        dp = [[0 for i in range(200)] for j in range(n)]

    if(index == n):
        if(sum == 0):
            subsets.append(subset)
            return 1

        else:
            return 0

    subset_1 = subset.copy()
    subset_2 = subset.copy()
    subset_1.append(array[index])

    temp_1 = find_subsets(array, n, index+1, sum + array[index], subset_1, dp)
    temp_2 = find_subsets(array, n, index+1, sum, subset_2, dp)

    dp[index][sum + n] = temp_1 + temp_2
    subset_count = dp[index][sum + n]

    return subset_count

def subset_sum_zero(array):
    n = len(array)
    subset_count = find_subsets(array, n)

    print("Array:", array)

    if(subset_count > 1):
        print("Example subset:", subsets[0])
        print("The array have", subset_count-1, "subset whose elements' sum equal to zero, except empty set.\n")

    else:
        print("There is only empty set!\n")

def test_3():
    array = [-1,6,4,2,3,-7,-5]
    #array = [1,2,3,4]
    #array = [0]

    print("--> Question 3\n")
    subset_sum_zero(array)

#################### Question 3 - End ####################

#################### Question 4 - Start ####################

def minimum_penalty(str_1, str_2, match_p = 2, mismatch_p = -2, gap_p = -1):
    match = match_p * -1
    mismatch = mismatch_p * -1
    gap = gap_p * -1

    m = len(str_1)
    n = len(str_2)
    dp = [[0 for i in range(m+n+1)] for j in range(m+n+1)]

    # Initialising table
    for i in range(m+n+1):
        dp[i][0] = i * 2;
        dp[0][i] = i * 2;

    # Calculating minimum penalty
    for i in range(1, m+1):
        for j in range(1, n+1):
            if(str_1[i-1] == str_2[j-1]):
                dp[i][j] = dp[i-1][j-1] + match

            else:
                dp[i][j] = min(dp[i-1][j-1] + mismatch, dp[i-1][j] + gap, dp[i][j-1] + gap)

    # Length
    l = m + n
    i = m
    j = n
    position_1 = l
    position_2 = l

    # Final answers
    answer_1 = [0 for i in range(l+1)]
    answer_2 = [0 for i in range(l+1)]

    # Constructing solution
    while(not(i == 0 or j == 0)):
        if(str_1[i-1] == str_2[j-1]):
            answer_1[position_1] = str_1[i-1]
            position_1 -= 1
            answer_2[position_2] = str_2[j-1]
            position_2 -= 1
            i -= 1
            j -= 1

        elif(dp[i-1][j-1] + mismatch == dp[i][j]):
            answer_1[position_1] = str_1[i-1]
            position_1 -= 1
            answer_2[position_2] = str_2[j-1]
            position_2 -= 1
            i -= 1
            j -= 1

        elif(dp[i-1][j] + gap == dp[i][j]):
            answer_1[position_1] = str_1[i-1]
            position_1 -= 1
            answer_2[position_2] = "_"
            position_2 -= 1
            i -= 1

        elif(dp[i][j-1] + gap == dp[i][j]):
            answer_1[position_1] = "_"
            position_1 -= 1
            answer_2[position_2] = str_2[j-1]
            position_2 -= 1
            j -= 1

    while(position_1 > 0):
        if(i > 0):
            i -= 1
            answer_1[position_1] = str_1[i]

        else:
            answer_1[position_1] = "_"

        position_1 -= 1

    while(position_2 > 0):
        if(j > 0):
            j -= 1
            answer_2[position_2] = str_2[j]

        else:
            answer_2[position_2] = "_"

        position_2 -= 1

    # Remove extra gaps from starting
    flag = 1

    for i in range(l, 0, -1):
        if(answer_1[i] == "_" and answer_2[i] == "_"):
            flag = i + 1
            break

    answer_1 = ''.join(answer_1[flag:])
    answer_2 = ''.join(answer_2[flag:])
    penalty =  dp[m][n] * -1

    # Print results
    print("\tInput: ")
    print("\t\tString 1:", str_1)
    print("\t\tString 2:", str_2)
    print("\tOutput: ")
    print("\t\tPenalty:", penalty)
    print("\t\tString 1:", answer_1)
    print("\t\tString 1:", answer_2, "\n")

def test_4():
    print("--> Question 4\n")
    print("Test 1:")
    minimum_penalty("alignment","slime")
    print("Test 2:")
    minimum_penalty("acggctc","atggcctc")
    print("Test 3:")
    minimum_penalty("agggct","aggca")

#################### Question 4 - End ####################

#################### Question 5 - Start ####################

def find_minimum(array):
    array.sort()

    operation_count = 0
    previous_sum = 0
    i = 0

    while(i < len(array)):
        if(i == 0):
            previous_sum = array[0] + array[1]
            i = 2

        else:
            previous_sum += array[i]
            i += 1

        operation_count += previous_sum

    return operation_count

def test_5():
    array_1 = [1,5,7,3]
    array_2 = [3,18,27,30,15]

    print("--> Question 5\n")
    print("Test 1:")
    print("\tArray:", array_1, "\n\tMinumum operation count:", find_minimum(array_1), "\n")
    print("Test 2:")
    print("\tArray:", array_2, "\n\tMinumum operation count:", find_minimum(array_2), "\n")

#################### Question 5 - End ####################

#################### Driver - Start ####################

def driver():
    print("CSE321 - Homework #5 Test\n")
    print("-------------------------\n")
    test_1()
    print("-------------------------\n")
    test_2()
    print("-------------------------\n")
    test_3()
    print("-------------------------\n")
    test_4()
    print("-------------------------\n")
    test_5()
    print("-------------------------\n")

#################### Driver - End ####################

if __name__ == "__main__":
    driver()
