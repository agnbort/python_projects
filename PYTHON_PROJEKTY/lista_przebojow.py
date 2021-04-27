#1.
hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU HERE']
#print(hitsTitles)

#2
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
#print(hitsTitles)

#3
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
#print(hitsTitles)

#4.
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)

#5.
print(hitsTitles.index('HOTEL CALIFORNIA'))

#6.
hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)

#7.

hitsTitles[0] = 'ENJOY THE SILENCE'
print(hitsTitles)

#8.

hitsToRead = hitsTitles[:]
print('hitsToRead:', hitsToRead)

#9.
hitsToRead.reverse()
print('hitsToRead odwrocona:', hitsToRead)

#10.
hitsToRead.sort()
print('hitsToRead posortowana:', hitsToRead)

#11.
hitsToRead.pop(0)
hitsToRead.pop(0)
print('usunięcie dwóch pozycji:', hitsToRead)

#12.

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
print('additionalSongs:', additionalSongs)

#13.

hitsToRead.extend(additionalSongs)
print('połączone listy:', hitsToRead)

#14.

print('ilość wystąpień WISH YOU WERE HERE: ',(hitsToRead.count('WISH YOU WERE HERE')))
print('ilość wystąpień RIDERS ON THE STORM: ',(hitsToRead.count('RIDERS ON THE STORM')))

#15.

hitsToRead.clear()
print(hitsToRead)

