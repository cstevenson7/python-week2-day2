# #Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “),
# return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.

# Example Input: “Hello World”
# Example Output: 5
# Example Input 2: “The brown loud cow plowed”
# Example Output 2: 6


# def find_length(str1):
#     word_list =  str1.split(" ")
#     last_word = word_list[-1] # this turns the string into a list, and the last word in the list is [-1]
#     return len(last_word)

# str1 = "Hello World"
# str3 = "The brown loud cow plowed"
# print(find_length(str3))



# authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
# sorted_list = sorted(authors, key=lambda x: x.split()[-1])
# print(sorted_list)

def fibonacci(num):
    if num <= 2:
        return num
    else:
        return num-1 + fibonacci(num-2)
    
print(fibonacci(5))












