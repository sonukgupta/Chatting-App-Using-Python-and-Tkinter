from tkinter import*
from tkinter import filedialog
import socket,threading
s=socket.socket()
host=socket.gethostname()
ipaddress = socket.gethostbyname(host)
print(host,ipaddress)
port=8080


class text_editor:


    def close(self):
        pass

    def exit_con(self):
        try:
            self.conn.close()
            exit()
        except:
            exit()

# Code for Establish Connection....................................................................
    def est_con(self):
        try:
            s.bind((host, port))
            s.listen(5)
            self.conn, addr = s.accept()
            print("Connected to client")
            self.status.config(text="Connected", bg='lightgreen')
            self.client_info.config(text=addr)
            threading.Thread(target=self.recv_module).start()
        except:
            print("connection error")
            self.conn.close()

# Code for Recv Module....................................................................
    def recv_module(self):
        while True:
            try:
                data = self.conn.recv(1024)
                data = data.decode()
                if data:
                    data = 'Client : ' + data + '\n'
                    self.history.insert("end", data)
            except Exception as e:
                print(e, "[=] Closing Connection [recv]")
                self.conn.close()
                break

# Code for Send Module....................................................................
    def send_module(self):
        input_data = self.Sending_info.get('1.0', 'end')
        if len(input_data) != 1:
            input_data_ = 'Me : ' + input_data + '\n'
            self.history.insert("end", input_data_)
            self.Sending_info.delete('1.0', 'end')
            input_data = input_data.encode()
            self.conn.send(input_data)
        else:
            print("[=] Input Not Provided")

# Code for Window Frame....................................................................
    def __init__(self,master): #self represent te and master represnt root
        self.master=master
        master.title("Server Side")

    # First For Connection Information
        self.Connection = LabelFrame(master, text='Connection Informations', fg='green', bg='bisque')
    # FRAME 1
        self.frame = Frame(self.Connection)
        self.frame.pack(side='top', padx=10, pady=10)
        Label(self.frame, text='Your IP Address', relief="groove", anchor='center', width=25).grid(row=1,column=1,ipadx=10,ipady=5)
        self.ip=Label(self.frame, text=ipaddress, relief='sunken', anchor='center', width=25)
        self.ip.grid(row=1, column=2,ipadx=10, ipady=5)
        Label(self.frame, text='Port Number', relief="groove", anchor='center', width=25).grid(row=2, column=1,ipadx=10,ipady=5)
        Label(self.frame, text=port, relief="sunken", anchor="center", width=25).grid(row=2, column=2, ipadx=10,ipady=5)
        Label(self.frame, text='Status', relief="groove", anchor="center", width=25).grid(row=3,column=1,ipadx=10,ipady=5)
        Label(self.frame, text='Connected with', relief='groove', anchor='center', width=25).grid(row=4,column=1,ipadx=10,ipady=5)
        self.status = Label(self.frame, text="Not Connected", relief="sunken", anchor='center', width=25,bg="red")
        self.status.grid(row=3, column=2, ipadx=10, ipady=5)
        self.client_info = Label(self.frame, text="192.168.00.12:5000", relief='sunken', anchor='center',width=25)
        self.client_info.grid(row=4, column=2, ipadx=10, ipady=5)
    # FRAME 2
        self.frame2 = Frame(self.Connection)
        self.frame2.pack(side='top', padx=10, pady=10)
        self.con_button = Button(self.frame2, text="Establish Connection",command=self.est_con,bg='lightsalmon',width=15,font=('arial 10 bold '),activebackground='olivedrab')
        self.con_button.grid(row=1, column=1, ipadx=10, ipady=5)
        self.exit_button=Button(self.frame2,text="Exit",width=15,bg='salmon',command=self.exit_con,font=('arial 10 bold '),activebackground='red')
        self.exit_button.grid(row=1, column=2, ipadx=10, ipady=5)
        self.Connection.pack(side='top', expand='yes', fill='both')


    # Creating Second For Chatting History
        self.chat_log = LabelFrame(master, text='Chatting ', fg='green', bg='wheat')
        self.history = Text(self.chat_log, font=('arial 12 bold italic'), width=50, height=15,bg="lightcyan")
        self.history.pack(side='top', expand='yes', fill='both')
        self.chat_log.pack(side='top', expand='yes', fill='both')


    # Creating Third For Sending Text Message
        self.Sending = LabelFrame(master, text='Send Text', fg='green', bg='powderblue')
        self.Sending_info = Text(self.Sending, font=('arial 12 italic'), width=35, height=5)
        self.Sending_info.pack(side='left', expand='yes', fill='both')
        self.Sending_Button = Button(self.Sending, text='Send', width=15, height=5, bg='orange', activebackground='lightgreen',command=self.send_module)
        self.Sending_Button.pack(side='left', expand='yes', fill='both')
        self.Sending.pack(side='top', expand='yes', fill='both')








root=Tk()

te=text_editor(root)


root.mainloop() #display window untill we closed