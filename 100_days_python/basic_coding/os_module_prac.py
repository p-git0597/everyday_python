# import os

# f = os.open(".\basic_coding\my_file.txt", os.O_RDONLY)
# contents = os.read(f, 1024)
# os.close(f)


import os

if(not os.path.exists("data")):
    os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")
    
