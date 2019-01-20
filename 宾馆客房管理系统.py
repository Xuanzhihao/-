# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
import pymysql
db = pymysql.connect(host='',
                     user='root',
                     passwd='',
                     db='sys',
                     port=10023,
                     charset='UTF8')


'''
import pymysql
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox 
import string

class Mysql_conn:
    def __init__(self):
        self.db = pymysql.connect(host='cdb-8qn7golk.bj.tencentcdb.com',
                     user='root',
                     passwd='xzh723619',
                     db='sys',
                     port=10023,
                     charset='UTF8')
        self.cursor = self.db.cursor()

    def insert(self, insert_words):
        try:
            # 执行sql语句
            self.cursor.execute(insert_words)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def select(self, select_words):
        try:
            # 执行SQL语句
            self.cursor.execute(select_words)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")

    def update(self, update_words):
        try:
            # 执行SQL语句
            self.cursor.execute(update_words)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def delete(self, delete_words):
        try:
            # 执行SQL语句
            self.cursor.execute(delete_words)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close_conn(self):
        self.db.close()
# 查找测试
#sw = "SELECT * FROM room"
#test1.select(sw)

# 增添测试
#iw = "INSERT INTO room(room_id,price, occupied)VALUES (9518,500,0)"
#test1.insert(iw)

# 更新测试
#uw = "UPDATE room SET price = 600 WHERE room_id = 9518"
#test1.update(uw)

# 删除测试
#dw = "DELETE FROM room WHERE room_id = 9518" 
#test1.delete(dw)

# test1.close_conn()

LARGE_FONT = ("Verdana", 20)

class Application(tk.Tk):
     def __init__(self):
         
         super().__init__()
 
         self.wm_title("宾馆客房管理系统")
         
         container = tk.Frame(self)
         container.pack(side="top", fill="both", expand = True)
         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight=1)
 
         self.frames = {}
         for F in (StartPage, PageOne, PageTwo, PageThree,PageFour,PageFive, PageSix):
             frame = F(container, self)
             self.frames[F] = frame
             frame.grid(row=0, column=0, sticky="nsew")  
 
         self.show_frame(StartPage)
 
         
     def show_frame(self, cont):
         frame = self.frames[cont]
         frame.tkraise() 
 
class StartPage(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="宾馆客房管理系统", font=LARGE_FONT)
         label.pack(pady=100)
         ft2=tkFont.Font(size=16)
         tk.Button(self, text="客房信息录入",font=ft2,command=lambda: root.show_frame(PageOne),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
         tk.Button(self, text="客人入住登记",font=ft2,command=lambda: root.show_frame(PageTwo),width=30,height=2).pack()
         tk.Button(self, text="客人退房结算",font=ft2,command=lambda: root.show_frame(PageThree),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
         tk.Button(self, text="查看全部客房",font=ft2,command=lambda: root.show_frame(PageFour),width=30,height=2).pack()
         tk.Button(self, text="客房信息查询",font=ft2,command=lambda: root.show_frame(PageFive),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
         tk.Button(self, text="客房信息删改",font=ft2,command=lambda: root.show_frame(PageSix),width=30,height=2).pack()
         tk.Button(self,text='退出系统',height=2,font=ft2,width=30,command=root.destroy,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
 

         
         
class PageOne(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="客房信息录入", font=LARGE_FONT)
         label.pack(pady=100)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         tk.Label(self,text='房间号：',font=ft3).pack()
         global v1
         v1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=v1,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='价格：',font=ft3).pack()
         global v2
         v2=tk.StringVar()
         tk.Entry(self,width=30,textvariable=v2,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='是否已经入住(用1/2表示,1为未入住)：',font=ft3).pack()
         global v3
         v3=tk.StringVar()
         tk.Entry(self,width=30,textvariable=v3,font=ft3,bg='Ivory').pack()
         tk.Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
         tk.Button(self, text="确定保存",width=8,font=ft4,command=self.save).pack()
         
     def save(self):
         coon_1 = Mysql_conn()
         a=str(v1.get())
         b=str(v2.get())
         c=str(v3.get())
         iw = "INSERT INTO room(room_id,price,occupied)VALUES("+a+","+b+","+c+")"
         coon_1.insert(iw)
         tk.messagebox.showerror("OK",a+b+c)
         tk.messagebox.showerror("OK","OK")
         coon_1.close_conn()
         
         
class PageTwo(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="客人入住登记", font=LARGE_FONT)
         label.pack(pady=100)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         tk.Label(self,text='客人身份证号：',font=ft3).pack()
         global var1
         var1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var1,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='房间号：',font=ft3).pack()
         global var2
         var2=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var2,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='姓名：',font=ft3).pack()
         global var3
         var3=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var3,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='入住日期：',font=ft3).pack()
         global var4
         var4=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var4 ,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='离开日期：',font=ft3).pack()
         global var5
         var5=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var5,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='预付款：',font=ft3).pack()
         global var6
         var6=tk.StringVar()
         tk.Entry(self,width=30,textvariable=var6,font=ft3,bg='Ivory').pack()
         tk.Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
         tk.Button(self, text="确定保存",width=8,font=ft4,command=self.save).pack()
         
     def save(self):
         coon_1 = Mysql_conn()
         a=str(var1.get())
         b=str(var2.get())
         c="'"+str(var3.get())+"'"
         d=str(var4.get())
         e=str(var5.get())
         f=str(var6.get())
         
         sw = "SELECT occupied FROM room where room_id="+b
         
         
         if(coon_1.select(sw)==2):
             tk.messagebox.showerror("Sorry", "Sorry, 房间已经被使用或无此房间")
             coon_1.close_conn() 
         else:
             iw = "INSERT INTO abc VALUES("+a+","+b+","+c+","+d+","+e+","+f+")"
             tk.messagebox.showerror("OK", iw)
             coon_1.insert(iw)
             uw = "UPDATE room SET occupied = 2 WHERE room_id = "+b
             coon_1.update(uw)
             coon_1.close_conn() 
                
                
class PageThree(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="客人退房结算", font=LARGE_FONT)
         label.pack(pady=100)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         tk.Label(self,text='客人身份证号：',font=ft3).pack()
         global va1
         va1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=va1,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='房间号：',font=ft3).pack()
         global va2
         va2=tk.StringVar()
         tk.Entry(self,width=30,textvariable=va2,font=ft3,bg='Ivory').pack()
         
         tk.Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
         tk.Button(self, text="确定退房",width=8,font=ft4,command=self.save).pack()
         
     def save(self):
         coon_1 = Mysql_conn()
         a = str(va1.get())
         b = str(va2.get())
         dw = "DELETE FROM abc WHERE room_id = "+b+" AND guest_id = "+a
         uw = "UPDATE room SET occupied = 2 WHERE room_id = "+b
         swin = "SELECT intime FROM abc WHERE room_id="+b+" AND guest_id = "+a
         swout = "SELECT outtime FROM abc WHERE room_id = "+b+" AND guest_id = "+a
         swm = "SELECT price FROM room WHERE room_id = "+b
         swmy = "SELECT money FROM abc WHERE room_id = "+b+" AND guest_id = "+a
         
         swinn = str(coon_1.select(swin))
         swout1 = str(coon_1.select(swout))
         swmoney = str(coon_1.select(swm))
         swmoneyy = str(coon_1.select(swmy))
         '''
         c = swout1 - swinn
         d = (c/10000)*365+((c-(c/10000)*10000)/100)*30+(c-(c/100)*100)*1

         e = d*swmoney
         f = d*swmoney - swmoneyy'''
         
         tk.messagebox.showerror("OK", "入住日期为"+swinn+"，离开日期为"+swout1+"，每晚单价为"+swmoney+"元，预付款为"+swmoneyy+"元。")
         coon_1.delete(dw)
         coon_1.update(uw)
         coon_1.close_conn()     
         
class PageFour(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="查看全部客房信息", font=LARGE_FONT)
         label.pack(pady=25)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         
         # 信息展示
         
         
         tk.Button(self, text="返回首页",width=16,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
         tk.Button(self, text="查看客房信息",width=16,font=ft4,command=self.save).pack()

         
     def save(self):
         coon_1 = Mysql_conn()
         sw = "SELECT * FROM room"


         sww = str(coon_1.select(sw))
         tk.messagebox.showerror("OK",sww)

         coon_1.close_conn()
         
class PageFive(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="客房信息查询", font=LARGE_FONT)
         label.pack(pady=100)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         tk.Label(self,text='姓名：',font=ft3).pack()
         global a1
         a1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=a1,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='房间号：',font=ft3).pack()
         global a2
         a2=tk.StringVar()
         tk.Entry(self,width=30,textvariable=a2,font=ft3,bg='Ivory').pack()
         
         tk.Button(self, text="返回首页",width=16,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
         tk.Button(self, text="按空房间查询",width=16,font=ft4,command=self.save1).pack()
         tk.Button(self, text="按姓名查询",width=16,font=ft4,command=self.save2).pack()
         tk.Button(self, text="按房间号查询",width=16,font=ft4,command=self.save3).pack()
         
     def save1(self):
         coon_1 = Mysql_conn()

         iw = "SELECT * FROM room WHERE occupied=1"
         aaa = coon_1.select(iw)
         tk.messagebox.showerror("OK",aaa)
         coon_1.close_conn()
         
     def save2(self):
         coon_1 = Mysql_conn()
         a = str(a1.get())

         iw = "SELECT * FROM abc WHERE name="+a
         aaa = coon_1.select(iw) 
         tk.messagebox.showerror("OK",aaa)
         coon_1.close_conn()
         
     def save3(self):
         coon_1 = Mysql_conn()
         a = str(a2.get())

         iw = "SELECT * FROM room WHERE room_id="+a
         aaa = coon_1.select(iw) 
         tk.messagebox.showerror("OK",aaa)
         coon_1.close_conn()

         
class PageSix(tk.Frame):
     def __init__(self, parent, root):
         super().__init__(parent)
         label = tk.Label(self, text="客房信息删改", font=LARGE_FONT)
         label.pack(pady=100)
 
         ft3=tk.font.Font(size=14)
         ft4=tk.font.Font(size=12)
         
         tk.Label(self,text='要删除的房间号：',font=ft3).pack()
         global b1
         b1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=b1,font=ft3,bg='Ivory').pack()
         tk.Button(self, text="确定删除",width=8,font=ft4,command=self.save1).pack()
         
         
         tk.Label(self,text='房间号：',font=ft3).pack()
         global c1
         c1=tk.StringVar()
         tk.Entry(self,width=30,textvariable=c1,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='价格：',font=ft3).pack()
         global c2
         c2=tk.StringVar()
         tk.Entry(self,width=30,textvariable=c2,font=ft3,bg='Ivory').pack()
         tk.Label(self,text='是否已经入住(用1/2表示,1为未入住)：',font=ft3).pack()
         global c3
         c3=tk.StringVar()
         tk.Entry(self,width=30,textvariable=c3,font=ft3,bg='Ivory').pack()
         
         tk.Button(self, text="确定修改",width=8,font=ft4,command=self.save2).pack()
         
         tk.Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)

         
     def save1(self):
         coon_1 = Mysql_conn()
         a = str(b1.get())

         iw = "DELETE FROM room WHERE room_id = "+a
         coon_1.delete(iw)
         coon_1.close_conn()
         tk.messagebox.showerror("OK","已删除")
         
     def save2(self):
         coon_1 = Mysql_conn()
         a=str(c1.get())
         b=str(c2.get())
         c=str(c3.get())
         iw1 = "UPDATE room SET price = "+b+" WHERE room_id = "+a
         iw2 = "UPDATE room SET occupied = "+c+" WHERE room_id = "+a
         coon_1.update(iw1)
         coon_1.update(iw2)
         tk.messagebox.showerror("OK",a+b+c)
         tk.messagebox.showerror("OK","OK")
         coon_1.close_conn()
         

app = Application()

app.mainloop()


