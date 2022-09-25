from dataclasses import field
from tkinter import RIDGE, ttk, Tk, PhotoImage, RIDGE, GROOVE

class FrontEnd:
    def __init__(self, master):
        self.master = master
        ################# Header Code ############################
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        # self.logo = PhotoImage(file="header.jpg").subsample(5,5)
        # print(self.logo)
        ttk.Label(self.frame_header, text="Welcome to the Image Editor App!").grid(row=0, column=1)
        ttk.Label(self.frame_header, text="Upload, edit and save your iamges Easily!").grid(row=1, column=1)
        ################## Main Frame Code ########################
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        ttk.Button(self.frame_menu, text="Upload An Image",command=self.upload_action).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Crop Image",command=self.crop_action).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Add Text",command=self.text_action_1).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Draw Over Image",command=self.draw_action).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Apply Filters",command=self.filter_action).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Blur/Smoothing",command=self.blur_action).grid(row=5, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Adjust Levels",command=self.adjust_action).grid(row=6, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Rotate",command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5)
        ttk.Button(self.frame_menu, text="Flip",command=self.flip_action).grid(row=8, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Save As",command=self.save_action).grid(row=9, column=0, padx=5, pady=5)

        ################Footer Frame ##########################
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()

        ttk.Button(self.apply_and_cancel, text="Apply", command=self.apply_action).grid(row=0, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.apply_and_cancel, text="Cancel",command=self.crop_action).grid(row=0, column=1, padx=5, pady=5, sticky='sw')
        ttk.Button(self.apply_and_cancel, text="Revert All Changes", command = self.revert_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')

    #Main Frame Functions
    def upload_action(self):
        pass
    
    def crop_action(self):
        pass
    
    def text_action_1(self):
        pass

    def draw_action(self):
        pass

    def filter_action(self):
        pass

    def blur_action(self):
        pass

    def adjust_action(self):
        pass

    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def save_action(self):
        pass 
    
    #Footer Frame Functions
    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        pass

root = Tk()
FrontEnd(root)
root.mainloop()