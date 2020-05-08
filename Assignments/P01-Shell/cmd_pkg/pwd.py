import os

# NAME
#        pwd - print name of current/working directory

# SYNOPSIS
#        pwd

# DESCRIPTION
#        Print the full filename of the current working directory.
def pwd(flags,params,directs):
    workingDir = os.getcwd()
    if directs:
        mode = directs[0]
        writefilename = directs[1]
        with open (writefilename, mode) as wf:
                wf.write(workingDir)
    else:

        return print(workingDir)


