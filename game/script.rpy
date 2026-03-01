# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cpu = Character("CPU")
define fan = Character("Fanny")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")

# The game starts here.

label start:
    scene bg black
    play music background 
    you "Hello?"
    "..."
    you "Why is it so dark...? Did the power go out?"
    play sound keyboard
    you "Wait. I was typing. I was finifhing the last paragraph. The conclusion... the bibliography-"
    show clock 1200
    you "Midnight."
    hide clock 1200
    you "No no no no - it's due at 6AM. I saved it. I definitley saved it."
    play sound error_sound
    show error_message
    you "...What?"
    hide error_message
    scene bg computer
    with fade
    you "Where am I?"
    cpu "You are inside the system"
    show CPU down
    jump CPU Intial

    return

label CPU Initial:
    scene bg computer
    play music background
    show CPU down
    cpu "Designation: Central Processing Unit. You may call me CPU."
    you "I'm... inside my computer?"
    cpu "Correct. At 11:58 PM, an unexpected corruption event occured. Criticak components destabilized. Data fragmentation followed."
    you "My homework. My history paper. Please tell me it's still here."
    cpu "The ile exists. However, it has been scattered."
    you "Scattered where?!"
    cpu "Across corrupted sectors of this system. The components that maintain this machine have been destabilized. Their memory banks fractured. Their trust parameters compromised."
    you "Trust parameters?"
    cpu "They will not relenquish what they guard to a stranger."
    you "So what do I do?"
    cpu "You must repair them."
    you "Repair... computer parts?"
    cpu "Not with tools. With connection."
    show CPU chill
    show Fan chill at left 
    with dissolve
    pause 1.0
    hide Fan chill with dissolve
    show RAM chill at left 
    with dissolve
    pause 1.0
    hide RAM chill with dissolve
    show CPU down
    cpu "each corrupted component holds a fragment of your file's location map. Gain their friendship. Stabilize their corruption. They will reward you eith their fragment."
    you "And if I don't?"
    cpu "At 6:00 AM, your assignment will remain lost."
    show clock 1203 at right 
    you "Six hours. i can do this. I think."
    hide clock 1203
    cpu "You will begin with the Memory Sector. The RAM entity is unstable but closest to recovery."
    you "RAM... like Random Access Memory?"
    cpu "Correct. Be warned corruption amplifies doubt and fear. The components may not behave logically."
    you "So I just... talk to them?"
    cpu "Listen to them. Help them remeber who they are."
    you "And then they give me a piece of the map?"
    cpu "If friendship threshold is achieved; yes."
    you "Friendship theshold?"
    cpu "A measurement of trust."
    you "Right. Sure. Fix my computer with the power of friendship. Before sunrise."
    pause 1.0
    cpu "Correct."
    show CPU down at right
    scene bg glowing tunnel
    cpu "Proceed. I will monitor system integrity. Return when you recover a fragment."
    you "Wait. Why are you not corrupted?"
    cpu "I am... partially shielded..."
    you "That's not reassuring."
    cpu "Time is a limited resource"
    play sound destabilizing
    scene bg destabilized tunnel
    cpu "And user-"
    you "Yeah?"
    cpu "You should know... the vorruption did not begin in the system."
    you "What does that mean?"
    cpu "you were the kast process running before failure."
    hide CPU down
    pause 0.1
    show CPU down at right 
    cpu "Memory sector initializing."
    cpu "Repair them. Reassemble the map. Retrieve your file."
    hide CPU down with dissolve
    you "Okay. RAM first. Then the others. Piece by piece."
    show clock 1207 at right
    "SYSTEM MESSAGE:
    OBJECTIVE UPDATED:
    -> Locate the Memory Sector
    -> Stabilize RAM
    -> Obtain Map Fragment 1"
    scene bg black with dissolve
    jump RAM

label RAM:
    



