from PyQt5 import QtWidgets, QtGui,QtCore
import PyQt5
from PyQt5.QtCore import QTimer,QTime
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import pyjokes
import wikipedia
import psutil
import pyautogui
import operator
import urllib.request
import cv2
import numpy as np
import pyaudio
from requests import get


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():


  hour=datetime.datetime.now().hour

  if hour >= 0 and hour < 12:

      speak("Hello,Good Morning  ,   I am online  ,How Can I Help You ")
 
  elif hour >= 12 and hour < 18:
 
      speak("Hello,Good Afternoon  ,  I am online  ,How Can I Help You ")

  else:

      speak("Hello,Good Evening  ,   I am online   ,How Can I Help You ")
      

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__() 

    def run(self):
        speak("plz say wake up to continue")
        while True:
            self.query=self.STT()
            if 'wake up' in self.query or 'hello diana' in self.query:
               self.DIANA()  

    def STT(self):
        R= sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recognizing......")
            text = R .recognize_google(audio,language='en-in')
            print("User Said ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def DIANA(self):
        wish()
        while True:
            self.query = self.STT()
            if 'goodbye' in self.query:
                speak("Your Virtual voice assistant Diana 1.0 is shutting down , Have a nice day, bye")
                sys.exit()

            elif 'open google' in self.query:
                webbrowser.open_new_tab('www.google.co.in')
                speak (" Google is open now")

            elif 'open youtube' in self.query:
                webbrowser.open_new_tab("www.youtube.com")
                speak("Yotube is open now")

            elif 'play a song' in self.query:
                speak("playing a song from pc")
                self.music_dir ="C:\music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))

            elif 'open flipkart' in self.query:
                webbrowser.open_new_tab('https://www.flipkart.com/')
                speak("flipkart is open now ")


            elif 'open amazon' in self.query:
                webbrowser.open_new_tab('https://www.amazon.com/')
                speak("flipkart is open now ") 


            elif'joke' in self.query:
              speak(pyjokes.get_joke())


            elif'covid ' in self.query:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers') 

            elif 'thank you' in self.query:
                speak('Your welcome ') 

            elif 'cricket' in self.query:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')  

            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences = 2)
                speak("According to Wikipedia")
                speak(results)

                        
            elif 'who are you' in self.query or 'what can you do' in self.query:
                    speak('I am Diana 1.0 , I am your personal assistant , I am programmed to manage your tasks like opening aplications, searching content and solve simple mathematics etcetra')


            elif 'you love me' in self.query or 'do you love me' in self.query:
                    speak('Yes, I love you to from my bottom of my heart')


            elif 'weather ' in self.query:
                news = webbrowser.open_new_tab("https://www.accuweather.com/en/in/mumbai/204842/weather-forecast/204842")
                speak('Here are some wheather reports from accuweather.com')

  
            elif 'covid ' in self.query or 'corona 'in self.query:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)


            elif 'open gmail' in self.query:
                webbrowser.open_new_tab('mail.google.com')
                speak("gmail is open now") 


            elif 'who made you' in self.query or 'who built you' in self.query:
                    speak('I was built by Aditya Parab and Sumit Aware ')  


            elif 'netflix' in self.query:
                news = webbrowser.open_new_tab("netflix.com/browse")
                speak('Netflix is open now')
            

            elif 'search on youtube about' in self.query:
                speak('Searching...')
                self.query =  self.query.replace("search on youtube", "")
                results = webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+ self.query)
                speak("Done")


            elif 'open prime video' in self.query:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")


            # Aditya Parab Special Add On Cammands :-

            elif 'do some calculations' in self.query or 'can you calculate' in self.query:
                speak("why Not")    
                R= sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate,example: 3 plus 3 ,3 multiply by 3")
                    print("listening........")
                    audio=R.listen(source)
                    my_string=R.recognize_google(audio)  
                    print(my_string)
                def get_operator_fn(op):
                    return{
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided':operator.__truediv__,
                         }[op]
                def eval_binary_expr(op1,oper,op2):
                    op1,op2=int(op1),int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))


            elif 'stock market' in self.query:
                    webbrowser.open_new_tab("https://www.moneycontrol.com/stocksmarketsindia/") 
                    speak("Here are the latest stock market news according to moneycontrol.com")


            elif 'news' in self.query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mumbai")
                speak('Here are some headlines from the Times of India, Happy reading')


            elif 'dictionary' in self.query:
                news = webbrowser.open_new_tab("https://www.dictionary.com/")
                speak('Dictionary is open now')


            elif 'flip a coin' in self.query:
                news = webbrowser.open_new_tab("https://www.google.com/search?q=Flip%20a%20coin&stick=H4sIAAAAAAAAAOOwfcQoyS3w8sc9YSmBSWtOXmPk4uJwzs_Mc8vJLOABAAUfYkMeAAAA")
                speak('fliping a coin')


            elif 'find my location' in self.query or 'locate me' in self.query:
                news = webbrowser.open_new_tab("https://www.google.com/maps/@")
                speak('finding your location')

             
            elif 'open instagram ' in self.query:
                news = webbrowser.open_new_tab("https://www.instagram.com/")
                speak('instagram is open now ') 
                
           
            elif 'open facebook ' in self.query:
                news = webbrowser.open_new_tab("https://www.facebook.com/")
                speak('facebook is open now ')


            elif 'how much power left' in self.query or 'how much power we have' in self.query:
                battery =psutil.sensors_battery()
                persentage= battery.percent
                speak(f'sir we have {persentage} percent battery')


                if persentage>=75:
                    speak('we have enough powerto continue our work')


                elif persentage>=40 and persentage<=75:  
                       speak('we should connect our system to charging point to charge our battery')


                elif persentage>=15 and persentage<=30:
                       speak('we dont have enough power to work, plz connect charging point to charge our battery')


                elif persentage<=15:
                     speak('we have very low power, plz connect to charing the system will shutdown very soon')  
                     

            elif "volume up" in self.query or "increase the volume" in self.query:
                pyautogui.press('volumeup')
                speak('volume is increased now')


            elif "volume down" in self.query or "decrease the volume" in self.query:
                pyautogui.press('volumedown')
                speak('volume is decreased now')


            elif "volume mute" in self.query or "mute the volume" in self.query:
                pyautogui.press('volumemute')
                speak('volume is muted now')


            elif "take screenshot" in self.query or "take a screenshot"in self.query:
                speak("please tell me the name for this screenshot file")
                name = self.STT().lower()
                speak("please hold the screen for few seconds,i am taking screenshot")
                time.sleep(3)
                img= pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("your screenshot has been saved , i am ready for next command")


            elif "open mobile camera" in self.query or "access mobile camera" in self.query:
                 speak("Your mobiles camera is open now")
                 URL ="http://192.168.87.219:8080/shot.jpg"
                 while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img=cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;

                    
                 cv2.destroyAllWindows()


            elif "open camera" in self.query:
                 speak(" camera is open now")
                 cap=cv2.VideoCapture(0)
                 while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k ==27:
                        break;

                 cap.release()   
                 cv2.destroyAllWindows()


            elif "switch the window" in self.query or "go to another window" in self.query:
                speak("switching to another tab")
                pyautogui.keyDown("alt") 
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt") 

            
           
            elif "shut down the system" in self.query:
                os.system("shutdown /s ")  


            elif " restart the system" in self.query:
                os.system("shutdown /r ") 


            elif "open notepad" in self.query:
                speak ("notepad is open now")
                os.system(" start notepad")


            elif "open command prompt" in self.query:
                speak ("command prompt is open now")
                os.system(" start cmd")


            elif "search my ip address" in self.query or "Ip address" in self.query:
                speak("searching")
                ip=get('https://api.ipify.org').text
                speak (f"your ip address is {ip}")


            elif "open github " in self.query or "github " in self.query:
                news = webbrowser.open_new_tab("https://github.com/")
                speak ("git hub is open now ")                      
               

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):

    def __init__(self,parent=None):

        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1366,768)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        
        self.ts = time.strftime("%H : %M :%S %p")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_6.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_6.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
