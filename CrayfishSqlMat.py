#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Installed Kivy in cmd from their website kivy.org. Followed steps 1-3 in the "Installing the kivy stable release"
#In cmd typed in kivy_venv\Scripts\activate in order to work in the kivy virtual environment. What that means?
import kivy


# In[2]:


#from kivy.core.window import Window
#Window.size = (300, 100)


# In[3]:


#Stops the fullscreen mode
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')


# In[4]:


from kivy.app import App


# In[ ]:


from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.core.text import LabelBase #For text fonts
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView
from kivy.factory import Factory
#from kivy.uix.spinner import Spinner 
import sqlite3 #Needed for submission of catches
#import pyrebase #Needed for Firebase
#import requests #Needed for Firebase
#import json #Needed for Firebase

#from KivyCalendar import DatePicker

#import pandas as pd #Needed for plotting with Firebase
import numpy as np  #Needed for plotting
import matplotlib #Needed for plotting
import matplotlib.pyplot as plt #Needed for plotting
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy") #Needed for plotting
from kivy.garden.matplotlib import FigureCanvasKivyAgg #Needed for plotting
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas #Needed for plotting


# In[ ]:


LabelBase.register(name="BattelLines", fn_regular= 'BattleLines.ttf')
LabelBase.register(name="MarkingPenRegular", fn_regular= 'MarkingPen Regular.ttf')


# In[ ]:


#Holds the desgin elements. Widgets that appear in the .kv file. Popup widget can only have one sub-layer
class Popup(Popup):
    pass

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass   

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class SixthWindow(Screen):
    pass

class SeventhWindow(Screen):
    
    permitnr = ObjectProperty(None)
    nrlobster = ObjectProperty(None)
    #spinner_id = ObjectProperty(None)
    #spinner_id_1 = ObjectProperty(None)
    fmonth = ObjectProperty(None)
    fyear = ObjectProperty(None)
    area = ObjectProperty(None)
    
    #def spinner_clicked(self, value): 
    #    print("Date is " + value) 
    
    #def button_submit(self):
    #    print("Permit nr: ", self.permitnr.text, "Date: ", self.spinner_id.text, "Area: ", self.spinner_id_1.text, "Nr lobster: ", self.nrlobster.text)
    
    
    def register(self):
        con = sqlite3.connect("reccatches1.db")
        cur = con.cursor()
        if self.ids["permitnr"].text and self.ids["nrlobster"].text and self.ids["fmonth"].text and self.ids["fyear"].text and self.ids["area"].text is not None:
            p = self.ids["permitnr"].text
            n = self.ids["nrlobster"].text
            m = self.ids["fmonth"].text
            y = self.ids["fyear"].text
            a = self.ids["area"].text
            cur.execute("INSERT INTO RecCatches VALUES(?, ?, ?, ?, ?)",(p, n, m, y, a))
            #self.manager.current = "user"
            con.commit()
    
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""
    


# In[ ]:


class Namaqua(Screen):
    pass

class StompneusShelly(Screen):
    pass

class WestCoast(Screen):
    pass


# In[ ]:


class EighthWindow(Screen):
    pass


# In[ ]:


con = sqlite3.connect('reccatches1.db')
c = con.cursor()

class NinthWindow(Screen):
    bar = ObjectProperty(None)
    
    
    def add_plot(self, *args):
        #plt.clf()
        #plt.cla()
        plt.cla()
        self.bar.clear_widgets()
        #----------------------------------------------------------------------------------------
        c.execute('SELECT area, count(distinct permitnr) as nrfishers FROM reccatches GROUP BY area')
        data = c.fetchall()

        area = []
        nrfishers = []

        for row in data:
            area.append(row[0])
            nrfishers.append(row[1])

        #----------------------------------------------------------------------------------------
        c.execute('SELECT area, avg(nrlobster) as avglobster FROM reccatches GROUP BY area')
        data = c.fetchall()

        area = []
        avglobster = []

        for row in data:
            area.append(row[0])
            avglobster.append(row[1])

        #-------------------------------------------------------------    
        fig = plt.figure()
        fig.suptitle('2019/2020 recreational catches', fontsize=16, color = "white")
        
        host = fig.add_subplot(111) #Main plot
        par1 = host.twinx() #Secondary plot, same x-axis
       
                
        host.set_xlabel("Area", color = "white") #Same x-axis for main and secondary
        host.tick_params(axis='x', colors="white")
        host.tick_params(axis='y', colors="darkgrey")
        host.set_ylabel("Average number of crayfish kept", color="darkgrey", fontsize = 14) #Main y-axis
        par1.set_ylabel("Number of active fishers", color="lightseagreen", fontsize = 14) #Secondary y-axis
        par1.set_yticks(np.arange(0, 5, 2)) #Secondary y-axis tick marks
        par1.tick_params(axis='y', colors="lightseagreen")
       
        host.bar(area,avglobster, label='Avg nr crayfish', color="darkgrey") #Main bar plot
        par1.plot(area,nrfishers, label='Nr fishers', color='lightseagreen', marker='o',linewidth=0, markersize=12) #Secondary dot plot
        
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        self.fig1 = NinthWindow.add_plot(self,1000)
        self.bar.add_widget(FigureCanvasKivyAgg(self.fig1))

    def Update(self):
        #self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        plt.cla()
        self.bar.clear_widgets()
        self.fig1 = NinthWindow.add_plot(self,1000)
        self.bar.add_widget(FigureCanvasKivyAgg(self.fig1))
        
    


# In[ ]:


class WindowManager(ScreenManager): #represents the transition between windows
    pass


# In[ ]:


kv=Builder.load_file("CrayfishSqlMat.kv")


# In[ ]:


#Runs the app, refers to the .kv file
class MyMainApp(App):
    def show_popup(self, dt):        
        Popup().open()  
      
    def build(self):
        Clock.schedule_once(self.show_popup, 0.1)
        return kv

    
def reset():  #Needed in order to run the app multiple times
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}


# In[ ]:


#Run the app
if __name__ == "__main__":
    reset()
    MyMainApp().run()


# In[ ]:




