# woc3.0-ecommerce-price-tracker-Taksh-Bhatt
This repository contains all files for project of web scrapping and automation using python, Django and Selenium

The **Scripts** directory contains python scripts that perform web scrapping and automation only, i.e. it does not contain any Django part.

The **django_part** directory contains **all** the required python and Django scripts which include web scrapping and automation scripts as well as Django part.

## To run the scripts in **Scripts** directory, follow the below steps:
(1) Open **main.py** file in Scripts directory.

(2) On line number 10 where it is written in double quotes("______Your email Id goes here___"), replace the text(not double quotes) with your email Id.
(3) On line number 12 where it is written in double quotes("___The password goes here___"), replace the text(not double quotes) with the app password(not that with which you login)
    that email service provider gives for your device.
(4) Finally, run **main.py** file.


## To run the whole project, open **django_part** directory, and follow the below steps:
(1) Open **Flibazon** directory.
(2) Open **main_script.py** file in it.
(3) On line number 14 where it is written in double quotes("___Your email Id goes here___"), replace the text(not double quotes) with your email Id.
(4) On line number 16 where it is written in double quotes("___The password goes here___"), replace the text(not double quotes) with the app password(not that with which you login)
    that email service provider gives for your device.
(5) Now, open **python console**(not terminal) of your python IDE and run following two commands:
      (i) From Flibazon import main_script
      (ii) main_script.run_main_script()
    These will start the backend process of scrapping websites and sending automated emails **even if the server is off**. The **main_script** will keep on running at
    every **10 second** interval until you stop it.
(6) Finally, open terminal, set the current directory as your project directory and run the following command:
      (i) python manage.py runserver
    This will start the server and then click on the link it provides at last to run the website.
