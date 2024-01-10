"""CATCHING EXCEPTIONS"""

# try:
#     file = open("a_file.txt")
#     dict = {"shiva":"a power"}
#     print(dict["nosuchkey"])
# except FileNotFoundError:
#     # print("there was an error")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The Key {error_message} does not exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed")
#     raise KeyError("THIS IS KEYERROR")




"""271.Raising your own exceptions"""
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height>3:
#     raise ValueError("normal human cannot have height more than 2mts")
#
# bmi = weight/height**2
# print(bmi)

"""272. handling indexerror"""

# fruits = eval(input())
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("FruitPie")
#     else:
#         print(fruit + "pie")
#
# make_pie(2)

"""273. KeyError Handling"""

fb_posts = eval(input())
total_likes = 0
for post in fb_posts:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError:
        pass
print(total_likes)