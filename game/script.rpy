# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cpu = Character("CPU")
define fan = Character("Fanny")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")
$ friendship = 0
$ memory_fragments_collected = 0
$ corruption_level = 63
$ map_fragments = 0

# The game starts here.

label start:
    scene bg black
    #play music background 
    you "Hello?"
    "..."
    you "Why is it so dark...? Did the power go out?"
    #play sound keyboard
    you "Wait. I was typing. I was finishing the last paragraph. The conclusion... the bibliography-"
    show clock 1200
    you "Midnight."
    hide clock 1200
    you "No no no no - it's due at 6AM. I saved it. I definitley saved it."
    #play sound error_sound
    show error_message
    you "...What?"
    hide error_message
    scene bg computer
    with fade
    you "Where am I?"
    cpu "You are inside the system"
    show CPU down
    jump CPU_Initial

    return

label CPU_Initial:
    scene bg computer
    #play music background
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
    #play sound destabilizing
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
    scene bg RAM gym 
    #play music background
    "SYSTEM MESSAGE:
    LOCATION: MEMORY SECTOR
    ENTITY DETECTED: RAM
    CORRUPTION LEVEL: 63%
    FRIENDSHIP: 0"
    show RAM WTF 
    ram "WHO ENTERS THE MEMORY MUSCLE ZONE?!"
    you "Uh... hi?"
    ram "STATE YOUR PROCESS!"
    menu:
        "What do you respond with?"
        "I'm looking for my homework file. I think you might have part of it."
            jump polite_RAM
        "Woah. You are huge. Do you bench-press hard drives?"
            jump flattery_RAM
        "Move I don't have time for this."
            jump rude_RAM

label polite_RAM:
    you "I'm looking for my homework file, I think you might have part of it."
    ram "Homework...? Words... paragraphs... citations..."
    show RAM confused
    ram "TOO MANY FILES! TOO MANY FRAGMENTS! I CAN'T HOLD IT ALL!"
    "+5 Friendship"
    $ friendship = 5
    you "It's okay. You're RAM, right? You hold things temporarily. That's your job."
    show RAM down
    ram "Temprary... yes. Fast. Strong. But corruption makes weights heaver..."
    jump RAM_continued

label flattery_RAM:
    you "Woah. You are huge. Do you bench-press hard drives?"
    show RAM thumbs
    ram "HA! I BENCH ENTIRE APPLICATIONS!"
    "+8 Friendship"
    $ friendship = 8
    show RAM down
    ram "But lately... weights feel scrambled. Fils slip. Thoughts fragment."
    you "Maybe you're overloaded?"
    ram "Over... loaded?"
    jump RAM_continued

label rude_RAM:
    you "Move. I don't have time for this."
    scene bg RAM gym red
    show RAM confused
    ram "DISRESPECT DETECTED"
    "-10 friendship"
    ram "YOU THINK MEMORY IS EASY?! I HOLD EVERYTHING FOR YOU!"
    "corruption level: 70%"
    jump RAM_failed

label RAM_continued
    show RAM down
    ram "Something is wrong. My stacks feel scrambled. I try to remeber... but it slips."
    you "What do you remeber about my homework?"
    ram "I remember... introduction... three body pragraphs..."
    show RAM confused
    ram "IT VANISHES!"
    menu:
        "What do you respond with?"
        "You're trying too hard. Maybe slow down."
            jump empathy_RAM
        "You just need to lift more. Push through it!"
            jump harder_RAM
        "This is useless. I'll find someone else."
            jump dismissive_RAM

label empathy_RAM:
    you "You're trying too hard. Maybe slow down."
    show RAM down
    ram "Slow...? But I am built for speed."
    you "Even strong systems need balance."
    "+10 friendship
    corruption level: 55%"
    $ corruption += 10
    ram "Balance... maybe I forgot that."
    jump RAM_minigame

label harder_RAM:
    you "you just need to lift more. Push through it!"
    show RAM confused
    ram "YES. MORE LOAD!"
    "-5 friendship
    corruption level: 75%"
    $ friendship -= 5 
    ram "TOO MUCH- TOO MUCH-"
    if friendship >= 5:
        jump RAM_minigame
    else:
        jump RAM_failed

label dismissive_RAM:
    you "This is useless. I'll find someone else."
    show RAM down
    ram "Memory is never useless."
    "-15 friendship"
    jump RAM_failed

label RAM_failed:
    scene bg RAM gym red
    show RAM confused
    ram "...Hmph. I don't know you well enough. I can't let you touch the fragments."
    you "Wait, but I just need a piece of the map..."
    ram "No. My circuits aren't ready to share. Not with someone I can't trust."
    "FRIENDSHIP TOO LOW - MINIGAME LOCKED
    CORRUPTION LEVEL 60%"
    scene bg black with fade
    jump ...

define cpu = Character("CPU")
define fan = Character("Fanny")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")
$ friendship = 0

# The game starts here.

label start:
    scene bg black
    #play music background 
    you "Hello?"
    "..."
    you "Why is it so dark...? Did the power go out?"
    #play sound keyboard
    you "Wait. I was typing. I was finishing the last paragraph. The conclusion... the bibliography-"
    show clock 1200
    you "Midnight."
    hide clock 1200
    you "No no no no - it's due at 6AM. I saved it. I definitley saved it."
    #play sound error_sound
    show error_message
    you "...What?"
    hide error_message
    scene bg computer
    with fade
    you "Where am I?"
    cpu "You are inside the system"
    show CPU down
    jump CPU_Initial

    return

label CPU_Initial:
    scene bg computer
    #play music background
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
    #play sound destabilizing
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
    scene bg RAM gym 
    #play music background
    "SYSTEM MESSAGE:
    LOCATION: MEMORY SECTOR
    ENTITY DETECTED: RAM
    CORRUPTION LEVEL: 63%
    FRIENDSHIP: 0"
    show RAM WTF 
    ram "WHO ENTERS THE MEMORY MUSCLE ZONE?!"
    you "Uh... hi?"
    ram "STATE YOUR PROCESS!"
    menu:
        "What do you respond with?"
        "I'm looking for my homework file. I think you might have part of it."
            jump polite_RAM
        "Woah. You are huge. Do you bench-press hard drives?"
            jump flattery_RAM
        "Move I don't have time for this."
            jump rude_RAM

label polite_RAM:
    you "I'm looking for my homework file, I think you might have part of it."
    ram "Homework...? Words... paragraphs... citations..."
    show RAM confused
    ram "TOO MANY FILES! TOO MANY FRAGMENTS! I CAN'T HOLD IT ALL!"
    "+5 Friendship"
    $ friendship = 5
    you "It's okay. You're RAM, right? You hold things temporarily. That's your job."
    show RAM down
    ram "Temprary... yes. Fast. Strong. But corruption makes weights heaver..."
    jump RAM_continued

label flattery_RAM:
    you "Woah. You are huge. Do you bench-press hard drives?"
    show RAM thumbs
    ram "HA! I BENCH ENTIRE APPLICATIONS!"
    "+8 Friendship"
    $ friendship = 8
    show RAM down
    ram "But lately... weights feel scrambled. Fils slip. Thoughts fragment."
    you "Maybe you're overloaded?"
    ram "Over... loaded?"
    jump RAM_continued

label rude_RAM:
    you "Move. I don't have time for this."
    scene bg RAM gym red
    show RAM confused
    ram "DISRESPECT DETECTED"
    "-10 friendship"
    ram "YOU THINK MEMORY IS EASY?! I HOLD EVERYTHING FOR YOU!"
    "corruption level: 70%"
    jump RAM_failed

label RAM_continued
    show RAM down
    ram "Something is wrong. My stacks feel scrambled. I try to remeber... but it slips."
    you "What do you remeber about my homework?"
    ram "I remember... introduction... three body pragraphs..."
    show RAM confused
    ram "IT VANISHES!"
    menu:
        "What do you respond with?"
        "You're trying too hard. Maybe slow down."
            jump empathy_RAM
        "You just need to lift more. Push through it!"
            jump harder_RAM
        "This is useless. I'll find someone else."
            jump dismissive_RAM

label empathy_RAM:
    you "You're trying too hard. Maybe slow down."
    show RAM down
    ram "Slow...? But I am built for speed."
    you "Even strong systems need balance."
    "+10 friendship
    corruption level: 55%"
    $ corruption += 10
    ram "Balance... maybe I forgot that."
    jump RAM_minigame

label harder_RAM:
    you "you just need to lift more. Push through it!"
    show RAM confused
    ram "YES. MORE LOAD!"
    "-5 friendship
    corruption level: 75%"
    $ friendship -= 5 
    ram "TOO MUCH- TOO MUCH-"
    if friendship >= 5:
        jump RAM_minigame
    else:
        jump RAM_failed

label dismissive_RAM:
    you "This is useless. I'll find someone else."
    show RAM down
    ram "Memory is never useless."
    "-15 friendship"
    jump RAM_failed

label RAM_failed:
    scene bg RAM gym red
    show RAM confused
    ram "...Hmph. I don't know you well enough. I can't let you touch the fragments."
    you "Wait, but I just need a piece of the map..."
    ram "No. My circuits aren't ready to share. Not with someone I can't trust."
    "FRIENDSHIP TOO LOW - MINIGAME LOCKED
    CORRUPTION LEVEL 60%"
    scene bg black with fade
    jump ...

label RAM_minigame:
    show RAM down
    ram "If you wish to help… prove your strength!"
    "He gestures to four corrupted memory blocks floating in mid-air."
    $ drag_blocks = ["Block A", "Block B", "Block C", "Block D"]
    $ block_positions = {}
    $ correct_slots = {}
    $ mini_game_score = 0
    python:
        import random
        slots_pos = {
            "Slot 1": (150, 400),
            "Slot 2": (350, 400),
            "Slot 3": (550, 400),
            "Slot 4": (750, 400),}
        for block in drag_blocks:
            correct_slots[block] = random.choice(list(slots_pos.keys()))
            block_positions[block] = (random.randint(100, 700), random.randint(100, 200))
    call screen ram_sort_minigame

screen ram_sort_minigame():
    scene bg RAM gym
    show RAM down at Position(xalign=0.5, yalign=0.1)
    for slot, pos in slots_pos.items():
        add "mem_slot.png" at Position(xpos=pos[0], ypos=pos[1])
    for block in drag_blocks:
        drag:
            draggable True
            drag_name block
            drag_area (0, 0, 800, 600)
            xpos block_positions[block][0]
            ypos block_positions[block][1]
            child Displayable("mem_block_" + str(drag_blocks.index(block)+1) + ".png")
    textbutton "Done" action Function(confirm_blocks) xpos 700 ypos 50

python:
    def confirm_blocks():
        global mini_game_score, memory_fragments_collected, friendship, corruption_level, map_fragments
        mini_game_score = 0
        for block in drag_blocks:
            x, y = block_positions[block]
            slot_x, slot_y = slots_pos[correct_slots[block]]
            if abs(x - slot_x) <= 50 and abs(y - slot_y) <= 50:
                mini_game_score += 1
                renpy.notify(f"{block} placed correctly!")
            else:
                renpy.notify(f"{block} in wrong slot.")
        if mini_game_score >= 3:
            memory_fragments_collected += 1
            friendship += 10
            corruption_level = 30
            map_fragments += 1
            renpy.jump("RAM_minigame_win")
        elif mini_game_score >= 1:
            friendship += 5
            corruption_level = 45
            renpy.jump("RAM_minigame_partial")
        else:
            friendship -= 10
            corruption_level = 80
            renpy.jump("RAM_minigame_lose")

label RAM_minigame_win:
    show RAM happy
    ram "Outstanding! You lightened my load and stabilized my memory."
    "Sheep hands you a fragment of the map."
    "MAP FRAGMENT 1 OBTAINED"
    "FRIENDSHIP +10"
    jump ...

label RAM_minigame_partial:
    show RAM down
    ram "Better… but not perfect. I can spare only partial recall."
    "You gain some memory stability but the map fragment is still locked."
    "FRIENDSHIP +5"
    jump ...

label RAM_minigame_lose:
    show RAM frustrated
    ram "OVERLOAD! The fragments scatter! You’ll have to come back when you can handle the load."
    "FRIENDSHIP -10"
    "MAP FRAGMENT LOCKED"
    jump ...




