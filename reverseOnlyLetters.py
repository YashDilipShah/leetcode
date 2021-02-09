"""917. Reverse Only Letters
Easy

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Note:

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122 
    S doesn't contain \ or "

"""
def reverseOnlyLetters(S):
    dicT = {}
    indexes = []
    for i in range(len(S)):
        if not S[i].isalpha():
            indexes.append(i)
            if S[i] in dicT.keys():
                dicT[S[i]].append(i)
            else:    
                dicT[S[i]] = [i]
    S = [i for i in S if i.isalpha()]
    S.reverse()
    for i in indexes:
        S.insert(i, "_")
    for key, val in dicT.items():
        for i in val:
            S[i] = key
    return "".join(S)

print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))