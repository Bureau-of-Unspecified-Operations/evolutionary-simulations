


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

def printPopulation(population,n):
    print("\n\nGeneration %d\n\n"%(n))
    freq = freqOfGenes(population)
    printFreq(freq)
    
def mutate(bit):
    return "0" if bit == "1" else "1"

def replicate(actor):
    children = list()
    for i in range(len(actor)):
        child = actor[:i] + mutate(actor[i]) + actor[i + 1:]
        children.append(child)
    return children


def generate():
    seed = "00000"
    population = list()
    population.append(seed)
    for t in range(MAX_GEN):
        printPopulation(population, t)
        nextGen = list()
        for actor in population:
            nextGen.extend(replicate(actor))
        population = nextGen

generate()
        

        
