import os
import zipfile
import shutil
path_from = "D:\\python\\Attendance_system_4th_year\\Temporary\\"
path_to = "E:\\refined datasets\\"

for i in os.listdir():
    pf = os.path.join(path_from,i)
    if pf.endswith('.zip'):
        with zipfile.ZipFile(pf, 'r') as zip_ref:
            os.chdir(path_to)
            folder_name = i[:-4]
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            pt = os.path.join(path_to,folder_name)
            os.chdir(pt)
            zip_ref.extractall()
            zip_ref.close()
            
            source = "D:\\python\\Attendance_system_4th_year\\Temporary\\{}".format(i)
            destination = "D:\\python\\Attendance_system_4th_year\\Temporary\\Done"
            
            shutil.move(source, destination)
            print("Done")
