# import tesseract
# import pytesseract
import pyocr
import sys
from PIL import Image, ImageTk
import tkinter
import tkinter.filedialog


class Shibie():
    msg = ""

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("识别验证码")
        self.root.geometry('800x300+560+390')
        self.file_name = tkinter.Label(self.root, text="文件名：")
        self.choose_button = tkinter.Button(self.root, command=self.choose, text="选择文件")
        self.photo = tkinter.Label(self.root)
        self.display_info = tkinter.Label(self.root)

    def gui_arrange(self):
        self.file_name.grid(row=0, column=0)
        self.photo.grid(row=1)
        self.choose_button.grid(row=0, column=1)
        self.display_info.grid(row=1, column=1)

    def choose(self):
        filename = tkinter.filedialog.askopenfilename()
        self.file_name.config(text="文件名：" + filename)
        tools = pyocr.get_available_tools()[:]
        if len(tools) == 0:
            self.msg += "no ocr tool found\n"
            self.display_info.config(text=self.msg)
            sys.exit(1)
        else:
            self.msg += "Using '%s' " % (tools[0].get_name()) + "\n"
            self.display_info.config(text=self.msg)
        image = Image.open(filename)
        img = ImageTk.PhotoImage(image)
        self.msg += tools[0].image_to_string(image,lang="chi_sim") + "\n"
        self.display_info.config(text=self.msg)
        self.photo.config(image=img)
        self.root.mainloop()


if __name__ == "__main__":
    sframe = Shibie()
    sframe.gui_arrange()
    tkinter.mainloop()
    pass
