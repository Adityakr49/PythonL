'''
Method	        Description
capitalize()	Converts the first character of a string to uppercase.
lower()	        Converts all characters of a string to lowercase.
upper()	        Converts all characters of a string to uppercase.
title()	        Converts the first character of each word in a string to uppercase.
swapcase()	    Inverts the case of all characters in a string.
strip()	        Removes whitespace characters from the beginning and end of a string.
rstrip()	    Removes whitespace characters from the end of a string.
lstrip()	    Removes whitespace characters from the beginning of a string.
join(iterable)	Concatenates all strings in an iterable (e.g., list or tuple)
                into a single string using the calling string as the separator.
split([separator[, maxsplit]])	Splits a string into a list of substrings at each
                occurrence of the specified separator. The maxsplit argument can be used to
                specify the maximum number of splits to make.
splitlines([keepends])	Splits a string into a list of lines at line breaks. The keepends
                argument can be used to determine whether to keep the line break characters
                in the resulting list.
replace(old, new[, count])	Replaces all occurrences of the old substring with the new substring
                in a string. The count argument can be used to specify the maximum number of
                replacements to make.
startswith(prefix[, start[, end]])	Determines whether a string starts with the specified prefix.
                The start and end arguments can be used to specify the substring to search.
endswith(suffix[, start[, end]])	Determines whether a string ends with the specified suffix.
                The start and end arguments can be used to specify the substring to search.
find(sub[, start[, end]])	Searches a string for the specified substring and returns the lowest
                index at which it occurs. If the substring is not found, -1 is returned. The start
                and end arguments can be used to specify the substring to search.
'''

name="Aditya"
print(len(name))
print(name.find("d"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("i"))
print(name.replace("d","i"))
print(name*3)