# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input:
# 3  
# flower  
# flight  
# flow


# Output:
# fl  

# Explanation: fl is the common in all the strings in the given array.

n = int(input())
k = input()

for i in range(n - 1):
    s = input()
    c = 0

    while c < len(s) and c < len(k):
        if s[c] == k[c]:
            c += 1
        else:
            break

    k = k[:c]

print(k)

