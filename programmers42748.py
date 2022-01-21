array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array, commands):
    result = []
    for i in range(len(commands)):
        first_index = commands[i][0] - 1
        last_index = commands[i][1]
        num = array[first_index:last_index]
        num.sort()
        pick_index = commands[i][2] - 1
        result.append(num[pick_index])
    return result

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))

# array = list(input())
# command = list(input())
#
# 1<=len(array)<=100
# 1 <= len(command) <= 50
# def solution():
#     a = array
#     b = int(command[0])
#     c = int(command[1])
#     d = int(command[2])
#     first_answer = a[b-1:c]
#     first_answer = sorted(first_answer)
#     print(first_answer)
#     second_answer = first_answer[d-1]
#     print(second_answer)
#
# solution()

