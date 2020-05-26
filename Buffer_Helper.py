#!/usr/bin/env python 

 
import time
import readline  
from Buffer_Package.__Client import  SERVER_BUFFER
from Buffer_Package.__Server import  Buffer_Over
from  Buffer_Package import  Banner

W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m" 

class Buffer_Helper():
                                         
       def __init__(self):
               global W
               global R
               global G
               global O
               global B
               global P
               global Y  
               print Banner.Banner          
               print O+"\n\t\t\t\t<+++++++++|Wellcome to BUffer_Helper|+++++++++>"+W
               print B+"\n\tBuffer_Helepr is Tool Help to Discover Buffer Overflow Vulnerabilities in 'FTP Server' and 'Client FTP''' "+W
               print B+"\n\t\t\t' Buffer_Helper have Two Modes if You Try To Target FTP 'Server' Select mode 1 "+W
               print B+"\n\t\t\t\t\t'To Target 'FTP CLInet'Select Mode 2\n"+W               
               print O+"\t\t ***_***"+W+Y+"NOTE"+W+O+"***_*** "+W
               print B+"\n\t\t**Requide To Start Listener tool**  "+W
               print R+"\n\t\t!_________Generate shellcode and post it in shellcode.py file________! \n"+W
               print O+(" "*25+"="*55)+W
               self.main()
 
       def main(self): 
         try:   
             selcet1= "1"
             selcet2= "2"
             time.sleep(2)
             print O+"\n[E]"+W+B+" Mode "+W+R+"'1'"+W+B+"To Target FTP Server Mode"+W+R+"'2'"+W+B+"To Target FTP Client "+W
             selcet3= str(raw_input(O+"\n[$]"+W+B+"Please Select Mode"+W+R+"'1'"+W+B+" or"+W+R+"'2'"+W+B+": "+W))
             if selcet3 == selcet1 and len(selcet3)==1:
             
                run = Buffer_Over()
                
             elif selcet3 == selcet2 and len(selcet3)==1:
             
                 run = SERVER_BUFFER()
             else:
                 time.sleep(2)
                 print Y+" \n[#]"+W+R+"Please Select Mode"+W
                 return self.main()
         except KeyboardInterrupt:
            print Banner.Banner
            exit()    
if __name__=="__main__":
   Buffer_Helper()    
  
  
  
  
  
             
