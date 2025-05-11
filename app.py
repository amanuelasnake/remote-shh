import tkinter as tk
import subprocess
from tkinter import ttk



def mainwindow():

    global pc_select


#Main Window Initialize
    main = tk.Tk()
    main.wm_attributes('-type', 'splash')


#Main FRAME
    Mframe = ttk.Frame(main, padding=12)
    Mframe.pack(fill=tk.BOTH, expand=True,padx=3)

#Title Bar
    title = ttk.Label(Mframe, text="Remote File Explorer\n(SSH + Terminal)",anchor="center",justify="center")
    title.pack(fill=tk.BOTH, expand=True)


#Select Machine
    pc_select = ttk.Button(Mframe, text="Connection Options", command=lambda:connectwindow())
    pc_select.pack(fill=tk.BOTH,expand=True)

#Quit
    corner_btn = tk.Button(font=1,command=lambda: quitfunc(),padx=0,pady=0,highlightthickness=0,borderwidth=0,foreground='red',text='x',activeforeground="red")
    corner_btn.place(x=1, y=1)
    
#QuitFunc
    def quitfunc():
        print("Quitting....")
        main.quit()
        print("Done")

    main.mainloop()


def connectwindow():

#Remove Button Functionality After 1 Click
    pc_select.config(command=lambda: None)  

#Connection FRAME
    Cframe = ttk.Frame(padding=10)
    Cframe.pack(fill=tk.BOTH,expand=True)

#Username Label + Entry
    userL = ttk.Label(Cframe, text="Username:")
    userE = ttk.Entry(Cframe)

#Hostname Label + Entry
    hostnameL = ttk.Label(Cframe, text="Machine Name:")
    hostnameE = ttk.Entry(Cframe)

#Username Password Label + Entry
    passwordL = ttk.Label(Cframe, text="User Password:")
    passwordE = ttk.Entry(Cframe,show='*')
#Connection Buttonp
    connectnowB = ttk.Button(Cframe, text="Connect Now",command=lambda:open_ssh_terminal(hostnameE.get(), userE.get(),passwordE.get()))


#Packing Order
    userL.pack(fill=tk.BOTH,expand=True)
    userE.pack(fill=tk.BOTH,expand=True)
    hostnameL.pack(fill=tk.BOTH,expand=True)
    hostnameE.pack(fill=tk.BOTH,expand=True)
    passwordL.pack(fill=tk.BOTH,expand=True)
    passwordE.pack(fill=tk.BOTH,expand=True,pady=1)
    connectnowB.pack(fill=tk.BOTH,expand=True,pady=1)


def open_ssh_terminal(hostname, username,ssh_pass):
    
    ssh_command = f"sshpass -p {ssh_pass} ssh {username}@{hostname}"
    
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', ssh_command])


mainwindow()


