s = input().lower()

vowels = ['a','e','i','o','u']

Stuart = 0
Kevin = 0
end = len(s)

def CountOccurrences(string, substring):
 
    # Initialize count and start to 0
    count = 0
    start = 0
 
    # Search through the string till
    # we reach the end of it
    while start < len(string):
 
        # Check if a substring is present from
        # 'start' position till the end
        pos = string.find(substring, start)
 
        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = pos + 1
 
            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return count
substring1 = []
substring2 = []


i=0

while i < end: 
    if s[i] in vowels:
        for j in range(i,end):
            substring = s[i:j+1]
            if substring not in substring1:
                substring1.append(substring)
            
            
        
    
    if s[i] not in vowels:
        for j in range(i,end):
            substring = s[i:j+1]
            if substring not in substring2:
                substring2.append(substring)
            
    
    i = i+1


for x in substring1:
    Kevin = Kevin + CountOccurrences(s,x)

for x in substring2:
    Stuart = Stuart + CountOccurrences(s,x)
        
if Stuart>Kevin:
    print("Stuart",Stuart)
elif Kevin>Stuart:
    print("Kevin",Kevin)       
else:
    print("Draw")
    


    
    
    













        
