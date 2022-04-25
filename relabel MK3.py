import os

path= os.chdir("C:\\Users\\admin\\OneDrive\Desktop\Software Question Bank\Physics\HL\Topic 12_ Quantum and nuclear physics\\12.2 Nuclear Physics")
#change file path here

def main():
    i = 1
    for image in os.listdir(path):
        if image[-12] == "_":
            #for 6 characters labels
            new_name= "{}_".format(i) + image[-11:-5] + "_" + image[:-11] + image[-5:]
            
            os.rename(image, new_name)

        elif image[-13] == "_":
            #for 7 characters labels
            new_name= "{}_".format(i) + image[-12:-5] + "_" + image[:-12] + image[-5:]
            
            os.rename(image, new_name)

        else:
            print("Label's outside characters limit")

        i += 1
        #for ordinal numbers

if __name__ == '__main__':
    main()
