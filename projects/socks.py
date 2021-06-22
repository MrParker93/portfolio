import matplotlib.pyplot as plt
import random
from algorithms.sort.bubble import bubble_sort

no_of_colours = 10

colour = ["#" + "".join([random.choice("0123456789ABCDEF") for hex_val in range(6)])
          for _ in range(no_of_colours)]

hex_to_int = []
sorted_hex = []

print(colour)

for i in colour:
    if "#" in i:
        new_str = i.replace("#", "")
        hex_to_int.append(int(new_str, 16))

print(hex_to_int)

colour_sorted = bubble_sort(hex_to_int)
print(colour_sorted)

for i in colour_sorted:
    hexed = hex(i)
    hex_val = hexed.replace("0x", "#")
    sorted_hex.append(hex_val.upper())

print(sorted_hex)
for i in range(no_of_colours):
    plt.scatter(random.randint(0, 10), random.randint(0, 10), c=sorted_hex[i], s=200)

plt.show()