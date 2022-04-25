import os

source= r'C:\\Users\\admin\OneDrive\Desktop\IB Bio\\Topic 6 - Human Physiology'

SL_dest= r'C:\\Users\\admin\OneDrive\Desktop\\Bio SL' + "\\"
HL_dest= r'C:\\Users\\admin\OneDrive\Desktop\\Bio HL' + "\\"


def moveFile():
    for path , dir, files in os.walk(source):
        if files:
            for file in files:
                if file[9] == "S" or file[10] == "S" or file[11] == "S":
                    os.rename(path + '\\' + file, SL_dest + file)
                else:
                    os.rename(path + '\\' + file, HL_dest + file)
                    

moveFile()
