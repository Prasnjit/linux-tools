# This project is all about how to install linux tool in a system using browser 
Basic requirement 
      python3 and Above
           Download the latest version of Python:
            sudo apt install python3
      Next, install Django:
      sudo apt install python3-django
       You can test that the installation was successful by typing:
       django-admin --version
IF you have two vesion of python install in your system 
      eg :- python Python 2.7.17  && Python 3.6.9
      only python 3 will work in such case use following command
        python3 manage.py runserver
click on the link and wirte the tool name
Note:- all linux tool is not install in this ways. all the tool are install as a python pip module
to list the install item you can run the command in terminal 
      pip list
      
It will give the lsit of all the tool 
Note:- You may find error while running code 

      python3 manage.py runserver 
      so, go to url and remove import url line the it will work fine 