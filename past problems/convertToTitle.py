"""168. Excel Sheet Column Title
Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""
def convertToTitle(n):
    res = ""
    while n//26 != 0:
        res += chr(64 + (n//26))
        n %= 26
    res += chr(64 + n)
    return res

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(702))