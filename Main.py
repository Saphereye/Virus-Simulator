from tkinter import*
from PIL import ImageTk, Image
import os
os.chdir(os.getcwd())
import matplotlib.pyplot as plt
import matplotlib
from tkinter import ttk
from ttkwidgets import TickScale
import numpy as np
from scipy.integrate import odeint
matplotlib.use('TkAgg')
import time
#Ro = beta/gamma

N = 1000
I0, R0 = 1, 0
S0 = N - I0 - R0
beta, gamma = 0.23, 0.17

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
t = np.linspace(0,500,500)
def data():
    global N,S0,I0,R0,beta,gamma,limit,t,newWindow,panelq
    newWindow = Toplevel(main_window)
    newWindow.title('Graph')
    close_button = Button(newWindow, text = 'Close',bg = 'red',command = newWindow.destroy).pack()
    newWindow.configure(bg='#00081e')
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt
    y0 = S0, I0, R0
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered')
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')
    ax.set_ylim(0,1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    ax.set_facecolor((0, 8/225, 30/225))
    fig.patch.set_facecolor((0, 8/225, 30/225))
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
        
    fig.savefig('worldgraph.png')
    imgq = ImageTk.PhotoImage(Image.open("worldgraph.png"))
    panelq = Label(newWindow,image = imgq).pack(fill = "none", expand = "no")
    panelq.configure(bg='#00081e')
    print(beta,gamma)
##def updatebeta(val):
##    global beta
##    beta = val
##    
##def updategamma(val):
##    global gamma
##    gamma = val
##    


upper_frame = Frame(main_window)
upper_frame.pack()
next_button = Button(upper_frame,text = 'Create Graph',command = data).pack(side = LEFT)
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
def set_img_color(img, color):
    """Change color of PhotoImage img."""
    pixel_line = "{" + " ".join(color for i in range(img.width())) + "}"
    pixels = " ".join(pixel_line for i in range(img.height()))
    img.put(pixels)

beta_button = Button(lower_left_frame, text=f"Rate of infection(0% to 100%) = {round(beta*100,2)}%",bg='#00081e',fg='white').pack()
gamma_button = Button(lower_left_frame, text = f"Rate of deaths/immunity(0% to 100%) = {gamma*100}%",bg='#00081e',fg='white').pack()
### normal slider
##img_slider = PhotoImage('img_slider', width=slider_width, height=slider_height, master=lower_left_frame)
##set_img_color(img_slider, "red")
### active slider
##img_slider_active = PhotoImage('img_slider_active', width=slider_width, height=slider_height, master=lower_left_frame)
##set_img_color(img_slider_active, '#c42323')
####
##style = ttk.Style(lower_left_frame)
##style.theme_use('clam')
##style.element_create('custom.Horizontal.Scale.slider', 'image', img_slider,
##                     ('active', img_slider_active))
##style.configure('custom.Horizontal.TScale', background='#00081e', foreground='grey',
##                troughcolor='#73B5FA')
##beta_label = Label(lower_left_frame,text="beta",bg='#00081e',fg='white').pack()
##scale = TickScale(lower_left_frame, from_=0, to=100, tickinterval=100, orient="horizontal",
##                  style='custom.Horizontal.TScale').pack()
##
##
####beta = Scale(lower_left_frame,from_ = 0,to = 100,bg = '#00081e',variable = beta,orient = HORIZONTAL).pack()
##
##buffer = Label(lower_left_frame,text=' ',bg='#00081e').pack()#
##
##gamma_label = Label(lower_left_frame,text="gamma",bg='#00081e',fg='white').pack()
##scale = TickScale(lower_left_frame, from_=0, to=100, tickinterval=100, orient="horizontal",
##                  style='custom.Horizontal.TScale').pack()

   

##
##lower_right_frame = Frame(lower_frame)
##lower_right_frame.pack(side='right')
##img = ImageTk.PhotoImage(Image.open("worldgraph.png"))
##panel = Label(lower_right_frame,image = img)
##panel.pack(side = "top", fill = "none", expand = "no")
def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


##x.append(days)
##y[0].append(healthy)
##y[1].append(infected)
##y[2].append(removed)
##fig = plt.figure(figsize=(5,5))#Dimension of figure
##ax = plt.subplot(111)
##ax.stackplot(x,y,labels=['Healthy','Infected','Removed'])
##plt.title('World Graph')
##ax.legend()
##ax.set_facecolor((0, 8/225, 30/225))
##fig.patch.set_facecolor((0, 8/225, 30/225))
##ax.spines['bottom'].set_color('white')
##ax.spines['top'].set_color('white') 
##ax.spines['right'].set_color('white')
##ax.spines['left'].set_color('white')
##ax.tick_params(axis='x', colors='white')
##ax.tick_params(axis='y', colors='white')
##ax.yaxis.label.set_color('white')
##ax.xaxis.label.set_color('white')
##ax.title.set_color('white')
##fig.savefig('worldgraph.png')
##    

main_window.mainloop()
