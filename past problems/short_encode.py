def minimumLengthEncoding(words):
    words = list(set(words))
    words = sorted(words, key=len)
    words.reverse()
    print(words)
    ans = len(words[0])
    for i in range(1, len(words)):
        for j in range(0, i):
            if words[j].endswith(words[i]):
                break
        else:
            ans += (1 + len(words[i]))
    return ans+1

print(minimumLengthEncoding(["time", "me", "bell"]))
print(minimumLengthEncoding((["time", "pastime", "me"])))