# Kivy-mobile-application
A mobile application created with Python's **Kivy v1.11.1**. Packaged in **Ubuntu v20.04.1** on a virtual machine. 

This mobile application demonstrates a platform to share information with recreational fishermen, and in this example the recreational rock lobster sector is the focus. General information on regulations, measuring lobster, closed areas (Marine Protected Areas) etc. are given as well as information that gets updated live; fishing dates, media releases. 

The app links to a Realtime Firebase database where recreational catch data is stored. The data is retrieved from Firebase and used to plot catches with matplotlib. 

An example of the packaged **.apk** is in my [Google Drive](https://drive.google.com/drive/folders/1i4SoU-VHveDU31Y8MAdPZqQrRvS_uyhb?usp=sharing)

These videos give a quick rundown of the app functioning in Jupyter and on the cellphone:
1. Crayfish cellphone.mp4
2. Crayfish Firebase.mp4
3. Crayfish Sql Matplotlib.mp4

## The following files were used to build the Firebase app:

1. CrayfishFirebase.py 
2. CrayfishFirebase.kv
3. Buildozer.spec

## The following files were used to build the SQL version of the app:

1. CrayfishSqlMat.py
2. CrayfishSqlMat.kv
3. RecCatches.py (creating the Sql database) 
4. RecCatches.db 




