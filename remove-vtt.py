import os
directory = '/mnt/0E61114E58069402/courses/REST APIs with Flask and Python'
modules = os.listdir(directory)
for module in modules:
    path = os.path.join(directory, module)
    files = os.listdir(path)
    deleting_files = [file for file in files if file.endswith('.vtt')]
    for file in deleting_files:
        path_to_file = os.path.join(path, file)
        os.remove(path_to_file)