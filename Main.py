from tkinter import*
from PIL import ImageTk, Image
import os
os.chdir(os.getcwd())
import matplotlib.pyplot as plt
import matplotlib
from tkinter import ttk
from ttkwidgets import TickScale
import numpy as np
from scipy.special import lambertw

matplotlib.use('TkAgg')
beta = int()
gamma = int()
#Ro = beta/gamma

population = 100
healthy = population
infected = 0
removed = 0
days = 0

"""
Start
"""
main_window = Tk()
main_window.title('Virus Simulator')
main_window.configure(bg='#00081e')
"""
#821616
"""
##head = Canvas(main_window,width  = 499,height = 67)
##head.pack()
##img = ImageTk.PhotoImage(Image.open("head.gif"))
##panel = Label(main_window,image = img)
##panel.pack(side = "top", fill = "none", expand = "no")


"""
img = ImageTk.PhotoImage(Image.open("map.gif"))
panel = Label(main_window,image = img)
panel.pack(side = "bottom", fill = "none", expand = "no")
"""
x,y = [],[[],[],[]]
beta =  0.015
gamma = 0.001
def data():
    global beta,gamma,healthy,infected,removed,days,x,y
    beta = beta*(1-np.exp((gamma)*days))
    print(beta,gamma,healthy,infected,removed,days,x,y)
    infected = population*(np.exp((beta-gamma)*days))
    removed = infected*gamma*days
    healthy = population -(infected+removed)
    days+=1
    if (infected<0) or (infected>population) or healthy<0 or removed<0 or (healthy>population) or (removed>population):
        print('Done')
        return None
    #World Graph is created
    x.append(days)
    y[0].append(healthy)
    y[1].append(infected)
    y[2].append(removed)
    fig = plt.figure(figsize=(5,5))#Dimension of figure
    ax = plt.subplot(111)
    ax.stackplot(x,y,labels=['Healthy','Infected','Removed'])
    plt.title('World Graph')
    ax.legend()
    ax.set_facecolor((0, 8/225, 30/225))
    fig.patch.set_facecolor((0, 8/225, 30/225))
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    fig.savefig('worldgraph.png')
    
    img = ImageTk.PhotoImage(Image.open("worldgraph.png"))
    panel = Label(lower_right_frame,image = img)
    panel.pack(side = "top", fill = "none", expand = "no")
    
def updatebeta(val):
    global beta
    beta = val
    
def updategamma(val):
    global gamma
    gamma = val
    


upper_frame = Frame(main_window)
upper_frame.pack()
next_button = Button(upper_frame,text = 'Next',command = data).pack(side = LEFT)
info_button = Button(upper_frame,text = 'Info').pack(side = RIGHT)
close_button = Button(upper_frame, text = 'Close',bg = 'red',command = main_window.destroy).pack()
#
lower_frame = Frame(main_window)
lower_frame.configure(bg='#00081e')
lower_frame.pack()

##
lower_left_frame = Frame(lower_frame)
lower_left_frame.configure(bg='#00081e')
lower_left_frame.pack(side = 'left')
img1 = ImageTk.PhotoImage(Image.open("virus.gif"))
panel1 = Label(lower_left_frame,image = img1)
panel1.pack(side = "top", fill = "none", expand = "no")

##
slider_width = 40
slider_height = 15
def set_img_color(img, color):
    """Change color of PhotoImage img."""
    pixel_line = "{" + " ".join(color for i in range(img.width())) + "}"
    pixels = " ".join(pixel_line for i in range(img.height()))
    img.put(pixels)
# normal slider
img_slider = PhotoImage('img_slider', width=slider_width, height=slider_height, master=lower_left_frame)
set_img_color(img_slider, "red")
# active slider
img_slider_active = PhotoImage('img_slider_active', width=slider_width, height=slider_height, master=lower_left_frame)
set_img_color(img_slider_active, '#c42323')
##
style = ttk.Style(lower_left_frame)
style.theme_use('clam')
style.element_create('custom.Horizontal.Scale.slider', 'image', img_slider,
                     ('active', img_slider_active))
style.configure('custom.Horizontal.TScale', background='#00081e', foreground='grey',
                troughcolor='#73B5FA')
beta_label = Label(lower_left_frame,text="beta",bg='#00081e',fg='white').pack()
scale = TickScale(lower_left_frame, from_=0, to=100, tickinterval=100, orient="horizontal",
                  style='custom.Horizontal.TScale',command = updatebeta,).pack()


##beta = Scale(lower_left_frame,from_ = 0,to = 100,bg = '#00081e',variable = beta,orient = HORIZONTAL).pack()

buffer = Label(lower_left_frame,text=' ',bg='#00081e').pack()#

gamma_label = Label(lower_left_frame,text="gamma",bg='#00081e',fg='white').pack()
scale = TickScale(lower_left_frame, from_=0, to=100, tickinterval=100, orient="horizontal",
                  style='custom.Horizontal.TScale',command = updategamma).pack()


##
lower_right_frame = Frame(lower_frame)
lower_right_frame.pack(side='right')
img = ImageTk.PhotoImage(Image.open("worldgraph.png"))
panel = Label(lower_right_frame,image = img)
panel.pack(side = "top", fill = "none", expand = "no")
def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


x.append(days)
y[0].append(healthy)
y[1].append(infected)
y[2].append(removed)
fig = plt.figure(figsize=(5,5))#Dimension of figure
ax = plt.subplot(111)
ax.stackplot(x,y,labels=['Healthy','Infected','Removed'])
plt.title('World Graph')
ax.legend()
ax.set_facecolor((0, 8/225, 30/225))
fig.patch.set_facecolor((0, 8/225, 30/225))
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white') 
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.title.set_color('white')
fig.savefig('worldgraph.png')
    

main_window.mainloop()




