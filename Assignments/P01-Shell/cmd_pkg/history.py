from os import path

def history(flags, params, directs):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..","history.log"))
    histDict = {}
    count =1 
    with open (filepath, "r") as f:
        for line in f.readlines():
            histDict[count] = line
            if not directs:
                print(f"{count}   {line}",end='')
            count+=1
    if directs:
        mode = directs[0]
        writefilename = directs[1]
        with open (writefilename, mode) as wf:
            for key in histDict:
                wf.write(f"{key} {histDict[key]}")
    else:
        return histDict