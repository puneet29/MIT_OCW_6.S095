#Input is a vector of F's, B's and H's, in terms of forwards, backwards and no caps
#Output is a set of commands (printed out) to get either all F's or all B's without
#instructing people with no caps on
#Fewest commands are the goal
#Problem exercise 1-3 implemented:

def keepThis(caps):
    """Returns the orientation of caps to keep in line
    params: caps {List consisting H's, F's and B's for current state of line}"""
    temp = []
    if(caps[0]!='H'):
        temp.append(caps[0])
    for i in range(len(caps)-1):
        if(caps[i]=='H' and caps[i+1]!='H'):
            temp.append(caps[i])
    if(temp.count('F')>=temp.count('B')):
        return('F')
    else:
        return('B')

def youWillConform(caps):
    """Prints the fewest commands to be spoken
    params: caps {List consisting H's, F's and B's for current state of line}"""
    start = 0
    intervals = []
    if(len(caps)!=0):
        #Get the orientation to keep in line and concatenate keep at the end of
        #input array to avoid end case
        keep = keepThis(caps)
        caps = caps + [keep]
        
        for i in range(len(caps)):
            if(caps[i] != caps[start]):
                if(caps[start] not in [keep, 'H']):
                    intervals.append([start, i-1])
                start = i

        for [i, j] in intervals:
            if(i==j):
                print("Person at position", i, "flip your cap!")
            else:
                print("People from position", i, "through", j, "flip your caps!")

if __name__ == "__main__":
    #caps = [x for x in input().split()]
    caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B']
    cap2 =	['F','F','B','H','B','F','B','B','B','F','H','F','F']
    cap3 = ['H','H','F','F','B','H','B','F','B','B','B','F','H','F','F']
    youWillConform(cap2)