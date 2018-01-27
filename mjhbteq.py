#! /usr/bin/python

import subprocess


Sql1 = "createdatabase.bteq"
# This can be modified to take different SQL files as parameters

if ??? :
   name = Sql1
   elif ??? :
   elif ??? :
   else :
   return 

name = "sh -v TDLogon.sh " + Sql1
print ("Going to run the script ", name)
   
   
# THE PROCESS TO RUN
process = subprocess.Popen(args=[name], shell=True)

#process = subprocess.Popen(args=['sh -v TDLogon.sh logon.sql'] , shell=True)

process.wait()
print ("Bteq login testing")