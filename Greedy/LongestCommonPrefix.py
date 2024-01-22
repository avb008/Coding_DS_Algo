def longestCommonPrefix(S):
    if "" in S or S == []:
        return ""
    prefix = S[0]
    for i in range(1, len(S)):
        print(i,prefix)
        while prefix != "":
            try:
                if str.index(str(S[i]), prefix) == 0:
                    break
                else:
                    prefix = prefix[:-1]
            except:
                prefix = prefix[:-1]
    return prefix


if __name__ == "__main__":
    # Your code goes here
    s = ["flower", "flow", "flight"]
    print(longestCommonPrefix(s))
