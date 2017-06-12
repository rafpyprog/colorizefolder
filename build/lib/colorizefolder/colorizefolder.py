#http://www.thewindowsclub.com/desktop-ini-file-windows

import os
from pkg_resources import resource_filename
import subprocess

import fire

def set_system_folder(folder_name):
    p = subprocess.run(['attrib', '+s', folder_name], check=True)
    return p

class DesktopIni():
    def __init__(self, folder_color, icon_set="default", info_tip="", icon_index=0,
                 confirm_file_op=0):
        ''' Creates de desktop.ini file to customize the folder.

        ConfirmFileOp – Set this to 0, and you won’t get the warning You Are
                        Deleting a System Folder while deleting/moving the
                        desktop.ini file.

        folder_color – Set it to 'blue', 'green', 'yellow' or 'red' to change
                       the color of the folder's icon.

        IconIndex – If you’re setting a custom icon for the underlying folder,
                    you need to set this entry as well. Set it to 0 if there
                    is only one icon file in the file specified for IconFile
                    attribute.

        InfoTip – Set a text string which can be used as an Informational Tip
                  about the folder. If you set this entry  to  a  text string
                  and then hover the cursor over the folder, the  text string
                  stored in the desktop.ini file is displayed there.
        '''

        self.data = {"ConfirmFileOp": confirm_file_op,
                     "IconFile": self.get_icon(icon_set, folder_color),
                     "IconIndex": icon_index,
                     "InfoTip": info_tip}

    def create(self):
        ''' Writes the cutstom settings to the desktop.ini file inside the
        folder '''
        with open('desktop.ini', 'w') as ini:
            # ShellClassInfo initializes the system property which allows you
            # to customize the underlying folder
            ini.write("[.ShellClassInfo]\n")
            for i in self.data:
                ini.write(i + '=' + str(self.data[i]) + '\n')

    def get_icon(self, icon_set, color):
        MODULE = 'colorizefolder'
        icon_file = 'icons/{}-{}.ico'.format(icon_set, color)
        icon_path = resource_filename(MODULE, icon_file)
        return icon_path


def command_line(folder_color, icon_set="default", info_tip=""):
    this_folder = os.getcwd()
    set_system_folder(this_folder)
    desktop_ini = DesktopIni(folder_color, icon_set, info_tip)
    desktop_ini.create()

def main():
    fire.Fire(command_line)

if __name__ == "__main__":
    main()
