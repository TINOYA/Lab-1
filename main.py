#Задание 1


# RED = '\u001b[41m'
# BLUE = '\u001b[44m'
# BLACK = '\u001b[30m'
# WHITE = '\u001b[47m'
# GREY = '\u001b[30;1m'
# END = '\u001b[0m'


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











#  ЗАДАНИЕ 3 ГРАФИК ФУНКЦИИ x^2


# COMA = '@'
# SPACE= "*"

# if __name__ == '__main__':
 
    
#     for i in range(10, 0, -1):
#         if i==10:
#             print(i**2,f'{SPACE*18}{COMA*2}')
#         elif i==9:
#             print(i**2,f'{SPACE*17}{COMA*2}{SPACE*2}')
#         elif i==8:
#             print(i**2,f'{SPACE*15}{COMA*2}{SPACE*4}')
#         elif i==7:
#             print(i**2,f'{SPACE*13}{COMA*2}{SPACE*6}')
#         elif i==6:
#             print(i**2,f'{SPACE*11}{COMA*2}{SPACE*8}')
#         elif i==5:
#             print(i**2,f'{SPACE*9}{COMA*2}{SPACE*10}')
#         elif i==4:
#             print(i**2,f'{SPACE*6}{COMA*2}{SPACE*13}')
#         elif i==3:
#             print(i**2,f'{SPACE*5}{COMA*2}{SPACE*15}')
#         elif i==2:
#             print(i**2,f'{SPACE*3}{COMA*2}{SPACE*17}')
#         else:
#             print(i**2,f'{SPACE}{COMA*2}{SPACE*19}')
#     print(0," ",1,2,3,4,5,6,7,8,9,10)







#  ЗАДАНИЕ 4 ДИАГРАММА ПРОЦЕНТНОГО СООТНОЩЕНИЯ: Количество чисел меньше и больше 0 







# with open('sequence.txt') as fh:
#     paper = []
#     for chislo in fh:
#         if chislo!=0:
#             paper.append(float(chislo))
#             print (paper)
# print ('Количество чисел меньше и больше 0:', len(paper))