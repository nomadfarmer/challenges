def main():
    pass

def likes(names):
    """ 
    Takes a list of names and returns a string in the following format:
    Empty list: "no one likes this"
    Single name: "Albert likes this"
    2-3 names: "Albert and Bert like this" or "Albert, Bert and Ched like this"
    4+ "Albert, Bert and 2 others like this"
    """

    outstring = ""
    if not names:
        outstring = "no one"
        
    elif len(names) == 1:
        outstring = names[0]
        
    elif len(names) == 2:
        outstring = names[0] + " and " + names[1]

    elif len(names) == 3:
        outstring = names[0] + ", " + names[1] + " and " + names[2]

    else:
        outstring = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others"

    if len(names) < 2:
        outstring += " likes this"
    else:
        outstring += " like this"

    return outstring

    

def test_likes_0():
    assert likes([]) == "no one likes this"

    
def test_likes_1():
    assert likes(["Albert"]) == "Albert likes this"

    
def test_likes_2():
    assert likes(["Albert", "Bert"]) == "Albert and Bert like this"

    
def test_likes_3():
    assert likes(["Albert", "Bert", "Ched"]) == "Albert, Bert and Ched like this"

    
def test_likes_4():
    assert likes(["Albert", "Bert", "Ched", "Donald"]) == "Albert, Bert and 2 others like this"

    
if __name__ == '__main__':
    main()
