import os
from .colorizefolder import set_system_folder, DesktopIni

def command_line(folder_color, info_tip=""):
    this_folder = os.getcwd()
    set_system_folder(this_folder)
    desktop_ini = DesktopIni(folder_color, info_tip)
    desktop_ini.create()

def main():
    fire.Fire(command_line)
