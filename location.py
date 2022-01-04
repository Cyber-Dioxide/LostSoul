

from setup.sprint import sprint

from setup.colors import c,r,ran,lr,lc,lg,g,ly,y

from setup.banner import banner,banner2,clear
from geopy import Nominatim

clear()
banner()
def main():
    geolocator = Nominatim(user_agent="maps.googleapis")
    im = input(c+"Enter name of place: "+lr)
    location = geolocator.geocode(im , language="en")

    print(lg+"\n\nLocation: "+c + im)
    print(lg+'Details: '  +c , location)
    try:
        data = location.raw
    except AttributeError:
        sprint(lr + "Struggling to find information of "+c+im)
        pass
    try:
        loc_data = data["display_name"].split()
        print(lg + 'Zip Code: ' + c, loc_data[-2])

    except UnboundLocalError:
        sprint(lc + "Sorry i wasn't able to find :-(" +ly + im)
        pass


def AltiLongi():
    geolocator = Nominatim(user_agent="geoapiExercises")
    alti = input(ly + "Type Latitude: " + lc)
    logi = input(ly + "Type Logitude: " + ran)
    lald = alti+","+logi
    print("Latitude and Longitude:",lald)
    location = geolocator.geocode(lald)
    print(lr + f"Location address of {lald} :")
    print(ran + location)

no = ["n" , "no"]
yes = ["y" , "yes"]
cont = ""

while cont not in no:
    print(lr + "[1]" + c +" Get Zip code")
    print(lr + "[2]" + c +" With Latitude $ Longitude")
    print(lr + "[3]" + c +" Find details")
    print(lr + "[4]" + c +" EXIT" +ly +"!!!")
    choice = input(ran+"\nroot@LostSoul~ ")
    if choice == "1":
        main()
    elif choice == "2":
        AltiLongi()
    elif choice == "3":
        main()
    elif choice == "4":
        exit()

    else:
        sprint(ran + "SUCCESSFULLY type Invalid Option!")
        sprint(ran +"Exiting tool...")
        exit()

    cont = input(ran+"Continue?"+lr+" [y/n]" + ly)
    if cont in no:
        banner2()
    else:
        banner2()




