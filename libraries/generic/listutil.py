def autoscale(MAX,l,MIN=0):
    '''
    Usable to autoscale a list of numbers to be inside a MAX and a MIN. 
    
    '''
    tempMax = max(l)
    MAX = MAX-MIN
    return [MIN+MAX*float(k)/tempMax for k in l]