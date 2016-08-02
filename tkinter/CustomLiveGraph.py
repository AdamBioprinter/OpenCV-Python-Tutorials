import tkinter as tk
from tkinter import ttk
import matplotlib
# changing the back end of matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

from matplotlib import style
import urllib
import json

import pandas as pd
import numpy as np

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

def animate(i):
  dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
  data = urllib.request.urlopen(dataLink)
  data = data.read().decode("utf=8")
  data = json.loads(data)
  data = data["btc_usd"]
  data = pd.DataFrame(data)
  
  buys = data[(data['type']=="bid")]
  buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
  buyDates = (buys["datestamp"]).tolist()
  
  sells = data[(data['type']=="ask")]
  sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
  sellDates = (sells["datestamp"]).tolist()

  a.clear()

  a.plot_date(buyDates, buys["price"], "#4F38FF", label="buys")
  a.plot_date(sellDates, sells["price"], "#05B0FF", label="sells")

  # a.legend() this command is enough to display legend
  # the problem is it doesn't readjust when zooming/panning, and can cover data
  a.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3,
      ncol=2, borderaxespad=0)

  title = "BTC-e BTCUSD Prices\nLast Price: "+str(data["price"][1999])
  a.set_title(title)


class SeaofBTCapp(tk.Tk):

  def __init__(self, *args, **kwargs):
               
    tk.Tk.__init__(self, *args, **kwargs)

    # In these two lines I tried to add an icon to the top left of the window
    # Unfortunately tkinter sucks, and sucks even more on a mac or linux system because it only
    
    # accepts .xbm files which are binarized pieces of shit. why it only accepts this, who knows.
    # strLoc = "@/~/Desktop/Digital\ Image\ processing/OpenCV-Python-Tutorial/tkinter/icons/poolbird.ico"
    #    tk.Tk.iconbitmap(self,default=strLoc)

    # Adding a title to the window
    tk.Tk.wm_title(self,"Sea of BTC client")

    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand = True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}

    for F in (StartPage, BTCE_page):
    
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
    label = tk.Label(self, text="Alpha Bitcoin trading application", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = ttk.Button(self,text="Agree",
        command=lambda: controller.show_frame(BTCE_page))

    button1.pack()

    button2 = ttk.Button(self,text="Disagree",
        command=quit)

    button2.pack()

class PageOne(tk.Frame):

  def __init__(self,parent,controller):
    
    tk.Frame.__init__(self,parent)
    label = tk.Label(self, text="Page ONE!!", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = ttk.Button(self,text="Back to Home",
        command=lambda: controller.show_frame(StartPage))

    button1.pack()
    
    button2 = ttk.Button(self,text="Page 2",
        command=lambda: controller.show_frame(PageTwo))

    button2.pack()


class BTCE_page(tk.Frame):

  def __init__(self,parent,controller):
    
    tk.Frame.__init__(self,parent)
    label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
    label.pack(pady=10,padx=10)

    button1 = ttk.Button(self,text="Back to Home",
        command=lambda: controller.show_frame(StartPage))

    button1.pack()

    canvas = FigureCanvasTkAgg(f, self)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand = True)

    toolbar = NavigationToolbar2TkAgg(canvas, self)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH, expand = True)

app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()

  
