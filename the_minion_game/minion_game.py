def minion_game(s):
    vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0
    end = len(s)

    for i in range(end):
        if s[i] in vowels:
            Kevin += (end - i)
        else:
            Stuart += (end - i)

    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")

# Example usage
if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
    


    
    
    













        
