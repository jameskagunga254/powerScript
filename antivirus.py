
import re
import subprocess
import smtplib


# the program is checking for the known ports that are used mostly by hackers and then it reports using email


def check_port():


    hackers_port=['8080','5677','68','4556']


    command="netstat -tulnp"

    response=subprocess.check_output(command,shell=True)

    ports=re.findall('(?:\d*.\d*.\d*.\d*:)(\d*\s)',response)


    for port in ports:

        port=port.strip()

        if port in hackers_port:

            return "[-]threat has been found" + str(port)

        else:

            pass


def sendmail(email,password,message):

    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(email,password)

    server.sendmail(email,email,message)

    server.quit()


threat=check_port()

if threat:

    sendmail("ancestor15@gmail.com","fibonacci",threat)
    

    
    


