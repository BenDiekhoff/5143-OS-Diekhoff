
# NAME
#        ls - list files and directories.

# SYNOPSIS
#        ls

# DESCRIPTION
#        - list files and directories.


#                       IMPORTS                                         #     
import os        # imports os module
import sys       # import sys module
import time      # import time module
import stat      # import stat- gets status of the specified path 
from os import stat
from datetime import datetime
from pprint import pprint  # import pprint import pprint module
import os.path,time
path = '.'   
#                       LS METHOD                                       #
def ls(flags,params,directs): # might need to include more later    
      case = 0
      print(flags)
      arr = [0,0,0]
      for flag in flags:
            if flag == '-a':
                  arr[0] = 1
            if flag == '-h':
                  arr[1] = 1
            if flag == '-l':
                  arr[2] =1
      print (arr)
            
      for i in range(0,3):
            case = case + arr[i]*(2**i) # ** means 2^i in this case
      print (case)
      files_Dir = os.listdir(path)   #contains all the directors,files                                            
      permission ={    #PERMISSIONS BEGIN# # The list of permissions for r-read, w-write, x-execute  
            0:('---'),         # belongs to user/group with ID 0- aka root=>     0  =  NO RIGHTS
            1:('--x'),         # 'x'=  Execute                                      =  1(Execute)                 Permission
            2:('-w-'),         # 'w'=  Write                                        =  2(Write)                   Permission
            3:('-wx'),         # 1(Execute) +(and)    2(Write)                      =  3(Execute + Write)         Permissions
            4:('r--'),         # 'r'=  Read                                        =  4(Read)                    Permission
            5:('r-x'),         # 4(Read)    +(and)    1(Execute)                    =  5(Read + Execute)          Permissions
            6:('rw-'),         # 4(Read)    +(and)    2(Write)                      =  6 (Read + Write)           Permissions
            7:('rwx'),         # 4(Read)    +(and)    2(Write)  +(and)  1(Execute)  =  7(Read + Write + Execute)  Permission
            8:('-'),            # directory
            9:('d----')
              }      
      info = os.stat(path)
      now = int(time.time())
      recent = now - (4*30*24*60*60) #4 months ago
      if not directs:
            for file in files_Dir: #for loop
                  if case == 0:  # ls
                  #for file in files_Dir: #for loop
                        try:
                                stat_info = os.lstat(path)
                        except:
                                sys.stderr.write("%s: No such file or directory\n" % path)
                                continue
                        if not flags:
                            if not file.startswith('.'): 
                               if os.path.isdir(file):
                                  print(file + "/")
                               else:
                                  print(file)
                  elif case == 1: # -a
                        try:
                              stat_info = os.stat(path)
                        except:
                                sys.stderr.write("%s: No such file or directory\n" % path)
                                continue
                        if file.startswith(path):
                              if os.path.isdir(file):
                                    print(file + "/")
                              else:
                                     print(file)             
                  elif case == 2: # -h
                         stat_info = os.stat(path)
                         if not file.startswith('.'):
                              size = stat_info.st_size
                              for unit in ['bytes','MB','KB','GB']: # Checks for size unit
                                    if size < 1024.0:
                                          h_size = str(size)+unit
                                          break
                                    else:
                                          size /= 1024.0
                                          print(size)
                  elif case == 3: # -h -a
                        stat_info = os.stat(path)
                        if os.path.isdir(file):
                              print(file + "/")
                        else:
                              print(file)              
                              if not file.startswith('.'):
                                    size = stat_info.st_size
                                    for unit in ['B','MB','KB','GB']: # Checks for size unit
                                          if size < 1024.0:
                                                h_size = str(size) + unit
                                                break
                                          else:
                                                size /= 1024.0
                                                #print(datetime.utcfromtimestap(time).strftime('%Y-%m-%d %H:%M:%S'), end= " ")
                                                print(file)
                  elif case == 4: # -l
                        stat_info = os.stat(path)
                        octalPerm= oct(stat_info.st_mode)[-3:]     # accessing permissions.
                        octalPerm = int(octalPerm)               # converting permissions to int --> Example: octal 230 [ownership --w-wx---]
                        octalP = octalPerm //10                  # Example:     23 = 230 // 10 
                        Owner = octalP // 10                     # Owner ex. 2 = 23  // 10
                        GroupP = octalP % 10                     # GroupP ex. 3 = 23  %  10
                        Others = octalPerm % 10                  # Others ex. 0 = 230 %  10
                        ts = stat_info.st_mtime
                        time_m = stat_info.st_mtime
                        if(ts<recent) or (ts> now):
                           time_fmt = "%b %e %Y"
                        else:
                           time_fmt = "%b %e %R"
                           time_str = time.strftime(time_fmt, time.gmtime(ts))
                           time_str2 = time.strftime(time_fmt,time.gmtime(time_m))
                           name = stat(file).st_uid  # User id of the owner                    
                           try:
                               name ="%-3s" % os.getcwd(stat_info.st_uid)[0]
                           except:
                               name = "%-3s" % (stat_info.st_uid)
                           try: 
                               group ="%-3s" % os.getegid(stat_info.st_gid)[0]
                           except:
                               group ="%-3s"% (stat_info).st_gid               # Group id of the owner
                           nlink = "%4d" % stat_info.st_nlink
                           total = len([name for name in os.listdir('.')if os.path.isfile(file)])
                          
                        if not file.startswith('.'):
                              print(permission[Others] + permission[GroupP] + permission[Owner], end =" " )
                              print(" " , nlink, end =" ") # @ detect a web request without extensions
                              size="%8d" % stat_info.st_size
                              print(name, end=" ")
                              print(group, end =" ")
                              print(size, end=" ")
                              print(time_str, end =" ")
                              if os.path.isdir(file):
                                 print(file + "/")
                              else:
                                 print(file)
                  elif case == 5: # -l -a
                        stat_info = os.stat(path)
                        octalPerm= oct(stat_info.st_mode)[-3:]     # accessing permissions.
                        octalPerm = int(octalPerm)               # converting permissions to int --> Example: octal 230 [ownership --w-wx---]
                        octalP = octalPerm //10                  # Example:     23 = 230 // 10 
                        Owner = octalP // 10                     # Owner ex. 2 = 23  // 10
                        GroupP = octalP % 10                     # GroupP ex. 3 = 23  %  10
                        Others = octalPerm % 10                  # Others ex. 0 = 230 %  10
                        ts = stat_info.st_mtime
                        time_m = stat_info.st_mtime
                        if(ts<recent) or (ts> now):
                               time_fmt = "%b %e %Y"
                        else:
                               time_fmt = "%b %e %R"
                        time_str = time.strftime(time_fmt, time.gmtime(ts))
                        time_str2 = time.strftime(time_fmt,time.gmtime(time_m))
                        name = stat(file).st_uid  # User id of the owner                    
                        try:
                          name ="%-3s" % os.getcwd(stat_info.st_uid)[0]
                        except:
                          name = "%-3s" % (stat_info.st_uid)
                          try: 
                              group ="%-3s" % os.getegid(stat_info.st_gid)[0]
                          except:
                              group ="%-3s"% (stat_info).st_gid               # Group id of the owner
                        nlink = "%4d" % stat_info.st_nlink
                        total = len([name for name in os.listdir('.')if os.path.isfile(file)])
                        if os.path.isdir(file):
                              print(file + "/")
                        else:
                              print(file) 
                        if not file.startswith('.'):
                              print(permission[Others] + permission[GroupP] + permission[Owner], end =" " )
                              print(" " , nlink, end =" ") # @ detect a web request without extensions
                              size="%8d" % stat_info.st_size
                              print(name, end=" ")
                              print(group, end =" ")
                              print(size, end=" ")
                              print(time_str, end =" ")
                              if os.path.isdir(file):
                                     print(file + "/")
                              else:
                                    print(file)
                  else:
                        try:
                              stat_info = os.lstat(path)
                        except:
                              sys.stderr.write("%s: No such file or directory\n" % path)
                              continue
                        if not flags:
                              if not file.startswith('.'): 
                                    if os.path.isdir(file):
                                          print(file + "/")
                              else:
                                  print(file)
                  pass
