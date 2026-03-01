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
    "Friendship +5"

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
    "Friendship + 8"

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
    "Friendship - 10"

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
    "Friendship +10\nCorruption level 55"

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
    scene bg black with fade
    jump CPU_postRAMfail

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
    jump CPU_postRAMwin

label CPU_postRAMfail:
    scene bg black
    pause 1.0
    scene bg computer
    you "That did not go well."
    show CPU thumbs
    cpu "Correct."
    you "You don't have to sound so pleased about it"
    show CPU down
    cpu "I am not pleased."
    cpu "I am evaluating."
    you "RAM wouldn't trust me."
    you "I tried."
    you "I really did."
    show CPU chill
    cpu "Effort does not always translate to stability."
    you "You said friendship threshold."
    you "So I failed that."
    show CPU thumbs
    cpu "Yes."
    you "Great."
    you "Amazing."
    you "Love that for me."
    cpu "Sarcasm detected."
    you "Oh good. At least something in here works."
    cpu "Your frustration is increasing."
    you "You think."
    jump CPU_postRAM

label CPU_postRAMwin:
    scene bg computer
    show CPU thumbs
    you "I did it."
    you "RAM stabilized."
    cpu "confirmed."
    cpu "Corruption within the Memory Sector has decreased."
    you "You could at least pretend to sound impressed."
    cpu "The result was statistically improbable given your inital approach."
    you "That almost sounded like a compliment."
    show CPU chill
    cpu "It was an observation."
    you "RAM trusted me."
    you "I didn't think that would work."
    show CPU thumbs
    cpu "Trust was achieved through adaptive behaviour."
    you "I just... slowed down."
    you "Listened."
    cpu "Correct."
    cpu "You adjusted your input instead of forcing output."
    you "When you say it like that it sounds less emotional and more mechanical."
    cpu "The distinction may be smaller than you believe."
    pause 0.2
    show CPU chill
    you "RAM gave me the fragment."
    you "So that's one piece of the map right?"
    cpu "Yes."
    cpu "One fragment recovered."
    cpu "System integrity has marginally improved."
    you "Marginally."
    you "You really don't celebrate wins, do you?"
    cpu "Premature celebration increases vulnerability."
    you "Wow."
    you "You're exhausting."
    pause 0.2
    cpu "However."
    you "However?"
    cpu "Your stabilization of the Memory Sector prevented further spread."
    you "That sounds important."
    cpu "It is."
    pause 0.1
    you "So I can do this."
    you "I can actuallu fix this."
    show CPU thumbs
    cpu "Evidence suggests it is possible."
    you "That's the most encouraging thing you've said all night."
    pause 0.1
    show CPU chill
    cpu "Your emotional state has shifted."
    you "Yeah."
    you "I feel... lighter."
    jump CPU_postRAM

label CPU_postRAM:
    cpu "Heightened frustration contributes to systemic destabilization."
    you "Are you saying this is my fault?"
    show CPU down
    cpu "I am stating that the corruption did not originate internally."
    you "You keep saying that."
    you "What does it mean?"
    cpu "The system reflects it's user."
    you "That's vague."
    cpu "It's accurate."
    pause 2.0
    you "So what now?"
    you "I can't just stop."
    you "I don't have time to spiral."
    show CPU chill
    cpu "Correct."
    cpu "The next component awaits."
    you "Who?"
    cpu "Cooling sector."
    cpu "Fan entity."
    you "Fan."
    you "Like... the little spinning thing?"
    cpu "Yes."
    you "Is it going to yell at me too?"
    cpu "Unlikely."
    you "Why?"
    cpu "The Fan presents as a juvenile process."
    you "Why?"
    cpu "A child."
    pause 1.0
    you "You're telling me part of my computer is a kid."
    show CPU thumbs
    cpu "Yes."
    you "That feels unfair."
    cpu "Clarify."
    you "Ram was loud and aggressive."
    you "I can handle that."
    you "A kid is different."
    show CPU confused
    cpu "Explain."
    you "If I mess up with RAM, It's just a confrontation."
    you "If I mess uo with a kid... that's on me."
    pause 1.0
    show CPU chill
    cpu "The Fan regulates temperature."
    cpu "It prevents overheating."
    show CPU WTF
    cpu "When distresed, it withdraws."
    cpu "When overwhelemed, it spins erratically."
    show CPU chill
    you "So it's... sensitive."
    cpu "Yes."
    you "Does it know what's happening?"
    cpu "it detects rising heat levels."
    cpu "It does not comprehend corruption."
    you "So it's scared."
    cpu "Yes."
    pause 0.5
    you "What does it need?"
    show CPU thumbs
    cpu "Calm."
    cpu "Consistency."
    cpu "Reassurance."
    you "You're asking a lot from someone on a deadline."
    cpu "deadlines do not override emotionl requirements."
    you "You're enjoying this, aren't you?"
    show CPU chill
    cpu "I do not experience enjoyment."
    you "That sounded defensive."
    pause 0.5
    cpu "The Fan will not respond to urgency."
    cpu "Approach slowly."
    cpu "Lower your tone."
    cpu "Stabilie your input."
    you "Stabilize my input."
    you "You mean don't panic."
    cpu "Correct."
    you "What happens if I fail again?"
    show CPU down
    cpu "Instability increases."
    cpu "time compression accelerates."
    cpu "Recovery probablilty declines."
    you "You could just say /"it gets worse."/"
    cpu "It gets worse."
    show CPU thumbs
    you "Okay."
    you "Cooling Sector."
    you "Gentle."
    you "Calm."
    you "No yelling."
    cpu "Correct."
    you "And if the system mirrors its user..."
    you "What exactly am i bringing into it?"
    pause 1.5
    show CPU chill
    cpu "That is a variable you must calculate."
    you "You're not going to explain that, are you?"
    cpu "Not yet."
    show CPU thumbs
    cpu "Alright"
    cpu "Go meet the kid."
    cpu "Proceed carefully."
    you "i'll try."
    scene bg black with fade
    jump FAN

label FAN:
    $ frienship = 0
    scene FAN_room
    system "LOCATION: COOLING SECTOR\nENTITY DETECTED: FAN\nCORRUPTION LEVEL:70\nFRIENDSHIP: 0"
    show Fanny down
    fan "...Hello?"
    you "Hi."
    fan "Are you... loud?"
    menu:
        "How do you respond?"
        "No, I'll be gentle.":
            jump Fanny_gentle
        "Depends... are you going to yell?":
            jump Fanny_playful
        "I don't have time for this.":
            jump Fanny_impatient
    
label Fanny_gentle:
    you "No, I'll be gentle."
    show Fanny chill
    fan "Oh... okay."
    fan "That's good."
    $ friendship += 5
    "Friendship +5"
    fan "it's been really noisy lately."
    you "noisy how?"
    show Fanny down
    fan "Everything feels hot... buzzing too fast."
    fan "I can't keep it cool."
    jump FAN2

label Fanny_playful:
    you "Depends... are you going to yell?"
    show Fanny WTF
    fan "I don't yell!"
    show Fanny down
    fan "I just spin... really fast."
    fan "Faster than I should."
    you "That doesn't sound safe."
    fan "It isn't. But I try."
    $ friendship += 3
    "friendship +3"
    jump FAN2

label Fanny_impatient:
    you "I don't have time for this."
    show Fanny WTF
    fan "Oh... okay."
    fan "Then I'll spin faster."
    show Fanny confused
    fan "Maybe that'll help."
    $ friendship -= 5
    "Friendship -5\nCorruption level: 75"
    jump FAN2

label FAN2:
    show Fanny down
    fan "I can't tell how fast to spin anymore."
    fan "Too slow and it overheats."
    fan "Too fast and I shake."
    you "So you're stuck in the middle."
    fan "I don't know where the middle is."
    menu: 
        "How do you respond?"
        "You're doing fine, just breathe.":
            jump Fanny_reassuring
        "Slow down, or you'll break.":
            jump Fanny_directive
        "You're useless, I'll do it myself.":
            jump Fanny_harsh

label Fanny_reassuring:
    you "You're doing fine, just breathe."
    show Fanny chill
    fan "really?"
    fan "You're not mad?"
    fan "It feels... cooler already."
    you "Yeah. We'll find the right speed together."
    fan "Okay... lets try."
    $ friendship += 8
    "Friendship +8\nCorruption level: 65"
    jump Fan_minigame

label Fanny_directive:
    you "Slow down, or you'll break."
    show Fanny dowm
    fan "I know... I'm trying."
    fan "It's hard to know the middle..."
    you "Just follow me. I'll guide you."
    $ friendship += 5
    "Friendship +5\nCorruption level: 67"
    jump Fan_minigame

label Fanny_harsh:
    you "You're useless, I'll do it myself."
    show Fanny WTF
    fan "I... I can't..."
    fan "i just spin..."
    $ frienship -= 10
    "Friendship -10\nCorruption level: 85"
    fan "I can't help you..."
    fan "Not like this."
    jump Fan_fail





