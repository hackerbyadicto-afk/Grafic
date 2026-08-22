import gradio as gr
from matplotlib import pyplot as plt
import numpy as np
import math
import mplcursors
def draw(n):
    x=np.linspace(-100,100,2000)
    plt.axhline(0)
    plt.axvline(0)
    x=np.array(x)
    n=eval(n,{"x":x,"np":np})
plt.plot(x,n,marker=".",ms=20,mfc="red")
    cursor=mplcursors.cursor(hover=True)
    @cursor.connect("add")
    def on_add(sel):
        x_val,y_val=sel.target
        sel.annotation.set_text(f"X:{x_val:.0f}\nY: {y_val:.0f}")
    plt.grid()
    return plt.gcf()
gr.Interface(fn=draw,inputs=gr.Textbox(label="Enter your Function : "),outputs=gr.Plot("Grafic")).launch()
