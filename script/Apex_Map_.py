import requests
import subprocess, sys
from datetime import datetime
from datetime import timedelta
import csv

url="https://apexlegendsstatus.com/current-map"
r = requests.get(url)
map_title= r.text.split("<h1 style=\"font-weight: 600; margin-bottom: 5px;\">Battle Royale: ")[1].split("</h1>")[0]
time_until=(r.text.split("</span> to <span data-tz=\"")[1][12:17])
time_object = datetime.strptime(time_until, '%H:%M')
Time_next= time_object +  timedelta(hours=5, minutes=30)
Time_next=str(Time_next)[11:16]
Final_output ="until " + Time_next + " hrs!"
print(Final_output)
# subprocess.call([r'New-BurntToastNotification -AppLogo "C:\Users\HP\Desktop\RPA SCE\Python only solution\APEX ICON bg-removed.png" -HeroImage "C:\Users\HP\Desktop\RPA SCE\Python only solution\olympus.png" -Text Apex Legends Map Rotation, map_title, Final_output'])

powershell=r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
app_logo=r"C:\Users\HP\Desktop\CPP\imagesd\apex.png"
title='\'Apex Legends Map Rotation\''
Final_output='\''+Final_output+'\''
O=r"C:\Users\HP\Desktop\CPP\imagesd\olympus.png"
W=r"C:\Users\HP\Desktop\CPP\imagesd\worldsedge.png"
K=r"C:\Users\HP\Desktop\CPP\imagesd\kingscanyon.png"
B=r"C:\Users\HP\Desktop\CPP\imagesd\brokenmoon.jpg"
S=r"C:\Users\HP\Desktop\CPP\imagesd\stormpoint.webp"
image=r"C:\Users\HP\Desktop\CPP\imagesd\apex.png"
if(map_title == 'Olympus'):
    image=O
if(map_title == 'Broken Moon'):
    image=B
if(map_title == 'King\'s Canyon'):
    map_title="King''s Canyon"
    image=K
if(map_title == 'World\'s Edge'):
    map_title="World''s Edge"
    image=W
if(map_title == 'Stormpoint'):
    image=S
map_title='\''+map_title+'\''
subprocess.run(f'{powershell} New-BurntToastNotification -AppLogo {app_logo} -HeroImage {image} -Text {title}, {map_title}, {Final_output}')
