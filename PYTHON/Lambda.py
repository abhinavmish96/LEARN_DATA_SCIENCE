contains_a = lambda word: "a" in word

print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

#Write your lambda function here
long_string = lambda str: len(str) > 12

print long_string("short")
print long_string("photosynthesis")

#Write your lambda function here
ends_in_a = lambda str: str[len(str) -1 ] == 'a'

print ends_in_a("data")
print ends_in_a("aardvark")
