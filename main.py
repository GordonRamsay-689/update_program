import os


path = __file__.strip('main.py')
print(path)


def git():
    os.system(f'cd {path}; git pull origin main')

def wget():
    os.system(f"cd {path}; wget -P {path} https://github.com/GordonRamsay-689/update_program/archive/refs/heads/main.zip; unzip {path}/main.zip; mv update_program-main/* ./;rm -r update_program-main")

wget()
