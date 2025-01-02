# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# Prints the character at index 2
name = "Dubem"
first_name = name[2]
print(first_name)

# Prints the characters at index 2-4
name = "Eneh"
last_name = name[2:4]
print(last_name)

# Prints the characters before index 5
name = "Dubem Eneh"
first_name = name[:5]
print(first_name)

# Prints the characters after index 6
name = "Dubem Eneh"
last_name = name[6:]
print(last_name)

# Prints every third character inlcuding the index 0
name = "Dubem Eneh"
funky_name = name[0:10:3]
print(funky_name)

# Prints every third character inlclduing the index 0(Easier)
name = "Dubem Eneh"
funky_name = name[::3]
print(funky_name)

# Reversing a string in python
name = "Dubem Eneh"
name_backwards = name[::-1]
print(name_backwards)

# Getting just the website name "google"

# Indexing
website = "https://google.com"
website_name = website[8:14:1]
print(website_name)

# Slicing
website = "https://google.com"
website2 = "https://bing.com"
slice = slice(8,-4)
print(website[slice])
print(website2[slice])