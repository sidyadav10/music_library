
print("==WELCOME==TO===MUSIC STATION===")
Songs = ["Blue eyes","Brown rang","Dopeshope","Mirror","Satya","Walkin miracle","One bottle down","Punya paap","One side","3.59","First kiss","Farak",
"Gandhi money","Remand","Drill karte","Rider","Half window down"]
borrowed = []
while True:
    print("\tPress 1 for available song:\n\tPress 2 for a donation:\n\tPress 3 for requesting a song:\n\tPress 4 to return a song:\n\tPress 5 to exit")
    listner = int(input("How may I help you: "))
    if listner == 1:
        print(f"Available Songs are: {Songs}")
        print()
    elif listner == 2:
        song = input("Which song would you like to dontate: ")
        song.capitalize()
        if song.capitalize() not in Songs:
            Songs.append(song.capitalize())
            print(f"Thank you  for donating a song {song.capitalize()}!!")
            print()  
        else:
            print("WE Have a song thank you")    
            print()
    elif listner == 3:
        request = input("Which song do you want to listen: ")
        request.capitalize()
        if request.capitalize() in Songs:
            print(f"You can listen to {request.capitalize()} for a week plz return on time Thank you!!")
            Songs.remove(request.capitalize())
            borrowed.append(request.capitalize())
            print()
        else:
            print(f"The requested song {request.capitalize()} is not available in Library yet or has been lend to someone plz try after some days!!!")
            print()
    elif listner == 4:
        returning = input("Enter song name whick you want to return:")
        returning.capitalize()
        if returning.capitalize()  not in borrowed:
            print(f"Sorry you have not borrowed {returning.capitalize()} from us!")
            print()
        else:
            print(f"Thankyou for returning {returning} ")
            borrowed.remove(returning.capitalize())
            Songs.append(returning.capitalize())
            print()
    elif listner == 5:    
        exit        
        break    
    elif listner != (1,2,3,4,5):
        print("Invalid Input !!")

    
    
