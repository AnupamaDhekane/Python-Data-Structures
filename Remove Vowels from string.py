def RemoveVowels(word):
    res = list()
    ans = ""
    for i in range(0, len(word)-1):
        j = i
        if word[i] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            res.append(word[i])
            ans += word[i]

    print(res)
    print(ans)
    
RemoveVowels("AajMeUpar")