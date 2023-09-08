# Strings

str = "String sample"
str1 = 'String sample'

print(str)
print(str1)

# concatenation and multiplication
result_str = str + str1
print(result_str)

str3times = 3*(str + " ")
print(str3times)

# take the sympol
str = "abcd"
print(str[0])
print(str[-2])

### string method and functions
# len()
str = "12345qwerasdf"
str_len = len(str)
print(str_len)

# str.split("")
str = "Ihor Diuba"
print(str)
fullName = str.split(" ")
print(fullName[0])
print(fullName[1])

# str.join()

fullName = ["Ihor", "Diuba"]
print(fullName)
str = " and ".join(fullName)
print(str)

'''
q = string.strip('.') # Видалення символів '.' з обох 
кінців рядка:
print(q)
q = string.capitalize() # Перше слово з великої літери
print(q)
q = string.title() # Всі слова з великої літери
print(q)
q = string.upper() # Всі слова великими літерами
print(q)
q = string.lower() # Всі слова маленькими літерами
print(q)
q = string.swapcase() # Зміна регістру літер
print(q)

'''


