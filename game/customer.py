import random
from drinks import Drinks


class Customer:
    def __init__(self):
        self.loc = None
        self.sprite = None
        self.name = None
        self.fdrinks = []
        self.line = None
        self.prevference = None
        self.state = 1
        self.satisfaction = None

    def __repr__(self):
        return f"Customer Name: {self.name}, Drinks: {self.fdrinks}"
    
    def get_drink(self):
        return self.fdrinks

    def get_order(self):
        if len(self.fdrinks) == 1:
            drink = self.fdrinks[0]
            self.line = random.choice([
                f"Hey there. I’ll have a {drink}, please.",
                f"I’ll have a {drink}, please.",
                f"I’ll have a {drink}.",
                f"Hi, I’ll have a glass of {drink}, please.",
                f"Could you make me a {drink}? Thanks!",
                f"Just a {drink} for me, please.",
                f"Hi! I’d like a {drink}, if that’s alright.",
                f"Can I get a {drink}? Thanks in advance!"
            ]).replace("_", " ")
        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Just got off the grid. I need something {self.prevference}.",
                f"Surprise me with something {self.prevference}, please.",
                f"I’m in the mood for something {self.prevference}. What do you recommend?",
                f"Anything {self.prevference} will do. I trust your choice!"
            ])
        self.line = self.name + " : " + self.line.replace("_", " ")

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"Wow, this is exactly what I wanted!",
                f"This is perfect!",
                f"This is exactly what I wanted!",
                f"Wow, this is amazing!",
                f"Thanks, this is just what I needed!",
                f"Perfect! You nailed it!",
                f"Ah, this is great. Thanks a lot!",
                f"Spot on! This is fantastic!"
            ])
            self.satisfaction = 1
            self.line = self.name + " : " + self.line
            return True
        else:
            self.line = random.choice([
                f"This is not what I ordered.",
                f"This is not what I wanted.",
                f"This is not what I expected.",
                f"Hmm, this isn’t quite right.",
                f"Sorry, but this isn’t what I asked for.",
                f"Uh, I think there’s been a mix-up. This isn’t my drink.",
                f"Not quite what I had in mind. Can we try again?"
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

    @classmethod
    def get_customer(cls):
        random_choice = random.randint(0, 100)
        if random_choice < 50:
            return random.choice([male_npc,female_npc])

        random_choice = random.randint(0, 100)
        if random_choice < 10:
            return pixelmiku
        if random_choice < 20:
            return sans
        if random_choice < 30:
            return mark
        if random_choice < 40:
            return cyberman
        if random_choice < 50:
            return dalek
        if random_choice < 60:
            return thedoctor
        if random_choice < 70:
            return bigboss
        if random_choice < 80:
            return kiryu
        if random_choice < 90:
            return masterchief
        if random_choice < 100:
            return steve


class male_npc(Customer):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["John", "Mike", "Tom", "Jack",
                                   "Alex", "Chris", "James", "Robert",
                                   "David", "William", "Joseph", "Daniel",
                                   "Matthew", "Andrew", "Ryan", "Brandon",
                                   "Kevin", "Brian", "Jason", "Eric"])
        self.sprite = self.get_sprite()
        self.randrink()
        self.get_order()

    def randrink(self):
        chance = random.randint(0, 100)
        if chance < 50:
            self.prevference = "Manly"

        elif chance < 70:
            self.prevference = "Classic"

        elif chance < 90:
            self.prevference = "Promo"

        elif chance < 100:
            self.prevference = "Girly"

        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("male1.png", (210.6,132.6)),
                                     ("male2.png", (161.8,47.2)),
                                     ("male3.png", (186.5,46.8))])
        return self.sprite

class female_npc(Customer):
    def __init__(self):
        super().__init__()
        self.name = random.choice([
            "Ant", "Lele", "Lucy", "Raven", 
            "Mia", "Luna", "Sophia", "Emma", 
            "Olivia", "Ava", "Isabella", "Amelia", 
            "Charlotte", "Harper", "Evelyn", "Abigail", 
            "Ella", "Scarlett", "Grace", "Chloe", 
            "Zoe", "Lily", "Hannah", "Aria", 
            "Aurora", "Penelope", "Layla", "Victoria", 
            "Nora", "Ellie"
        ])
        self.sprite = self.get_sprite()
        self.randrink()
        self.get_order()

    def randrink(self):
        chance = random.randint(0, 100)
        if chance < 50:
            self.prevference = "Girly"

        elif chance < 70:
            self.prevference = "Promo"

        elif chance < 90:
            self.prevference = "Classy"

        elif chance < 100:
            self.prevference = "Manly"

        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("female1.png", (204.2,102.6)),
                                     ("female2.png", (220.6,156.3)),
                                     ("female3.png", (212.4,139.6))])
        return self.sprite

class pixelmiku(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Pixelated Miku"
        self.fdrinks = ["Blue_Fairy","Mercuryblast", "Zen_Star"]
        self.prevference = "Promo"
        self.sprite = ("PixelMiku.png",(201.3, 154.5))
        self.randrink()
        self.get_order()
    
    def randrink(self):
        self.fdrinks = random.choice([[random.choice(self.fdrinks)],Drinks().get_drink_list_w_con(self.prevference)])
    
    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([
                f"Hi hi~! Could I get a {self.fdrinks[0]}? Oh! And a cute straw, if you have one!",
                f"Can I please get a {self.fdrinks[0]}?",
                f"Just {self.fdrinks[0]} again. yeah, still not weird.",
                f"Heeey~ could I get a {self.fdrinks[0]}? The bluer, the better! Like... my hair!",
                f"Oooh~ a {self.fdrinks[0]} sounds perfect right now! Pretty please?",
                f"Konnichiwa~! Could I have a {self.fdrinks[0]}? Make it extra sparkly, okay?",
                f"Hey hey~! I’d love a {self.fdrinks[0]}! Let’s make it as sweet as my songs!",
                f"Yoohoo~! Can I get a {self.fdrinks[0]}? Something magical, just like me!",
                f"Ahhh~ a {self.fdrinks[0]} would be perfect! Let’s make it shine like a concert stage!",
                f"Hey there~! Could I get a {self.fdrinks[0]}? Make it as vibrant as my melodies!"
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True

        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Can I please get something {self.prevference}?",
                f"Hmmm~ I’m in the mood for something {self.prevference}! Surprise me!",
                f"Could you mix up something {self.prevference}? I trust your taste!",
                f"Let’s go with something {self.prevference} today! Make it fun and colorful!",
                f"How about something {self.prevference}? Let’s make it as cheerful as my fans!",
                f"Could you whip up something {self.prevference}? Let’s make it sparkle like a star!"
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"Hatsune Miku loves this drink!",
                f"Hatsune Miku wants to invite you to the concert!",
                f"This is better than Teto's.",
                f"Yay~! Thank you so much! It looks super sparkly — you're amazing!",
                f"Sugoi~! That looks like a dessert in a dream! Arigatou!",
                f"Kyaaa~! It’s perfect! This could be a music video prop! Thank you, thank you~!",
                f"Ooooh~ it’s so cute!! This deserves its own photo shoot! Thank you so much!",
                f"Wow~! This drink is as sweet as my favorite melody! Thank you!",
                f"Eeee~! This is so good, I could sing about it! You’re the best!",
                f"Ahhh~ this is like a dream come true! Thank you for making it so special!"
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([
                f"Hatsune Miku does not want this drink.",
                f"Hatsune Miku hates this drink.",
                f"What is this drink? Hatsune Miku did not order this drink.",
                f"Ugh~ this isn’t what I wanted... Did I say something wrong?",
                f"Eh? This doesn’t look right... Can we try again, please?",
                f"Oops~! This isn’t what I ordered. Let’s fix it together, okay?"
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False
        

class sans(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Sans Undertale"
        self.fdrinks = []
        self.prevference = "Strong"
        self.sprite = ("Sans.png",(202.1,208.2))
        self.randrink()
        self.get_order()

    
    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])
    
    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([
                f"Yo. gimme a hot dog... wait, wrong place. eh, just a {self.fdrinks[0]} then.",
                f"Evenin’. how ‘bout a {self.fdrinks[0]}? make it lazy, like me.",
                f"Just {self.fdrinks[0]} again. yeah, still not weird.",
                f"Hey, got any ketchup? No? Fine, I’ll settle for a {self.fdrinks[0]}.",
                f"Sup. I’ll take a {self.fdrinks[0]}. Make it snazzy, or don’t. I’m not picky."
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True

        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Hey, can I get a {self.prevference} drink?",
                f"Got anything {self.prevference}? Surprise me, I’m feeling adventurous.",
                f"How ‘bout a mix of {self.prevference} drinks? Keep it chill, like me."
            ])
            self.line = self.name + " : " + self.line
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"nice work. you’ve got un-grill-ievable taste. keep ‘em comin’.",
                f"you’re a real mixer-upper. thanks, pal.",
                f"thanks, kid. you squeezed in some quality tonight.",
                f"cheers. that hit the skel-e-tone just right.",
                f"this is a real treat. you’re a true artist, kid.",
                f"not bad. you really bean around the block, huh?",
                f"heh, you nailed it. this drink’s got some backbone.",
                f"wow, this is so good, it’s practically humerus."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([
                f"uh... did you forget the soul? 'cause this tastes like lemon water with trust issues.",
                f"hmm... this thing kinda flat. no offense, but it's got no pop.",
                f"this one’s chunky. either the bottle’s cursed...or you are.",
                f"yikes, this drink’s so bad, even papyrus wouldn’t serve it.",
                f"uh, this tastes like it fell into the core. not a compliment."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False
        

class mark(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Mark"
        self.prevference = "Promo"
        self.sprite = ("Mark.png",(340.6,137.4))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([f"Hello again. Can I get some {self.fdrinks[0]}.",
                                       f"Evening. I’ll have the usual — {self.fdrinks[0]}, please. Rough day today.",
                                       f"Hey, good to see you again. Mind making me a {self.fdrinks[0]}? Just need to switch off for a bit."])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True
        elif len(self.fdrinks) > 1:
            self.line = random.choice([f"Hey again. Just the usual {self.prevference} drinks, please.",])
            self.line = self.name + " : " + self.line
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"Appreciate it as always. You’ve got a real knack for this.",
                                       f"Ahh… that hits the spot. Thanks a ton — you’ve got great taste.",
                                       f"Man, you always get it just right. Appreciate it, really."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([f"Hmm, not quite what I expected. Maybe a different bottle next time? No worries though.",
                                       f"Sorry, I think you grabbed the wrong bottle. I’ll pass on this one.",])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False
        

class cyberman(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Cyberman"
        self.prevference = "Promo"
        self.sprite = ("Cyberman.png",(-113.4, 98.8))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = Drinks().get_drink_list_w_con("Promo")

    def get_order(self):
        self.line = random.choice([f"HYDRATION REQUEST: INITIATE DISPENSATION OF {self.prevference} DRINKS. FAILURE TO COMPLY WILL RESULT IN UPGRADE.",
                                   f"COMMAND: PROVIDE LIQUID REFRESHMENT. SPECIFICATION: {self.prevference}. NON-COMPLIANCE IS INEFFICIENT.",
                                   f"REQUEST: BEVERAGE UNIT. TYPE: {self.prevference}. YOU WILL BE UPGRADED FOR YOUR SERVICE."])
        self.line = self.name + " : " + self.line

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"ACKNOWLEDGEMENT: BEVERAGE ACCEPTABLE. YOU WILL BE SPARED FROM IMMEDIATE UPGRADE.",
                                       f"CONFIRMATION: DRINK MEETS CYBER STANDARDS. GRATITUDE IS IRRELEVANT, BUT NOTED.",
                                       f"COMPLIANCE DETECTED: DRINK IS SUFFICIENT. YOU MAY CONTINUE TO EXIST."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([f"ERROR: DRINK DOES NOT MEET CYBER REQUIREMENTS. YOU WILL BE UPGRADED TO IMPROVE EFFICIENCY.",
                                       f"WARNING: INFERIOR BEVERAGE DETECTED. YOU ARE INEFFICIENT. PREPARE FOR UPGRADE.",
                                       f"ALERT: DRINK QUALITY SUBSTANDARD. YOU WILL BE RECONFIGURED FOR OPTIMAL PERFORMANCE."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class dalek(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Dalek"
        self.prevference = "Strong"
        self.get_sprite()
        self.randrink()
        self.get_order()

    def get_sprite(self):
        self.sprite = random.choice([("Dalek1.png", (136.9, 100)),
                                     ("Dalek2.png", (131, 155.7))])
        return self.sprite

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        self.line = random.choice([f"I REQUIRE A BEVERAGE! BRING ME... {self.fdrinks}! OBEY! OBEY!!",
                                   f"DELIVER TO ME A {self.fdrinks}! {self.prevference}! OBEY OR BE DESTROYED!",
                                   f"BRING ME A {self.fdrinks}! IT MUST BE {self.prevference}!"])
        self.line = self.name + " : " + self.line.replace("_", " ")

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"YOU HAVE SERVED THE DALEK EMPIRE! YOUR ACTION WILL BE... REMEMBERED! FOR NOW... YOU MAY CONTINUE TO EXIST",
                                       f"COMPLIANCE NOTED. YOU HAVE PERFORMED A FUNCTION. THIS IS... ACCEPTABLE.",
                                       f"YOU HAVE FULFILLED YOUR PURPOSE! THIS DRINK IS... ADEQUATE. PRAISE IS UNNECESSARY."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([f"UNACCEPTABLE! THE DRINK IS IMPURE! CONTAMINATION DETECTED! YOU WILL BE... REPORTED! POSSIBLY EXTERMINATED!",
                                       f"YOU HAVE FAILED TO ADD CELERY! UNFORGIVABLE! PREPARE FOR... CUSTOMER COMPLAINT ESCALATION!",
                                       f"THE GLASS IS SMUDGED! FILTHY! UNHYGIENIC! YOUR SERVICE IS INFERIOR! INFERIOR! INFERIOR!"])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class thedoctor(Customer):
    def __init__(self):
        super().__init__()
        self.name = "The Doctor"
        self.prevference = "Classy"
        self.sprite = ("TheDoctor.png", (293.1, 97.3))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = Drinks().get_drink_list_w_con(self.prevference)

    def get_order(self):
        self.line = random.choice([f"Right then! Let’s have something {self.prevference}. Make it snappy, I’ve got a universe to save!",
                                    f"Oooh, I’ll take something {self.prevference}. And no pears, alright? Never liked pears.",
                                    f"Surprise me with something {self.prevference}. Just like the TARDIS — full of surprises!"])
        self.line = self.name + " : " + self.line

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"Ah, brilliant! This is exactly what I needed. You’ve got a knack for this, haven’t you?",
                                       f"Fantastic! That’s a proper drink. You, my friend, are a genius. Cheers!",
                                       f"Spot on! This is going straight into my top drinks across all of time and space. Well done!"])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([f"Well, that’s... different. Not quite what I was expecting. Care to give it another go?",
                                       f"Blimey, that’s a bit off! Feels like I’ve just licked a TARDIS console. Let’s try again, shall we?",
                                       f"Hmm... interesting choice! Not bad, but not quite right either. Let’s see if we can improve on that."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class masterchief(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Master Chief"
        self.prevference = "Strong"
        self.sprite = ("chief.png", (199.9, 131.6))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([f"Spartan 117 reporting in. I’ll take a {self.fdrinks[0]}.",
                                        f"Evening. I’ll have the usual — {self.fdrinks[0]}, please. Long mission today.",
                                        f"Hey, bartender. Mind making me a {self.fdrinks[0]}? Need to recharge for the next op.",
                                        f"Chief here. A {self.fdrinks[0]} will do. Make it strong.",
                                        f"Got a moment to breathe. I’ll take a {self.fdrinks[0]}. Thanks."])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True
        elif len(self.fdrinks) > 1:
            self.line = random.choice([f"Spartan 117 here. Just the usual {self.prevference} drinks, please.",
                                        f"Hey again. I’ll take a mix of {self.prevference} drinks. Need to stay sharp.",
                                        f"Chief here. Load me up with some {self.prevference} drinks. Mission’s not over yet."])
            self.line = self.name + " : " + self.line
            return False
    
    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"Good work. That’s exactly what I needed. Thanks.",
                                       f"Perfect. You’ve got a steady hand. Appreciate it.",
                                       f"That’s spot on. You’re reliable, just like a Spartan teammate. Thanks."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([f"Not quite what I was expecting. Let’s try that again.",
                                       f"Hmm... this isn’t what I ordered. Maybe double-check next time?",
                                       f"Close, but not the right mix. Let’s get it right next time."])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class bigboss(Customer):
    def __init__(self):
        super().__init__()
        self.name = "BigBoss"
        self.prevference = "Strong"
        self.sprite = ("BOSS.png", (166.6, 46))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([
                f"Call me Snake. I’ll take a {self.fdrinks[0]}.",
                f"Mission’s not over yet. I need a {self.fdrinks[0]}.",
                f"Got any {self.fdrinks[0]}? Make it strong — I’ve been through a lot.",
                f"Hey. A {self.fdrinks[0]} will do. Keep it simple.",
                f"Snake here. I’ll take a {self.fdrinks[0]}. Thanks."
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True
        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Snake here. Just the usual {self.prevference} drinks, please.",
                f"Load me up with some {self.prevference} drinks. I’ve got a mission to complete.",
                f"Let’s go with a mix of {self.prevference} drinks. Keep it sharp."
            ])
            self.line = self.name + " : " + self.line
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"Good. This is exactly what I needed. Thanks.",
                f"Perfect. You’ve got a steady hand. Appreciate it.",
                f"That’s spot on. You’re reliable, just like a good ally. Thanks."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([
                f"This isn’t what I ordered. Let’s try again.",
                f"Hmm... not quite right. Double-check next time.",
                f"Close, but not the right mix. Let’s fix it."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class kiryu(Customer):
    def __init__(self):
        super().__init__()
        self.name = "(not) Kiryu Kazuma"
        self.prevference = "Classic"
        self.sprite = ("Joryu.png", (193.5, 79.6))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([
                f"I’ll take a {self.fdrinks[0]}. Simple and classic, just like me.",
                f"Hey. A {self.fdrinks[0]} sounds good right now.",
                f"Let’s go with a {self.fdrinks[0]}. Keep it straightforward.",
                f"One {self.fdrinks[0]}, please. No frills, just the drink.",
                f"A {self.fdrinks[0]} will do. I’m not one for complicated orders.",
                f"Make it a {self.fdrinks[0]}. Something reliable, like me.",
                f"I’ll have a {self.fdrinks[0]}. Nothing fancy, just the good stuff."
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True
        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Surprise me with something {self.prevference}. I trust your skills.",
                f"Anything {self.prevference} will do. Just make it good.",
                f"I’m in the mood for something {self.prevference}. Your call.",
                f"Pick something {self.prevference} for me. I’ll leave it to you.",
                f"Let’s go with something {self.prevference}. I’m sure you’ll make it right."
            ])
            self.line = self.name + " : " + self.line
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"Perfect. This is exactly what I needed. Thanks.",
                f"Good work. You’ve got a talent for this.",
                f"Spot on. You’ve got my respect for this one.",
                f"Excellent. This is just what I was looking for.",
                f"Great job. You’ve got a knack for making drinks.",
                f"Impressive. This drink is just right. Thanks."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([
                f"This isn’t quite right. Let’s try again.",
                f"Hmm... not what I ordered. Can you fix it?",
                f"Close, but not what I had in mind. Let’s redo it next time.",
                f"Not quite what I was expecting. Let’s give it another shot.",
                f"This isn’t what I asked for. Let’s try again, shall we?",
                f"Almost, but not quite. Let’s get it right next time."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False

class steve(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Steve"
        self.prevference = "Classy"
        self.sprite = ("Steve.png", (204.5, 88.9))
        self.randrink()
        self.get_order()

    def randrink(self):
        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_order(self):
        if len(self.fdrinks) == 1:
            self.line = random.choice([
                f"Hey there! I’ll take a {self.fdrinks[0]}. Something simple, like building blocks.",
                f"Can I get a {self.fdrinks[0]}? Keep it straightforward, like crafting a table.",
                f"A {self.fdrinks[0]} sounds good. Nothing too fancy, just like me.",
                f"I’ll have a {self.fdrinks[0]}. Simple and reliable, like a wooden pickaxe."
            ])
            self.line = self.name + " : " + self.line.replace("_", " ")
            return True
        elif len(self.fdrinks) > 1:
            self.line = random.choice([
                f"Surprise me with something {self.prevference}. I trust your crafting skills.",
                f"Anything {self.prevference} will do. Just make it good, like a diamond sword.",
                f"I’m in the mood for something {self.prevference}. Your call, bartender.",
                f"Pick something {self.prevference} for me. I’ll leave it to you, like mining for diamonds."
            ])
            self.line = self.name + " : " + self.line
            return False

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([
                f"Perfect! This drink is as good as finding diamonds. Thanks!",
                f"Wow, this is great! You’re as skilled as a master builder.",
                f"Spot on! This drink is as satisfying as finishing a big build.",
                f"Excellent! This is just what I needed after a long day mining."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 1
            return True
        else:
            self.line = random.choice([
                f"Hmm, this isn’t quite right. Feels like I crafted the wrong item.",
                f"Not what I ordered. Let’s try again, like fixing a broken tool.",
                f"Close, but not quite. Let’s redo it, like rebuilding a creeper explosion.",
                f"This isn’t what I asked for. Let’s give it another shot, like respawning after a fall."
            ])
            self.line = self.name + " : " + self.line
            self.satisfaction = 0
            return False