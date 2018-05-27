


#########################################33
# Actors are binary strings
# an actor is mutated by flipping a single bit
# upon replication, an action of length n produces n children,
# one for each possible mutation
#
# This simulation demonstrates of no evolution occurs in
# the absense of of selection pressures. The population
# can change over time, and will get huge, but all change
# will be centered around the seed actor.
#
# Because there is no cap on population growth, it is still possible
# to produce arbitrarily complex genotypes (complex as in most
# distant from the seed)


MAX_GEN = 9



def freqOfGenes(population):
    freq = dict()
    for actor in population:
        if actor in freq:
            freq[actor] += 1
        else:
            freq[actor] = 1
    return freq


def printFreq(freq):
    for actor in freq.keys():
        print("%s: %d\n"%(actor,freq[actor]))

def printPopulation(population, n):
    print("\n\nGeneration %d\n\n"%(n))
    printFreq(population)

def update(dict, key, val):
    if key in dict:
        dict[key] += val
    else: dict[key] = val
    
def mutate(bit):
    return "0" if bit == "1" else "1"

def replicate(actor):
    children = list()
    for i in range(len(actor)):
        child = actor[:i] + mutate(actor[i]) + actor[i + 1:]
        children.append(child)
    return children



def mutate(actor, i):
    mut = "0" if actor[i] == "1" else "1"
    return actor[:i] + mut + actor[i+1:]

def replicate(actor, cnt, nextGen):
    for i in range(len(actor)):
        child = mutate(actor, i)
        update(nextGen, child, cnt)
        

def generate():

    population = dict()
    seed = "00000000"
    population[seed] = 1
    for t in range(MAX_GEN):
        printPopulation(population, t)
        nextGen = dict()
        for actor in population.keys():
            replicate(actor, population[actor], nextGen)
        population = nextGen

        
generate()
        

        
