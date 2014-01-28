# You can place the script of your game in this file.

# Declare images below this line, using the image statement.

image bg firstday = "img/firstday.jpg"
image bg lecturehall = "img/lecturehall.jpg"
image bg day_two = "img/time/day2.png"
image bg angrybird = "img/angrybird.jpe"
image bg corridor = "img/corridor.jpg"
image bg late = "img/time/late.png"
image bg nokia = "img/mobile.png"
image bg chemistry_lab = "img/chemistry_cat.png"
image bg broken_flask = "img/broken_flask.jpg"
image bg next_day = "img/time/next_day.png"
image bg mess = "img/canteen.jpg"
image bg line =  "img/queue.jpg"
image bg later = "img/time/later_2.png"


image prof = "img/prof.png"
image fifteen_min = "img/time/15min.png"
image board math = "img/mathboard.jpg"
image rhoit happy = "img/happy_smile.png"
image lecturehall = "img/lecturehall.jpg"
image physic teacher = "img/einstein-science1.png"
image breakTime = "img/breaktime.jpg"
image onWall = "img/wall.jpg"
image walkinglady = "img/preetylady1.jpg"

# Declare characters used by this game.
define khalasi = Character('खलािस')
define crush = Character('मन पर्ने केटी', color="#c8ffc8")
define mjt = Character('मनीस', color="#c8ffff")
define prof = Character('सर', color="#c8ffdd")
define rho = Character('rohit', color="#fff000")

# The game starts here.
label start:
    play music "audio/illurock.ogg"

    scene bg firstday
    "first day of college"

    menu:
        "you excited":
            "hell yaaAAAA"

        "why should I be??":
            "new boring place"

    show rhoit happy at left
    rho "hi there! whats your name?"

    menu:
        "Respond":
            "hi! am Manish... n u?"

        "dont care":
            "who the heck are your"

        "look far away":
            "that girl looks hot"

    scene bg later
    "in the class"

label firstClass:

    scene lecturehall
    show physic teacher at center
    "physic teacher come in"

    menu:
        "Greet him":
            "Good Morning sir"
        "confused":
            "look into others eyes"
        "who cares":
            "Like a boss"

    show breakTime
    "finally yay"

label breaktime:
    scene onWall
    "Staring at the outside road"

    scene walkinglady
    "cute girl walks by"

    menu:
        "avoid eye contact":
            "hmmm"
        "stare at her":
            "not a good habbit"
        "ignore her":
            "o.O"

label nextday:
    scene bg next_day

    mjt "college मा नयाँ िदन"

    scene bg lecturehall
    with fade

    "सर लाई कुर्दै"

    show prof
    with dissolve

    prof "शुभ प्रभात class"
    prof "आज Partial Diffential equation..."

    scene fifteen_min
    with fade

    mjt "केह बुझेन"

    menu:
        "try to concentrate":
            call study

        "check mobile":
            call mobile

    jump decide

label mobile:
    show bg nokia
    with dissolve

    mjt "Angry Bird खेल्नु पर्ला"

    show bg angrybird
    with fade

    mjt "le me playing"
    return

label study:
    show board math
    with fade

    "एक घण्टा class पिछ"

    show prof at right
    with dissolve

    prof "भोिल अाँउदा Execersie 2.12 को हिसाव गरेर आउनु"
    mjt "ल class सके छ"

    "you came out in the corridor"
    return


label decide:
    show bg corridor
    with fade

    "now what to do"

    show bg corridor



    menu:
        "goto canteen":
            "where is the canteen"
            jump canteen

        "goto hang around":
            "You spend the time doing nothing"
            jump lab

        "goto library":
            "Oh libary is close"
            jump decide

label canteen:
    "finally found it"
    "Oh! college has the big canteen"

    scene bg mess
    with fade

    mjt "कस्तो भोक लाग्यो"

    scene bg line
    with fade

    mjt "line रहेछ"

    menu:
        "stay in line":
            "you got the lunch"
            jump bench


        "go at beggining of the line":
            jump bench

label bench:
    "you are eating with your friends"
    "a girl walk bay"

    "you are late"

label lab:
    "now its time for chemistry lab"

    scene bg chemistry_lab
    prof "आज titration"

    scene bg broken_flask
    with fade

    prof "कसले के फुटायो"

    "what you want to do now!"

    menu:
        "tell you broke the flask":
            "you got the excuse"

        "blame your partner":
            "you made the enemy"

        "keep quite":
            "no one tells anything"

label bus:
    "now it time to go home"

    khalasi "ID card"

    mjt "ला...! काड ल्याउन िबर्सो"

    menu:
        "try to bluff":
            return

        "goto hang around":
            return

        "goto library":
            return

label normal_day:
    scene bg next_day
    with fade

label late:
    scene bg late
    with fade

    "८ बजे class!"

    return
