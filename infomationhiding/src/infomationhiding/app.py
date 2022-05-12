"""
Ung dung giau tin trong anh
"""
from logging import PlaceHolder
from PIL import Image
import numpy as np
from ctypes import alignment
from tkinter import CENTER
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class InfomationHiding(toga.App):
    
    
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction = COLUMN))
        

        main_label = toga.Label("Insert image or Image's URL:")
        self.image_url = toga.TextInput(style=Pack(flex=1, padding = (5,0)))
        
        select_button = toga.Button("Select File",on_press=self.button_handler,
        style=Pack(
            width=200, 
            padding = (5,0), 
            height = 40,
            background_color = "#359061"))
        
        select_box = toga.Box(style=Pack(direction=COLUMN, padding=10,  alignment = CENTER))
        select_box.add(main_label)
        select_box.add(self.image_url)
        select_box.add(select_button)

        text_label = toga.Label("Insert text:")
        self.text_input = toga.TextInput(style=Pack(flex=1, padding = (5,0)))

        text_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        text_box.add(text_label)
        text_box.add(self.text_input)

        encoding_button  = toga.Button("Encoding",on_press=self.encoding,
        style=Pack(
            flex=1,
            padding_right = 5,
            height = 40,
            background_color = "#FCC937"))
        decoding_button  = toga.Button("Decoding",on_press=self.decoding,
        style=Pack(
            flex=1,
            height=40,
            background_color="#9BAB30"))
        
        button_box = toga.Box(style=Pack(direction = ROW,padding = 10))
        button_box.add(encoding_button)
        button_box.add(decoding_button)

        result_box = toga.Box(style=Pack(direction = ROW,padding = 10))
        result_label = toga.Label("Status:")
        self.result_text = toga.Label ("pending...",style=Pack(flex=1))
        result_box.add(result_label)
        result_box.add(self.result_text)

        reset_button = toga.Button("Reset",on_press=self.reset, 
        style=Pack(
            flex=1,
            padding = 10,
            height=40,
            background_color="#C24F3A"))

        main_box.add(select_box)
        main_box.add(text_box)
        main_box.add(button_box)
        main_box.add(result_box)
        main_box.add(reset_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_handler(self,widget):
         try:
              # selected_file = list(widget.window.open_file_dialog('Select Files', multiselect=True))
              selected_file = widget.window.open_file_dialog('Select Files', multiselect=False)
         except ValueError:
              self.image_url.value= "No file select"
         else:
              self.image_url.value = selected_file  

    def encoding (self,widget):
         if self.image_url.value == "" or self.text_input.value == "":
            self.result_text.text = "Error! Must be filled out completely!"
         else:   
            msg=self.text_input.value+"$"
            bit_msg = ''.join([format(ord(i), "08b")for i in msg])
            print(bit_msg)
            Sopixcan = len(bit_msg)
            
            org_img = Image.open(self.image_url.value,'r')
            w,h = org_img.size
            arr = np.array(list(org_img.getdata()))
            SumPix = arr.size//3

            i=0
            StartPix=0
            for p in range(SumPix) :
                for q in range(0,3) :
                    if i < Sopixcan :
                        arr[StartPix+p][q] = int(bin(arr[StartPix+p][q])[2:9]+bit_msg[i],2)
                        i+=1
            arr = arr.reshape(w,h,3)
            new_img = Image.fromarray(arr.astype('uint8'), org_img.mode)   #mode="RBG"
            new_img.save("encrypted_image.png")
            self.result_text.text = "Encoding Success!"
            # Display the image
            new_img.show()  
            new_img.close()

    def decoding (self,widget):    
         if self.image_url.value == "":
            self.result_text.text = "Error! Select file first!"
         else:   
            org_img = Image.open(self.image_url.value,'r')
            arr = np.array(list(org_img.getdata()))
            SumPix = arr.size //3
            src_bits=""
            StartPix = 0
            for p in range(SumPix) :
                for q in range(0,3) :
                    src_bits = src_bits + (bin(arr[StartPix+p][q])[2:][-1])
            src_bits = [src_bits[i:i+8] for i in range(0, len(src_bits), 8)]

            msg = ""
            for i in range(len(src_bits)):
                if msg[-1:] == "$":
                    break
                else:
                    msg = msg + chr(int(src_bits[i], 2))
            nmsg = ""
            for i in range(len(msg)-1):
                nmsg = nmsg + msg[i]
            print(nmsg)
            self.result_text.text = "Decoding Success! Message is: " + nmsg;
    
    def reset(self,widget):
         self.image_url.value=""
         self.text_input.value=""
         self.result_text.text = "pending..."


def main():
    return InfomationHiding()
