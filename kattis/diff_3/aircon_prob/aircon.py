
def room_creation(minions):
    number_of_rooms = 0
    temp_dict = {}
    for x in minions:
        initial_temp = int(x[0])
        while initial_temp <= int(x[1]):
            temp_dict[initial_temp] = 0
            initial_temp += 1
    print(temp_dict)
    for y in temp_dict:
        for min in minions:
            if(int(min[0]) <= y <= int(min[1])):
                temp_dict[y] += 1
    print(temp_dict)
    key_max = 0
    value_max = 0
    while(True):
        for dic in temp_dict:
            if(temp_dict[dic] > key_max):
                key_max = temp_dict[dic]
                value_max = dic
        print(key_max,value_max)
        print(minions)

        del temp_dict[key_max]
        #for x in minions:
        #    break
        break

    return number_of_rooms



    '''
    num_of_satisfied_minions = 0 #counter to count # of sat minions
    start_value = 0 #this will be used to itirate through a minions range
    room_sat_dict = {} # dict that hold rooms (temp is their key, # of satified minions = value)

    #start with minions 0 first temp, see how many minions it satisfies
    #try every value from minions 0 low temo to high temp
    #the temp that satifies the most minions is used and the satified minions are taken out
    for x in minions:
        pos_room_temp = int(x[0])
        #test the first possible temp for room see how many diff minions can fit in it
        #this while loop test every value from low to high of minion
        while pos_room_temp <= int(x[1]):
            room_sat_dict[pos_room_temp] = 0
            for y in minions:
                if(int(y[0]) <=pos_room_temp<= int(y[1])):
                    room_sat_dict[pos_room_temp] = room_sat_dict[pos_room_temp] + 1 #it satisfies one more minion
            pos_room_temp +=1
        print(room_sat_dict)
        temp_max = 0
        #finds the temp that satisfies the most minions
        for z in room_sat_dict:
            if room_sat_dict[z] > temp_max:
                temp_max = room_sat_dict[z]
        print(temp_max)
        for a in room_sat_dict:
            if(room_sat_dict)

    #do this untill you have tried all possibilties for the first minions
    #do this for the next minion not already in a room
    '''
def minion_data(num_of_iter,minions):
    for x in range(num_of_iter): #iterates from 0 to (num_of_iter-1) gettting all minions data
        line = input()
        contents = line.split(" ")
        minions.append(contents)
    return minions

def main():
    minions = []
    rooms = []
    num_of_iter = int(input())
    minion_data(num_of_iter,minions)
    #print(minions) #minions = 2D array that has all the minions and their data
    answer = 0
    answer = room_creation(minions)



if __name__ == "__main__":
    main()
