#Задание 1


RED = '\u001b[41m'
BLUE = '\u001b[44m'
BLACK = '\u001b[30m'
WHITE = '\u001b[47m'
GREY = '\u001b[30;1m'
END = '\u001b[0m'


# for i in range(6):
#     if i==0:
#         print(f'{BLUE}{"  "*4} {WHITE}{"  "*4} {RED}{"  "*4}{END}')
#     elif i==1:
#         print(f'{BLUE}{"  " * (2+2*i)} {WHITE}{"  " * (2+2*i)} {RED}{"  " *(2+2*i)}{END}')
#     elif i==2:
#         print(f'{BLUE}{"  "* (8- (2*i))} {WHITE}{"  "*(8- (2*i))} {RED}{"  "*(8- (2*i))}{END}')
#     elif i==3:
#         print(f'{BLUE}{"  "*(10- (2*i))} {WHITE}{"  "*(10- (2*i))} {RED}{"  "*(10- (2*i))}{END}')
#     elif i==4:
#         print(f'{BLUE}{"  "*(12- (2*i))} {WHITE}{"  "*(12- (2*i))} {RED}{"  "*(12- (2*i))}{END}')
#     else :
#         print(f'{BLUE}{"  "*(14- (2*i))} {WHITE}{"  "*(14- (2*i))} {RED}{"  "*(14-(2*i))}{END}')

        





# Задание 2 УЗОР



# for i in range(9):
#     if i==0:
#         print(f'{RED}{"  "*4}{WHITE}{"  "*4}',f'{RED}{"  "*4}{END}')
#     elif i==1:
#         print(f'{RED}{"  "*(6-(2*i))}{WHITE}{"  "* (6-(2*i))}',f'{RED}{"  "*(6-(2*i))}{END}')
#     elif i==2:
#         print(f'{RED}{"  "*((8-2*i))}{WHITE}{"  "* (8-(2*i))}',f'{RED}{"  "*(8-(2*i))}{END}')
#     elif i==3:
#         print(f'{WHITE}{"  "*((10-2*i))}{RED}{"  "* (10-(2*i))}',f'{WHITE}{"  "*(10-(2*i))}{END}')
#     elif i==4:
#         print(f'{WHITE}{"  "*((12-2*i))}{RED}{"  "* (12-(2*i))}',f'{WHITE}{"  "*(12-(2*i))}{END}')
#     elif i==5:
#         print(f'{WHITE}{"  "*((14-2*i))}{RED}{"  "* (14-(2*i))}',f'{WHITE}{"  "*(14-(2*i))}{END}')
#     elif i==6:
#          print(f'{RED}{"  "*((16-2*i))}{WHITE}{"  "* (16-(2*i))}',f'{RED}{"  "*(16-(2*i))}{END}')
#     elif i==7:
#          print(f'{RED}{"  "*((18-2*i))}{WHITE}{"  "* (18-(2*i))}',f'{RED}{"  "*(18-(2*i))}{END}')
#     else:
#          print(f'{RED}{"  "*((20-2*i))}{WHITE}{"  "* (20-(2*i))}',f'{RED}{"  "*(20-(2*i))}{END}')











# ЗАДАНИЕ 3 ГРАФИК ФУНКЦИИ x^2


plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]
for i in range(10):
    result[i] = i ** 3
step = round(abs(result[0] - result[9]) / 9, 2)
print(step)
for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step
for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1
for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')







# # for i in range(10):
# #     print(plot_list[i])
# #     pass
# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# print(list)