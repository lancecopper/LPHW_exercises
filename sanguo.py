from sys import exit
from random import randint

class Engine(object):
    def __init__(self, map):
        self.map = map

    def play(self):
        next = self.map.start
        
        while True:
            print "\n--------"
            room = getattr(self.map, next)
            next = room()
            
            
class Map(object):

    def __init__(self, start):
        self.quips = [
        "乱世凶险，壮士请重新来过",
        "小样儿，这水平还不如回家种红薯",
        "菜Bbbbbb~~~",
        "作者为你的智力感到惋惜。"
        ]
        self.start = start
    
    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)
        
    def qingzhou(self):
        print "公元184年的东亚，天气转寒，帝国中心的权柄在外戚与宦官间频繁易手，社会土地兼并愈演愈烈。然而这些都跟你没有蛋关系，\
        几年前，你为了避免卖身为奴的命运，打杀了催讨地租的地主，远离家乡，隐姓埋名来到青州城避祸。"
        print "\n"
        print "青州城里也难讨生活，年景不好，大家都要挨饿，白露时节的晚上，寒气已然逼人，你和几个同伴相约吃酒，商量个出路。\
        粗豪猛壮的焦大说：\“前日，大贤良师张角真人举世，所经处，信众归附，官军望之披靡，吾等可归之。\"另一个童猛反驳：\“汉室虽然衰微\
        天下尚未离心，刘氏宗室为宰牧者众，张角事必败。\" 众人各有倾向，一时相持不下，纷纷把目光投向了你"
        
        print "You're running down the central corridor to the Weapon \
        Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, \
        and  evil clown costume flowing around his hate filled body. \
        He'sblocking the door to the Amory and about to pull a weapon \
        to blast you."
        
        action = raw_input(">")
        if action == "shoot!":
            print "Quik on the draw you yank out your blaster and \
            fire it at the Gothon."    
            print "His clown costume is flowing and moving around \
            his body, which throws "
            print "off your aim. Your laser hits his costume but \
            misses him entirely. This"
            print "completely ruins his brand new costume his \
            mother bought him, which"
            print "makes him fly into an insane rage and blast you \
            repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'
    
        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip \
            and slide right"
            print "as the Gothon's blaster cranks a laser past your \
            head."
            print "Int the middle of your artful dodge your foot \
            slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the \
            Gothon stomps on"
            print "your head and eats you."
            return 'death'
    
        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults\
            in the academy"
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur \
            ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laught, then busts \
            out laughing and can't move."
            print "While he's laughing you run up and shoot him \
            square in the head"
            print "putting him down, then jump through the Weapon \
            Armory door."
            return 'laser_weapon_armory'
    
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
    
    def laser_weapon_armory(self):
        print "You do a dive roll into the Weapon Armory, crouch \
        and scan the room"
        print "for more Gothons that might be hiding. It's dead \
        quiet, too quiet."
        print "You stand up and run to the far side of the room \
        and find the"
        print "neutron bomb in its container. There's a keypad \
        lock on the box"
        print "and you need the code to get the bomb out. If you \
        ge the code"
        print "worng 10 times then the lock closes forever and you \
        can't"
        print"get the bomb. The code is 3 digits."

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]>")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        
        if guess == code:
            print "The container clicks open and the seal breaks, \
            letting gas out."
            print "You grab the neutron bomb and run as fast as \
            you can to the "
            print"bridge where you must place it in the right spot."
            return 'the bridge'
        else:
            print "The lock buzzes one last time and then you hear \
            a sickening"
            print "melting sound as the mechanism si fused \
            together."
            print "You decide to sit there, and finally the \
            Gothons blow up the "
            print "ship from their ship and you die."
            return 'death'
        
    def the_bridge(self):
        print "You burst onto the Bridge with the neutron destruct \
        bomb"
        print "under your arm and surprise 5 Gothons who are trying \
        to"
        print "take control of the ship. Each of them has an even \
        uglier"
        print "clown costume than the last. They haven't pulled \
        their"
        print "weapons out yet, as they see the active bomb under \
        your"
        print "arm and don't want to set it off."
    
        action =  raw_input("> ")
    
        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of \
            Gothons"
            print "and make a leap for the door. Right as you drop\
            it a"
            print "Gothon shoots you right in the back killing \
            you."
            print "As you die you see another Gothon frantically \
            try to disarm"
            print "the bomb. You die knowing they will probably \
            blow up when"
            print "it goes off"
            return 'death'
       
        elif action == "slowly place the bomb":
            print "You point our blaster at the bomb under your \
            arm"
            print "and the Gothons put their hands up and start \
            to sweat."
            print "You inch backward to the door, open it, and then \
            carefully"
            print "place the bomb on the floor, pointing your \
            blaster at it."
            print "You then jump back through the door, punch the \
            close button"
            print "and blast the lock so Gothons can't get \
            out"
            print "Now that the bomb is placed ou run to the escape \
            pod to"
            print "get off this tin can."
            return 'escape_pod'
        
        else:
            print "DOES NOT COMPUTE"
            return 'the_bridge'
        
    
    def escape_pod():
        print "You rush through the ship desperately tring to make \
        it to "
        print "the escape pod before the whole ship explodes. It \
        seems like"
        print "hardly any Gothons are on the ship, so your run is \
        clear of"
        print "interference. You get to the chamber with the \
        escape pods, and"
        print "now need to pick one to take Some of them could \
        be damaged"
        print "but you don't have time to look. There's 5 pods, \
        which one"
        print "do you take?"
    
        good_pod = randint(1,5)
        guess_inut ("[pod #]> ")
    
        if int(guess) != good_pod:
            print"You jump into pod %s and hit the ejectbutton." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures crushing your body"
            print "into jam jelly."
            return 'death'
        
        else:
            print "You jump into pod%s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implodes then explode like a"
            print "bright star, taking out th Gothon ship at the same"
            print "time. You won!"
        
            exit(0)
            
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()