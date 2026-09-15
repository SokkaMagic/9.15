# You can remove 'pass' if you written code in the function
# Exercise 1

def find_all_positions(data, target):
    lst=[]
    for i in range(len(data)):
        if target == data[i]:
            lst.append(i)
    return lst
# Exercise 2
def find_student_by_id(records, student_id):
    for i in range(len(records)):
        if student_id == records[i][0]:
            return records[i][1]



# Exercise 3
def binary_search_steps(data, target):
    low =0
    high = len(data)-1
    steps=0
    result=[]
    while low <= high:
        mid = (low + high) // 2
        steps+=1

        if data[mid] == target:
            result.append(mid)
            result.append(steps)
            return result

        elif data[mid] < target:
            low = mid + 1  # target is in the right half
        else:
            high = mid - 1  # target is in the left half

    return [-1,steps+1]



# Exercise 4
def find_insert_position(data, value):
    # Write your code here
    pass

# Exercise 5
def first_and_last_position(data, target):
    # Write your code here
    pass
