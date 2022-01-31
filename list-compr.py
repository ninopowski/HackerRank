
x = 1
y = 1
z = 2

n = 3

#all_items = [[i for i in range(0, x+1)],[j for j in range(0, y+1)], [k for k in range(0, z+1)]]

all_items = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if (i + j + k) != n:
                all_items.append([i, j, k])

second_option = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(z+1) if (i + j + k) != n]

print(all_items)
print(second_option)

