

world = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def count(w,r,c):
    
    dir=[[-1,0],[-1,1],[-1,-1],[1,0],[1,-1],[1,1],[0,1],[0,-1]]
    count = 0

    for i in dir:
        raw = r+int(i[0])
        col = c+int(i[1])
        try:

            if bool(w[raw][col]):
                count += 1
    
        except IndexError:
            continue

    return count

x = int(input("Enter the nubmer of weeks" \n))

for XD in range(0,x):
    die = []
    live = []
    for raw in range(len(world)):
        for i in range(len(world[raw])):
            if bool(world[raw][i]):
                if count(world,raw,i) < 2 or count(world,raw,i) > 3:
                    die.append([raw,i])            
            elif count(world,raw,i) == 3:
                    live.append([raw,i])
    
    print((world[7][13]))        
    for i in die:
        world[int(i[0])][int(i[1])] = 0

    for i in live:
        world[int(i[0])][int(i[1])] = 1
print(die)

'''update'''         
x=""
for raw in world:
    for i in raw:
        if bool(i):
            x += "O"+" "
        else:
            x += "."+" "
    x += "\n"
print(x)
