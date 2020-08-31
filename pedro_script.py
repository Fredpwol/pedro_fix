import os
import time
import shutil as sh
import getpass
import sys
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from  PIL import Image,ImageTk


game_name = "My Friend Pedro - Blood Bullets Bananas.exe"
def_path = os.path.join(os.getcwd(),game_name) if game_name in os.listdir() else os.getcwd()
game_path = ""
user = getpass.getuser()

dest_path = 'C:\\Users\\' + user + '\\AppData\\LocalLow\\DeadToast Entertainment\\My Friend Pedro_ Blood Bullets Bananas\\Save data\\Steam\\76561200452375493'
local_path = 'C:\\Users\\' + user + '\\AppData\\LocalLow\\DeadToast Entertainment\\My Friend Pedro_ Blood Bullets Bananas\\Save data\\Steam'

try:
    game_file = open('PATH','r')
    game_path = game_file.readlines()[0]
    game_file.close()
except :
    pass

def show_error():
    messagebox.showerror(title='PATH Error', message='Error no game FILE found!!!')

def main():
    global game_path
    try:
        if(game_path != def_path) and (not os.path.exists(game_path)):
            game_path = def_path
    except NameError:
        show_error()

    try:
        sh.move(f'{dest_path}\\mfp_save.dat',local_path)
        os.startfile(game_path)
        time.sleep(9)

        if os.path.exists(f'{dest_path}\\mfp_save.dat'):
            os.unlink(f'{dest_path}\\mfp_save.dat')
            
        sh.move(f'{local_path}\\mfp_save.dat',dest_path)

    
    except FileNotFoundError:
       # print(e,'Please input the file PATH to the game using the python pedro_script.py --p "<path to file>"')
        show_error()
    except  FileNotFoundError:
        # print(e,'Please input the file PATH to the game using the python pedro_script.py --p "<path to file>"')
        show_error()
    except:
        if( os.path.exists(f'{local_path}\\mfp_save.dat')):
            sh.move(f'{local_path}\\mfp_save.dat',dest_path)
            os.startfile(game_path)
            time.sleep(9)
            print("Loaded!!")
        
def file_path():
    global game_path
    filepath = filedialog.askopenfilename(initialdir=def_path,title="Select game file",
                filetypes=(('executable','*.exe'),('all files','*.*')))
    with open('PATH','w') as save:
        save.write(filepath)
    game_path = filepath


if __name__ == "__main__":
    button_height = 50
    button_width = 100
    root = tkinter.Tk()
    root.geometry('400x500')
    root.title('My Friend Pedro Fix')
    photo_image = ImageTk.PhotoImage(Image.open('images.jpeg'))
    tkinter.Label(image=photo_image).pack()
    label = tkinter.Label(root,text='My Friend Pedro v1.02 Patch by FreddThink',font=('Algerian',13))
    label.place(relx=0.5,rely=0.2,anchor='n')
    tkinter.Label(text='follow on twitter @FreddThink').place(x=60,y=60)
    path_button = tkinter.Button(root,text='Set File Path',bg='red',command=file_path)
    path_button.place(relx=0.5,rely=0.3,height=button_height,width=button_width,anchor='n')
    open_button = tkinter.Button(root,text='Run Game',bg='red',command=main)
    open_button.place(relx=0.5,rely=0.5,height=button_height,width=button_width,anchor='n')
    root.mainloop()