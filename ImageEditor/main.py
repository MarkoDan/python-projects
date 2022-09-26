from audioop import lin2adpcm
from dataclasses import field
from tkinter import HORIZONTAL, RIDGE, Canvas, Scale, filedialog, ttk, Tk, PhotoImage, RIDGE, GROOVE, colorchooser, ROUND
from turtle import title
import cv2
from PIL import Image, ImageTk
import numpy as np

class FrontEnd:
    def __init__(self, master):
        self.master = master
        ################# Header Code ############################
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        # self.logo = PhotoImage(file="header.jpg").subsample(5,5)
        # print(self.logo)
        self.master.geometry('750x630+250+10')
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
        ##########Canvas##############
        self.canvas = Canvas(self.frame_menu, bg="gray", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)

        ##########Side Frame##########
    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass
        
        # self.canvas.unbind("<ButtonPress>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease>")
        # self.display_image(self.edited_image)
        
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))
    
    
    

    #Main Frame Functions
    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filter_image = cv2.imread(self.filename)

        self.display_image(self.original_image)

    def crop_action(self):
        self.rectagle_id = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>",self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)    
    
    def start_crop(self,event):
        self.crop_start_x = event.x
        self.crop_end_y = event.y

    def crop(self,event):
        if self.rectagle_id:
            self.canvas.delete(self.rectagle_id)
        
        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectagle_id = self.canvas.create_rectangle(self.crop_start_x, self.crop_end_y, self.crop_end_x, self.crop_end_y, width=1)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        
        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.filtered_image = self.edited_image[y, x]
        self.display_image(self.filtered_image)
    
    def text_action(self):
        self.rectagle_id = 0
        self.crop_start_x = 0
        self.crop_end_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)

    def draw_action(self):
        self.color_code = ((255,0,0), '#ff0000')
        self.refresh_side_frame()
        self.canvas.bind("<ButtonPress>",self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.draw_color_button = ttk.Button(self.side_frame, text="Pick a Color", command=self.choose_color)
        self.draw_color_button.grid(row=0, column=2, padx=5, pady=5, sticky='sw')

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Choose color")
    
    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []
    
    def draw(self,event):
        print(self.draw_ids)
        self.draw_ids.append(self.canvas.create_line(self.x, self.y, self.x, event.y, width=2, fill=self.color_code[-1], capstyle=ROUND, smooth=True ))

        cv2.line(self.filter_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
        (int(event.x * self.ratio), int(event.y * self.ration)),
        (0, 0, 255), thickness=int(self.ratio * 2),
        lineType=8)

        self.x = event.x
        self.y = event.y
    
    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(self.side_frame, text="Negative", command=self.negative_action).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.side_frame, text="Black And White", command=self.bw_action).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(self.side_frame, text="Stylisation", command=self.stylisation_action).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=3, column=2, padx=5, pady=5)
        ttk.Button(self.side_frame, text="Emboss", command=self.emb_action).grid(row=4, column=2, padx=5, pady=5)
        ttk.Button(self.side_frame, text="Sepia", command=self.sepia_action).grid(row=5, column=2, padx=5, pady=5)    
        ttk.Button(self.side_frame, text="Binary Thresholding", command=self.binary_threshold_action).grid(row=6, column=2, padx=5, pady=5, sticky="sw")
        ttk.Button(self.side_frame, text="Erosion", command=self.erosion_action).grid(row=7, column=2, padx=5, pady=5, sticky="sw")
        ttk.Button(self.side_frame, text="Dilation", command=self.negative_action).grid(row=8, column=2, padx=5, pady=5, sticky="sw")

    def blur_action(self):
        self.refresh_side_frame()

        ttk.Label(self.side_frame, text="Averaging Blur").grid(row=0, column=2, padx=5, sticky="sw")
        self.average_slider = Scale(self.side_frame, from_ = 0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5, sticky='sw')

        ttk.Label(self.side_frame, text="Gausian Blur").grid(row=2, column=2, padx=5, sticky='sw')
        self.gaussian_slider = Scale(self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3, column=2, padx=5, sticky='sw')

        ttk.Label(self.side_frame, text="Median Blur").grid(row=4, column=2, padx=5, sticky='sw')
        self.median_slider = Scale(self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5, column=2, padx=5, sticky='sw')

    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5, sticky='sw')
        self.brightness_slider = Scale(self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5, sticky='sw')

        ttk.Label(self.side_frame, text="Saturation").grid(row=2, column=2, padx=5, pady=5, sticky='sw')
        self.saturation_slider = Scale(self.side_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL, command=self.saturation_action)
        self.saturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
        self.saturation_slider.set(0)

    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(self.side_frame, text="Rotate Left", command=self.rotate_left_action).grid(row=0, column=2, padx=5)
        ttk.Button(self.side_frame, text="Rotate Right", command=self.rotate_right_action).grid(row=1, column=2, padx=5)

    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(row=0, column=2, padx=5)
        ttk.Button(self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(row=1, column=2, padx=5)
    def save_action(self):
        pass 
    
    #Footer Frame Functions
    def apply_action(self):
        self.edited_image = self.filtered_image
        self.display_image(self.edited_image)

    def cancel_action(self):
        self.display_image(self.edited_image)

    def revert_action(self):
        self.edited_image = self.original_image.copy()
        self.display_image(self.original_image)




    #########Action Functions##################
    def negative_action(self):
        self.filter_image = cv2.bitwise_not(self.edited_image)
        self.display_image(self.filter_image)
    def bw_action(self):
        self.filter_image = cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filter_image = cv2.cvtColor(self.filter_image, cv2.COLOR_BAYER_BG2BGR)
        self.display_image(self.filter_image)
    def sepia_action(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filter_image)
        
    def sketch_action(self):
        ret, self.filtered_image = cv2.pencilSketch(self.edited_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
        self.display_image(self.filter_action)
    def stylisation_action(self):
        self.filter_image = cv2.stylization(self.edited_image, sigma_s=150, sigma_r=0.25)
        self.display_image(self.filter_image)
    def emb_action(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)
    def erosion_action(self):
        kernel = np.ones((5,5), np.uint8)
        self.filtered_image = cv2.erode(self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)
    def dilation_action(self):
        kernel = np.ones((5,5), np.uint8)
        self.filtered_image = cv2.dilate(self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)
    def binary_threshold_action(self):
        ret, self.filtered_image = cv2.threshold(self.edited_image, 127, 255, cv2.THRESH_BINARY)
        self.display_image(self.filtered_image)


    def averaging_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.blur(self.edited_image, (value, value))
        self.display_image(self.filtered_image)
    def median_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.medianBlur(self.edited_image, value)
        self.display_image(self.filtered_image)
    def gaussian_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.GaussianBlur(self.edited_image, (value, value), 0)
        self.display_image(self.filtered_image)
    
    def rotate_left_action(self):
        self.filtered_image = cv2.rotate(self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.display_image(self.filtered_image)
    
    def rotate_right_action(self):
        self.filtered_image = cv2.rotate(self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)
    
    def vertical_action(self):
        self.filtered_image = cv2.flip(self.edited_image, 0)
        self.display_image(self.filtered_image)
    
    def horizontal_action(self):
        self.filtered_image = cv2.flip(self.edited_image, 2)
        self.display_image(self.filtered_image)

    def brightness_action(self, value):
        self.filtered_image = cv2.convertScaleAbs(self.edited_image, alpha=self.brightness_slider.get())
        self.display_image(self.filtered_image)
        
    
    def saturation_action(self, event):
        self.filtered_image = cv2.convertScaleAbs(self.edited_image, alpha=1, beta=self.saturation_slider.get())
        self.display_image(self.filtered_image)

    def display_image(self, image=None):
        #Destroys the old canvas
        self.canvas.delete("all")
        #If image is not passed, we are going to show the recent edited_image
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image
        
        #Converting BGR color scheme for tkinter canvas to render the image properly
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_heigth = height
        #If the image size is greater than the canvas, we are assigning new height and width to the image
        if height > 400 or width > 300:
            if ratio < 1:
                new_width = 300
                new_heigth = int(new_width * ratio)
            else:
                new_heigth = 400
                new_width = int(new_heigth * (width / height))
        
        self.ratio = height / new_heigth
        #Resizing the image to new height and width
        self.new_image = cv2.resize(image, (new_width, new_heigth))

        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_heigth)
        self.canvas.create_image(new_width / 2, new_heigth / 2, image=self.new_image)
        
    
   
root = Tk()
FrontEnd(root)
root.mainloop()