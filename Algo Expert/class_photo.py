def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    
    blueShirtHeights.sort(reverse=True)
    redShirtHeights.sort(reverse=True)
    if blueShirtHeights[0] > redShirtHeights[0]:
        tall = blueShirtHeights
        short = redShirtHeights
    else:
        tall = redShirtHeights
        short = blueShirtHeights
    for i in range(len(redShirtHeights)):
        if tall[i] < short[i]:
            return False
    return True

blueShirtHeights = [5, 6, 7, 2, 3, 1, 2, 3]
redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
print(classPhotos(redShirtHeights, blueShirtHeights))