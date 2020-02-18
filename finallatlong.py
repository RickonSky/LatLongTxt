song = []
artiste = []
insong= ""
byartist= ""
end = "end"
back = "prev"


#functoin to take input values from of lat from user appending to list named song
def insong():
    insong = input("({}). enter lat.: ".format(len(song) + 1)).lower()
    song.append(insong)
    if insong == back:
        previousS()
    elif insong ==end:
        song.remove(song[-1])
        return False
#function to execute reverse prevois input while maintaining serial numbering
def previousS():
    song.remove(song[-1])
    artiste.remove(artiste[-1])
    byartist()
    insong()
#same as input func above       
def byartist():
    byartist = input("({}). enter long.?: ".format(len(artiste) + 1)).lower()
    artiste.append(byartist)
    if byartist == back:
        previousA()
    elif byartist ==end:
        artiste.remove(artiste[-1])
        return False
#same as reversal func above
def previousA():
    artiste.remove(artiste[-1])
    song.remove(song[-1])
    insong()
    byartist()

    
file = input("Enter filename(e.g. 'filename.txt'): ")
dbms = open(file, 'w')
print("PUSH ENTER TO CONTINUE OR TYPE 'PREV' TO RETURN TO PREVIOUS INPUT\n OR ENTER 'END' (CONTINUALLY IF NRCCESSARY) WHEN DONE")

try:
    while True:
        val=insong()
        if val== False:
            break
        
        val2=byartist()
        if val2 == False:
            break
except IndexError:
 #error handlin for cases where prev fuction tries to remove value from empty list   
    print("no values to return to!")
      
dbms.write(str(song)+str(artiste))
dbms.close()
#to display the contents of file with the values
r= open("rickon.txt", "r")
print(r.read())

#when the code flow running within the reversal functions end doesnt end the task.
