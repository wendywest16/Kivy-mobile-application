#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Installed Kivy in cmd from their website kivy.org. Followed steps 1-3 in the "Installing the kivy stable release"
#In cmd typed in kivy_venv\Scripts\activate in order to work in the kivy virtual environment. What that means?
import kivy


# In[2]:


#Stops the fullscreen mode
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '900')


# In[3]:


from kivy.app import App


# In[4]:


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
from kivy.uix.spinner import Spinner 
#import sqlite3
import pyrebase
import requests
import json

from KivyCalendar import DatePicker

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas


# In[5]:


LabelBase.register(name="BattelLines", fn_regular= 'BattleLines.ttf')
LabelBase.register(name="MarkingPenRegular", fn_regular= 'MarkingPen Regular.ttf')


# In[6]:


#Holds the desgin elements. Widgets that appear in the .kv file. Popup widget can only have one sub-layer
#class Popup(Popup):
#    pass

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init) #List all id label functions here?

    def _finish_init(self, dt):

        #Get database data
        result = requests.get('https://crayfish1-faf11.firebaseio.com/fishingdates.json')
        data=json.loads(result.content.decode())

        #Assign database data to label id
        fdtitle_text = self.ids['title_text'] #Kivy label
        fdtitle_text.text = data['title'] #Database label
        
        date1_text = self.ids['1date'] #Kivy label
        date1_text.text = data['1date'] #Database label
        day1_text = self.ids['1day'] #Kivy label
        day1_text.text = data['1day'] #Database label
        lowtide1_text = self.ids['1lowtide'] #Kivy label
        lowtide1_text.text = data['1lowtide'] #Database label
        
        date2_text = self.ids['2date'] #Kivy label
        date2_text.text = data['2date'] #Database label
        day2_text = self.ids['2day'] #Kivy label
        day2_text.text = data['2day'] #Database label
        lowtide2_text = self.ids['2lowtide'] #Kivy label
        lowtide2_text.text = data['2lowtide'] #Database label
        
        date3_text = self.ids['3date'] #Kivy label
        date3_text.text = data['3date'] #Database label
        day3_text = self.ids['3day'] #Kivy label
        day3_text.text = data['3day'] #Database label
        lowtide3_text = self.ids['3lowtide'] #Kivy label
        lowtide3_text.text = data['3lowtide'] #Database label
        
        date4_text = self.ids['4date'] #Kivy label
        date4_text.text = data['4date'] #Database label
        day4_text = self.ids['4day'] #Kivy label
        day4_text.text = data['4day'] #Database label
        lowtide4_text = self.ids['4lowtide'] #Kivy label
        lowtide4_text.text = data['4lowtide'] #Database label
        
        date5_text = self.ids['5date'] #Kivy label
        date5_text.text = data['5date'] #Database label
        day5_text = self.ids['5day'] #Kivy label
        day5_text.text = data['5day'] #Database label
        lowtide5_text = self.ids['5lowtide'] #Kivy label
        lowtide5_text.text = data['5lowtide'] #Database label
        
        date6_text = self.ids['6date'] #Kivy label
        date6_text.text = data['6date'] #Database label
        day6_text = self.ids['6day'] #Kivy label
        day6_text.text = data['6day'] #Database label
        lowtide6_text = self.ids['6lowtide'] #Kivy label
        lowtide6_text.text = data['6lowtide'] #Database label
        
        date7_text = self.ids['7date'] #Kivy label
        date7_text.text = data['7date'] #Database label
        day7_text = self.ids['7day'] #Kivy label
        day7_text.text = data['7day'] #Database label
        lowtide7_text = self.ids['7lowtide'] #Kivy label
        lowtide7_text.text = data['7lowtide'] #Database label
        
        date8_text = self.ids['8date'] #Kivy label
        date8_text.text = data['8date'] #Database label
        day8_text = self.ids['8day'] #Kivy label
        day8_text.text = data['8day'] #Database label
        lowtide8_text = self.ids['8lowtide'] #Kivy label
        lowtide8_text.text = data['8lowtide'] #Database label
        
        date9_text = self.ids['9date'] #Kivy label
        date9_text.text = data['9date'] #Database label
        day9_text = self.ids['9day'] #Kivy label
        day9_text.text = data['9day'] #Database label
        lowtide9_text = self.ids['9lowtide'] #Kivy label
        lowtide9_text.text = data['9lowtide'] #Database label
        
        date10_text = self.ids['10date'] #Kivy label
        date10_text.text = data['10date'] #Database label
        day10_text = self.ids['10day'] #Kivy label
        day10_text.text = data['10day'] #Database label
        lowtide10_text = self.ids['10lowtide'] #Kivy label
        lowtide10_text.text = data['10lowtide'] #Database label
        
        date11_text = self.ids['11date'] #Kivy label
        date11_text.text = data['11date'] #Database label
        day11_text = self.ids['11day'] #Kivy label
        day11_text.text = data['11day'] #Database label
        lowtide11_text = self.ids['11lowtide'] #Kivy label
        lowtide11_text.text = data['11lowtide'] #Database label
        
        date12_text = self.ids['12date'] #Kivy label
        date12_text.text = data['12date'] #Database label
        day12_text = self.ids['12day'] #Kivy label
        day12_text.text = data['12day'] #Database label
        lowtide12_text = self.ids['12lowtide'] #Kivy label
        lowtide12_text.text = data['12 lowtide'] #Database label
    
class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class SixthWindow(Screen):
    pass

class SeventhWindow(Screen):
    
    def datepicker(self):
        super(SeventhWindow, self).__init__()
    
    def patch(self, permitnr, nrlobster, fdate, area):
        url = 'https://crayfish1-faf11.firebaseio.com/catches.json' 
        permitdata = {"permitnr": permitnr, "nrlobster": nrlobster, "fdate": fdate, "area":area}
        requests.post(url = url, json = permitdata)
    
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""


# In[7]:


class Namaqua(Screen):
    pass

class StompneusShelly(Screen):
    pass

class WestCoast(Screen):
    pass


# In[8]:


config = {
    "apiKey": "AIzaSyBNBq3Fvfom87qKMM2ChpawxkuLjst6gFI",
    "authDomain": "crayfish1-faf11.firebaseapp.com",
    "databaseURL": "https://crayfish1-faf11.firebaseio.com",
    "projectId": "crayfish1-faf11",
    "storageBucket": "crayfish1-faf11.appspot.com",
    "messagingSenderId": "751214937520",
    "appId": "1:751214937520:web:4a859a70ed484fcb228275",
    "measurementId": "G-JKKRELREYN"
}

class EighthWindow(Screen):
    

    def __init__(self, **kwargs):
            super(EighthWindow, self).__init__(**kwargs)
            Clock.schedule_once(self._finish_init) #List all id label functions here?

    def _finish_init(self, dt):

        #Get database data
        result = requests.get('https://crayfish1-faf11.firebaseio.com/media.json')
        data=json.loads(result.content.decode())

        #Assign database data to label id
        media1_text = self.ids['media1_text'] #Kivy label
        media1_text.text = data['media1'] #Firebase label
        
        media2_text = self.ids['media2_text'] #Kivy label
        media2_text.text = data['media2'] #Firebase label
        
        media3_text = self.ids['media3_text'] #Kivy label
        media3_text.text = data['media3'] #Firebase label
        
    def Retrieve(self):
        
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "/media/190926 Media Statement TAC determined for the 2019-2020 WCRL TAC Fishing Season.pdf"  #Document to fetch
        #path_local ='Letter.pdf' #Document to upload
        #storage.child(path_on_cloud).put(path_local)  #Upload files
        storage.child(path_on_cloud).download("WCRL_1920_announcement.pdf") #Download files
        
    def Retrieve2(self):
               
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "/media/Postponement Notice WCRL Recreational 2 days.pdf"  #Document to fetch
        #path_local ='Letter.pdf' #Document to upload
        #storage.child(path_on_cloud).put(path_local)  #Upload files
        storage.child(path_on_cloud).download("WCRL_Apr_postponed.pdf") #Download files
    
    def Retrieve3(self):
        
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "/media/Public Notice WCRL Recreational last two fishing days.pdf"  #Document to fetch
        #path_local ='Letter.pdf' #Document to upload
        #storage.child(path_on_cloud).put(path_local)  #Upload files
        storage.child(path_on_cloud).download("WCRL_Jun20.pdf") #Download files


# In[9]:


class NinthWindow(Screen):
    bar = ObjectProperty(None)
    
    
    def add_plot(self, *args):
        
        plt.cla()
        self.bar.clear_widgets()
        #----------------------------------------------------------------------------------------
        
        #--------------------------------------------------------------------------------------------
        df = pd.read_json (r'https://crayfish1-faf11.firebaseio.com/catches.json')
        df1 = df.transpose()
        df1[['nrlobster']] = df1[['nrlobster']].astype(int)
        df2 = df1.groupby('area')['nrlobster'].sum().reset_index(name ='Total Amount lobster')
        df3 = df1.groupby('area')['permitnr'].nunique().reset_index(name ='Number of fishers')
        
        #-------------------------------------------------------------    
        fig = plt.figure()
        fig.suptitle('2019/2020 recreational catches', fontsize=16, color = "white")
        
        host = fig.add_subplot(111) #Main plot
        par1 = host.twinx() #Secondary plot, same x-axis
       
        host.set_xlabel("Area", color = "white") #Same x-axis for main and secondary
        host.tick_params(axis='x', colors="white")
        host.tick_params(axis='y', colors="darkgrey")
        host.set_ylabel("Number of crayfish kept", color="darkgrey", fontsize = 14) #Main y-axis
        par1.set_ylabel("Number of active fishers", color="lightseagreen", fontsize = 14) #Secondary y-axis
        par1.set_yticks(np.arange(0, 5, 2)) #Secondary y-axis tick marks
        par1.tick_params(axis='y', colors="lightseagreen")
       
        host.bar(df2['area'],df2['Total Amount lobster'], label='Avg nr crayfish', color="darkgrey") #Main bar plot
        par1.plot(df3['area'],df3['Number of fishers'], label='Nr fishers', color='lightseagreen', marker='o',linewidth=0, markersize=12) #Secondary dot plot
        
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


# In[10]:


class WindowManager(ScreenManager): #represents the transition between windows
    pass


# In[11]:


kv=Builder.load_file("CrayfishFirebase.kv")


# In[12]:


#Runs the app, refers to the .kv file
class MyMainApp(App):
 
    def build(self):
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


# In[13]:


#Run the app
if __name__ == "__main__":
    reset()
    MyMainApp().run()


# In[ ]:




