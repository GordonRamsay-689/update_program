import os

# comment

path = __file__.strip('main.py')
print(path)

os.system(f'cd {path}; git pull origin main')
