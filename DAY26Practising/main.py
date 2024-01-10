# numbers = [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
# new_num = [num**2 for num in numbers]
# print(new_num)
#
# even_num = [num for num in numbers if num%2 == 0]
# print(even_num)

# with open("file1.txt") as file1:
#     file1_num = file1.readlines()
#     print(file1_num)
#
# with open("file2.txt") as file2:
#     file2_num = file2.readlines()
#     print(file2_num)
#
# result = [int(num) for num in file1_num if num in file2_num]
# print(result)

# sentence = input()
# print(sentence.split())
#
# # result = {print(word) for word in sentence.split()}
# result = {word:len(word) for word in sentence.split()}
# print(result)


# sentence = "what is the price of new XUV700"
# result = {word: len(word) for word in sentence.split()}
# print(result)



# temp_f = {"Monday": 42, "Tuesday": 40, "Wednesday": 41,"Thursday": 39,"Friday": 35,"Saturday": 38,"Sunday": 37}
# temp_c = {"Monday": 12,"Tuesday": 14,"Wednesday": 15,"Thursday": 14,"Friday": 21,"Saturday": 22,"Sunday": 24}

# weather_c = eval(input())
# weather_f = {}
# print(weather_c.items())
# weather_f = (print(day, temp) for (day, temp) in weather_c.items())
# print(weather_f)
# weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)


import pandas

student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(key, value) in student_data_frame.items():
    print(value)
    print(key)
#
for (index, row) in student_data_frame.iterrows():
    print(index)
    if row.student == "angela":
        print(row.score)
