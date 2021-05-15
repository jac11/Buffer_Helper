#!/usr/bin/env python2 

 
import time
import readline 

from Buffer_Package             import  Banner 
from Buffer_Package.__Server    import  SERVERSOCKET
from Buffer_Package.__Client    import  LISTEN_BIND
from Buffer_Package.HTTP_LOGIN  import  HTTPLOGIN

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
               print B+"\n\tBuffer_Helepr it's Tool Help for classic Buffer Overflow Vulnerabilities "+W  
               print
               print O+"\t\t ***_***"+W+Y+"NOTE"+W+O+"***_*** "+W
               print B+"\n\t\t**Requide To Start Listener tool**  "+W
               print R+"\n\t\t!_________Generate shellcode and post it in shell_code.py file________! \n"+W
               print O+(" "*25+"="*55)+W
               self.main()
 
       def main(self): 
         try:   
             selcet1= "1"
             selcet2= "2"
             selcet3= "3"
             time.sleep(2)
             print O+"\n[+]"+W+B+" selcet Mode "+W
             print Y+"="*20+W
             print
             print R+"\n[*]"+W+Y+"'1')"+W+B+ " To Target Server "+W
             print R+"\n[*]"+W+Y+"'2')"+W+B+ " To Target FTPClient "+W
             print R+"\n[*]"+W+Y+"'3')"+W+B+ " To Target HTTP Login Page"+W
             selcet4= str(raw_input(O+"\n[$]"+W+B+"Please Select Mode : "+W))
             if selcet4 == selcet1 and len(selcet4)==1:             
                run = SERVERSOCKET()                
             elif selcet4 == selcet2 and len(selcet4)==1:             
                 run = LISTEN_BIND()
             elif selcet4 == selcet3 and len(selcet4)==1: 
                 run = HTTPLOGIN()
             else:
                 time.sleep(2)
                 print Y+" \n[#]"+W+R+"Please Select Mode"+W
                 return self.main()
         except KeyboardInterrupt:
            print Banner.Banner
            exit()    
if __name__=="__main__":
   Buffer_Helper()    
  
  
  
  
  
             
