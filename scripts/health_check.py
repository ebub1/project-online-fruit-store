#!/usr/bin/env python3

import psutil
import shutil
import socket
import os

disk = shutil.disk_usage("/")
available_dsk_percentage = disk.free/disk.total
mem = psutil.virtual_memory()
available_memory = mem.free

#send email
def send_email(subject_line):
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()

    msg['Subject'] = subject_line
    msg['From'] = "@example.com"
    msg['To'] = "{}@example.com".format(os.environ["USER"])
    body = "Please check your system and resolve the issue as soon as possible."
    msg.set_content(body)
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

#Check CPU usage
if  psutil.cpu_percent(4) > 80:
    subject_line = "Error - CPU usage is over 80%"
    send_email(subject_line)
#Check disk space
if available_dsk_percentage > 20:
    subject_line = "Error - Available disk space is less than 20%"
    send_email(subject_line)
#Check memory
if available_memory < 524288000:
    subject_line = "Error - Available memory is less than 500MB"
    send_email(subject_line)
#Check localhost
if socket.gethostbyname("localhost") != "127.0.0.1":
    subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
    send_email(subject_line)