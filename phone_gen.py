#Use With Python 3
import requests,re,sys,random,time,os
import os
from colorama import Fore, Back, init
from threading import Thread
init (autoreset = True)
from random import choice
init()
def logo():
    os.system('cls')
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
 
                ██╗  ██╗███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗ 
                ╚██╗██╔╝████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║ 
                 ╚███╔╝ ██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║ 
                 ██╔██╗ ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║ 
                ██╔╝ ██╗██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗
                    ╚═╝  ╚═╝╚═╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝ 
                                 CODED BY XEON :")
                        
                       Bulk Phone Number Generator V1.0   |  Coded by xMarvel ( xeon )                          
                                         Greetinz to : Mad-Hacker    
                      
                                [+] My Telegram: @xe0on      [+]
                                [+]Author: XEON              [+]
                                [+]Support: @xMarvel_support [+]
                                [+]Channel: @xMarvel_OfficIal[+]
                                          
                              +-------- With Great Power Comes Great Toolz! --------+

			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

print('-'*33)
cc = input(str('Enter the Country Code { EX +1 For USA } : '))
print('-'*33)
sc = input(str('Enter the Area Code { EX 910 } : '))
print('-'*33)
n = int(input("Enter Amount of numbers: "))
print('-'*33)
lent = int(input('Length Remaining Digits [ 7 FOR USA ] : '))
print('-'*33)
mow = str('9'*lent)
print('-'*33)
def random_phone_num_generator():
    first = str(random.randint(0,int(mow))).zfill(lent)
    return (first)

save = open('Phone.txt','a+')
for i in range(0,n):
    rez = cc+sc+random_phone_num_generator()
    save.write(rez + '\n')
print('Phone Numbers Saved In Phone.txt')
input('Enter any Key to exit')


