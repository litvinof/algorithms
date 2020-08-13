from collections import defaultdict


def build_palindrom(s):
    char_count = defaultdict(int)
    for c in s:
        char_count[c] += 1

    odd_char = ""
    palindrome = ""

    for c, cnt in char_count.items():
        if cnt % 2 == 0:
            palindrome += c * (cnt // 2)
        elif not odd_char:
            odd_char = c
            palindrome += c * (cnt // 2)
        else:
            return None
    return palindrome + odd_char + palindrome[::-1]


print(build_palindrom("mommo"))
print(build_palindrom("mommmo"))
