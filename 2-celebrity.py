#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Problem exercise 1 and 2:

def preprocessing(Time):
    """Returns important range of time in which the celebrities enter the room
    params: Time {2D array containing entering and leaving time of each celebrity}"""

    impRange= Time.copy()
    impRange = list(set([a[0] for a in impRange]))
    impRange.sort()
    return impRange

def bestTimeToParty(schedule, ystart, yend):
    """Prints the maximum number of celebrities present in given schedule of celebrities(schedule)
    params: schedule {2D array containing entering and leaving time of each celebrity}
    ystart {Starting time of range to check for celebrities availability}
    yend {Ending time of range to check for celebrities availability}"""

    #Initializing the number of celebrities present previously and frequency
    #of celebrities at each important time interval
    initial = 0
    freq = {}
    impRange = preprocessing(schedule)

    for i in range(len(impRange)):
        freq[impRange[i]] = initial
        for r0, r1 in schedule:
            if(r0==impRange[i]):
                freq[impRange[i]] +=1
            if(r1==impRange[i]):
                freq[impRange[i]] -=1
            initial = freq[impRange[i]]
    res = {}
    for i in freq:
        if(i>=ystart and i<yend):
            res[i] = freq[i]
    res = max(res, key=res.get)
    print(f"Best time to attend party is at {res} o'clock: {freq[res]} celebrities will be attending!")

if __name__ == "__main__":
    time = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
    sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), 
              (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
    bestTimeToParty(sched2, 10.0, 12.0)
