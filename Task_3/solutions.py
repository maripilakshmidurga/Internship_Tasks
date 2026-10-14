
# Q1. Find the Frequency of Each Word in a Sentence

# Q1. Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    result = {}
    words = sentence.split()

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


print(word_frequency("python is easy and python is powerful"))
print(word_frequency("banana apple banana"))


# Q2. Find the Frequency of Each Character in a Word

def character_frequency(word):
    result = {}

    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(character_frequency("banana"))
print(character_frequency("hello"))


# Q3. Find the First Non-Repeating Character in a Word

def first_non_repeating(word):
    for char in word:
        if word.count(char) == 1:
            return char

    return None


print(first_non_repeating("swiss"))
print(first_non_repeating("aabb"))


# Q4. Check Whether Two Strings Are Anagrams

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))


# Q5. Find the First Repeating Character in a String

def first_repeating_char(word):
    seen = set()

    for char in word:
        if char in seen:
            return char
        seen.add(char)

    return None


print(first_repeating_char("programming"))
print(first_repeating_char("python"))


# Q6. Move All Zeros to the End of a List

def move_zeros(nums):
    result = [num for num in nums if num != 0]
    result.extend([0] * (len(nums) - len(result)))
    return result


print(move_zeros([0, 3, 0, 1, 2, 0, 4]))
print(move_zeros([0, 1, 0, 2]))


# Q7. Find the Second Highest Distinct Number

def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)

    if len(unique_nums) < 2:
        return None

    return unique_nums[1]


print(second_highest([10, 20, 40, 30, 40, 20]))
print(second_highest([5, 5, 5]))


# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print(remove_duplicates([1, 1, 2, 3, 2]))


# Q9. Find the Missing Number from 1 to N

def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


print(missing_number([1, 2, 4, 5, 6], 6))
print(missing_number([1, 2, 3, 5], 5))


# Q10. Find Two Numbers Whose Sum Equals a Target

def two_sum(nums, target):
    seen = []

    for num in nums:
        needed = target - num

        if needed in seen:
            return [needed, num]

        seen.append(num)

    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([1, 4, 6, 8], 10))


# Q11. Find the Number Closest to Zero

def closest_to_zero(nums):
    return min(nums, key=lambda num: (abs(num), -num))


print(closest_to_zero([-8, -3, 2, 5, -2]))
print(closest_to_zero([-4, -1, 1, 3]))


# Q12. Find Common Elements Between Two Lists

def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(common_elements([2, 2, 3, 4], [2, 4, 6]))


# Q13. Rotate a List to the Right by K Positions

def rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k else nums[:]


print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1, 2, 3, 4], 1))


# Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


print(max_consecutive_sum([4, 7, 2, 9, 5]))
print(max_consecutive_sum([1, 8, 3, 6]))


# Q15. Find All Pairs Whose Sum Equals a Target

def all_pairs(nums, target):
    result = []
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            pair = sorted([needed, num])

            if pair not in result:
                result.append(pair)

        seen.add(num)

    result.sort(key=lambda pair: pair[0])

    return result


print(all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print(all_pairs([1, 2, 3, 4, 5], 6))
