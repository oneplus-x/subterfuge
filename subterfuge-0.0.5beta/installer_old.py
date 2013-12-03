#!/usr/bin/python
import os
import sys
import time


def main():

   if not os.getuid() == 0:
      sys.exit("\nSubterfuge Installer must be run as root\n")

      #Checks for sane arguments
   if len(sys.argv) != 2:
      usage()

      #Help menu
   if sys.argv[1] == "-h" or sys.argv[1] == "--help":
      print "\nSubterfuge courtesy of r00t0v3rr1d3 & 0sm0s1z \n"
      print "Usage: python install.py [OPTIONS] \n"
      print "Installation Options:"
      print "   -i,--install     install subterfuge with dependencies"
      print "   -s,--setup       setup subterfuge dependencies"
      print "   -l,--list        list subterfuge dependencies"
      print "   -h,--help        display this message\n"
      ##########################################################################
		
   if sys.argv[1] == "-i" or sys.argv[1] == "--install":
      install()
   elif sys.argv[1] == "-s" or sys.argv[1] == "--setup":
      setup()
   if sys.argv[1] == "-l" or sys.argv[1] == "--list":
      listdep()
      
def install(): 
   print "Installing Dependencies:"
   print "Unpacking python-twisted"
   os.system("tar -xvf dependencies/Twisted-12.0.0.tar.bz2")
   print "Installing python-twisted"
   time.sleep(1)
   os.system("mv Twisted-12.0.0/* ./")
   os.system("python setup.py install")
   print "Unpacking Django"
   os.system("tar -xvf dependencies/Django-1.3.1.tar.gz")
   print "Installing Django"
   time.sleep(1)
   os.system("python Django-1.3.1/setup.py install")
   print "Unpacking python-scapy"
   os.system("tar -xvf dependencies/scapy-latest.tar.gz")
   print "Installing python-scapy"
   time.sleep(1)
   os.system("cd scapy-2.2.0; python setup.py install; cd ..")
   print "Unpacking arptables"
   os.system("tar -xvf dependencies/arptables-v0.0.3-4.tar.gz")
   print "Installing arptables"
   time.sleep(1)
   os.system("cd arptables-v0.0.3-4; make; make install; cd ..")
   print "Unpacking Sqlite3"
   os.system("tar -xvf dependencies/sqlite3.tar.gz")
   print "Installing Sqlite3"
   time.sleep(1)
   os.system("cd sqlite3; sh configure; make; make install")
   print "Installation of Dependencies Complete...\n"
   print "Installing Subterfuge"
   print "Unpacking Subterfuge to /usr/share/"
   os.system("tar -xvf subterfuge_packages.tar.gz")
   os.system("mv subterfuge/subterfuge /bin/")
   os.system("mv subterfuge/ /usr/share/")
   print "Installation Complete"
   
def setup(): 
   print "Installing Dependencies:"  
   print "Unpacking python-twisted"
   os.system("tar -xvf dependencies/Twisted-12.0.0.tar.bz2")
   print "Installing python-twisted"
   time.sleep(1)
   os.system("python dependencies/Twisted-12.0.0/setup.py install")
   print "Unpacking Django"
   os.system("tar -xvf dependencies/Django-1.3.1.tar.gz")
   print "Installing Django"
   time.sleep(1)
   os.system("python Django-1.3.1/setup.py install")
   print "Unpacking python-scapy"
   os.system("tar -xvf dependencies/scapy-latest.tar.gz")
   print "Installing python-scapy"
   time.sleep(1)
   os.system("cd scapy-2.2.0; python setup.py install; cd ..")
   print "Unpacking arptables"
   os.system("tar -xvf dependencies/arptables-v0.0.3-4.tar.gz")
   print "Installing arptables"
   time.sleep(1)
   os.system("cd arptables-v0.0.3-4; make; make install; cd ..")
   print "Unpacking Sqlite3"
   os.system("tar -xvf dependencies/sqlite3.tar.gz")
   print "Installing Sqlite3"
   time.sleep(1)
   os.system("cd sqlite3; sh configure; make; make install")
   print "Installation of Dependencies Complete...\n"
   
def listdep(): 
   print "python-twisted"
   print "Django"
   print "python-scapy"
   print "arptables"
   print "Sqlite3"

def usage(): 

   print "\nSubterfuge courtesy of r00t0v3rr1d3 & 0sm0s1z \n"
   print "Usage: python install.py [OPTIONS] \n"
   print "Installation Options:"
   print "   -i,--install     install subterfuge with dependencies"
   print "   -s,--setup       setup subterfuge dependencies"
   print "   -l,--list        list subterfuge dependencies"
   print "   -h,--help        display this message\n"
   sys.exit(1)
 
if __name__ == '__main__':
    main()	
