#import libraries
from tkinter import *    
#tkinter is a python Library which is used to create GUI application!
from gtts import gTTS    
#Here we are importing the required module for text to speech conversion!
from playsound import playsound   
#This module is imported so that we can play the converted audio!







#Initializing the window!
root = Tk()                  
#root is the name which we reffer to our window    
#Here Tk() is used to initialize tkinter which will be used for GUI
root.geometry('300x300')     
#Here geometry is used to set height and width of the window!
root.resizable(0,0) #(height=None,width=None)
#resizable() method is used to allow Tkinter root window to change it’s size according to the users need
#as well we can prohibit resizing of the Tkinter window.
root.config(bg = 'Cyan4')    
#Here config is used to acces window attributes!   
#bg is used to set the color of the background! 
root.title('TEXT TO SPEECH') 
#Title is used to set the title of the window!







#creating the icon of the window
root.iconbitmap('C:/Users/User/Desktop/Competitive coding/Week 7/text to speech/Text-to-speech-icon.ico')
#iconbitmap()method is used to set the icon of the window/frame. 
#The bitmap must be an ico type, but not png or jpg type, otherwise  the image will not display as the icon.







#heading of the window (not the title)
#Label() here is a widget, which is used to display one or 
# more than one line of text that users can’t able to modify.
#text will be displayed on the label       
#font is the style of text    
#bg stands for background!
#pack() method is used to declare the position of the widget
#place() method is used to organize widgets by placing them in a specific position(for example x=50,y=40)
Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='sky blue').pack()
Label(root, text ='Enter Text', font ='Helvetica', bg ='sky blue').place(x=20,y=60)
Label(root, text ='By VISHWAJEET ANAND' , font ='arial 15 bold', bg = 'sky blue').pack(side = BOTTOM)







#Msg is a string type variable!
Msg = StringVar()







#Entry() widget is used to accept single-line text strings from the user
#textvariable is used to bring the current text to entry widget
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)







#user define function to convert text to speech
def Text_to_speech():
    Message = entry_field.get()
    #Message variable stores the value of entry_field
    speech = gTTS(text = Message, lang='en', slow=False)  
    #speech stores the converted voice from the text!
    #lang takes the language to read the text. The default language is English.
    #slow use to reads text more slowly. The default is False.
    speech.save('vishwajeet.mp3')  
    #saving the converted audio file in a mp3 file named vishwajeet
    playsound('vishwajeet.mp3')    
    #playing the converted audio file!







#function to exit
def Exit():
    root.destroy()
    #root.destroy() this function will quit the program by stopping the mainloop().







#Reset function 
def Reset():
    Msg.set("")
    #Reset function set Msg variable to empty strings







#Button widget is used to display buttons on the window!
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = 'sky blue', width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'sky blue').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg= 'sky blue').place(x=175 , y =140)
#command is a method to be called when the button is clicked







#infinite loop to run program
root.mainloop()



