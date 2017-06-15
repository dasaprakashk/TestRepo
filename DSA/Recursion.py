def TowerOfBrahma(numberOfDisks, fromPeg, toPeg, auxPeg):
    if(numberOfDisks ==1):
        print("Moving from peg " + fromPeg + " to peg " + toPeg)
        return
    TowerOfBrahma(numberOfDisks-1, fromPeg, auxPeg, toPeg)
    TowerOfBrahma(1, fromPeg, toPeg, auxPeg)       
    TowerOfBrahma(numberOfDisks-1, auxPeg, toPeg, fromPeg)        

def isArraySorted(array, index):
    if(index == 1):
        return true
    if(array[index] < array[index-1]):
        return False
    isArraySorted(array, index-1)
