import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
def dispPhoto(path):
    # 画像を読み込む
    newImage = PIL.Image.open(path).resize((300,300))
    # labelに表示
    # error
    #imageData = PIL.ImageTK.PhotoImage(newImage)
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        #erro
        #dispPhoto(fpath)
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()

