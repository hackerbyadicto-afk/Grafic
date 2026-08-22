import gradio as gr
from matplotlib import pyplot as plt
import numpy as np
import math
import os
def draw(n):
    x=np.linspace(-100,100,2000)
    plt.axhline(0)
    plt.axvline(0)
    x=np.array(x)
    n=eval(n,{"x":x,"np":np})
    plt.plot(x,n,lw=3,marker=".",ms=5,mfc="red",markevery=100)
    plt.grid()
    return plt.gcf()
gr.Interface(fn=draw,inputs=gr.Textbox(label="Enter your Function : "),outputs=gr.Plot(label="Grafic")).launch(server_name="0.0.0.0",server_port=int(os.environ.get("PORT",7860)))
