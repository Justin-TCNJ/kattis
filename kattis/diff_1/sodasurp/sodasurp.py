# https://open.kattis.com/problems/sodasurpler

#here we have the total amount of bottles
def recycle(cost,total_bottles,cash):

    total_bottles += cash//cost #total number of bottles purchased

    bought_this_round = cash//cost

    cash = (cash%cost) + (bought_this_round)#
    if(cash >= cost):
        return(recycle(cost,total_bottles,cash))
    else:
        return(total_bottles)

def main():
    data = input()
    numbers = data.split(" ")
    total_bottles = 0
    cash = int(numbers[0])+int(numbers[1])
    cost = int(numbers[2])

    answer = 0
    answer = recycle(cost,total_bottles,cash)
    print(answer)

if __name__ == "__main__":
    main()
