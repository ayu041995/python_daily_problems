def length_of_longest_substring(string):
    max_len = 0
    non_rep = ''
    for right in range(len(string)):
        if string[right] not in non_rep:
            non_rep += string[right]
            max_len = max(max_len,len(non_rep))
        while left < right and  



print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")