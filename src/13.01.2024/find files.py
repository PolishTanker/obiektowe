import os

dir_ = '.'
for f in os.listdir(dir_):
    full_f = os.path.join(dir_, f)
    if os.path.isfile(full_f):
        print(f)
    if os.path.isdir(full_f):
        print('DIR', f)