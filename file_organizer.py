import os,shutil
path = r"C:/Users/nexora Technology/New folder (2)/"
file_name= os.listdir(path)
folder_names=[ "csv_files","image files","text files"]
for loop in range (0,3):
    if not  os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.mkdir((path + folder_names[loop]))


for file in file_name:
    if ".csv" in file and not  os.path.exists(path + "csv_files/"+ file):
        shutil.move(path + file,path + "csv_files/"+ file)
    elif ".png" in file and not  os.path.exists(path + "image files/"+ file):
        shutil.move(path + file,path + "image files/"+ file)    
    elif ".txt" in file and not  os.path.exists(path + "text files/"+ file):
        shutil.move(path + file,path + "text files/"+ file)  
  
