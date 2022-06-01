import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st
from PIL import Image
from playsound import playsound
import time

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
audio_file = open('Alarm.wav', 'rb')
audio_bytes = audio_file.read()
i=0
x1=10000
y1=10000
a1=10000
b1=10000
c1=10000
d1=10000
e1=10000
f1=10000
image = Image.open('Sensor.png')
st.image(image, caption='DFC Mine', width=1000)
while i == 0:
#Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/1708546/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if x1 != x:
  if x > 22:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20temperatures%20above%2022%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1th/main/S1TH.py)")
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 15:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20temperatures%20below%2015%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1tl/main/S1TL.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
 x1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1708546/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if y1 != x:
  if x > 50:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20humidity%20levels%20above%2050%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1hh/main/S1HH.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 0:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20humidity%20levels%20below%200%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1hl/main/S1HL.py)") 
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
 y1=x
#Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if a1 != x:
  if x > 22:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20temperatures%20above%2022%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2th/main/S2TH.py)")
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 15:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20temperatures%20below%2015%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2tl/main/S2TL.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
 a1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if b1 != x:
  if x > 50:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20humidity%20levels%20above%2050%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2hh/main/S2HH.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 0:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20humidity%20levels%20below%200%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2hl/main/S2HL.py)") 
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
  b1=x
 #Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if c1 != x:
  if x > 22:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20temperatures%20above%2022%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3th/main/S3TH.py)")
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 15:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20temperatures%20below%2015%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3tl/main/S3TL.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
 c1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if d1 != x:
  if x > 50:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20humidity%20levels%20above%2050%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3hh/main/S3HH.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 0:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20humidity%20levels%20below%200%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3hl/main/S3HL.py)") 
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
 d1=x
 #Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738082/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if e1 != x:
  if x > 22:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20temperatures%20above%2022%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4th/main/S4TH.py)")
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 15:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20temperatures%20below%2015%20degree%20celcius%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4tl/main/S4TL.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
 e1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/1738082/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if f1 != x:
  if x > 50:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20humidity%20levels%20above%2050%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4hh/main/S4HH.py)")  
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  elif x < 0:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20humidity%20levels%20below%200%Percent%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4hl/main/S4HL.py)") 
   st.audio(audio_bytes, format='audio/wav', start_time=0)
  else:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
 f1=x
 time.sleep(6)
i=0




