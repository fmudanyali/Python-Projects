import pickle,os
if not os.path.isfile('default.savefile'):
    print("Welcome to this game uhh, you do this and thaat.")
    #money,speed,stamina
    save=[200,5,80]
    with open('default.savefile', 'wb') as filehandle:
        pickle.dump(save, filehandle)
else:
    print("Yeah welcome back.")
    with open('default.savefile', 'rb') as filehandle:  
        save = pickle.load(filehandle)

print("1. Check Stats")
print("2. Work: Gives "+str(round(20*(save[1]**0.2)))+" dollars but consumes 20 stamina.")
print("3. Sleep: Rest until the next day, the daily rent is 50 dollars.")
print("exit. Exit the game and save your progress.")
xp=0
while 1:
    select=input("What do you want to do?:")
    if select=="1":
        print("Your money "+str(save[0]))
        print("Your speed "+str(round(save[1])))
        print("Your stamina "+str(save[2]))
    if select=="2":
        if save[2]>=15:
            save[0]+=20*(round(save[1]**0.5))
            save[2]-=15
            xp+=0.2
            print("You worked hard and earned "+str(round(20*(save[1]**0.2)))+" dollars.")
            
            print("Your current stamina is: "+str(save[2]))
        else:
            print("You're too tired.")
    if select=="3":
        save[0]-=50
        save[2]=80
        save[1]+=xp
        if xp>0:
            print("You have gained ample rest, you also gained "+str(xp)+" speed.")
            print("Your current speed is: "+str(round(save[1])))
        else:
            print("You have gaained ample rest.")
        xp=0
    if select=="exit":
        with open('default.savefile', 'wb') as filehandle:
            pickle.dump(save, filehandle)
        break
        