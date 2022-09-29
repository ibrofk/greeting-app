#!/usr/bin/env python3

import random
names = 'ibrahim omer ahmed frok micke 3alli both jacob isma3il Alba, Jessica Alberti Leone Battista Albom Mitch Alcott Louisa May Alcuin Aldiss Brian Alexander Alexie Sherman'
def greet(name):
   print('my name is AI, how are u doin ' + name)
names = names.split()
greet(names[random.randint(0,len(names)-1)])
