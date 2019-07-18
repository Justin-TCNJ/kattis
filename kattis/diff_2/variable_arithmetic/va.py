#Justin Fernandez
#july 8 2019
#dont know why seconed test case doesnt work, wrong answer 
# sample in
# 1 + 2
#length + width + 3 + depth
#length = 3
#length + width + 3 + depth
#width = 7
#length + width + 3 + depth
#depth = 2
#length + width + 3 + depth
#depth = 1
#length + width + 3 + depth
#computercost + televisioncost
#0
num_dict = {}

def just_var(line):
    pass


def equal_use(line,run_total):
    #print("enter equal")
    contents = line.split(" = ")
    #print(contents)
    dkey = contents[0]
    danswer = contents[1]
    num_dict[dkey] = danswer
    #print("dict is curr = ", end =  " ")
    #print(num_dict)



def plus_use(line,run_total,end_string):
    #print(line)
    # parse the string for the first variable or number
    contents = line.split(" + ")
    #print(contents)
    #this is trying to see if it is a number or not
    for i in contents:
        try: #try to convert to int if can it is int
            int(i)
            curr_val = int(i)
            run_total += curr_val
        except ValueError: #not an int so need to check dict if in
            #print("not an int")
            #check if in the num_dict
            if (i in num_dict):
                run_total += int(num_dict[i])
            else:
                end_string = end_string+" + "+i



    return run_total, end_string
    # if number add to total and move on
    # if varibale, see if in dict, if not add and change

def main():
    run_total = 0
    line = ""
    adder = 0
    end_string = "" #this is to have an added sting at the end
    plus = "+"
    equal = "="
    #we are looking for plus in string so if present go to plus_use

    #decision = pos int go to plus_use
    while(True):
        line = input()
        if(line == "0"): #end of file so break
            break
        decisionp = line.find(plus) #decide if = or +
        decisione = line.find(equal)
        if(decisione >= 0): #decision = -1 no plus so go to equal
            equal_use(line,run_total)
        elif(decisionp >= 0):
            adder, end_string = plus_use(line,run_total,end_string)

        try:
            print(num_dict[line])#this is looking for single variables (try path)
        except:
            pass
        if(line.isdigit()):
            print(line)
        #print (decision)
        run_total += adder
        if(decisionp != -1):
            if (run_total == 0):
                print(end_string[3:])
            else:
                print(str(run_total)+end_string)
        adder = 0
        run_total = 0
        end_string = ""





if __name__ == "__main__":
    main()
