define cpu = Character("CPU")
define fan = Character("Fanny")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")

default friendship = 0
default memory_fragments_collected = 0
default corruption_level = 63
default map_fragments = 0
default slots_pos = {
    "Slot 1": (150, 400),
    "Slot 2": (350, 400),
    "Slot 3": (550, 400),
    "Slot 4": (750, 400),
}

# ----------------------------------------
# START OF GAME
# ----------------------------------------
label start:
    scene bg black
    you "Hello?"
    "... "
    you "Why is it so dark...? Did the power go out?"
    you "Wait. I was typing. I was finishing the last paragraph. The conclusion... the bibliography-"
    show clock 1200
    you "Midnight."
    hide clock 1200
    you "No no no no - it's due at 6AM. I saved it. I definitely saved it."
    show error_message
    you "...What?"
    hide error_message
    scene bg computer with fade
    you "Where am I?"
    cpu "You are inside the system."
    show CPU down
    jump CPU_Initial

label CPU_Initial:
    scene bg computer
    show CPU down
    cpu "Designation: Central Processing Unit. You may call me CPU."
    you "I'm... inside my computer?"
    cpu "Correct. At 11:58 PM, an unexpected corruption event occurred. Critical components destabilized. Data fragmentation followed."
    you "My homework. My history paper. Please tell me it's still here."
    cpu "The file exists. However, it has been scattered."
    you "Scattered where?!"
    cpu "Across corrupted sectors of this system. The components that maintain this machine have been destabilized. Their memory banks fractured. Their trust parameters compromised."
    you "Trust parameters?"
    cpu "They will not relinquish what they guard to a stranger."
    you "So what do I do?"
    cpu "You must repair them."
    you "Repair... computer parts?"
    cpu "Not with tools. With connection."
    show CPU chill
    show Fan chill at left with dissolve
    pause 1.0
    hide Fan chill with dissolve
    show RAM chill at left with dissolve
    pause 1.0
    hide RAM chill with dissolve
    show CPU down
    cpu "Each corrupted component holds a fragment of your file's location map. Gain their friendship. Stabilize their corruption. They will reward you with their fragment."
    you "And if I don't?"
    cpu "At 6:00 AM, your assignment will remain lost."
    show clock 1203 at right
    you "Six hours. I can do this. I think."
    hide clock 1203
    cpu "You will begin with the Memory Sector. The RAM entity is unstable but closest to recovery."
    you "RAM... like Random Access Memory?"
    cpu "Correct. Be warned, corruption amplifies doubt and fear. The components may not behave logically."
    you "So I just... talk to them?"
    cpu "Listen to them. Help them remember who they are."
    you "And then they give me a piece of the map?"
    cpu "If friendship threshold is achieved; yes."
    you "Friendship threshold?"
    cpu "A measurement of trust."
    you "Right. Sure. Fix my computer with the power of friendship. Before sunrise."
    pause 1.0
    cpu "Correct."
    show CPU down at right
    scene bg glowing_tunnel
    cpu "Proceed. I will monitor system integrity. Return when you recover a fragment."
    you "Wait. Why are you not corrupted?"
    cpu "I am... partially shielded..."
    you "That's not reassuring."
    cpu "Time is a limited resource."
    scene bg destabilized_tunnel
    cpu "And user-"
    you "Yeah?"
    cpu "You should know... the corruption did not begin in the system."
    you "What does that mean?"
    cpu "You were the last process running before failure."
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

# ----------------------------------------
# RAM ENCOUNTER
# ----------------------------------------
label RAM:
    scene bg RAM_gym
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
        "I'm looking for my homework file, I think you might have part of it.":
            jump polite_RAM
        "Woah. You are huge. Do you bench-press hard drives?":
            jump flattery_RAM
        "Move. I don't have time for this.":
            jump rude_RAM

label polite_RAM:
    you "I'm looking for my homework file, I think you might have part of it."
    show RAM confused
    ram "Homework...? Words... paragraphs... citations..."
    ram "TOO MANY FILES! TOO MANY FRAGMENTS! I CAN'T HOLD IT ALL!"
    $ friendship = 5
    "FRIENDSHIP +5"
    you "It's okay. You're RAM, right? You hold things temporarily. That's your job."
    show RAM down
    ram "Temporary... yes. Fast. Strong. But corruption makes weights heavier..."
    jump RAM_continued

label flattery_RAM:
    you "Woah. You are huge. Do you bench-press hard drives?"
    show RAM thumbs
    ram "HA! I BENCH ENTIRE APPLICATIONS!"
    $ friendship = 8
    "FRIENDSHIP +8"
    show RAM down
    ram "But lately... weights feel scrambled. Files slip. Thoughts fragment."
    you "Maybe you're overloaded?"
    ram "Over... loaded?"
    jump RAM_continued

label rude_RAM:
    you "Move. I don't have time for this."
    scene bg RAM_gym_red
    show RAM confused
    ram "DISRESPECT DETECTED"
    $ friendship -= 10
    "FRIENDSHIP -10"
    ram "YOU THINK MEMORY IS EASY?! I HOLD EVERYTHING FOR YOU!"
    $ corruption_level = 70
    "CORRUPTION LEVEL: 70%"
    jump RAM_failed

label RAM_continued:
    show RAM down
    ram "Something is wrong. My stacks feel scrambled. I try to remember... but it slips."
    you "What do you remember about my homework?"
    ram "I remember... introduction... three body paragraphs..."
    show RAM confused
    ram "IT VANISHES!"
    menu:
        "What do you respond with?"
        "You're trying too hard. Maybe slow down.":
            jump empathy_RAM
        "You just need to lift more. Push through it!":
            jump harder_RAM
        "This is useless. I'll find someone else.":
            jump dismissive_RAM

label empathy_RAM:
    you "You're trying too hard. Maybe slow down."
    show RAM down
    ram "Slow...? But I am built for speed."
    you "Even strong systems need balance."
    $ friendship += 10
    "FRIENDSHIP +10"
    $ corruption_level = 55
    "CORRUPTION LEVEL: 55%"
    ram "Balance... maybe I forgot that."
    jump RAM_minigame

label harder_RAM:
    you "You just need to lift more. Push through it!"
    show RAM confused
    ram "YES. MORE LOAD!"
    $ friendship -= 5
    "FRIENDSHIP -5"
    $ corruption_level = 75
    "CORRUPTION LEVEL: 75%"
    ram "TOO MUCH- TOO MUCH-"
    if friendship >= 5:
        jump RAM_minigame
    else:
        jump RAM_failed

label dismissive_RAM:
    you "This is useless. I'll find someone else."
    show RAM down
    ram "Memory is never useless."
    $ friendship -= 15
    "FRIENDSHIP -15"
    jump RAM_failed

label RAM_failed:
    scene bg RAM_gym_red
    show RAM confused
    ram "...Hmph. I don't know you well enough. I can't let you touch the fragments."
    you "Wait, but I just need a piece of the map..."
    ram "No. My circuits aren't ready to share. Not with someone I can't trust."
    "FRIENDSHIP TOO LOW - MINIGAME LOCKED"
    "CORRUPTION LEVEL: 60%"
    scene bg black with fade
    return

# ----------------------------------------
# RAM MINI-GAME
# ----------------------------------------
label RAM_minigame:
    if friendship < 5:
        jump RAM_failed

    show RAM down
    ram "If you wish to help… prove your strength!"
    "He gestures to four corrupted memory blocks floating in mid-air."

    $ drag_blocks = ["Block A", "Block B", "Block C", "Block D"]
    $ block_positions = {}
    $ correct_slots = {}
    $ mini_game_score = 0

    python:
        import random
        for block in drag_blocks:
            correct_slots[block] = random.choice(list(slots_pos.keys()))
            block_positions[block] = (random.randint(100, 700), random.randint(100, 200))

    call screen ram_sort_minigame

# ----------------------------------------
# DRAG-AND-DROP SCREEN
# ----------------------------------------
screen ram_sort_minigame():
    add "bg_RAM_gym.png"
    add "RAM_down.png" at Position(xalign=0.5, yalign=0.1)
    for slot, pos in slots_pos.items():
        add "mem_slot.png" at Position(xpos=pos[0], ypos=pos[1])
    for block in drag_blocks:
        drag:
            draggable True
            drag_name block
            xpos block_positions[block][0]
            ypos block_positions[block][1]
            add "mem_block_" + str(drag_blocks.index(block)+1) + ".png"
    textbutton "Done" action Function(confirm_blocks) xpos 700 ypos 50

# ----------------------------------------
# MINI-GAME LOGIC
# ----------------------------------------
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
    return

label RAM_minigame_partial:
    show RAM down
    ram "Better… but not perfect. I can spare only partial recall."
    "You gain some memory stability but the map fragment is still locked."
    "FRIENDSHIP +5"
    return

label RAM_minigame_lose:
    show RAM frustrated
    ram "OVERLOAD! The fragments scatter! You’ll have to come back when you can handle the load."
    "FRIENDSHIP -10"
    "MAP FRAGMENT LOCKED"
    returndefine cpu = Character("CPU")
define fan = Character("Fanny")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")

default friendship = 0
default memory_fragments_collected = 0
default corruption_level = 63
default map_fragments = 0
default slots_pos = {
    "Slot 1": (150, 400),
    "Slot 2": (350, 400),
    "Slot 3": (550, 400),
    "Slot 4": (750, 400),
}

# ----------------------------------------
# START OF GAME
# ----------------------------------------
label start:
    scene bg black
    you "Hello?"
    "... "
    you "Why is it so dark...? Did the power go out?"
    you "Wait. I was typing. I was finishing the last paragraph. The conclusion... the bibliography-"
    show clock 1200
    you "Midnight."
    hide clock 1200
    you "No no no no - it's due at 6AM. I saved it. I definitely saved it."
    show error_message
    you "...What?"
    hide error_message
    scene bg computer with fade
    you "Where am I?"
    cpu "You are inside the system."
    show CPU down
    jump CPU_Initial

label CPU_Initial:
    scene bg computer
    show CPU down
    cpu "Designation: Central Processing Unit. You may call me CPU."
    you "I'm... inside my computer?"
    cpu "Correct. At 11:58 PM, an unexpected corruption event occurred. Critical components destabilized. Data fragmentation followed."
    you "My homework. My history paper. Please tell me it's still here."
    cpu "The file exists. However, it has been scattered."
    you "Scattered where?!"
    cpu "Across corrupted sectors of this system. The components that maintain this machine have been destabilized. Their memory banks fractured. Their trust parameters compromised."
    you "Trust parameters?"
    cpu "They will not relinquish what they guard to a stranger."
    you "So what do I do?"
    cpu "You must repair them."
    you "Repair... computer parts?"
    cpu "Not with tools. With connection."
    show CPU chill
    show Fan chill at left with dissolve
    pause 1.0
    hide Fan chill with dissolve
    show RAM chill at left with dissolve
    pause 1.0
    hide RAM chill with dissolve
    show CPU down
    cpu "Each corrupted component holds a fragment of your file's location map. Gain their friendship. Stabilize their corruption. They will reward you with their fragment."
    you "And if I don't?"
    cpu "At 6:00 AM, your assignment will remain lost."
    show clock 1203 at right
    you "Six hours. I can do this. I think."
    hide clock 1203
    cpu "You will begin with the Memory Sector. The RAM entity is unstable but closest to recovery."
    you "RAM... like Random Access Memory?"
    cpu "Correct. Be warned, corruption amplifies doubt and fear. The components may not behave logically."
    you "So I just... talk to them?"
    cpu "Listen to them. Help them remember who they are."
    you "And then they give me a piece of the map?"
    cpu "If friendship threshold is achieved; yes."
    you "Friendship threshold?"
    cpu "A measurement of trust."
    you "Right. Sure. Fix my computer with the power of friendship. Before sunrise."
    pause 1.0
    cpu "Correct."
    show CPU down at right
    scene bg glowing_tunnel
    cpu "Proceed. I will monitor system integrity. Return when you recover a fragment."
    you "Wait. Why are you not corrupted?"
    cpu "I am... partially shielded..."
    you "That's not reassuring."
    cpu "Time is a limited resource."
    scene bg destabilized_tunnel
    cpu "And user-"
    you "Yeah?"
    cpu "You should know... the corruption did not begin in the system."
    you "What does that mean?"
    cpu "You were the last process running before failure."
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

# ----------------------------------------
# RAM ENCOUNTER
# ----------------------------------------
label RAM:
    scene bg RAM_gym
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
        "I'm looking for my homework file, I think you might have part of it.":
            jump polite_RAM
        "Woah. You are huge. Do you bench-press hard drives?":
            jump flattery_RAM
        "Move. I don't have time for this.":
            jump rude_RAM

label polite_RAM:
    you "I'm looking for my homework file, I think you might have part of it."
    show RAM confused
    ram "Homework...? Words... paragraphs... citations..."
    ram "TOO MANY FILES! TOO MANY FRAGMENTS! I CAN'T HOLD IT ALL!"
    $ friendship = 5
    "FRIENDSHIP +5"
    you "It's okay. You're RAM, right? You hold things temporarily. That's your job."
    show RAM down
    ram "Temporary... yes. Fast. Strong. But corruption makes weights heavier..."
    jump RAM_continued

label flattery_RAM:
    you "Woah. You are huge. Do you bench-press hard drives?"
    show RAM thumbs
    ram "HA! I BENCH ENTIRE APPLICATIONS!"
    $ friendship = 8
    "FRIENDSHIP +8"
    show RAM down
    ram "But lately... weights feel scrambled. Files slip. Thoughts fragment."
    you "Maybe you're overloaded?"
    ram "Over... loaded?"
    jump RAM_continued

label rude_RAM:
    you "Move. I don't have time for this."
    scene bg RAM_gym_red
    show RAM confused
    ram "DISRESPECT DETECTED"
    $ friendship -= 10
    "FRIENDSHIP -10"
    ram "YOU THINK MEMORY IS EASY?! I HOLD EVERYTHING FOR YOU!"
    $ corruption_level = 70
    "CORRUPTION LEVEL: 70%"
    jump RAM_failed

label RAM_continued:
    show RAM down
    ram "Something is wrong. My stacks feel scrambled. I try to remember... but it slips."
    you "What do you remember about my homework?"
    ram "I remember... introduction... three body paragraphs..."
    show RAM confused
    ram "IT VANISHES!"
    menu:
        "What do you respond with?"
        "You're trying too hard. Maybe slow down.":
            jump empathy_RAM
        "You just need to lift more. Push through it!":
            jump harder_RAM
        "This is useless. I'll find someone else.":
            jump dismissive_RAM

label empathy_RAM:
    you "You're trying too hard. Maybe slow down."
    show RAM down
    ram "Slow...? But I am built for speed."
    you "Even strong systems need balance."
    $ friendship += 10
    "FRIENDSHIP +10"
    $ corruption_level = 55
    "CORRUPTION LEVEL: 55%"
    ram "Balance... maybe I forgot that."
    jump RAM_minigame

label harder_RAM:
    you "You just need to lift more. Push through it!"
    show RAM confused
    ram "YES. MORE LOAD!"
    $ friendship -= 5
    "FRIENDSHIP -5"
    $ corruption_level = 75
    "CORRUPTION LEVEL: 75%"
    ram "TOO MUCH- TOO MUCH-"
    if friendship >= 5:
        jump RAM_minigame
    else:
        jump RAM_failed

label dismissive_RAM:
    you "This is useless. I'll find someone else."
    show RAM down
    ram "Memory is never useless."
    $ friendship -= 15
    "FRIENDSHIP -15"
    jump RAM_failed

label RAM_failed:
    scene bg RAM_gym_red
    show RAM confused
    ram "...Hmph. I don't know you well enough. I can't let you touch the fragments."
    you "Wait, but I just need a piece of the map..."
    ram "No. My circuits aren't ready to share. Not with someone I can't trust."
    "FRIENDSHIP TOO LOW - MINIGAME LOCKED"
    "CORRUPTION LEVEL: 60%"
    scene bg black with fade
    return

# ----------------------------------------
# RAM MINI-GAME
# ----------------------------------------
label RAM_minigame:
    if friendship < 5:
        jump RAM_failed

    show RAM down
    ram "If you wish to help… prove your strength!"
    "He gestures to four corrupted memory blocks floating in mid-air."

    $ drag_blocks = ["Block A", "Block B", "Block C", "Block D"]
    $ block_positions = {}
    $ correct_slots = {}
    $ mini_game_score = 0

    python:
        import random
        for block in drag_blocks:
            correct_slots[block] = random.choice(list(slots_pos.keys()))
            block_positions[block] = (random.randint(100, 700), random.randint(100, 200))

    call screen ram_sort_minigame

# ----------------------------------------
# DRAG-AND-DROP SCREEN
# ----------------------------------------
screen ram_sort_minigame():
    add "bg_RAM_gym.png"
    add "RAM_down.png" at Position(xalign=0.5, yalign=0.1)
    for slot, pos in slots_pos.items():
        add "mem_slot.png" at Position(xpos=pos[0], ypos=pos[1])
    for block in drag_blocks:
        drag:
            draggable True
            drag_name block
            xpos block_positions[block][0]
            ypos block_positions[block][1]
            add "mem_block_" + str(drag_blocks.index(block)+1) + ".png"
    textbutton "Done" action Function(confirm_blocks) xpos 700 ypos 50

# ----------------------------------------
# MINI-GAME LOGIC
# ----------------------------------------
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
    return

label RAM_minigame_partial:
    show RAM down
    ram "Better… but not perfect. I can spare only partial recall."
    "You gain some memory stability but the map fragment is still locked."
    "FRIENDSHIP +5"
    return

label RAM_minigame_lose:
    show RAM frustrated
    ram "OVERLOAD! The fragments scatter! You’ll have to come back when you can handle the load."
    "FRIENDSHIP -10"
    "MAP FRAGMENT LOCKED"
    return




