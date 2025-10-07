import queue as Q
dict_gn = {
    'Arad': {'Zerind': 32, 'Sibiu': 2, 'Timisoara': 10},
    'Zerind': {'Arad': 75, 'Sibiu': 2},
    'Sibiu': {'Timisoara': 10},
    'Timisoara': {'Arad': 34}
}
dict_hn = {
    "Arad": 34,
    "Sibiu": 2,
    "Zerind": 33,
    "Timisoara": 10
}
start = 'Arad'
goal = 'Timisoara'
result = ''
def get_fn(citystr):
    cities=citystr.split(",")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)
def printout(cityq):
    for i in range(0, cityq.qsize()):
        print(cityq.queue[i])
def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    nexttot = 999
    if not cityq.empty():
        nexttot,nextcitystr,nextthiscity=cityq.queue[0]
    if thiscity== goal and tot < nexttot:
        result = citystr + "::" + str(tot)
        return
    print("Expaded city ---------", thiscity)
    print("second best f(n)---------", nexttot)
    tempq = Q.PriorityQueue()
    for cty in dict_gn[thiscity]:
        tempq.put((get_fn(citystr+','+cty), citystr+','+cty, cty))
    for ctr in range(1,3):
        ctrtot, ctrcitystr ,ctrthiscity = tempq.get()
        if ctrtot < nexttot:
            cityq.put((ctrtot, ctrcitystr,ctrthiscity))
        else:
            cityq.put((ctrtot, citystr, thiscity))
            break
    printout(cityq)
    expand(cityq)
def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((999, "NA", "NA"))
    cityq.put((get_fn(start), start, thiscity))
    expand(cityq)
    print(result)
main()
