#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jun 22, 2024 04:48:02 PM CEST  platform: Linux

import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)


_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class GUI:
        def __init__(self, window):
                '''This class configures and populates the toplevel window.
                top is the toplevel containing window.'''

                self.input_text = tk.StringVar()
                self.input_text1 = tk.StringVar()
                self.path = ''
                self.frame = ''

                window.geometry("190x245+325+195")
                window.minsize(1, 1)
                window.maxsize(1905, 1050)
                window.resizable(1,  1)
                window.title("")

                self.top = window

                self.Labelframe1 = tk.LabelFrame(self.top)
                self.Labelframe1.place(relx=0.058, rely=0.041, relheight=0.433
                        , relwidth=0.889)
                self.Labelframe1.configure(relief='groove')
                self.Labelframe1.configure(font="-family {Noto Sans} -size 10")
                self.Labelframe1.configure(labelanchor="n")
                self.Labelframe1.configure(text='''Selection du fichier midi''')

                self.Entry_path = tk.Entry(self.Labelframe1)
                self.Entry_path.place(relx=0.065, rely=0.66, height=23, relwidth=0.864
                        , bordermode='ignore')
                self.Entry_path.configure(background="white")
                self.Entry_path.configure(cursor="fleur")
                self.Entry_path.configure(font="-family {DejaVu Sans Mono} -size 10")
                self.Entry_path.configure(selectbackground="#d9d9d9")
                self.Entry_path.configure(textvariable=self.input_text)

                self.Button_Open = tk.Button(self.Labelframe1)
                self.Button_Open.place(relx=0.047, rely=0.283, height=33, width=151
                        , bordermode='ignore')
                self.Button_Open.configure(activebackground="#d9d9d9")
                self.Button_Open.configure(font="-family {Noto Sans} -size 10")
                self.Button_Open.configure(text='''Ouvrir un fichier Midi''')
                self.Button_Open.configure(command=lambda: self.get_mid_file_path())

                self.Button_Validation = tk.Button(self.top)
                self.Button_Validation.place(relx=0.316, rely=0.776, height=33, width=71)
                self.Button_Validation.configure(command=lambda: self.validate())

                self.Button_Validation.configure(activebackground="#d9d9d9")
                self.Button_Validation.configure(cursor="fleur")
                self.Button_Validation.configure(font="-family {Noto Sans} -size 10")
                self.Button_Validation.configure(text='''Valider''')

                self.Labelframe2 = tk.LabelFrame(self.top)
                self.Labelframe2.place(relx=0.053, rely=0.49, relheight=0.224
                        , relwidth=0.895)
                self.Labelframe2.configure(relief='groove')
                self.Labelframe2.configure(font="-family {Noto Sans} -size 10")
                self.Labelframe2.configure(labelanchor="n")
                self.Labelframe2.configure(text='''Nombre de frames''')

                self.Entry_frames = tk.Entry(self.Labelframe2)
                self.Entry_frames.place(relx=0.235, rely=0.364, height=23, relwidth=0.506
                        , bordermode='ignore')
                self.Entry_frames.configure(background="white")
                self.Entry_frames.configure(font="-family {DejaVu Sans Mono} -size 10")
                self.Entry_frames.configure(selectbackground="#d9d9d9")
                self.Entry_frames.configure(textvariable=self.input_text1)
        
        def get_mid_file_path(self):
                self.path = askopenfilename() 
                self.input_text.set(self.path)

        def get_mid_path(self): 
                return self.path

        def get_frame_per_sec(self):
                return self.frame

        def validate(self):
                self.path = self.input_text.get()
                self.frame = self.input_text1.get()
                self.top.destroy()