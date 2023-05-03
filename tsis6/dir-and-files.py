import os

# problem 1
# path = "C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\"
# files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# both = [x for x in os.listdir(path)]
# print("Files:")
# print(files)
# print("Directory:")
# print(dirs)
# print("All directories, files:")
# print(both)

# problem 2
# print('Exist:', os.access('C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\', os.F_OK))
# print('Readable:', os.access('C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\', os.R_OK))
# print('Writable:', os.access('C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\', os.W_OK))
# print('Executable:', os.access('C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\', os.X_OK))

# problem 3
# path = "C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\tsis6\\dir-and-files.py"  # Replace with the actual path you want to test
# if os.path.exists(path):
#     print("Path exists.")
#     filename = os.path.basename(path)
#     directory = os.path.dirname(path)
#     print("Filename:", filename)
#     print("Directory:", directory)
# else:
#     print("Path does not exist.")

# problem 4
# with open("test.txt", "r") as f:
#     print(sum(1 for _ in f))

# problem 5
# lista = [123, 23, 53, 23]
# with open('text.txt', 'w') as f:
# 	for i in lista:
# 		f.write('%s\n' % i)
# content = open('text.txt')
# print(content.read())

# problem 6
# list1 = ['A' , 'B' , 'C' , 'D', 'E' , 'F' ,'G' , 'H' ,'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
# for i in list1:
#     files = f"file_{i}.txt"
#     with open(files, "w") as file:
#         file.write('a')

# problem 7 
# from shutil import copyfile
# copyfile('test.txt', 'file_Z.txt')

# problem 8 
# path = 'C:\\Users\\Huawei\\OneDrive\\pp2-22B050872\\'
# if os.access(path, os.F_OK) and (os.path.isfile('delete.txt')):
#    os.remove('delete.txt')
#    print('ok')
# else:
#     print(f'{path} does not exist')