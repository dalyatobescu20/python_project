# Declararea unei liste
initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Initial list:", initial_list)

asc_sorted_list = sorted(initial_list)
print("ascending order:", asc_sorted_list)

desc_sorted_list = sorted(initial_list, reverse=True)
print("descending order:", desc_sorted_list)

even_indexed_numbers = initial_list[1::2]
print("even indices", even_indexed_numbers)

# Afișarea numerelor cu indici impari din listă (folosind DOAR slice)
odd_indexed_numbers = initial_list[::2]
print("odd indices:", odd_indexed_numbers)

# Afișarea elementelor multipli ai lui 3
multiple_of_three = [num for num in initial_list if num % 3 == 0]
print("multiple of three:", multiple_of_three)
