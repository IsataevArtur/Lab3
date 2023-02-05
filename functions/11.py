def func(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string == string[::-1]

string = input()
print(func(string))