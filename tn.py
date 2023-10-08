#150
# with open('havayu.txt', 'r') as file:
#     res = file.readlines()
#     res = res[::-1]
#     print(res[0:10])

#155
# def func(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             res = file.read()
#         res = res.replace('\n', ' ')
#         res = res.split(' ')
#         mydict = {i:res.count(i) for i in res}
#         return mydict
#     except FileNotFoundError:
#         print('File not found')
# print(func(input('enter file name:')))


#156
# sum = 0
# while True:
#     tiv = input("Greq tiv: ")
#     try:
#         if tiv == '':
#             print(f"obshi->{sum}")
#             break
#         else:
#             tiv = float(tiv)
#             sum += tiv
#         print(sum)
#     except ValueError:
#         print("Enter True Value[float]")



#158
# def func(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#             res = res.replace('#', '')
#         return res
#     except FileNotFoundError:
#         return 'No file'
# print(func(input('enter file name:')))



# def func(name):
#     try:
#         with open(name,'r') as file:
#             res = file.read()
#         res = res.replace('\n', '')
#         mydict = {i:round((res.count(i) / 26) * 100, 2) for i in res}
#         return mydict
#     except FileNotFoundError:
#         print("file not found")
# print(func(input('enter file name: ')))




