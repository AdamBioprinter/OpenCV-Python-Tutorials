import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

  def __init__(self, *args, **kwargs):
               
    tk.Tk.__init__(self, *args, **kwargs)
    container = tk.Frame(self)

    container.pack(side="top", fill="both", expand = True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}

    for F in (StartPage, PageOne, PageTwo):
    
      # StartPage is another object that is defined below
      frame = F(container, self)

      self.frames[F] = frame

      frame.grid(row=0, column=0, sticky="nsew")

    self.show_frame(StartPage)

  def show_frame(self, cont):

      frame = self.frames[cont]
      frame.tkraise()

# This function is passed on to the button command
# For now, it just prints a string to the console, but funcionally, it serves to execute a command upon a button click
def qf(param):
  print(param)

class StartPage(tk.Frame):

  def __init__(self, parent, controller):
    
    tk.Frame.__init__(self,parent)
    label = tk.Label(self, text="Start Page", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = tk.Button(self,text="Visit Page 1",
        command=lambda: controller.show_frame(PageOne))

    button1.pack()

    button2 = tk.Button(self,text="Visit Page 2",
        command=lambda: controller.show_frame(PageTwo))

    button2.pack()

class PageOne(tk.Frame):

  def __init__(self,parent,controller):
    
    tk.Frame.__init__(self,parent)
    label = tk.Label(self, text="Page ONE!!", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = tk.Button(self,text="Back to Home",
        command=lambda: controller.show_frame(StartPage))

    button1.pack()
    
    button2 = tk.Button(self,text="Page 2",
        command=lambda: controller.show_frame(PageTwo))

    button2.pack()


class PageTwo(tk.Frame):

  def __init__(self,parent,controller):
    
    tk.Frame.__init__(self,parent)
    label = tk.Label(self, text="Page two!!", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = tk.Button(self,text="Back to Home",
        command=lambda: controller.show_frame(StartPage))

    button1.pack()

    button2 = tk.Button(self,text="Page One",
        command=lambda: controller.show_frame(PageOne))

    button2.pack()

app = SeaofBTCapp()
app.mainloop()

  
