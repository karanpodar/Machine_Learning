def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    if len(redShirtSpeeds) == 0:
        return 0

    blueShirtSpeeds.sort()
    redShirtSpeeds.sort(reverse = True) if fastest == True else redShirtSpeeds.sort()
    output = 0
    
    for i in range(len(blueShirtSpeeds)):
        output += max(blueShirtSpeeds[i], redShirtSpeeds[i])
        
    return output
