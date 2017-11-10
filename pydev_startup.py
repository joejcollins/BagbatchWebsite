''' Debugging in VSCode '''
import sys
import os
import ptvsd

#Assuming that pdvsd is located in the working folder
sys.path.append(os.getcwd())


# Modify the secret and port number as desired; you're debugging locally so the values don't matter.
# However, be sure the port is not blocked on your computer.
ptvsd.enable_attach(secret='gae', address=('0.0.0.0', 3000))

#The debug server has started and you can now use VS Code to attach to the application for debugging
print "Google App Engine has started, ready to attach the debugger"
