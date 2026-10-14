
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating,
    are_anagrams,
    first_repeating_char,
    move_zeros,
    second_highest,
    remove_duplicates,
    missing_number,
    two_sum,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_sum,
    all_pairs
)

print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 Test:", word_frequency("hello hello world"))

print("Q2:", character_frequency("banana"))
print("Q2 Test:", character_frequency("hello"))

print("Q3:", first_non_repeating("swiss"))
print("Q3 Test:", first_non_repeating("aabb"))

print("Q4:", are_anagrams("listen", "silent"))
print("Q4 Test:", are_anagrams("hello", "world"))

print("Q5:", first_repeating_char("programming"))
print("Q5 Test:", first_repeating_char("python"))

print("Q6:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Test:", move_zeros([0, 1, 0, 2]))

print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 Test:", second_highest([5, 5, 5]))

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Test:", remove_duplicates([1, 1, 2, 3, 2]))

print("Q9:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Test:", missing_number([1, 2, 3, 5], 5))

print("Q10:", two_sum([2, 7, 11, 15], 9))
print("Q10 Test:", two_sum([1, 4, 6, 8], 10))

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Test:", closest_to_zero([-4, -1, 1, 3]))

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Test:", common_elements([2, 2, 3, 4], [2, 4, 6]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Test:", rotate_right([1, 2, 3, 4], 1))

print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Test:", max_consecutive_sum([1, 8, 3, 6]))

print("Q15:", all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Test:", all_pairs([1, 2, 3, 4, 5], 6))
