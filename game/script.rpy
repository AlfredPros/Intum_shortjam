define s = Character("Sumi")
define h = Character("Hana")
define k = Character("Kana")
define a = Character("Aiko")
define y = Character("You")

label start:

    hide screen main_menu

    show text "{color=#44527C}PROLOGUE: DREAM OF A GIRL NAMED KANA{/color}":
        zoom 1.75
    with fade

    pause

    hide text

# ----PROLOGUE START----

    scene black
    
    with dissolve

    "Night falls..."

    "Your eyes start to feel drowsy..."

    "It won't be long before you enter dreamland..."

    y "ZZZ ZZZ"

    show homescreen with dissolve

    show kanaclosedsmile with dissolve

    play music timeforrest

    k "Why hello th--"

    hide kanaclosedsmile

    show kanafrown

    k "You can't be serious..."

    k "Still asleep, Really?"

    k "HEY, WAKE UP!! A cute girl's talking to you here!"

    "You woke up from your peaceful sleep to see that there's a girl shouting
    at you"

    hide kanafrown

    show kanaclosedsmile

    k "There you go, let's start from the beginning."

    hide kanaclosedsmile

    show kanaopen

    k "ahem... Why hello there! My name is Kana, and this might seem a bit
    strange to you, but you've been chosen to embark on an adventure!"

    y "What the hell?? Where am I? Am I still dreaming?"

    hide kanaopen

    show kanafrown

    k "Oh relax for a bit, yes, you're still dreaming, this is a dream."

    hide kanafrown

    show kanaclosedsmile

    k "But I'm 100 percent real! and trying to communicate to you as we speak!"

    y "Alright, somehow I'm not surprised anymore... Let's just get this over
    with."

    k "Nice of you to co-operate. Now to business, the <Adventure> that I
    mentioned requires you to save 3 girls in your hometown, each with their
    own problems."

    y "Wait wait wait, why the hell would I do that? What's in it for me?"

    hide kanaclosedsmile

    show kanaopen

    k "Let's just say that those girls will open up to you, and YOU... will get
    a chance at dating them."

    k "And who knows, maybe I'll throw in a bonus for you at the end."

    hide kanaopen

    show kanaclosedsmile

    k "C'mon I know you're still single and desperate."

    y "Wow, no need to rub salt on my wound..."

    hide kanaclosedsmile

    show kanaopen

    k "Aaaaanyways, let's get started then!"

    k "The three girls that I mentioned are Aiko, Sumi, and Hana. They each have
    different problems within their hearts that you need to solve via playing a
    <RHYTHM GAME> through this <KOKORO DEVICE>!"

    "Got <KOKORO DEVICE>"

    y "Wow... what is this? A cliche dating sim minigame??"

    hide kanaopen

    show kanafrown

    k "Yeah I know it's stupid, but this is my best idea."

    y "Alright then, I'm convinced, how does this device work though?"

    hide kanafrown

    show kanaopen

    k "Oh, let me show you. I'll let you use it on me for now."

    stop music fadeout 1

    "A gameplay is about to start..."
    window hide Dissolve(0.2)
    
    python:
        toffset = 16
        fruit = "apple"
        minigame_mode = True
    show screen minigame(1) with Dissolve(1)
    
    pause
    pause
    
    return

    # --Tutorial Gameplay--
    # semua dialog di bawah ini pas lagi main ya

    k "First things first, that <BOWL> down there, that's you."

    # Highlight / tunjukin bowl ke player

    k "There are also <LANES>, three of them to be exact, you can move your
    bowl to other lanes by using arrow keys."

    k "Left = left lane, Down = middle lane, Right = right lane."

    # Kasih player kesempatan buat gerakin bowlnya pake arrow key
    # Left = left lane, Down = middle lane, Right = right lane

    k "There will be falling <HEARTS> from above, your objective is to catch
    them according to the beat of the song. Go ahead, try catching them!"

    # Kasih player kesempatan buat coba tangkep beberapa hati yang jatoh
    # Abaikan hasil (Ketangkep semua / Miss beberapa / Miss semua)

    k "Careful though, if you miss a heart, your <LIFE POINT> will decrease by
    1. Each stage gives you 5 life points, so don't miss up to 5 hearts or you'll
    fail."

    # Highlight / tunjukin life points dalam bentuk hearts ke player
    # Pasang sprite life point

    k "Alright, now give it a try yourself!"

    # Gameplay tanpa tutorial mulai
    # Abaikan hasil (Menang ampe akhir / Kalah di tengah)

    # --Balik ke dialog screen--

label after_level1:
    
    pause 1.5
    
    play music timeforrest

    hide kanaopen

    show kanaopen
    
    window show Dissolve(0.2)
    k "There you go, that wasn't so hard was it?"

    y "Not gonna lie, that's pretty cool. Alright then, thanks Kana."

    k "Awww... after all that, you still remember my name, now go get 'em
    them, tiger!!"

    k "The things I do for a chance at getting a girlfriend..."

    "And with that, your journey begins!"
    window hide Dissolve(0.2)

    stop music fadeout 1

    scene black with Dissolve(1)

# ----PROLOGUE FINISH----

    show text "{color=#44527C}PROLOGUE END{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

    show text "{color=#44527C}CHAPTER 1: A LOST AIKO{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

# ----CHAPTER: AIKO START----

    window show Dissolve(0.2)
    "The next day."

    show skyday with dissolve

    play music lettinggomain

    "You woke up with a headache because of your dream with Kana last night."

    "You shrug it off and start preparing yourself for school. Little did you
    know, you're already 5 minutes late"

    show shopsday with dissolve

    y "...So all of it is real, the <KOKORO DEVICE>... It's real! Huh, then
    that Kana girl really has some guts showing up at my dream uninvited."

    show aikofrown with dissolve

    a "Hey! Out of my way!! I'm sooo late for class today!"

    y "Wh--"

    hide aikofrown

    stop music fadeout 1

    "Without time to react, you got hit by a girl in a school uniform."

    show aikoclosedfrown

    play music shenanigans

    a "Ow ow ow...!"

    y "Ow... are you okay there?"

    hide aikoclosedfrown

    show aikofrown

    a "What the hell's your problem jerk?!"

    y "Excuse me?! You're the one who hit me!"

    hide aikofrown

    show aikoclosedfrown

    a "Well-- damn you! I need to hurry to cla-- OW!!"

    y "You have a scratch on your knee!"

    y "Let me help patch it up, luckily I have a band-aid with me."

    a "Fine! Just make it quick!"

    scene black with dissolve

    stop music fadeout 1

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    hide aikoclosedfrown

    hide shopsday
    
    python:
        toffset = 1.0
        win = False
        health = 5
        position = 1
        fruit = "blueberry"
        minigame_mode = True
    show screen minigame(2) with Dissolve(1)
    
    pause
    pause
    return

    # --Aiko (Easy) Gameplay--

label after_level2:
    
    pause 1.5

    show shopsday with dissolve

    show aikofrownblush with dissolve

    play music shenanigans
    
    window show Dissolve(0.2)
    a "Th-- Thank you..."

    y "Don't mention it, next time be more careful alright."

    hide aikofrownblush

    show aikoopen

    a "Don't mean to be rude, but I'm already late for class!"

    a "And by the look of your uniform, we're from the same school."

    y "Really now?"

    "You check your phone to see that you're both already late 15 minutes."

    y "OH CRAP!! YOU'RE RIGHT!"

    hide aikoopen

    show aikosmile

    a "Told you nerd. Now let's get going!"

    scene black with dissolve

    stop music fadeout 1

    "You and Aiko quickly rushed to school together."

    "You came in class late, yet there's no teacher and none of your friends
    actually notice you came in."

    "After what feels like an eternity, a day of classes finally came to an
    end."

    hide aikosmile

    hide shopsday

    show skynoon with dissolve

    play music lettinggomain

    y "Ahh finally, classes are over."

    y "Gonna go hit the cafeteria, I'm starving!"

    "You went to the school cafeteria to get some food, and went to the park to
    eat"
    
    stop music fadeout 1
    
    show parknoon with dissolve

    queue music shenanigans

    y "Huh weird, usually it's crowded here at this time of day...
    Wait isn't that the girl from before?"

    y "Aiko right...? If I remembered correctly from glancing at her
    schoolbag's name tag"

    "you approach Aiko while she's eating alone."

    show aikofrown with dissolve

    y "Hi there, quite a coincidence meeting you here!"

    hide aikofrown

    show aikoclosedfrown

    a "Wh-- Are you stalking me?! Pervert!"

    y "I'm not stalking you! I swear!"

    hide aikoclosedfrown

    show aikoopen

    a "Hahaha! I'm just kidding, sit here!"

    "You sat next to her and start eating as well."

    y "So... if you don't mind me asking, are you always alone here?"

    hide aikoopen

    show aikosmile

    a "No... I don't usually come to the park, I'm usually playing at the arcade
    at this time."

    y "So why didn't you?"

    hide aikosmile

    show aikofrown

    a "I don't know, I don't feel like it... Today's been very rough."

    y "How so?"

    a "When I came in to class late, the teacher Immediately fail my test that
    we're gonna have today at a later hour. Not only that, my classmates laughed
    at me all day long everytime there's no teacher present."

    y "That's just wrong..."

    hide aikofrown

    show aikoclosedfrown

    a "D-- Do you think I'm worthless??"
    
    stop music fadeout 1

    scene black with dissolve

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    hide aikoclosedfrown

    hide parknoon
    
    python:
        win = False
        health = 5
        position = 1
        minigame_mode = True
    show screen minigame(3) with Dissolve(1)
    
    pause
    pause
    return

    # --Aiko (Hard) Gameplay--

label after_level3:
    
    pause 1.5
    
    play music shenanigans
    
    show parknoon with dissolve

    show aikoclosedfrown with dissolve

    y "No you're not, you did your best, and that's all that matters."

    y "Just ignore your classmates."

    y "About the test, try talking to your teacher at the office, I'll
    acompany you if I have too."

    hide aikoclosedfrown

    show aikosmile

    a "Thank you, for helping me the second time already."

    a "Actually I have a confession."

    y "Oh?"

    a "At morning, when I hit you on the way to class, I did it on purpose, I
    happened to meet you at the same time we're late to school."

    a "I tried to get your attention, but as a result, I bruised my ankle, yet
    you quickly took care of me, that's sweet."

    y "Wait, for what purpose did you puposefully hit me?"

    a "I was testing to see if you'd care about me at all..."

    hide aikosmile

    show aikoopen

    a "And now I got my answer, not only that, you reinforced my belief by
    talking to me when you came by to me when the park is all empty."

    y "So the park is empty because of you?"

    stop music fadeout 1

    a "Yes... I made empty so that I can test you again."

    a "It seems like you're the perfect boy... My perfect boy."

    y "I appreciate the gesture, but this is getting kinda creepy..."

    scene aikoyanderesummerserabg with dissolve

    play music splatters

    a "I'm trying to propose to you here, as your future wife!"

    y "...What?! Now who's the stalker and why do you have a knife?!"

    a "Don't be like that, sweetheart, you're all mine now..."

    y "Stop it! That's enough!!"

    a "Wha...?"

    y "I'm not afraid of you, I know that you won't play around with that
    knife."

    a "Oh yeah? How so?!"

    y "You're trembling from the feet up."

    a "Ah... Is it really that obvious..."

    stop music fadeout 1

    queue music evansfull

    a "I... All I ever wanted was just want a friend... A partner..."

    y "I can relate to you, I don't have many friends, or even had a partner
    ever in my life, but that's not how you treat people."

    a "I don't understand, then what can I do."

    y "Understand their feelings, try to be on their good side."

    y "I'll be your friend, and possibly your boyfriend, ok? But you have to
    stop being manipulative and stop threatening people with knives, promise?"

    a "Ok, I promise... Thank you..."

    a "Thank you for understanding me... I'm in your care."
    window hide Dissolve(0.2)
    
    stop music fadeout 1

    scene black with Dissolve(1)

# ----CHAPTER: AIKO FINISH----

    show text "{color=#44527C}CHAPTER 1 END{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

    show text "{color=#44527C}CHAPTER 2: YOUR SWEET NEIGHBOR, SUMI{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

# ----CHAPTER: SUMI START----
    
    window show Dissolve(0.2)
    "School semester has finally ended, winter rolls in and you get to enjoy a
    month of holiday."

    hide aikoopen

    hide parknoon

    hide aikoyanderesummerserabg

    show snownoon with dissolve

    play music lettinggomain

    y "Ahh finally, last day of the semester is finished. Gonna enjoy some good
    gaming when I get home, 'cuz holiday's here baby!!"

    y "Better wear my coat and beanie, it's freezing out there!"

    "You wore your coat and beanie, and start walking home."

    "...Little did you know that the coat you're wearing is already worn out."

    hide snownoon

    show snowroadnight with dissolve

    y "The wind is pretty strong today... wonder wh--"

    "Suddenly, your coat tore on your back."

    y "HEY! WHAT GIVES?! My coat just tore in half!"

    y "Brrr... Great... now it's freezing out here."

    "Suddenly from one of the houses by the street..."

    show sumiopen with dissolve

    s "Hey! You seem to be struggling with the cold! Come inside!"

    y "Wh-- No, it's okay!"

    s "I insist! Come on in! Your house is just a few blocks away right?"

    y "Alright alright!"

    scene black with dissolve

    "You accepted the stranger's offer and went in her home."

    stop music fadeout 1

    hide sumiopen

    hide snowroadnight

    show roomnight with dissolve

    show sumiopen with dissolve

    queue music guitaronthewater

    s "Your coat's torn! Here, let me take it off!"

    y "No it's okay."

    s "I insist, I can help stitch it for you."

    y "If you say so..."

    "The stranger helped take off your coat."

    hide sumiopen

    show sumismile

    s "I'm Sumi by the way, nice to meet you!"

    y "Nice to meet you too, Sumi."

    s "I'm going to put this coat on my sewi--"

    hide sumismile

    show sumiclosedopen

    s "WAA!!"

    "Sumi suddenly slipped from all the melted snow from the coat."

    scene black with dissolve

    stop music fadeout 1

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    hide sumiclosedopen
    
    python:
        win = False
        health = 5
        position = 1
        fruit = "grape"
        minigame_mode = True
    show screen minigame(4) with Dissolve(1)
    
    pause
    pause
    return

    # --Sumi (Easy) Gameplay--

label after_level4:
    
    pause 1.5
    
    window show Dissolve(0.2)
    "You react quickly to catch her."

    show roomnight

    show sumiclosedopen

    play music guitaronthewater

    y "Woah! careful there!"

    hide sumiclosedopen

    show sumismile

    s "Ehehe... Thanks."

    s "Sorry, I'm just gonna leave your coat by the couch."

    y "Alright, so, I have a question, why did you call out to me to come by
    your house? Even though I'm a stranger to you."

    hide sumismile

    show sumiopen

    s "Well, I saw you pass by my house nearly every weekday, I'm sure that you
    live around these neighborhood."

    y "Yeah, I my house is just a couple blocks away, but that doesn't mean that
    I'm always a good guy, I could have bad intentions."

    s "...But you're still here, sitting and chatting with me, right?"

    hide sumiopen

    show sumiclosedfrown

    s "Besides, if I'm gonna be honest with you, you look... Sad and lonely
    everytime I see you pass by..."

    y "Yeah, you're right... Life hasn't really been good these days."

    y "All my friends already have a partner, some have a sidejob, some are
    excelling at their class, and making names for themselves."

    y "Yet here I am, still single, still holed up in my room playing dating
    sims."

    hide sumiclosedfrown

    show sumifrown

    s "I understand... You're just like me."

    s "I don't have any self-esteem, always doubting myself if I'm ever worth
    anything as a friend or even a daughter to anybody."

    s "I'm failing at my classes because I need to take care of sick grandma."

    s "I'm so lost, I don't know what to do in life..."

    y "I get ya."

    s "I know we've just met, but, do you feel the same way as everybody did?
    do you think I'm also worthless...?"

    hide sumifrown

    show sumiclosedfrownblush

    s "S-- Sorry for asking such a question, forget it."

    scene black with dissolve

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    stop music fadeout 1

    hide sumiclosedfrownblush

    hide roomnight
    
    python:
        win = False
        health = 5
        position = 1
        minigame_mode = True
    show screen minigame(5) with Dissolve(1)
    
    pause
    pause
    return

    # --Sumi (Hard) Gameplay--
    
label after_level5:
    
    pause 1.5

    show roomnight with dissolve

    show sumiclosedfrown with dissolve

    play music evansfull
    
    window show Dissolve(0.2)
    y "No way, of course not! The fact that you helped me from the cold just
    out of your kindness, not knowing what danger I might pose..."

    y "You're a very kind and caring person, Sumi. Not everyone in this world
    has that kind of trait."

    y "Whatever stuff is happening in your life, know that there are a lot of
    people that care and are rooting for you. Just forget the ones that don't."

    hide sumiclosedfrown

    show sumifrownblush

    s "Y-- You really think so? Thank you! It really means a lot to me..."

    y "And as a bonus, I wanna know more about you too, so if there's anything
    that you need help with... Just call, here's my phone number."

    "You gave Sumi your phone number."

    y "My house is also a few blocks away as I said, don't hesitate to come by,
    okay!"

    hide sumifrownblush

    show sumismileblush

    s "Okay, I will... Thank you so much!"

    y "Huh, would you look at that, the snow storm's already died down. Guess I
    can leave my coat up to you then?"

    s "Of course! I'll sew it up in a jiffy! Once it's ready, I'll come deliver
    it to your house, and maybe we can chat some more there!"

    y "Sure, I'll look forward to it."

    stop music fadeout 1

    scene black with dissolve

    "Some time have passed, you decided to take Sumi to the park again."

    "Coincidentally, the park is decorated with beautiful winter-themed
    decorations."

    scene sumicgwintersmileblush with dissolve

    play music guitaronthewater

    s "I've noticed that you're still using the coat that I stitched up for
    you."

    y "Yeah, you're sewing is a work of art!"

    s "Hehe! You're too sweet!"

    s "Thank you... these past few weeks have been so fun."

    s "You've been coming to my house non-stop these past few days. I wish I
    can repay the favor."

    y "Seeing your happy face is more than enough."

    s "Hehe... I hope we can stay like this forever..."

    y "...Maybe more than what we are now in the near future."

    s "I hope so! with all my heart!"
    window hide Dissolve(0.2)

    stop music fadeout 1

    scene black with Dissolve(1)

# ----CHAPTER: SUMI END----

    show text "{color=#44527C}CHAPTER 2 END{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

    show text "{color=#44527C}CHAPTER 3: THE TRAGEDY BEHIND HANA{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

# ----CHAPTER: HANA START----

    window show Dissolve(0.2)
    "At the winter holiday, you spent most of your time going to Sumi's house to
    help with her studies and chat with her about hobbies."

    "You free up a few days to go and eat together with Aiko, trying out
    different eating places around town."

    "But eventually, the holiday came to an end, a new semester is starting."

    hide sumismileblush

    hide roomnight

    hide sumicgwintersmileblush

    show skynoon with dissolve

    play music lettinggomain

    y "Oh boy, It's only been the first month, and I feel like my eyebags
    are starting to pull my eyes out."

    y "I need to take a break, might as well hit the new cafe that just opened."

    "You decided to try out the new cafe that just opened near town."

    stop music fadeout 1

    queue music relax

    show cafeexteriornoon

    "You arrived at the cafe, suprised by it's exterior look."

    y "Woah... Is this the right place? It looks really nice!"

    y "Now I understand why people were so hyped talking about this place at
    school."

    "You entered the cafe, and are greeted by a few waitresses wearing maid
    maid outfits."

    show cafeinteriornoon with dissolve

    show hanasmile with dissolve

    h "Welcome to our maid cafe, master! table for one?"

    y "Yes ma'am."

    h "Alright, please be seated! I'll fetch the menu book!"

    hide hanasmile

    "You watch the girl as she walks elegantly to fetch the menu book."

    show hanasmile

    h "Here's the menu book master, what would you like to order?"

    y "I'll have a look first, thank y-- Wait... Is that you, Hana? I didn't
    recognize you in that outfit!"

    hide hanasmile

    show hanaopenblush

    h "Ehehh... I don't know who you're talking about master..."

    y "I uhh... Okay then, Hana, why are you here as a maid?"

    "Suddenly, Hana crouched and whispered to you."

    hide hanaopenblush

    show hanaclosedfrownblush

    h "Please don't ruin this for me, I know I look ridiculous, but this job is
    all I have."

    h "If the others in class know that I work here as a maid, I'd be a laughing
    stock..."

    hide hanaclosedfrownblush

    show hanafrown

    h "Please, don't tell anyone, just play along..."

    scene black with dissolve

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    hide hanafrown

    hide cafeinteriornoon

    stop music fadeout 1
    
    python:
        win = False
        health = 5
        position = 1
        fruit = "banana"
        minigame_mode = True
    show screen minigame(6) with Dissolve(1)
    
    pause
    pause
    return

    # --Hana (Easy) Gameplay--
    
label after_level6:
    
    pause 1.5

    show cafeinteriornoon with dissolve

    show hanafrown with dissolve

    play music relax
    
    window show Dissolve(0.2)
    y "Alright, you have my word, now can I have a moment to take a look at the
    menu?"

    "Hana stands right up again and puts a smile on her face."

    hide hanafrown

    show hanasmile

    h "Sure thing, master!"

    "You look through the menu and decided to have a latte and a sugar donut."

    y "Can I have a latte and a sugar donut? Extra strong."

    h "Certainly master, I'll be back with your food in a couple of minutes!"

    hide hanasmile

    "Hana walks away elegantly again."

    "After a few minutes, Hana came back with your order."

    show hanasmile

    h "Sorry for the wait, master! I've prepared your extra strong latte, and
    your sugar donut!"

    y "Thank you! these look really nice!"

    hide hanasmile

    show hanaclosedsmile

    h "I'm glad you like it, enjoy!"

    "You quickly whispered to Hana."

    y "After your shift is done, meet me at the park."

    y "Don't worry, I'm not going to do anything weird, I just wanna talk."

    hide hanaclosedsmile

    show hanaclosedopenblush

    h "Th-- that's a weird request, but okay"

    h "If you so much as do something perverted to me, I swear..."

    y "I promise it'll be worth your time."

    stop music fadeout 1

    scene black with dissolve

    "You enjoyed your meal, paid the menu, and went to the park to wait for
    Hana."

    hide hanaclosedopenblush

    hide cafeinteriornoon

    show parknight with dissolve

    play music lettinggomain

    y "Damn, It's been 2 hours... Should've asked when her shift ends."

    show hanafrown with dissolve

    h "H-- Hi, sorry I kept you waiting."

    y "It's alright... Wait, you're still wearing that outfit? It's dangerous
    out at this time with that."

    h "Yeah, I forgot to bring a change, it's either this or my school outfit.
    I'm more unnoticable by my friends in this outfit anyways."

    y "Alright... Anyways, how's life, Hana?"

    hide hanafrown

    show hanaopen

    h "It's fine, life's good."

    y "I've noticed that you haven't been yourself lately in class, and now
    you're working as a maid in a cafe... What's wrong."

    h "No! Nothing's wrong! I'm fine, really!"

    y "It doesn't seem that way to me..."

    hide hanaopen

    show hanaclosedopen

    h "Why do you care?! Stop butting into someone's problems!"

    y "Because I wanna help! You helped me before when I was in a rough spot."

    y "And now... I just couldn't bear to see you hurt like this, I wanna help
    so bad, but I haven't got the opportunity and courage to ask."

    y "So please, if you have any problem worth sharing, talk to me, I won't
    judge, nor will I tell anyone about it. You have my word."

    hide hanaclosedopen

    show hanaopen

    h "I-- Alright... but you better promise!"

    y "Like I said, you have my word."

    hide hanaopen

    show hanafrown

    play music death

    h "It all began at the start of winter holiday, my father wasn't feeling
    too good, he gets tired more easily, his appetite is messed up, and his
    face looked like as if he lost his soul."

    h "My mom and I were worried, we tried asking him, but he wouldn't budge
    saying that everything is okay."

    h "Not long after, he suddenly collapsed in the middle of the living room."

    y "Oh no..."

    hide hanafrown

    show hanaclosedfrown

    h "We called the ambulance, we rushed to the hospital, sadly my dad...
    passed away in the ambulance, while holding both me and my mom's hand."

    h "His final words were that he's sorry that he wasn't brave enough to tell
    us earlier and that he's glad to have a wondeful family."

    h "At the hospital, We learned that he had a stadium 5 cancer, almost
    untreatable, that's why he decided to keep it a secret..."

    h "And that's why I started working, I want to make things easier for mom.
    I have to take responsibility from now on."

    scene black with dissolve

    "A gameplay is about to start..."
    window hide Dissolve(0.2)

    hide parknight

    hide hanaclosedfrown

    stop music fadeout 1
    
    python:
        win = False
        health = 5
        position = 1
        minigame_mode = True
    show screen minigame(7) with Dissolve(1)
    
    pause
    pause
    return

    # --Hana (Hard) Gameplay--

label after_level7:
    
    pause 1.5

    show parknight with dissolve

    show hanaclosedfrown with dissolve

    play music death

    window show Dissolve(0.2)
    y "I-- I'm very sorry Hana, it's very sad to see your dad go..."

    y "My condolences to you and your mom."

    hide hanaclosedfrown

    show hanafrown

    h "Thank you..."

    y "I'm here for you Hana, whenever you need help or just need someone to
    talk to, I'm here..."

    y "You don't have to bear all that responsibility alone..."

    "Hana starts crying, luckily you chose a spot where people don't usually
    walk through."

    hide hanafrown

    show hanaclosedsmileblush

    h "Thank you... Thank you so much!!"

    "Hana hugs you tightly while her tears run down your shoulder."

    y "You've helped me in the past, now it's my turn. Share your pain with
    me, it's alright."

    stop music fadeout 1

    scene black with dissolve

    "After that, you regularly talk to her at class whenever you had a chance."

    "You comfort her whenever she feels sad and lonely."

    "And you visit the cafe more often than you think, ordering the same latte
    but with a different food."

    play music relax

    scene hanamaidcgsmile with dissolve

    h "Welcome back, master! Wow, you've become quite a regular in here!"

    y "Why thank you! never a dull sight with you around to brighten up the
    place!"

    h "Aww, thank you master! So now, lemme guess... The usual with a side of
    today's special dish?"

    y "You bet! studies have been killing my energy!"

    h "Right away master!"
    window hide Dissolve(0.2)

    hide hanaclosedsmileblush

    hide parknight

    stop music fadeout 1

    scene black with Dissolve(1)

# ----CHAPTER: HANA END----

    show text "{color=#44527C}CHAPTER 3 END{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

    show text "{color=#44527C}EPILOGUE: FAREWELL, KIND SPIRIT KANA{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

# ----EPILOGUE START----

    window show Dissolve(0.2)
    "..."

    "After taking care of Aiko, Sumi, and Hana for what feels like months,
    one night, you had a dream with Kana again."

    show homescreen with dissolve

    show kanaclosedsmile with dissolve

    play music timeforrest

    k "Well well well... Look who dozed off in front of a cute girl again..."

    y "ZZZ ZZZ"

    hide kanaclosedsmile

    show kanaclosedopen

    k "Well... Can't really blame him after all that work."

    k "He deserves some rest. Maybe I'll check in with him another night."

    scene black with dissolve

    "Just when Kana was about to disappear, you suddenly woke up."

    y "Did... did I hear that correctly?"

    y "Wow... you're actually proud of me, aren't ya? Hehe..."

    show homescreen with dissolve

    show kanafrownblush with dissolve

    k "Wha...? Oh haha very funny. You know, I still wonder how you managed to
    pull those three off even when you're still THIS rude..."

    y "Thought you'd be more understanding. Alright, I'll go back to sleep
    then."

    hide kanafrownblush

    show kanaclosedfrown

    k "NO WAIT! I was just kidding!"

    hide kanaclosedfrown

    show kanafrown

    k "I will not be visiting your dreams again for a while after I deliver my
    message."

    y "Aww, do I need to play a <RHYTHM GAME> with you too?"

    k  "Ugh... Alright enough with the jokes."

    hide kanafrown

    show kanasmile

    play music guitaronthewater

    k "I came here to congratulate you, for saving those girls from a life that
    they will regret living."

    y "I have to thank you too, it feels like I'm far more happier than before
    I met you."

    y "But I have to ask, why them out of all the girls around me? How could
    you tell that they need saving?"

    hide kanasmile

    show kanaclosedfrown

    k "Because I was them, I lived a life full of regrets and misery. The only
    difference being that I don't have anyone to save me."

    k "I commited suicide because I can't live with myself, and I eventually
    regretted that too."

    hide kanaclosedfrown

    show kanafrown

    k "But right when I was about to pass on, a spirit called out to me, said
    that I still have a purpose to fulfill, to seek other's like me and save
    them."

    y "And instead I was the one doing all the work...?"

    hide kanafrown

    show kanaclosedsmile

    k "Not really, I helped from behind the scenes too you know! The park, the
    snow storm, the cafe, to steer you into the right direction."

    k "The reason you played the part the most is that... because you are also
    one of the person that I'm trying to save."

    y "...Heh, yeah, gotta agree I was miserable before I met you."

    k "I played it smart with my head, not with my muscles. As a result, I
    don't really have to waste energy... Right?"

    "Kana said as she smiles with a bit of guilt."

    y "Alright alright, smartass. You're lucky all of this had passed."

    hide kanaclosedsmile

    show kanaopen

    h "Hey! I literally helped you get in contact with 3 wifey materials!"

    y "Heh... Alright, so... I guess this is goodbye then?"

    hide kanaopen

    show kanasmile

    k "I have other people to save, but this doesn't mean goodbye."

    k "You do know that I'm letting you keep the <KOKORO DEVICE> right? So that
    I will always remember to visit you one day."

    k "Who knows? Maybe I'll visit again when you're already married to one of
    those lovely girls?"

    y "Hehehe... we'll see"

    y "Like the idea of having one of them as my wife though."

    hide kanasmile

    show kanaopen

    k "Haha! Welp, I gotta go now, people out there need me. Good luck with your
    future endeavors!!"

    y "And to you too, Kana! Thank you for everything! I'm gonna miss you!!"

    scene black with dissolve

    stop music fadeout 1

    "You then wake up, feeling refreshed and invigorated, until you realized..."

    hide homescreen

    hide kanaopen

    show skyday with dissolve

    play music lettinggomain

    y "Shoot! I'm late for class again! I'm never going to hear the end of
    those girls when they know of this!"

    "And thus, your story has come to an end."

    "...Or has it?"
    window hide Dissolve(0.2)

    stop music fadeout 1

    scene black with Dissolve(1)

    show text "{color=#44527C}EPILOGUE END{/color}" with dissolve:
        zoom 1.75

    pause

    hide text with dissolve

    show text "{color=#44527C}THANK YOU FOR PLAYING!{/color}" with dissolve:
        zoom 2.0

    pause

    hide text with dissolve
    
    pause 0.5

# ----EPILOGUE END----

    # This ends the game.

    return
