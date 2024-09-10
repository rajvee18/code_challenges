n = int(input())

grades = []

for i in range(n):

    name = input().lower()
    score = float(input())
    grades.append([name,score])

grades.sort(reverse=True)

marks = []

for i in range(n):
    marks.append(grades[i][1])


second_lowest = sorted(set(marks))[1]

name_list =[]

for i in range(n):
    if grades[i][1]==second_lowest:
        name_list.append(grades[i][0])

name_list.sort()

for i in name_list:
    print(i)











