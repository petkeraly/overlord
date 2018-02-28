
def folder_size(path):
    import os
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    print ("The size of "+path+" is:")
    print (str(total)+" bytes")
    return total
    
