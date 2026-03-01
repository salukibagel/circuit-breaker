# =====================================================
# CHARACTERS
# =====================================================

define cpu = Character("CPU")
define ram = Character("Sheep")
define you = Character("User")
define clock = Character("Clock")
define error_message = Character("404")
define system = Character(None)
define fan = Character("Fanny")

$ friendship = 0
$ map_fragments = 0

image CPU WTF = Transform('images/CPU WTF.png', zoom=0.5)
image CPU chill = Transform('images/CPU chill.png', zoom=0.5)
image CPU thumbs = Transform('images/CPU thumbs.png', zoom=0.5)
image CPU confused = Transform('images/CPU confused.png', zoom=0.5)
image CPU down = Transform('images/CPU down.png', zoom=0.5)
image RAM down = Transform('images/RAM down.png', zoom=0.5)
image RAM confused = Transform('images/RAM confused.png', zoom=0.5)
image RAM chill = Transform('images/RAM chill.png', zoom=0.5)
image RAM WTF = Transform('images/RAM WTF.png', zoom=0.5)
image RAM thumbs = Transform('images/RAM thumbs.png', zoom=0.5)
image Fanny down = Transform('images/Fanny down.png', zoom=0.35)
image Fanny thumbs = Transform('image/Fanny thumbs.png', zoom=0.35)
image Fanny WTF = Transform('images/Fanny WTf.png', zoom=0.35)
image Fanny chill = Transform('images/Fanny chill.png', zoom=0.35)
image Fanny confused = Transform('images/Fanny confused.png', zoom=0.35)
image clock 1200 = Transform('images/clock 1200.png', zoom=0.25)
image clock 1203 = Transform('images/clock 1203.png', zoom=0.25)
image clock 1207 = Transform('images/clock 1207.png', zoom=0.25)
image error_message = Transform('images/error_message.png', zoom=0.25)
image bg black = Transform('images/bg black.png', zoom = 3.0)
image bg FAN_room = 'images/bg FAN_room.png'
image bg destabilized_tunnel = 'images/bg destabilized_tunnel.png'
image bg RAM_gym = 'images/bg RAM_gym.png'
image bg computer = 'images/bg computer.png'
image bg glowing_tunnel = 'images/bg glowing_tunnel.png'
image bg RAM_gym_red = 'images/bg RAM_gym_red.png'
image bg light_tunnel = Transform('images/bg light_tunnel.png', zoom = 3.0)

# =====================================================
# DEFAULT VARIABLES
# =====================================================

default friendship = 0
default corruption_level = 63
default memory_fragments_collected = 0
default map_fragments = 0

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
    "... "
    you "Why is it so dark...? Did the power go out?"
    you "Wait. I was typing. I was finishing the last paragraph."
    you "The conclusion... the bibliography—"

    show clock 1200 at truecenter
    you "Midnight."
    hide clock 1200

    you "No no no no — it's due at 6AM."
    you "I saved it."
    you "I definitely saved it."

    show error_message at truecenter
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
    hide clock 1203

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
    show CPU chill at right

    cpu "Proceed."
    cpu "Return when you recover a fragment."

    you "Wait."
    you "Why are you not corrupted?"

    cpu "I am partially shielded."

    you "That's not reassuring."

    cpu "Time is a limited resource."

    scene bg destabilized_tunnel
    show CPU chill at right

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
# RAM FULL DIALOGUE
# =====================================================

label RAM:

    scene bg RAM_gym

    system "Location: Memory Sector\nEntity Detected: RAM\nCorruption level 63\nFriendship 0"

    show RAM WTF

    ram "WHO ENTERS THE MEMORY MUSCLE ZONE?!"

    you "Uh... hi?"

    ram "STATE YOUR PROCESS!"

    menu:
        "What do you respond with?"
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
    "Friendship +8"

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

    show RAM confused

    ram "Disrespect detected."
    ram "You think memory is easy?"
    ram "I hold everything for you."

    $ friendship -= 10
    "Friendship -10"

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
        "What do you respond with?"
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

    you "You just need to lift more. Push through it."

    show RAM confused

    ram "YES. MORE LOAD!"

    $ friendship -= 5
    $ corruption_level = 75
    "Friendship -5\nCorruption level 75"

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
    "Friendship -15"

    jump RAM_failed

label RAM_failed:

    show RAM angry
    ram "I do not trust you."
    ram "I cannot share the fragments."
    scene bg black with fade
    jump CPU_postRAMfail

label RAM_minigame:

    scene bg RAM_gym
    show RAM chill

    ram "Alright… let's see if you truly understand memory."
    ram "Answer correctly, and I can trust you to stabilize me."

    # ==================================================
    # Question 1
    # ==================================================
    menu:
        "1) What is the main function of RAM in a computer?"
        "A) To store files permanently":
            $ friendship -= 5
            ram "No… that's not me. I forget when power is off."
        "B) To temporarily store data for quick access by the CPU":
            $ friendship += 5
            ram "Correct! Fast access is my job."
        "C) To control the computer's cooling system":
            $ friendship -= 5
            ram "No, I don't deal with that."

    # ==================================================
    # Question 2
    # ==================================================
    menu:
        "2) What happens if RAM is insufficient for running programs?"
        "A) The computer will run slower or programs may crash":
            $ friendship += 5
            ram "Exactly! I can only hold so much at once."
        "B) The computer gains more permanent storage":
            $ friendship -= 5
            ram "No, I can't create permanent storage."
        "C) The CPU will shut down immediately":
            $ friendship -= 5
            ram "Not quite. Programs just lag or fail."

    # ==================================================
    # Question 3
    # ==================================================
    menu:
        "3) Which type of memory is volatile and loses data when power is off?"
        "A) RAM":
            $ friendship += 5
            ram "Correct! I only remember while powered."
        "B) Hard drive":
            $ friendship -= 5
            ram "No… hard drives are permanent storage."
        "C) SSD":
            $ friendship -= 5
            ram "No, that's also non-volatile."

    # ==================================================
    # Evaluate Result
    # ==================================================
    if friendship >= 15:
        show RAM thumbs
        ram "Outstanding! You really understand memory."
        ram "I can safely give you a fragment."
        "Friendship +5\nCorruption level decreases to 50"
        $ memory_fragments_collected += 1
        "MAP FRAGMENT 1 OBTAINED"
        jump CPU_postRAMWin
    else:
        show RAM WTF
        ram "I cannot trust you yet…"
        "Friendship -5\nCorruption level increases to 75"
        "MAP FRAGMENT LOCKED"
        jump CPU_postRAMFail

# =====================================================
# CPU RESPONSE AFTER RAM
# =====================================================

label CPU_postRAMfail:
    scene bg computer
    show CPU thumbs
    you "That did not go well."
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
    cpu "Confirmed."
    cpu "Corruption within the Memory Sector has decreased."
    you "You could at least pretend to sound impressed."
    cpu "The result was statistically improbable given your initial approach."
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
    you "I can actually fix this."
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
    cpu "The system reflects its user."
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
    you "RAM was loud and aggressive."
    you "I can handle that."
    you "A kid is different."
    show CPU confused
    cpu "Explain."
    you "If I mess up with RAM, It's just a confrontation."
    you "If I mess up with a kid... that's on me."
    pause 1.0
    show CPU chill
    cpu "The Fan regulates temperature."
    cpu "It prevents overheating."
    show CPU WTF
    cpu "When distressed, it withdraws."
    cpu "When overwhelmed, it spins erratically."
    show CPU chill
    you "So it's... sensitive."
    cpu "Yes."
    you "Does it know what's happening?"
    cpu "It detects rising heat levels."
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
    cpu "Deadlines do not override emotional requirements."
    you "You're enjoying this, aren't you?"
    show CPU chill
    cpu "I do not experience enjoyment."
    you "That sounded defensive."
    pause 0.5
    cpu "The Fan will not respond to urgency."
    cpu "Approach slowly."
    cpu "Lower your tone."
    cpu "Stabilize your input."
    you "Stabilize my input."
    you "You mean don't panic."
    cpu "Correct."
    you "What happens if I fail again?"
    show CPU down
    cpu "Instability increases."
    cpu "Time compression accelerates."
    cpu "Recovery probability declines."
    you "You could just say 'it gets worse.'"
    cpu "It gets worse."
    show CPU thumbs
    you "Okay."
    you "Cooling Sector."
    you "Gentle."
    you "Calm."
    you "No yelling."
    cpu "Correct."
    you "And if the system mirrors its user..."
    you "What exactly am I bringing into it?"
    pause 1.5
    show CPU chill
    cpu "That is a variable you must calculate."
    you "You're not going to explain that, are you?"
    cpu "Not yet."
    show CPU thumbs
    cpu "Alright."
    cpu "Go meet the kid."
    cpu "Proceed carefully."
    you "I'll try."
    scene bg black with fade
    jump FAN

# =====================================================
# FAN INTERACTION
# =====================================================

label FAN:
    $ friendship = 0
    scene bg FAN_room
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
    you "Noisy how?"
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
    "Friendship +3"
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
    fan "Really?"
    fan "You're not mad?"
    fan "It feels... cooler already."
    you "Yeah. We'll find the right speed together."
    fan "Okay... let's try."
    $ friendship += 8
    $ corruption_level = 65
    "Friendship +8\nCorruption level: 65"
    jump Fan_minigame

label Fanny_directive:
    you "Slow down, or you'll break."
    show Fanny down
    fan "I know... I'm trying."
    fan "It's hard to know the middle..."
    you "Just follow me. I'll guide you."
    $ friendship += 5
    $ corruption_level = 67
    "Friendship +5\nCorruption level: 67"
    jump Fan_minigame

label Fanny_harsh:
    you "You're useless, I'll do it myself."
    show Fanny WTF
    fan "I... I can't..."
    fan "I just spin..."
    $ friendship -= 10
    $ corruption_level = 85
    "Friendship -10\nCorruption level: 85"
    fan "I can't help you..."
    fan "Not like this."
    jump Fan_fail

label Fan_minigame:

    scene bg FAN_room
    show Fanny chill

    fan "Okay… let's see if you understand me."
    fan "Answer correctly, and I can trust you to help me stabilize."

    # ==================================================
    # Question 1
    # ==================================================
    menu:
        "1) What is the primary purpose of a fan in a computer?"
        "A) To help the CPU run faster":
            $ friendship -= 5
            fan "Hmm… that's not quite right."
        "B) To cool down the components and maintain optimal temperature":
            $ friendship += 5
            fan "Yes! Cooling is very important."
        "C) To increase storage capacity":
            $ friendship -= 5
            fan "No, that doesn't help me at all."

    # ==================================================
    # Question 2
    # ==================================================
    menu:
        "2) How does a computer fan typically work?"
        "A) By circulating hot air inside the case":
            $ friendship -= 5
            fan "Not exactly… we need to get rid of hot air."
        "B) By pushing cool air in and pulling warm air out":
            $ friendship += 5
            fan "Correct! That's how I keep the system balanced."
        "C) By generating electricity to power the computer":
            $ friendship -= 5
            fan "No, that's not my job at all."

    # ==================================================
    # Question 3
    # ==================================================
    menu:
        "3) What happens if a fan in a computer fails?"
        "A) The system becomes more powerful":
            $ friendship -= 5
            fan "No… overheating is dangerous!"
        "B) The computer will overheat, leading to potential damage or shutdown":
            $ friendship += 5
            fan "Exactly! That's why I need to be careful."
        "C) The computer will run silently and consume less power":
            $ friendship -= 5
            fan "Wrong. Silence doesn't fix heat."

    # ==================================================
    # Evaluate Result
    # ==================================================
    if friendship >= 15:
        show Fanny thumbs
        fan "You really understand me!"
        fan "I can trust you to help me stabilize."
        "Friendship +5\nCorruption level decreases to 60"
        $ memory_fragments_collected += 1
        "MAP FRAGMENT 2 OBTAINED"
        jump CPU_postFanWin
    else:
        show Fanny WTF
        fan "I cannot trust you yet…"
        "Friendship -5\nCorruption level increases to 80"
        "MAP FRAGMENT LOCKED"
        jump CPU_postFanFail

# =====================================================
# CPU RESPONSE AFTER FAN
# =====================================================

label CPU_postFanwin:
    scene bg computer
    show CPU thumbs
    you "I did it."
    you "The Fan stabilized."
    cpu "Confirmed."
    cpu "Corruption within the Cooling Sector has decreased."
    you "Another fragment?"
    cpu "Yes."
    cpu "System integrity improved further."
    jump ENDGAME  # Continue to next component logic

label CPU_postFanfail:
    scene bg computer
    show CPU down
    you "That didn't go well."
    cpu "Instability increases."
    cpu "You will need to attempt recovery again later."
    jump ENDGAME # Continue to next component logic

# =====================================================
# ENDGAME SEQUENCE
# =====================================================

label ENDGAME:

    scene bg computer with fade
    show CPU chill
    pause 1.0

    cpu "You have returned."
    cpu "Evaluation complete."

    if map_fragments == 2:
        # Player collected both RAM and FAN fragments
        show CPU thumbs
        cpu "You recovered all memory fragments."
        cpu "System integrity is nearly restored."
        you "So... my homework?"
        cpu "Confirmed."
        cpu "With all fragments restored, I can reconstruct your file."
        cpu "Congratulations. Your assignment is complete."
        you "I can't believe it... I actually fixed it!"
        cpu "Your adaptive strategies and measured actions resulted in maximum recovery."
        you "So I really did it..."
        cpu "Yes. Your file is intact, and the system is stable."
        scene bg light_tunnel with fade
        you "I saved my homework. Finally."
        system "ENDGAME: SUCCESS - ALL FRAGMENTS RECOVERED"
        return

    elif map_fragments == 1:
        # Player collected one fragment
        show CPU chill
        cpu "You recovered one memory fragment."
        cpu "Partial stability achieved."
        you "Can I get my homework?"
        cpu "Insufficient fragments to reconstruct the file."
        you "So... I only partially succeeded?"
        cpu "Correct. You may leave the system."
        show CPU down
        you "At least I stabilized part of it."
        cpu "System remains partially corrupted."
        system "ENDGAME: PARTIAL SUCCESS - ONE FRAGMENT RECOVERED"
        scene bg light_tunnel with fade
        return

    else:
        # Player collected no fragments
        show CPU WTF
        cpu "You recovered no memory fragments."
        cpu "System integrity failure imminent."
        you "No... what happens now?"
        cpu "Corruption has reached 100."
        cpu "All processes destabilized."
        scene bg black with fade
        you "My homework... everything..."
        system "ENDGAME: FAILURE - SYSTEM FULLY CORRUPTED"
        return






