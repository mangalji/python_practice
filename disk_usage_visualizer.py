# import os.path
# import sys

# filelists = []

# path = input("~/Desktop/python")

# for path, subdir, files in os.walk(path):
#   for name in subdir:
#       print(os.path.join(path,name))
#   for name in files:
#       print(os.path.join(path,name))

# # for root in os.walk('~/Desktop/python'):
# #     print(root)
# #     for dir_ in root:
# #         for files in dir_:
# #             filelists.append(files)

# # print(filelists)


# from os.path import join, getsize
# for root, dirs, files in os.walk('home/raj/Desktop/python/disk_usage_visualizer.py'):
#   print(root,"consumes",end=" ")
#   print(sun(getsize(join(root,name)) for name in files), end=" ")
#   print("bytes in", len(files), "non-directory files")
#   if '__pycache__' in dirs:
#       dirs.remove('__pycache__')

# from pathlib import Path

# path = Path("/home/raj/Desktop/python/disk_usage_visualizer.py")
# relative = Path("disk_usage_visualizer.py")
# base = Path("/home/raj/Desktop/python")

# for root, dirs, files in os.walk("/home/raj/Desktop/python"):
#   print("Current Directory:",root)
#   print("Sub-directories:",dirs)
#   print("Files:",files)
#   print("-"*30)

# from pathlib import Path

# p = Path("/home/raj/Desktop/python")

# for item in p.iterdir():
#   print(item)
# print('-----------------')

# for file in p.rglob("*"):
#   print(file)
import os


path = "/home/raj/Desktop"

def folder_sizes_func(path):
    # size=0
    folder_size = {}
    import ipdb; ipdb.set_trace()
    for root, dirs, files in os.walk(path):
        # print(root)
        # print(dirs)
        # print(files)
        if any(extra_files in root for extra_files in['.venv','.git','__pycache__','lib','Javascript']):
            continue
        ipdb.set_trace()
        folder_name = os.path.relpath(root,path)
        # print(folder_name)
        # break

        size = 0
        
        for file in files:
            file_path = os.path.join(root,file)
            if os.path.isfile(file_path):
                size = size + os.path.getsize(file_path)
            # print(size)

        folder_size[folder_name] = size
        # print(folder_size)
        # break

    # return size
    return folder_size

result = folder_sizes_func(path)
# print(result)

sorted_result = sorted(result.items(),key=lambda item: item[1], reverse=True)
# print(sorted_result)

for folder, size in sorted_result:
    print(f"{folder}  {size//1024} KB") 

