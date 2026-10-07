# video number 17 
# finding palindrom

# Using for loop:
def palindrome2(n):
    for i in range(len(n)):
        if n[i]!=n[len(n)-1-i]:
            print("Not palindrome")
            break
    else:
        print("palindrome")

        
    
# palindrome2(n)




# two pointer method


# Using recursion:
n=input()
i=0
j=len(n)-1
def palindrome(n,i,j):
    if i>=j:
        return "it's a palindrome"
    
    
    elif n[i]!=n[j]:
        return "Not palindrome"
    
    elif n[i]==n[j]:
        return palindrome(n,i+1,j-1) 

print(palindrome(n,i,j))


 

# similarly it can be done using while loop  



