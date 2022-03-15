#APP作成基本コマンド
import tkinter

class Application(tkinter.Frame):#フレームのクラスを作成継承
    def __init__(self,root=None):#処理 受けとる(基底クラス=Frameのイニシャライザーを呼ぶ)
        super().__init__(root, width=380, height=280,#横幅,　縦幅
                         borderwidth=4, relief='groove')#境界線の太さ4　境界線の種類groove
        self.root = root#classの別メソッドでも使用する為インスタンス変数に代入
        self.pack()#位置の設定
        self.pack_propagate(0)#サイズ調整
        self.create_widgets()
        

    def create_widgets(self):
        #閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn["text"] = '閉じる' #ボタンに表示させる文字 ＝ '閉じる'
        quit_btn["command"] = self.root.destroy #ボタンを押した際の命令　＝　アプリを閉じる
        quit_btn.pack(side='bottom')

        #テキストボックスの作成
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()

        #実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn["text"] = "実行"
        submit_btn["command"] = self.input_handler
        submit_btn.pack()

        #メッセージの出力
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):#値の習得
        text = self.text_box.get()
        self.message["text"] = text + '!!'#習得したtextに文字列"!!"を結合

        
root = tkinter.Tk() #作成したオブジェクトをrootに代入Tkのスペル注意
root.title('練習アプリ')#appの名前
root.geometry('400x300')#縦の長さx横の長さ
app = Application(root=root)#topレベルのリジェクトを引数に渡す

#部品や処理の記載欄

root.mainloop()#アプリ起動

