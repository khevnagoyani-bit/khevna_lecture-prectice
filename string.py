# python string manipulation

S1 = 'Hello'
S2 = "world"
S3 = '''multiline
string'''
S4 = r"Raw \n String"

print(S1)
print(S2)
print(S3)
print(S4)

# Common string methad

S = " Hello, world!"

print (S.upper())
print (S.lower())
print (S.split())
print (S.endswith("!"))
print (S.startswith("H"))
print (S.find("Hello"))
print (S.count("l"))

# syting formatting

name = "alic"
age = 30

# f -string

print(f"name: {name}, age:{age}")

# slicing

S = "hello , python !!"

print(S[0])
print(S[9])
print(S[0:5])
print(S[::-1])

# joinig and spliting in python

words= "hello"

print (" ".join(words))
print ("_".join(words))

splits = "a,b,c"

print (splits.split(","))
