# accept a string and reverse the same

text = input("Enter text: ")

lst = list(text)
lst.reverse()
rev = "".join(lst)


# Using the for loop
# ------------------------------------
# for ch in text:
# 	rev = ch + rev


# Using the while loop
# ------------------------------------
# n = len(text)-1

# while n>=0:
# 	rev += text[n]
# 	n -= 1

print("The reversed input is:", rev)
