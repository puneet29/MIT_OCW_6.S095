#Problem description: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/puzzle-2-the-best-time-to-party/MIT6_S095IAP18_Puzzle_2.pdf
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
    print(impRange)
    return impRange

def celemax(schedule):
    """Prints the maximum number of celebrities present in given schedule of celebrities(schedule)
    params: schedule {2D array containing entering and leaving time of each celebrity}"""

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
    res = max(freq, key=freq.get)
    print(f"Best time to attend party is at {res} o'clock: {freq[res]} celebrities will be attending!")

if __name__ == "__main__":
    time = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
    sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), 
              (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
    celemax(time)
