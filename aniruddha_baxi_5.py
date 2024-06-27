str= "The quick brown fox Jumps over the lazy dog"

print(str)

print(len(str))

print(str.upper())

print(str.lower())

print(str.title())

print(str[::-1])

str= "The quick brown fox Jumps over the lazy dog"
str_reverse=str[::-1]
print(str_reverse.title())


print(str.count("a"))

print(str.count("the"))

print(str.replace("the", "a"))


str= "The quick brown fox Jumps over the lazy dog"
letter_frequency = {}
for i in str: letter_frequency[i]= str.count(i)
print(letter_frequency) 


people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]
for people,sex,age in zip(people, sex, age): print(f"{people} the {sex} is {age} years old")



