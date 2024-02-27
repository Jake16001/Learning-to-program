# fourth program made | on my own
language = str(input("Can you speak English, Chinese, or French?: "))
unit = input("Which one?: ")

if unit.upper() == "ENGLISH" or unit.upper() == "E":
    print("You speak English? How boring! Go learn a new language you scallywag!")
elif unit.upper() == "CHINESE" or unit.upper() == "C":
    print("Chinese is a cool language. Especially the characters; it's like an art!")
elif unit.upper() == "FRENCH" or unit.upper() == "F":
    print("French is a cool language. It sounds fancy!")
elif unit.upper() == "ALL" or unit.upper() == "A":
    print("Dang, you can speak all!? That's quite impressive!")
