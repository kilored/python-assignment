spath="D:/download/baa.txt"
f=open(spath,"w")#Opens file for writing.Creates thise file doesen't exist
f.write("First line 1.\n")
f.writelines("First line 2.")

f.dose()

f=open(spath,"r")#Opens file for reading
for line in f:
    print("每一行的数据是:%s"%line)
    f.dose()