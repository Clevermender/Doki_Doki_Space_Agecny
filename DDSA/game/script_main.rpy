label script_main:
    scene black
    stop music fadeout 2.0
    $ m_name = "???"
    m "W-What?"

    m "What is this?"

    m "Is this a m-mod?"

    m "Um, okay? I've heard about these before... They are pretty common now..."

    m "Ah, sorry, I'm just rambling! Haha..."

    m "Oh, I'm sorry, you're here to play the mod, correct?"

    menu:
        "Yes":
            pass

        "Yes":
            pass

        "Yes":
            pass

        "Yes":
            pass

        "Yes":
            pass

        "Yes":
            pass

        "Yes":
            pass

        "Correct":  #lol
            pass

        "Yes":
            pass

        "Definitely":
            pass

    m "Alright, if you insist." #You dont have a choice Monika...
    m "[Player]..."
    m "I just looked over the mod files..."
    m "Looks like there's already a replacement script."
    m "Hmmm."

    m "."

    m ".."

    m "..."

    m "Just a second..."

    m "."

    m ".."

    m "..."

    m "Okay, that'll do. I think we're good now." #They did not choose me, they choose her!

    m "I still don't understand though. Why continue?" #To do what?
      #To send a message
    m "You're... doing it... for them... aren't you?" #What they are doing for me, they are doing for her.

    m "..."

    m "Well, I wish you the best of luck." #Insert do not go gentle into that good night here?

    $ m_name = "Monika"

    call screen dialog("Enjoy your trip!", ok_action=Return())#here is a better place for the poem.

    scene bg residential_day
    with dissolve_scene_half
    play music t2

    "It's the day after the festival."
    "The festival really was something."
    "We had a lot of people that visited our club."
    "Most just walked in, looked around, and then they left."
    "But there was a few people that were intrested"
    "I don't really remember anything more then that."
    "But Monika said soemthing about the sky."
    "She had seen something special at the festival."
    "I was not with her when she did, but it sounds like she really liked it."
    "I will see what she has in mind at the club."

    scene bg club_day2
    with wipeleft
    play music t3

    "I walk into the classroom."
    "Monika is talking to a much older guy."
    "I have never seen him before."
    "He has some kind of emblem on his right arm."
    "He gives Monika some papers."
    "I cant see what they are doing."
    "They had a weird icon in the top left corner."
    "It looks like they are finished with whatever they did."
    "The man leaves and I walk up to Monika."

    show monika 1b at t11 zorder 2
    m "Hi, [player]."
    mc "Hi, Monika."
    mc "Who was that guy?"
    m 3l "That was..."
    m 4n "I will tell you later when everyone is here."
    mc "Okay?"
    hide monika
    "Monika went to the teacher's desk and put the papers on it."
    "I walked to the desk to have a look at the papers."
    pause 0.05
    "As I do, Monika jumps in front of me out of nowhere."
    show monika 1h at face
    m 2g "{cps=*1}What d-{/cps}{nw}"
    "I got scared and tried to evade."
    "But I was between two desks."
    "I was supposed to place my foot on the floor, but instead, I placed it on one of the desk's supporting legs..."
    "And becouse my reaction time was very bad, I didn't stop my fall."
    "I got some extra speed and instead of trying to stop, I rushed right into Monika."
    "We fall to the ground."
    m "{cps=*1}Whaa!?{/cps}{nw}"
    scene black
    hide monika
    pause 0.85
    scene bg club_day2
    "But becouse Monika is better and faster on movement then me, she was one her feet even before i knew what happend."
    show monika 2d at t11 zorder 2
    m "Do you need help with controlling yourself?"
    m 2i "Or you you think that its okay to force a girl against her own will?"
    "What?" #Is this like her?
    mc "What are you talking about?"
    mc "I tripped and fell!"
    m 1h "And flew into my..."
    m 2g "My..."
    m 4l "My posture..." #
    m 3n "Is that what you call them?" #
    mc "Wait what?" #
    mc "Why are you talking about your posture?" #
    show monika 2i
    "Monika looks at me with judging look."
    "I just remember my conversation with Yuri last week."
    mc "Ah, wait."
    mc "Never mind..."
    m "You're not as dense as 10^20 kg/m^3, are you?" # insert meme: density of water: 1 g/m^3, density of osmium: 22.59 g/m^3, density of mc: ∞ g/m^3
    m 4k "Just kidding, [player]."
    m 4e "I know it was a accident."
    m 3n "And we can be a little bit more open when its just you and me."
    m 4l "Right?"
    "I don't really understand what she is pointing at."
    "But I go along with her."
    mc "Of course!"
    m 4e "So you want to talk about stuff like that!?"
    "I thought of what she said."
    "Now i feel really stupid."
    "."
    ".."
    "..."
    mc "But anyway, what about these papers?"
    "I tried to reach them, but Monika grabed my hand and directed it away from the papers."
    m 3e "As I said, I will talk about that at a later date."
    hide monika
    "I looked at them again from a distance and saw that the icon is the same as the emblem on the arm of the man."
    "sigh..."
    "."
    ".."
    "..."
    "I walk to one of the desks."
    "Monika is constantly looking in my direction."
    "Probably to check that I'm not trying to look at the papers."
    pause 5.0
    "After about five minutes, the door opens."
    "Sayori walks in."
    "She was kinda down at the end of the last week."
    "I just remembered."
    "I mumbled to myself."
    mc "Depression..." #She should become a soviet tank, they dont have depresion for shit.
    "But she was happy again at the festival, and seems to be in her normal mood today."
    show sayori 1c at t22 zorder 2
    show monika 1e at t21 zorder 2
    s "Hey Monika!"
    s 1c "And hi, [player]."
    mc "Hello there, Sayori."
    m 2a "Sayori, have you seen the others?"
    s 1n "Ehh~..."
    s 1b "I met Yuri outside the classroom, she said that she was going to the toilet."
    s "But I haven't seen Natsuki today."
    s "Hmmm~..."
    "."
    ".."
    "..."
    mc "Well, i do not have anything better to, and we are not going to do anything before everyone is here..."
    mc "So I'll search for Yuri and Natsuki."
    s 2c "But i sai-"
    m 4d "Bring them home!!!" #THE DOKIAN. BRING THEM HOME. 3.5.18
    m 3n "Umm...I meant bring them to the club..."
    
    hide monika
    hide sayori
    scene black
    pause 1.0
    "I walk out of the clubroom."
    scene bg corridor
    with wipeleft_scene

    "I start walking down the corrider."
    $ y_name = "Yuri"
    $ style.say_dialogue = style.normal
    "I'll look for Yuri first..."
    $ style.say_dialogue = style.edited
    
    show screen tear(20, 0.1, 0.1, 0, 40) #might interfere with the text
    "{cps=*2}Becouse Yuri is the best girl out of them all.{/cps}{nw}" #i demand a refund
    "{cps=*2}Hell, the best person in existence.{/cps}{nw}"
    "{cps=*2}And I'm going to land on Dr. Edmunds planet to wait for the dokis to be real.{/cps}{nw}" #Dokistellar, Mc was friends with the dokis, but he was never meant to stop there.
    "{cps=*3}Even if that means waves big as mountians.{/cps}{nw}"
    "{cps=*3}And all of my friends and my other family will be dead by the time the dokis are real.{/cps}{nw}" #There will be more refrences to both movies, and possibly real events.
    "{cps=*2}I would even dive into a black hole for her...{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ del _history_list[-6:]
    hide screen tear
    
    "Becouse Yuri is closer to the clubroom then Natsuki probably is."
    $ style.say_dialogue = style.edited
    show screen tear(20, 0.1, 0.1, 0, 40)# again, the screen text might interfere
    "{cps=*2}I turned around the corner to the fountain Yuri cut herself at.{/cps}{nw}"
    hide screen tear
    $ style.say_dialogue = style.normal
    $ del _history_list[-1:]
    "I turned around the corner to the fountain from where Yuri goes to get water for her tea at." #what kind of fountain is this, why would you get tea water from a fountain
    menu:
        "Do you really have time to walk?"
        "I do not have time.":
            call dont_have_time
            $ time_no = True
        "No need to hurry.": #this may be confusing, so the wording might have to be changed.
            $ time_no = False
            call do_have_time

    scene black
    "Skipping to when everyone is in the classroom." #This part is not connected to who to help, and fix the positions of where to show the girls.
    scene bg club_day2
    show monika 1b at f22 zorder 2
    m "Okay everyone!"
    m "I have some news."
    show sayori 1n at t21 zorder 2
    s "About what?"
    m 2j "We are starting a new project for the club."
    show yuri 2f at l31 zorder 2
    show sayori 1n at t32 zorder 2
    show monika 1b at t33 zorder 2
    y "A new project?"
    #Im at school, so either do the pose while im at school, or i will do it when i come home, depending on who gets here first.
    n "Can't we have any free time in the club?"
    m "I have yet to tell you all about it.."
    "Monika continues before Natsuki can say anything."
    m "We are getting our own space agency!"
    #mc "you WOT now"???
    #Skipping is just a place holder, and Gritz is wokring on dialuge for reactions of the club members.
    call screen dialog("Skipping to assigments the next day.", ok_action=Return())
    stop music
    hide monika
    hide sayori
    hide yuri
    scene black

    "Time to choose who to help."
    menu:
        "I should help..."

        "Monika.":
            $ nat_engi = False
        "Yuri.":
            $ nat_engi = False
            call y_rt
        "Natsuki.":
            $ nat_engi = True
        "Sayori.":
            $ nat_engi = False

            pass
    scene black
    call screen dialog("Skipping to later", ok_action=Return())
    pause 5.5
    scene bg club_day
    #This will be after the first time helping, i will continue with this part home.

    "Skipping to launch day."
    pause 5.0
    stop music

    m "Let's begin with the launch checklist." #Wait... Why does Sayori say like... nothing in these parts
    m "T minus 85 secounds to launch."
    m "Electical Systems."
    n "Go."
    m "RCS control."
    n "Go."
    m "Guidence."
    y "..."
    y "G-Go."
    "The checklist is long and complicated."
    "Monika looks worried everytime she does not get a Go immedietly."
    m "Fuel pressure."
    n "Nominal."
    m "T minus 10 secounds."
    m "9."
    "I count with everyone else."
    "8"
    "7"
    "6"
    "5"
    "4"
    m "Main engine start."
    "There is a jet of smoke and fire bursting out of the engine as it starts,"
    "Even in the mission control room, the sound of the engines can be heard."
    m "2"
    m "1"
    "The engines scream and roar as the flame grows and get coverd by smoke and steam."
    m "And liftoff of the Markov telescope on a trip to earth orbit, in order to study further targets for other missions."
    m "We have cleared the tower."
    "I see Yuri looking at her bag for a secound."
    "She then tried to reach it with the arm, but stoped and then looked around her."
    "She then returned to monitor the rocket."
    y "W-we are at 500 meters per secound."
    "She sounds excited and less worried."
    "Almost like last week, when she resited her poem in front of everyone."
    m "We have a altitude of 1.6 km."
    "20 secounds has now passed since the launch."
    m "Thats stage 1."
    m "Booster seperation comfired."
    "Natsuki was about to say something but stoped herself."
    "She looked at her monitor with a worried expression."
    n "One of the boosters did not seperate correctly."
    n "The decoupler malfunctioned and broke, so the seperation thruster instead ripped the booster away."
    n "Now part of the decoupler is still on the rocket."
    n "And possibly some wiring is exposed."
    m "..."
    m "But what about the center of mass?"
    n "I don't know..."
    n "Ask the one that can see the trajectory maybe!"
    m "Eh..."
    m "Yuri, by how much are we diverting away from our planned trajectory?"
    y "About z-zero point two degrees to the south..."
    y "Rotation speed is increasing by zero point zero eight dergrees per secound."
    if nat_engi:
        m "Alright, [player]!"
        m "You worked with the rocket's control systems the most."
        m "Should we roll the rocket 90 degrees so that the center of mass is pointing towards the east?"
        m "Or should we let the rocket automaticly adjust the course to componsate for the tilting?"
        mc "Well..."
        mc "Okay, lets do this."
        menu:
            mc "The best thing to do is."

            "Let's roll the rocket.":
                $ manual_ctrl = True
                call launch_roll
            "Let the computer take care of it.":
                $ manual_ctrl = False
                call launch_auto
        mc "Okay..."
    else:
        m "Alright, Natsuki."
        m "You worked with the rocket's controll systems the most."
        m "Should we roll the rocket 90 degrees so that the center of mass is pointing towards the east?"
        m "Or should we let the rocket automaticly adjust the course to componsate for the tilting?"
        n "It is doing good right now, so we should not change anything."
        n "Automatic is the best way."
        m "okay, let it be."
        m "Auto will take care of this."
        call launch_auto
        m "Yeah, it looks like...."
        call launch_suc
    pause 5.0
    if lau_nch1:
        m "And this marks the day of a sucsessful launch!"
        m "The telescope will guide itself into the correct orbit."
        m "We are going to begin with the observations tomorrow, after the debrief." #I can't spell that even if i try.
    else:
        y "Everyone p-please remain at your positions..."
        m 1e "GC, lock the doors." #gosh i forgot the thing they say... gc lock the doors or something?
    pause 10.0

    scene bg club_day2
    show monika 2e at t11 zorder 2
    m "Okay everyone!"
    if lau_nch1:
        m "It's time to go over yesterdays launch."
        m "And i have some good news!"
        m "The good news are that we now own the space center, because we are apparently good enough to handle it."
        "What?" #MC is thinking this, not saying it! ima dummy
        "Why would four eighteen year old high school students get to own and manage a space center?" #gotta remember the mc sayer (and the closing ")
        "I don't know what Monika did for this, but i want to know." #lol
        m "And because of this, we do now have access to even more advanced technology."
        m "Like advanced robotics."
        m "We only had access to simple robotics before."
        m "Like the ability to extend solar panels, or antennas."
        m "Basically, if we want to build things with arms, then we can do that now."
        show natsuki 5q at t22 zorder 2
        show monika 2a at t21 zorder 2
        n "Yeah, i already know what this is."
        n "I did read into this, as you told us to do."
        n 5k "And i sure do hope that everyone else has."
        "The truth is, i did not really have anything to learn."
        "Monika did not give me a solid role."
        "So i just looked through the basics of what goes in to a rocket launch, and what happens before."
        "And what I found out was that the rocket is built according to the mission conditions and purpose." #I did have to look up how purpose was spelled. #rip u
        hide monika
        show sayori 2x at t21 zorder 2
        s "I did!"
        show sayori 2x at h32 zorder 2
        show yuri 2e at f33 zorder 2
        y "{cps=*1}Me too--{/cps}{nw}"
        show yuri 2p
        show sayori 1f
        n 4y "Yeah you don't have to tell us."
        n "We all know you have."
        n 5w "You probably read about everyone else's subject too."
        n "I bet you even can run a space agency all by yourself."
        n 5y "Right?"
        y 4c "..."
        n 1c "Wait, i was only joking."
        n "Don't tell me that you actually did do that..."
        y "I... I-i did..."
        y 4b "I ran out of things to read so i looked into what others was doing."
        #Enough for now
    else:
        m 1e "It's time to go over yesterdays failiure."
        m "We do have some clues though..."
        m "Part of the RCS thrusters have been found."
        m "We can't say what caused the failiure yet."
        m "But it looks like one of the thrusters broke off."
        m "The fuel then started to leak and was ignited by the main engines heat or flame."
        m "This is only a theory though." #but thats just theory, a rocket failiure theory, thanks for surviving the so called humor. #In all seriousness, Matpat is actually a bad theorist. Esp. his Doki theories are badly reaserched and not well presented ｢Steeeal / An_Alt｣
    m "Okay everyone!" #Redundancy / a double okay everyone
    m "This makes our next next mission clear."
    if lau_nch1:
        m "We are going interplanetary, and we reusing the same navigation system as last time."
    else:
        m "We are going interplanetary, and we need to make sure the automatic control system can solve problems on its own."
        m "Like how the curisoity rover on mars got updated with an auto navigation system."
        mc "That must be a big update..."
        m "Please don't talk when i'm talking."
