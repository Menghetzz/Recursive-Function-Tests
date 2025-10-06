def sum_numbers(a,b):
    if a == b:
        return b
    elif a > b:
        somma = b
        return somma + sum_numbers(a, b + 1)
    else:
        somma = a
        return somma + sum_numbers(a + 1, b)
   
def pow(a, n):
    if n == 0:
        return 1
    elif a == 0:
        return 0
    else:
        return a * pow(a, n - 1)
   
def list_contains(lst, elem):
    if len(lst) == 0:
        return False
   
    if lst[0] == elem:
        return True
    else:
        lst.pop(0)
        return list_contains(lst, elem)
   
def palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 0:
        return True
    if s[0] == s[len(s) - 1]:
        return palindrome(s[1:-1])
    else:
        return False
   
 
 
 
print(sum_numbers(1, -2))

print(pow(0, 3))
 
print(list_contains(['cia', 2, 3 ,4], 'cia'))
 
print(palindrome("itopinonavevanonipoti"))