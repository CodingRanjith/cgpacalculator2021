#!/usr/bin/env python3

""" cgpacalculator2021 	: 	Anna University CGPA Calculator Regulation 2021
    Author      	    : 	CODING RANJITH
    Version     	    : 	1.0
    Github      	    : 	https://github.com/CodingRanjith/cgpacalculator2021 """

# Copyright (C) 2022  CODING RANJITH (https://github.com/CodingRanjith/cgpacalculator2021)

from os import system
from time import sleep

# COLORS #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
orange = "\033[33m"

#def gpacgpa():
    #print("\n1")

def banner():
    print("""\033[91;1m
░█████╗░███╗░░██╗███╗░░██╗░█████╗░  ██╗░░░██╗███╗░░██╗██╗██╗░░░██╗███████╗██████╗░░██████╗██╗████████╗██╗░░░██╗
██╔══██╗████╗░██║████╗░██║██╔══██╗  ██║░░░██║████╗░██║██║██║░░░██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝╚██╗░██╔╝
███████║██╔██╗██║██╔██╗██║███████║  ██║░░░██║██╔██╗██║██║╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║░░░██║░░░░╚████╔╝░
██╔══██║██║╚████║██║╚████║██╔══██║  ██║░░░██║██║╚████║██║░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░░██║░░░░░╚██╔╝░░
██║░░██║██║░╚███║██║░╚███║██║░░██║  ╚██████╔╝██║░╚███║██║░░╚██╔╝░░███████╗██║░░██║██████╔╝██║░░░██║░░░░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░
\nCGPA CLCULATOR REGULATION 2021\t\t\t\033[94;1mVersion : 1.0\t\t\t\033[96;1mKINGS ENIGINEERING COLLEGE
\n\033[97;1m[\033[92;1m-\033[97;1m]\t\033[94;1mTool Created by CODING RANJITH (C.RANJITH KUMAR)
\n\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
\n\t\033[91;1mGPA  : \033[93;1mGRADE POINT AVERAGE
\t\033[91;1mCGPA : \033[93;1mCUMULATIVE GRADE POINTS AVERAGE
\n\033[97;1m[\033[92;1m::\033[97;1m] \033[91;1mDEPARTMENTS\033[97;1m[\033[92;1m::\033[97;1m]
\n\033[97;1m[\033[92;1m01\033[97;1m]\033[33m B.E.-COMPUTER SCIENCE AND ENGINEERING\t\t\033[97;1m[\033[92;1m05\033[97;1m]\033[33m B.E.-MECHANICAL ENGINEERING
\n\033[97;1m[\033[92;1m02\033[97;1m]\033[33m B.TECH-INFORMATION TECHNOLOGY\t\t\t\033[97;1m[\033[92;1m06\033[97;1m]\033[33m B.E.-BIOMEDICAL ENGINEERING
\n\033[97;1m[\033[92;1m03\033[97;1m]\033[33m B.E.-ROBOTICS AND AUTOMATION ENGINEERING\t\t\033[97;1m[\033[92;1m07\033[97;1m]\033[33m B.E.-ELECTRONICS AND COMMUNICATION ENGINEERING
\n\033[97;1m[\033[92;1m04\033[97;1m]\033[33m B.TECH-ARTIFICIAL INTELLIGENCE AND DATA SCIENCE
""")

def course():
    dep=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR DEPARTMENT : " ))
    if(dep==1):
        cse()    
    elif(dep==2):
        it()
    elif(dep==3):
        rae()
    elif(dep==4):
        aids()
    elif(dep==5):
        me()
    elif(dep==6):
        be()
    elif(dep==7):
        ece()                        
    else:
        print("\n\033[97;1m[!] Invalid Option.......")
        sleep(0.5)
        system("clear")
        main()

def smailbanner():
    print("""\033[94;1m

░█▀▀█ ▒█▄░▒█ ▒█▄░▒█ ░█▀▀█ 　 ▒█░▒█ ▒█▄░▒█ ▀█▀ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▀█▀ ▀▀█▀▀ ▒█░░▒█ 
▒█▄▄█ ▒█▒█▒█ ▒█▒█▒█ ▒█▄▄█ 　 ▒█░▒█ ▒█▒█▒█ ▒█░ ░▒█▒█░ ▒█▀▀▀ ▒█▄▄▀ ░▀▀▀▄▄ ▒█░ ░▒█░░ ▒█▄▄▄█ 
▒█░▒█ ▒█░░▀█ ▒█░░▀█ ▒█░▒█ 　 ░▀▄▄▀ ▒█░░▀█ ▄█▄ ░░▀▄▀░ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ ▄█▄ ░▒█░░ ░░▒█░░
                     𝑪𝑮𝑷𝑨 𝑪𝑳𝑪𝑼𝑳𝑨𝑻𝑶𝑹 𝑹𝑬𝑮𝑼𝑳𝑨𝑻𝑰𝑶𝑵 2021
\n\033[97;1m[\033[92;1m::\033[97;1m] \033[91;1mSEMESTERS: \033[97;1m[\033[92;1m::\033[97;1m]
\n\t\033[97;1m[\033[92;1m01\033[97;1m]\033[33m SEMESTER\t\t\033[97;1m[\033[92;1m05\033[97;1m]\033[33m SEMESTER
\n\t\033[97;1m[\033[92;1m02\033[97;1m]\033[33m SEMESTER\t\t\033[97;1m[\033[92;1m06\033[97;1m]\033[33m SEMESTER
\n\t\033[97;1m[\033[92;1m03\033[97;1m]\033[33m SEMESTER\t\t\033[97;1m[\033[92;1m07\033[97;1m]\033[33m SEMESTER
\n\t\033[97;1m[\033[92;1m04\033[97;1m]\033[33m SEMESTER\t\t\033[97;1m[\033[92;1m08\033[97;1m]\033[33m SEMESTER

""")
print("\n")


def cse():
    system("clear")
    smailbanner()
    cse=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(cse==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")
        sa1=int(input("\n\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mCY3171 ENGINEERING CHEMISTRY \t\t\t\t\033[92;1m3  \t\t: "))
        sa2=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mGE3151 PROBLEM SOLVING AND PYTHON PROGRAMMING \t\t\033[92;1m3 \t\t: "))
        sa3=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mHS3151 PROFESSIONAL ENGLISH - 1 \t\t\t\033[92;1m4 \t\t: "))
        sa4=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mMA3151 MATRICES AND CALCULUS \t\t\t\t\033[92;1m4 \t\t: "))
        sa5=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mPH3151 ENGINEERING PHYSICS \t\t\t\t\033[92;1m3 \t\t: "))
        sa6=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mBS3171 PHYSICS AND CHEMISTRY LABORATORY \t\t\033[92;1m2 \t\t: "))
        sa7=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mGE3171 PROBLEM SOLVING AND PYTHON PROGRAMMING LABORATORY\033[92;1m2 \t\t: "))        
        cgpa=sa1*3+sa2*3+sa3*4+sa4*4+sa5*3+sa6*2+sa7*2

        print("\n\033[94;1mTHE FIRST SEMESTER GPA IS : \033[94;1m ",cgpa/21)

    elif(cse==2):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")
        sa1=int(input("\n\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mHS3251 PROFESSIONAL ENGLISH - 2 \t\t\t\033[92;1m3  \t\t: "))
        sa2=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mMA3251 STATISTICS AND NUMERICAL METHODS \t\t\033[92;1m3 \t\t: "))
        sa3=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mPH3256 PHYSICS FOR INFORMATION SCIENCE \t\t\t\033[92;1m4 \t\t: "))
        sa4=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mBE3251 BASIC ELECTRICAL AND ELECTRONICS ENGINEERING \t\033[92;1m4 \t\t: "))
        sa5=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mGE3251 ENGINEERING GRAPHICS \t\t\t\t\033[92;1m3 \t\t: "))
        sa6=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mCS3251 PROGRAMMING IN C \t\t\t\t\033[92;1m2 \t\t: "))
        sa7=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mGE3271 ENGINEERING PRACTICS LABORATORY \t\t\t\033[92;1m2 \t\t: "))
        sa8=int(input("\033[97;1m[\033[92;1m01\033[97;1m]\033[33m\t\033[93;1mCS3271 PROGRAMMING IN C LABORATORY \t\t\t\033[92;1m2 \t\t: "))        
        cgpa=sa1*2+sa2*4+sa3*3+sa4*3+sa5*4+sa6*3+sa7*2+sa8*2

        print("\n\033[94;1mTHE SECOND SEMESTER GPA IS : \033[94;1m ",cgpa/23)
        



    elif(cse==2):
        print("Not updated") 
    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()    

def it():
    system("clear")
    smailbanner()
    it=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(it==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")
    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()        

def rae():
    system("clear")
    smailbanner()
    rae=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(rae==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")   
    
    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()    


def me():
    system("clear")
    smailbanner()
    me=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(me==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")             

    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()    
         
def aids():
    system("clear")
    smailbanner()
    aids=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(aids==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")

    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()    


def be():
    system("clear")
    smailbanner()
    be=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(be==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")  

    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()        

def ece():
    system("clear")
    smailbanner()
    ece=int(input("\033[97;1m[\033[92;1m-\033[97;1m] \033[91;1mENTER YOUR SEMESTER : "))
    if(ece==1):
        system("clear")
        print("""\033[97;1m[\033[92;1m-\033[97;1m]\033[91;1m NOTE:
        \t\033[97;1m[\033[92;1m!\033[97;1m]\033[93;1m ONLY ENTERED POINTS......
        \n\t\033[91;1mLETTER GRADE \t\tGRADE POINTS *
        \n\t\033[93;1mO (Outstanding)\t\t\033[92;1m10
        \033[93;1mA+ (Excellent)\t\t\033[92;1m9
        \033[93;1mA (Very Good)\t\t\033[92;1m8
        \033[93;1mB+ (Good)\t\t\033[92;1m7
        \033[93;1mB (AVerage)\t\t\033[92;1m6
        \033[93;1mC (Satisfactory)\t\033[92;1m5
        """)
        print("""\n\033[91;1mSEM\t\tSUBJECT\t\t\t\t\t\tCREDITS\t\tPOINTS *""")  

    else:
        system("clear")
        print("\n\n\tNo update for Anna University............")
        sleep(1)
        main()                   

def main():
    system("clear")
    banner()
    course()
main()


