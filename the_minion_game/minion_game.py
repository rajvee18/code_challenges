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


i=0

while i < end: 
    if s[i] in vowels:
        for j in range(i,end):
            substring = s[i:j+1]
            x = CountOccurrences(s,substring)
            Kevin = Kevin + x
        
    i = i+1



i=0
while i < end:
    if s[i] not in vowels:
        for j in range(i,end):
            substring = s[i:j+1]
            x = CountOccurrences(s,substring)
            Stuart = Stuart + x
        
    i = i+1   


    
    
    


print(Stuart,Kevin)










        