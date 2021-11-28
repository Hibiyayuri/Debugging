import tkinter as tk
from tkinter import StringVar, IntVar
from tkinter import filedialog
import tkinter.messagebox
import random
import os
import glob
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import time


        
class MyDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('新增題庫')
        self.setup_UI()
        
        
    def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1,text='新增題目', font=("標楷體"), width=30).pack(side=tk.LEFT)
        self.question = tk.StringVar()
        tk.Entry(row1, textvariable=self.question, width=30).pack(side=tk.LEFT)
        
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='請輸入題目的選項： ', font=("標楷體"), width=30).pack(side=tk.LEFT)
        self.option = tk.StringVar()
        tk.Entry(row2, textvariable=self.option, width=30).pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row3, text='請輸入答案： ', font=("標楷體"), width=30).pack(side=tk.LEFT)
        self.anw = tk.StringVar()
        tk.Entry(row3, textvariable=self.anw, width=30).pack(side=tk.LEFT)

        row4 = tk.Frame(self)
        row4.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row4, text='請輸入相關檔案： ', font=("標楷體"), width=30).pack(side=tk.LEFT)
        self.file= tk.StringVar()
        tk.Entry(row4, textvariable=self.file, width=30).pack(side=tk.LEFT)

        row5 = tk.Frame(self)
        row5.pack(fill="x")
        tk.Button(row5, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row5, text="確定", command=self.ok).pack(side=tk.RIGHT)
        
    #檢查是否輸入完整題目資訊
    def ok(self):
        self.userinfo = [self.question.get(), self.option.get(), self.anw.get(), self.file.get()]
        if (self.question.get() == '' or self.option.get() == '' or self.anw.get() == '' or self.file.get() == ''):
            tk.messagebox.showerror(title='錯誤', message='請輸入完整資料')
        elif( self.anw.get().isdigit() == False):
            tk.messagebox.showerror(title='錯誤', message='答案請輸入數字')
        else:
            tk.messagebox.showinfo(title='添加成功', message='已新增題目')
            file = open('question.txt',  "a", encoding='UTF-8') 
            file.write("\n")
            file.write(self.question.get() + "\n")
            file.write(self.option.get() + "\n")
            file.write(self.anw.get() + "\n")
            file.write(self.file.get() + "\n")
            file.close()
        self.destroy() 
    
    def cancel(self):
        self.userinfo = None 
        self.destroy()


window = tk.Tk()
window.title('台南知識王')
window.resizable(False, False)
window.geometry('{}x{}'.format(600, 650))

reply=0
correct=0
no=0
record=[]
for i in range(11):
    record.append(0)

# 獲取picture文件夾的絕對路徑
pathdir = os.path.abspath('.')  


Qtype=0
#玩家骰骰子
def Die():
    global Qtype, tk, picture, img_gif
    Qtype = random.randint(1,2)
    print(Qtype)
    print(picture)
    img = Image.open(picture[no].rstrip())
    img = img.resize((200, 200), Image.ANTIALIAS)
    img_gif = ImageTk.PhotoImage(image=img)
    label_img.configure(image=img_gif, width = 200,height=200)
    if Qtype==1:
        y.set('民俗文化題')
    elif Qtype==2:
        y.set('美食題')
    elif Qtype==3:
        y.set('景點題')
    elif Qtype==4:
        y.set('名人名言題')
    elif Qtype==5:
        y.set('文學題')
    else:
        y.set('藝術題')
   
tk.Button(window, text = '選類型', command = Die, width = 30).pack()

#從question.txt讀取題目，解答和相關圖片名稱
if Qtype==1:
    fp = open('question1.txt', "r", encoding='UTF-8')
    path_p = 'pic1'
    pic_path = os.path.join(pathdir, path_p)
 
else:
    fp = open('question6.txt', "r", encoding='UTF-8')
    path_p = 'pic6'
    pic_path = os.path.join(pathdir, path_p)
    
lines=fp.readlines()
question=[]
choose=[]
answer=[]
picture=[]
for i in range(len(lines)):
    if i%4==0:
        question.append(lines[i])
    elif i%4==1:
        choose.append(lines[i])
    elif i%4==2:
        answer.append(lines[i])
    else:
        lines[i].rstrip()
        picture.append(os.path.join(pic_path, lines[i]))
fp.close()


#設定初始顯示文字與圖片
question_text= StringVar()
question_text.set(question[no])
choose_text= StringVar()
choose_text.set(choose[no])
no_text= StringVar()
no_text.set("第"+str(no+1)+"題")
correct_text= StringVar()
correct_text.set("答對"+str(correct)+"/"+str(no)+"題")
y= StringVar()
y.set("")
#tk.Label(window, text=t, font=("標楷體"), width=16).pack()
tk.Label(window, textvariable=y, font=("標楷體"), width=16).pack()
tk.Label(window, text='歡迎參加台南知識王', font=("標楷體", 16)).pack()
img = Image.open(picture[no].rstrip())
img = img.resize((200, 200), Image.ANTIALIAS)
img_gif = ImageTk.PhotoImage(image=img)
label_img = tk.Label(window, image = img_gif, width = 200,height=200)
label_img.pack()
tk.Label(window, textvariable=no_text, font=("標楷體", 16)).pack()
tk.Label(window, textvariable=question_text, font=("標楷體", 16)).pack()
tk.Label(window, textvariable=choose_text, font=("標楷體", 16)).pack()
tk.Label(window, textvariable=correct_text, font=("標楷體", 16)).pack()

e1 = []
e2 = []
e3 = []
e4 = []
confirm_ok = 0
    



#重來設置
def play():
    plt.close(1)
    plt.close(2)
    global question, choose, answer, no, correct, img_gif, picture
    if Qtype==1:
        fp = open('question.txt', "r", encoding='UTF-8')
    elif Qtype==2:
        fp = open('question.txt', "r", encoding='UTF-8')
    elif Qtype==3:
        fp = open('question.txt', "r", encoding='UTF-8')
    elif Qtype==4:
        fp = open('question.txt', "r", encoding='UTF-8')
    elif Qtype==5:
        fp = open('question.txt', "r", encoding='UTF-8')
    else:
        fp = open('question.txt', "r", encoding='UTF-8')
    lines=fp.readlines()
    question=[]
    choose=[]
    answer=[]
    picture=[]
    for i in range(len(lines)):
        if i%4==0:
            question.append(lines[i])
        elif i%4==1:
            choose.append(lines[i])
        elif i%4==2:
            answer.append(lines[i])
        else:
            lines[i].rstrip()
            picture.append(os.path.join(pic_path, lines[i]))

    ran = [x for x in range(len(question))]
    random.shuffle(ran)  
    question=[question[k] for k in ran]
    choose=[choose[k] for k in ran]
    answer=[answer[k] for k in ran]
    picture=[picture[k] for k in ran]	
    no=0
    correct=0
    no_text.set("第"+str(no+1)+"題")
    question_text.set(question[no])
    choose_text.set(choose[no])
    correct_text.set("答對"+str(correct)+"/"+str(no)+"題")
    img = Image.open(picture[no].rstrip())
    img = img.resize((200, 200), Image.ANTIALIAS)
    img_gif = ImageTk.PhotoImage(image=img)
    label_img.configure(image=img_gif, width = 200,height=200)
    fp.close()

#檢查答案
def checkans(reply):
    global question,choose,answer,no,correct,img_gif,record
    if reply==int(answer[no]) and no<10:
        correct=correct+1
        record[no]=1

    if no<9:
        no=no+1
        no_text.set("第"+str(no+1)+"題")
        question_text.set(question[no])
        choose_text.set(choose[no])
        correct_text.set("答對"+str(correct)+"/"+str(no)+"題")
        img = Image.open(picture[no].rstrip())
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_gif = ImageTk.PhotoImage(image=img)
        label_img.configure(image=img_gif, width = 200,height=200)

    elif no==9: 
        #答到最後一題需要按“再來一局”才可以重玩，不然就停在最後一題的畫面
        no_text.set("第10題")
        question_text.set(question[9])
        choose_text.set(choose[9])
        correct_text.set("答對"+str(correct)+"/10題")
        img = Image.open(picture[no].rstrip())
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_gif = ImageTk.PhotoImage(image=img)
        label_img.configure(image=img_gif, width = 200,height=200)
        no=no+1

        #匯出每題對錯的直方圖
        plt.figure(1)
        x=[1,2,3,4,5,6,7,8,9,10]
        plt.xlabel("question no")
        plt.ylabel("true or false")
        plt.yticks(range(10))
        plt.bar(x,record[0:10])

        #匯出對錯率的圓餅圖
        plt.figure(2)
        labels=['correct','wrong']
        percent=[correct/10,(10-correct)/10]
        out=(0,0.1)
        plt.pie(percent,						# 數值
            labels = labels,					# 標籤
            autopct = "%1.1f%%",				# 將數值百分比並留到小數點一位
            explode = out,						# 設定分隔的區塊位置
            pctdistance = 0.6,					# 設定分隔的區塊位置
            textprops = {"fontsize" : 12},		# 文字大小
            shadow=True)   						# 設定陰影					
        plt.show()

def ans1():
    global reply
    reply=1
    checkans(reply)

def ans2():
    global reply
    reply=2
    checkans(reply)

def ans3():
    global reply
    reply=3
    checkans(reply)



def new_dialog():
    inputDialog =  MyDialog()
    window.wait_window(inputDialog) 
    print(inputDialog.userinfo)

#按鍵設置
tk.Button(window, text = '選擇1', command = ans1, width = 30).pack()
tk.Button(window, text = '選擇2', command = ans2, width = 30).pack()
tk.Button(window, text = '選擇3', command = ans3, width = 30).pack()
tk.Button(window, text ='再來一局', command = play, width = 30).pack()
tk.Button(window, text ='新增題庫', command = new_dialog, width = 30).pack()
#label
tk
'''
#增加題庫設置
tk.Label(window, text='\n').pack()
tk.Label(window, text='新增題目', font=("標楷體")).pack()
tk.Label(window, text='請輸入新題目: ', font=("標楷體")).pack()
e1 = tk.Entry(window)
e1.pack()
tk.Label(window, text='請輸入題目的選項： ', font=("標楷體")).pack()
e2 = tk.Entry(window)
e2.pack()
tk.Label(window, text='請輸入答案： ', font=("標楷體")).pack()
e3 = tk.Entry(window)
e3.pack()
tk.Label(window, text='請輸入相關檔案名稱： ', font=("標楷體")).pack()
e4 = tk.Entry(window)
e4.pack()

button_confirm = tk.Button(window, text ='新增', command = check_question, width = 30).pack()
'''
window.mainloop()
