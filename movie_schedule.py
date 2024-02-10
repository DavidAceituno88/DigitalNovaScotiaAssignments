current_movies = {'The Grinch' : '3:00am',
                  'Rudolph' : '11:00am',
                  'Mad Max' : '4:00pm',
                  'No manches Frida' : '12:00pm'
                            }

print('We are showing the following movies: ')
for movie in current_movies :
    print(movie)

choice = input("Wich movie would you like to watch? \n")

showtime = current_movies.get(choice)

if showtime == None :
    print("Requested movie is not playing, please select another movie.")
else:
    print(f'{choice} is playing at {showtime}')
