import shutil, os, pprint
import glob

pprint.pprint(os.listdir("C:\\Users\\admin\\Desktop"))
source="C:\\Users\\admin\\Desktop\\Source\\Example.txt"
destination= "C:\\Users\\admin\\Desktop\\Dist\\"

#copy_con=shutil.copyfile(source,destination)             #To copy content from source
#shutil.rmtree(destination)                               #To delete  folder

temp_folder = glob.glob('C:\\Users\\admin\\AppData\\Local\\Temp\\**\*.*', recursive=True)
for file in temp_folder:
    #Exception Handling
    try:
        os.remove(file)
    except OSError as e:
        print("Error: %s : %s" % (file, e.strerror))
