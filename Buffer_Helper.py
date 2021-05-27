#!/usr/bin/env python2 

 
import time
import readline 
import sys
from Buffer_Package             import  Banner 
from Buffer_Package.__Server    import  SERVERSOCKET
from Buffer_Package.__Client    import  LISTEN_BIND
from Buffer_Package.HTTP_LOGIN  import  HTTPLOGIN

W = '\033[0m'     
R = '\033[31m'    
G = '\033[0;32m'  
O = '\33[37m'     
B = '\033[34m'    
P = '\033[35m'   
Y = '\033[1;33m' 
try:  
   if sys.argv[0] and '-c' in sys.argv[1] and  len(sys.argv[1])==2 \
   and'off' in sys.argv[2] and\
   len(sys.argv[2])==3 :
      W = ''     
      R = ''    
      G = ''  
      O = ''     
      B = ''    
      P = ''   
      Y = ''
   
   else: 
       print 'Plsase set color to off'
       exit()
except IndexError:
          try:
            if sys.argv[1]:
               print 'Plsase set color to off'
               exit()  
          except IndexError:
               pass
class Buffer_Helper():
                                         
       def __init__(self):
  
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
             print R+"[*] "+W+Y+ "1-"+W+B+ " To Target Server "+W
             print R+"[*] "+W+Y+ "2-"+W+B+ " To Target FTPClient "+W
             print R+"[*] "+W+Y+ "3-"+W+B+ " To Target HTTP Login Page"+W
             selcet4= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))
             if selcet4 == selcet1 and len(selcet4)==1:             
                run = SERVERSOCKET()                
             elif selcet4 == selcet2 and len(selcet4)==1:             
                 run = LISTEN_BIND()
             elif selcet4 == selcet3 and len(selcet4)==1: 
                 run = HTTPLOGIN()
             else:
                 time.sleep(2)
                 print Y+"\n\r\r!---___"+W+R+ "Please Select Mode Number"+W+Y+'___---!'+W
                 return self.main()
         except KeyboardInterrupt:
            print Banner.Banner
            exit()    
if __name__=="__main__":
   Buffer_Helper()    
  
  
  
  
  
             
