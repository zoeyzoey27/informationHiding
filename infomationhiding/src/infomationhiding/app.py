"""
Ung dung giau tin trong anh
"""
from logging import PlaceHolder
from tkinter.tix import AUTO
from turtle import width
from PIL import Image
import numpy as np
from ctypes import alignment
from tkinter import CENTER
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import math


class InfomationHiding(toga.App):
    
    
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction = COLUMN))
        
        title = toga.Label("INFORMATION HIDING", 
        style=Pack(
            flex=1, 
            direction=ROW, 
            font_size=25, 
            text_align = CENTER,
            padding_top = 20,
            color = "#008080"))
        view = toga.ImageView(id="view", image = "C:\\Users\\Admin\\beeware\\infomationhiding\\logo_ct.png",style=Pack(flex =1, width = 150, height = 150, padding = (20,250)))
       
        encoding_button  = toga.Button("Encrypt your information",on_press=self.openWindowEncode,
        style=Pack(
            flex=1,
            padding = (0,100,10,100),
            height = 40,
            background_color = "#F0F8FF",
            font_size=9))
        decoding_button  = toga.Button("Decrypt your information",on_press=self.openWindowDecode,
        style=Pack(
            flex=1,
            padding_left = 100,
            padding_right = 100,
            height=40,
            background_color="#B0C4DE",
            font_size=9))
        
        main_box.add(title)
        main_box.add(view)
        main_box.add(encoding_button)
        main_box.add(decoding_button)
        
        self.main_window = toga.MainWindow(title='Home')
        self.main_window.content = main_box
        self.main_window.show()

    def button_handler(self,widget):
         try:
              # selected_file = list(widget.window.open_file_dialog('Select Files', multiselect=True))
              selected_file = widget.window.open_file_dialog('Select Files', multiselect=False)
         except ValueError:
              self.main_window.error_dialog('Dialog','Error! No file selected!')
         else:
              self.image_url.value = selected_file 
    

    def openWindowEncode (self,widget):
        encode_box = toga.Box(style=Pack(direction = COLUMN, padding = 20))

        title = toga.Label("Encrypt your information", 
        style=Pack(
            flex=1, 
            direction=ROW, 
            font_size=18, 
            text_align = CENTER,
            padding_bottom = 20,
            color = "#008080"))
        
        main_label = toga.Label("Insert image or Image's URL:",style=Pack(font_size=9))
        self.image_url = toga.TextInput(style=Pack(flex=1, padding = (5,0),font_size=9))
        
        select_button = toga.Button("Select file",on_press=self.button_handler,
        style=Pack(
            flex=1, 
            padding = (5,0), 
            height = 40,
            font_size = 9,
            background_color = "#B0C4DE"))
        
        select_box = toga.Box(style=Pack(direction=COLUMN, padding=(10,0),  alignment = CENTER))
        select_box.add(main_label)
        select_box.add(self.image_url)
        select_box.add(select_button)

        text_label = toga.Label("Insert text:",style=Pack(font_size=9))
        self.text_input = toga.TextInput(style=Pack(flex=1, padding = (5,0),font_size=9))

        text_box = toga.Box(style=Pack(direction=COLUMN, padding=(10,0)))
        text_box.add(text_label)
        text_box.add(self.text_input)

        key_label = toga.Label("Enter keys:",style=Pack(font_size=9))
        key_input_box = toga.Box(style=Pack(direction=ROW, padding=(10,0)))
        self.key_input_1 = toga.TextInput(style=Pack(flex=1, padding_top=5, padding_bottom = 5, padding_right=10,font_size=9))
        self.key_input_2 = toga.TextInput(style=Pack(flex=1, padding = (5,0),font_size=9))
        key_input_box.add(self.key_input_1)
        key_input_box.add(self.key_input_2)
        
        key_box = toga.Box(style=Pack(direction=COLUMN, padding=(10,0)))
        key_box.add(key_label)
        key_box.add(key_input_box)

        encoding_button  = toga.Button("Start",on_press=self.encoding,
        style=Pack(
            flex=1,
            padding_right = 5,
            height = 40,
            font_size = 9,
            background_color = "#339966"))
        
        reset_button = toga.Button("Reset",on_press=self.reset, 
        style=Pack(
            flex=1,
            height = 40,
            font_size = 9,
            background_color="#CCCCCC"))
        
        
        button_box = toga.Box(style=Pack(direction = ROW,padding = (10,0)))
        button_box.add(encoding_button)
        button_box.add(reset_button)

        result_box = toga.Box(style=Pack(direction = ROW,padding = (10,0),alignment=CENTER))

        # result_label = toga.Label("Progress:", style=Pack(font_size = 10, color = "#006400"))
        self.result_text = toga.Label ("Progress: 0%",style=Pack(font_size=10,flex=1, color = "#006400",text_align=CENTER))
        # result_box.add(result_label)
        result_box.add(self.result_text)


        encode_box.add(title)
        encode_box.add(select_box)
        encode_box.add(text_box)
        encode_box.add(key_box)
        encode_box.add(button_box)
        encode_box.add(result_box)

        self.second_window = toga.Window(title='Encode')
        self.windows.add(self.second_window)
        self.second_window.content = encode_box
        self.second_window.show()
        
    def openWindowDecode (self,widget):
        decode_box = toga.Box(style=Pack(direction = COLUMN, padding = 20))

        title = toga.Label("Decrypt your information", 
        style=Pack(
            flex=1, 
            direction=ROW, 
            font_size=18, 
            text_align = CENTER,
            padding_bottom = 20,
            color = "#008080"))
        
        main_label = toga.Label("Insert image or Image's URL:",style=Pack(font_size=9))
        self.image_url = toga.TextInput(style=Pack(flex=1, padding = (5,0),font_size=9))
        
        select_button = toga.Button("Select file",on_press=self.button_handler,
        style=Pack(
            flex=1, 
            padding = (5,0), 
            height = 40,
            font_size = 9,
            background_color = "#B0C4DE"))
        
        select_box = toga.Box(style=Pack(direction=COLUMN, padding=(10,0),  alignment = CENTER))
        select_box.add(main_label)
        select_box.add(self.image_url)
        select_box.add(select_button)

        key_label = toga.Label("Enter keys:",style=Pack(font_size=9))
        key_input_box = toga.Box(style=Pack(direction=ROW, padding=(10,0)))
        self.key_input_1 = toga.TextInput(style=Pack(flex=1, padding_top=5, padding_bottom = 5, padding_right=10,font_size=9))
        self.key_input_2 = toga.TextInput(style=Pack(flex=1, padding = (5,0),font_size=9))
        key_input_box.add(self.key_input_1)
        key_input_box.add(self.key_input_2)
        
        key_box = toga.Box(style=Pack(direction=COLUMN, padding=(10,0)))
        key_box.add(key_label)
        key_box.add(key_input_box)

        decoding_button  = toga.Button("Start",on_press=self.decoding,
        style=Pack(
            flex=1,
            padding_right = 5,
            height = 40,
            font_size = 9,
            background_color = "#339966"))
        
        reset_button = toga.Button("Reset",on_press=self.reset, 
        style=Pack(
            flex=1,
            height = 40,
            font_size = 9,
            background_color="#CCCCCC"))
        
        
        button_box = toga.Box(style=Pack(direction = ROW,padding = (10,0)))
        button_box.add(decoding_button)
        button_box.add(reset_button)

        result_box = toga.Box(style=Pack(direction = ROW,padding = (10,0),alignment=CENTER))
        # result_label = toga.Label("Progress:", style=Pack(font_size = 10, color = "#006400"))
        self.result_text = toga.Label ("Progress: 0%",style=Pack(font_size=10,flex=1, color = "#006400",text_align=CENTER))
        # result_box.add(result_label)
        result_box.add(self.result_text)


        decode_box.add(title)
        decode_box.add(select_box)
        decode_box.add(key_box)
        decode_box.add(button_box)
        decode_box.add(result_box)

        self.second_window = toga.Window(title='Decode')
        self.windows.add(self.second_window)
        self.second_window.content = decode_box
        self.second_window.show()

    def encoding (self,widget):
         if self.image_url.value == "" or self.text_input.value == "":
            # self.result_text.text = "Error! Must be filled out completely!"
            self.main_window.error_dialog('Dialog','Error! Must be filled out completely!')
         else:
            k1=int(self.key_input_1.value)
            k2=int(self.key_input_2.value)
            message = self.text_input.value+"$"
            msg = ''
            j = 0
            for i in range(len(message)):
                char = message[i]
                if "A" <= char <= "Z":
                    if j == 0:
                        msg += chr((ord(char) + k1 - 65) % 26 + 65)
                        j = 1
                    else:
                        msg += chr((ord(char) + k2 - 65) % 26 + 65)
                        j = 0
                elif 97 <= ord(char) <= 122:
                    if j == 0:
                        msg += chr((ord(char) + k1 - 97) % 26 + 97)
                        j = 1
                    else:
                        msg += chr((ord(char) + k2 - 97) % 26 + 97)
                        j = 0
                else:
                    msg += char
            
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
            self.result_text.text = "Progress: Done!"
            self.main_window.info_dialog('Dialog','Encoding Success!')
            
            # Display the image
            new_img.show()  
            new_img.close()

    def decoding (self,widget):    
         if self.image_url.value == "":
            # self.result_text.text = "Error! Select file first!"
            self.main_window.error_dialog('Dialog','Error! Must be filled out completely!')
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
            
            k1=int(self.key_input_1.value)
            k2=int(self.key_input_2.value)
            result = ''
            j = 0
            for i in range(len(nmsg)):
                char = nmsg[i]
                if "A" <= char <= "Z":
                    if j == 0:
                        result += chr((ord(char) - k1 - 65) % 26 + 65)
                        j = 1
                    else:
                        result += chr((ord(char) - k2 - 65) % 26 + 65)
                        j = 0
                elif 97 <= ord(char) <= 122:
                    if j == 0:
                        result += chr((ord(char) - k1 - 97) % 26 + 97)
                        j = 1
                    else:
                        result += chr((ord(char) - k2 - 97) % 26 + 97)
                        j = 0
                else:
                    result += char

            self.result_text.text = "Progress: Done! Message is: " + result
            self.main_window.info_dialog('Dialog',"Decoding Success!")
            
    
    def reset(self,widget):
        if self.main_window.confirm_dialog('Dialog', 'Are you sure you want to reset?'):
            self.image_url.value=""
            self.text_input.value=""
            self.result_text.text = "0%"
            return True
        else:
            return False
    


         


def main():
    return InfomationHiding()
