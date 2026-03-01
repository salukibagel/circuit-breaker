# =====================================================
# CHARACTERS
# =====================================================

define cpu = Character("CPU")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")
define system = Character(None)

# =====================================================
# DEFAULT VARIABLES
# =====================================================

default friendship = 0
default corruption_level = 63
default memory_fragments_collected = 0

default drag_blocks = []
default correct_slots = {}
default slots_pos = {
    "Slot 1": (150, 420),
    "Slot 2": (350, 420),
    "Slot 3": (550, 420),
    "Slot 4": (750, 420),
}

# =====================================================
# START
# =====================================================

label start:

    scene bg black

    you "Hello?"
    "..."
    you "Why is it so dark...? Did the power go out?"
    you "Wait. I was typing. I was finishing the last paragraph."
    you "The conclusion... the bibliography—"

    show clock 1200
    you "Midnight."
    hide clock

    you "No no no no — it's due at 6AM."
    you "I saved it."
    you "I definitely saved it."

    show error_message
    you "...What?"
    hide error_message

    scene bg computer with fade

    you "Where am I?"

    show CPU down

    cpu "You are inside the system."

    jump CPU_Initial


# =====================================================
# CPU FULL DIALOGUE
# =====================================================

label CPU_Initial:
    show CPU down

    cpu "Designation: Central Processing Unit."
    cpu "You may call me CPU."

    you "I'm... inside my computer?"

    cpu "Correct."
    cpu "At 11:58 PM, an unexpected corruption event occurred."
    cpu "Critical components destabilized."
    cpu "Data fragmentation followed."

    you "My homework."
    you "My history paper."
    you "Please tell me it's still here."

    cpu "The file exists."
    cpu "However, it has been scattered."

    you "Scattered where?!"

    cpu "Across corrupted sectors of this system."
    cpu "The components that maintain this machine have been destabilized."
    cpu "Their memory banks fractured."
    cpu "Their trust parameters compromised."

    you "Trust parameters?"

    cpu "They will not relinquish what they guard to a stranger."

    you "So what do I do?"

    cpu "You must repair them."

    you "Repair computer parts?"

    cpu "Not with tools."
    cpu "With connection."

    cpu "Each corrupted component holds a fragment of your file's location map."
    cpu "Gain their friendship."
    cpu "Stabilize their corruption."
    cpu "They will reward you with their fragment."

    you "And if I don't?"

    cpu "At 6:00 AM, your assignment will remain lost."

    show clock 1203 at right
    you "Six hours."
    you "I can do this."
    you "I think."
    hide clock

    cpu "You will begin with the Memory Sector."
    cpu "The RAM entity is unstable but closest to recovery."

    you "RAM. Like Random Access Memory?"

    cpu "Correct."
    cpu "Be warned."
    cpu "Corruption amplifies doubt and fear."
    cpu "The components may not behave logically."

    you "So I just talk to them?"

    cpu "Listen to them."
    cpu "Help them remember who they are."

    you "And then they give me a piece of the map?"

    cpu "If friendship threshold is achieved. Yes."

    you "Friendship threshold?"

    cpu "A measurement of trust."

    you "Right."
    you "Sure."
    you "Fix my computer with the power of friendship."
    you "Before sunrise."

    cpu "Correct."

    scene bg glowing_tunnel with fade

    cpu "Proceed."
    cpu "Return when you recover a fragment."

    you "Wait."
    you "Why are you not corrupted?"

    cpu "I am partially shielded."

    you "That's not reassuring."

    cpu "Time is a limited resource."

    scene bg destabilized_tunnel

    cpu "And user—"

    you "Yeah?"

    cpu "You should know."
    cpu "The corruption did not begin in the system."

    you "What does that mean?"

    cpu "You were the last process running before failure."

    hide CPU down with dissolve

    you "Okay."
    you "RAM first."
    you "Then the others."
    you "Piece by piece."

    system "Objective Updated\nLocate Memory Sector\nStabilize RAM\nObtain Map Fragment"

    jump RAM


# =====================================================
# RAM FULL DIALOGUE RESTORED
# =====================================================

label RAM:

    scene bg RAM_gym

    system "Location: Memory Sector\nEntity Detected: RAM"

    show RAM WTF

    ram "WHO ENTERS THE MEMORY MUSCLE ZONE?!"

    you "Uh... hi?"

    ram "STATE YOUR PROCESS!"

    menu:
        "I'm looking for my homework file. I think you might have part of it.":
            jump polite_RAM
        "Woah. You are huge. Do you bench-press hard drives?":
            jump flattery_RAM
        "Move. I don't have time for this.":
            jump rude_RAM


label polite_RAM:

    you "I'm looking for my homework file. I think you might have part of it."

    show RAM confused

    ram "Homework...?"
    ram "Words... paragraphs... citations..."
    ram "Too many files."
    ram "Too many fragments."
    ram "I can't hold it all."

    $ friendship += 5

    you "It's okay."
    you "You're RAM, right?"
    you "You hold things temporarily."
    you "That's your job."

    show RAM down

    ram "Temporary... yes."
    ram "Fast."
    ram "Strong."
    ram "But corruption makes weights heavier..."

    jump RAM_continued


label flattery_RAM:

    you "Woah. You are huge. Do you bench-press hard drives?"

    show RAM thumbs

    ram "HA!"
    ram "I bench entire applications!"

    $ friendship += 8

    show RAM down

    ram "But lately..."
    ram "Weights feel scrambled."
    ram "Files slip."
    ram "Thoughts fragment."

    you "Maybe you're overloaded?"

    ram "Overloaded..."

    jump RAM_continued


label rude_RAM:

    scene bg RAM_gym_red

    show RAM angry

    ram "Disrespect detected."
    ram "You think memory is easy?"
    ram "I hold everything for you."

    $ friendship -= 10

    jump RAM_failed


label RAM_continued:

    show RAM down

    ram "Something is wrong."
    ram "My stacks feel scrambled."
    ram "I try to remember..."
    ram "But it slips."

    you "What do you remember about my homework?"

    show RAM confused

    ram "I remember..."
    ram "Introduction..."
    ram "Three body paragraphs..."
    ram "It vanishes."

    menu:
        "You're trying too hard. Maybe slow down.":
            jump empathy_RAM
        "You just need to lift more. Push through it.":
            jump harder_RAM
        "This is useless. I'll find someone else.":
            jump dismissive_RAM


label empathy_RAM:

    you "You're trying too hard. Maybe slow down."

    show RAM down

    ram "Slow...?"
    ram "But I am built for speed."

    you "Even strong systems need balance."

    $ friendship += 10
    $ corruption_level = 55

    ram "Balance..."
    ram "Maybe I forgot that."

    jump RAM_minigame


label harder_RAM:

    $ friendship -= 5
    if friendship >= 5:
        jump RAM_minigame
    else:
        jump RAM_failed


label dismissive_RAM:

    $ friendship -= 15
    jump RAM_failed


label RAM_failed:

    show RAM angry
    ram "I do not trust you."
    ram "I cannot share the fragments."

    return


# =====================================================
# MINI GAME
# =====================================================

label RAM_minigame:

    show RAM determined

    ram "If you wish to help..."
    ram "Prove your strength."
    ram "Sort the memory blocks."
    ram "Show me you can handle the load."

    python:
        import random
        drag_blocks = ["A","B","C","D"]
        correct_slots = {}
        for block in drag_blocks:
            correct_slots[block] = random.choice(list(slots_pos.keys()))

    call screen ram_sort_minigame
    return


screen ram_sort_minigame():

    modal True

    add "bg_RAM_gym.png"

    for slot, pos in slots_pos.items():
        add "mem_slot.png" xpos pos[0] ypos pos[1]

    for block in drag_blocks:

        drag:
            drag_name block
            draggable True
            xpos renpy.random.randint(100,700)
            ypos 150
            dragged snap_block
            add "mem_block.png"

    textbutton "Done" action Function(confirm_blocks) xpos 850 ypos 50


init python:

    def snap_block(drags, drop):
        drag = drags[0]
        block = drag.drag_name
        slot_x, slot_y = slots_pos[correct_slots[block]]
        if abs(drag.x - slot_x) < 60 and abs(drag.y - slot_y) < 60:
            drag.snap(slot_x, slot_y)

    def confirm_blocks():
        renpy.jump("RAM_win")


label RAM_win:

    show RAM happy
    ram "Outstanding."
    ram "My memory stabilizes."
    ram "Take the map fragment."
    hide RAM happy

    return




