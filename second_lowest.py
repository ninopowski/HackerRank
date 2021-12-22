
#second highest scores, printed in a new line aplabeticaly

#example input data:
records = [["nino", 10], ["ana", 12], ["ida", 1], ["megi", 2], ["petre", 2], ["boni", 1], ["mitre", 1]]


sorted_records = sorted(records, key=lambda x: x[1])

lowest_score = sorted_records[0][1]

sum = 0
for entry in sorted_records:
    if entry[1] == lowest_score:
        sum += 1

new_sorted = sorted_records[sum:]

second_lowest = new_sorted[0][1]

second_lowest_list = []
for item in new_sorted:
    if item[1] == second_lowest:
        second_lowest_list.append(item)
sorted_second_lowest = sorted(second_lowest_list)
for name in sorted_second_lowest:
    print(name[0])