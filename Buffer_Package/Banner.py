

import sys

W='\033[0m'     
R='\033[31m' 
try:
   if sys.argv[0] and '-c' in sys.argv[1] and  len(sys.argv[1])==2 \
   and'off' in sys.argv[2] and\
   len(sys.argv[2])==3 :
      W=''     
      R=''    
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
Banner =  R+ """	         ____         __  __             _   _      _                  
		| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
		|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
		| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
		|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
				                             |_|by:jacstory           
				                                         """+W 
                                                                            

