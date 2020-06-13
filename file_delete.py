import shutil, os, pprint

pprint.pprint(os.listdir("C:\\Users\\admin\\Desktop"))
source="C:\\Users\\admin\\Desktop\\Source\\Example.txt"
destination= "C:\\Users\\admin\\Desktop\\Dist\\"

#copy_con=shutil.copyfile(source,destination)                 #To copy content from src
#shutil.rmtree(destination)                                         #To delete  folder

temp_folder = glob.glob('C:\\Users\\admin\\AppData\\Local\\Temp\\**\*.*', recursive=True)
for file in temp_folder:
    try:
        os.remove(file)
    except OSError as e:
        print("Error: %s : %s" % (file, e.strerror))