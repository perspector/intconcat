import itertools
import datetime
import time


# Get input numbers separated by spaces, example:
# Input data: 42 2 2 9 4 76 107
in_nums_str = input("Input data: ")
in_nums = [x for x in in_nums_str.split(" ")]

start = datetime.datetime.now()

# Get all possible permutations
combos = list(itertools.permutations(in_nums, len(in_nums)))
combos.sort(reverse=True)
concat_combos = []
for i in combos:
    concat_combos.append(int(''.join(i)))

maximum = 0
current = 0
columns = 65

# For each permutation
for combo in combos:
    current += 1
    perc = round(current / len(combos) * 100)
    combo_str = ""
    for integer in combo:
        combo_str += str(integer)
    
    # Check if new permutation is greater than the previous maximum
    if int(combo_str) > maximum:
        # If it is, then update the max value recorded
        maximum = int(combo_str)
    current_time = datetime.datetime.now()

    # Cool, yet inefficient progress bar. May implement tqdm in the future.
    print(f"\n\n\n\n\n\n\n\n\n\n\033[3A{perc}% |{(chr(9608) * (round(perc * (columns/100)) - 1)) + '>' + ' ' * (columns-(round(perc*(columns/100)-1)))}|\nCurrent: {combo_str}\nCurrent Max: {maximum}\nTime: {(current_time - start)}")

print("\n\n================")
print(f"Input data: {in_nums_str.replace(' ',', ')}")
print(f"Maximum: {maximum}")
