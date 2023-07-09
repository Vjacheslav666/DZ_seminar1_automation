from my_library_and_files import print_text as pt
from my_library_and_files import functional_menu as mfm

def main_menu():
    print(pt.greeting_user())
    print(pt.main_menu_text())
    print(pt.list_of_tasks())
    mfm.functional()