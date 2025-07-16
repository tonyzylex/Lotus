import tkinter as tk

class LoginPanel():
    def __init__(self):
        self.root = tk.Tk()
        self.root.update_idletasks()  

        width = 1200
        height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Login Panel")

        self.MainFrame = tk.Frame(self.root, bg="lightblue")
        self.MainFrame.pack(fill=tk.BOTH, expand=True)

        self.MainFrame.columnconfigure(0, weight=1)
        self.MainFrame.columnconfigure(1, weight=1)
        self.MainFrame.rowconfigure(0, weight=1)
        

        self.ImageFrame = tk.Frame(self.MainFrame, bg="#dbbf8b")
        self.ImageFrame.grid(row=0, column=0, sticky="nsew")

        self.LoginFrame = tk.Frame(self.MainFrame, bg="white")
        self.LoginFrame.grid(row=0, column=1, sticky="nsew")

       
        self.LoginFrame.rowconfigure(0, weight=0)  
        self.LoginFrame.rowconfigure(1, weight=1)  
        self.LoginFrame.columnconfigure(0, weight=1)
        self.LoginFrame.rowconfigure(2, weight=1)
        self.LoginFrame.grid_propagate(False)

        self.LogoFrame = tk.Frame(self.LoginFrame, bg="white")
        self.LogoFrame.grid(row=0, column=0, sticky="nsew")

        self.CompanyLogo = tk.PhotoImage(file="Lotus/Images/CompanyLogo.png")
        self.CompanyLogoLabel = tk.Label(self.LogoFrame, image=self.CompanyLogo, bg="white")
        self.CompanyLogoLabel.pack(pady=30)

        self.GridFrame = tk.Frame(self.LoginFrame, bg="white")
        self.GridFrame.grid(row=1, column=0, sticky="nsew")

        self.UserLogo = tk.PhotoImage(file="Lotus/Images/UserLogo.png")
        self.UserLogoLabel = tk.Label(self.GridFrame, image=self.UserLogo, bg="white")
        self.UserLogoLabel.grid(row=0, column=0,padx=35,pady=20)

        self.LockLogo = tk.PhotoImage(file="Lotus/Images/LockLogo.png")
        self.LockLogoLabel = tk.Label(self.GridFrame, image=self.LockLogo, bg="white")
        self.LockLogoLabel.grid(row=1, column=0,padx=35,pady=20)

        self.TextBoxFrame1 = tk.PhotoImage(file="Lotus/Images/TextBox.png")
        self.TextBoxBg1 = tk.Label(self.GridFrame, image=self.TextBoxFrame1, bg="white")
        self.TextBoxBg1.grid(row=0, column=1, padx=10, pady=20)

        self.TextBox1 = tk.Entry(
        self.GridFrame,
        bg="#ae9371",
        font="Fredoka 15 bold",
        fg="#dbbf8b",
        bd=0,
        relief="flat",
        highlightthickness=0,
        insertbackground="#dbbf8b"
        )
        self.TextBox1.place(in_=self.TextBoxBg1, relx=0.5, rely=0.5, anchor="center", width=300, height=30)
        self.TextBox1.insert(0, "Username")

        self.TextBoxFrame2 = tk.PhotoImage(file="Lotus/images/TextBox.png")
        self.TextBoxFrame2Label = tk.Label(self.GridFrame, image=self.TextBoxFrame1, bg="white")
        self.TextBoxFrame2Label.grid(row=1, column=1)

        self.TextBox2 = tk.Entry(
        self.GridFrame,
        bg="#ae9371",
        font="Fredoka 15 bold",
        fg="#dbbf8b",
        bd=0,
        relief="flat",
        highlightthickness=0,
        insertbackground="#dbbf8b",
        show="•"
        )
        self.TextBox2.place(in_=self.TextBoxFrame2Label, relx=0.5, rely=0.5, anchor="center", width=300, height=30)
        self.TextBox2.insert(0, "Password")

        self.BottomFrame = tk.Frame(self.LoginFrame, bg="white")
        self.BottomFrame.grid(row=2, column=0, sticky="nsew")

        self.ButtonImage = tk.PhotoImage(file="Lotus/images/ButtonBar.png")
        self.ButtonImageLabel = tk.Button(self.BottomFrame,
        image=self.ButtonImage,
        bg="white",
        activebackground="white",
        bd=0,
        highlightthickness=0,
        relief="flat",            
        overrelief="flat",        
        command=self.on_click,
        text="Sign-in",
        font="Poppins 32 bold",
        fg="white",
        activeforeground="white",
        compound="center",
        cursor="hand2")
        self.ButtonImageLabel.pack(side="top")

        self.TextBox1.bind("<FocusIn>", lambda event: self.TextBox1.delete(0, "end") if self.TextBox1.get() == "Username" else None)
        self.TextBox1.bind("<FocusOut>", lambda event: self.TextBox1.insert(0, "Username") if self.TextBox1.get() == "" else None)
        self.TextBox2.bind("<FocusIn>", lambda event: self.TextBox2.delete(0, "end") if self.TextBox2.get() == "Password" else None)
        self.TextBox2.bind("<FocusOut>", lambda event: self.TextBox2.insert(0, "Password") if self.TextBox2.get() == "" else None)     

        self.root.mainloop()
    
    def on_click(self):
        username = self.TextBox1.get()
        password = self.TextBox2.get()
        
        if username == "Username" or password == "Password":
            print("Please enter valid credentials.")
        else:
            print(f"Username: {username}, Password: {password}")
            # Here you can add the logic to handle the login process, such as checking credentials against a database.


        

# Run on main.py


  

#      self.UserLogo = tk.PhotoImage(file="images/UserLogo.png")
#      self.UserLogoLabel = tk.Label(self.LoginFrame, image=self.UserLogo, bg="white")
#      self.UserLogoLabel.pack(side="left",padx=30)

#      self.LockLogo = tk.PhotoImage(file="images/LockLogo.png")
#      self.LockLogoLabel = tk.Label(self.LoginFrame, image=self.LockLogo, bg="white")
#      self.LockLogoLabel.pack(side="bottom", padx=30)