import string

text='''Freshly baked news: the baguette, the long, crusty loaf bread that is a delicious staple of French life, has been awarded special protected status, placing it in a culinary pantheon alongside other regional food delicacies from around the world.
The "artisanal know-how and culture of the baguette" is now officially recognized on UNESCO's list of Intangible Cultural Heritage, the organization announced Wednesday, inscribing the expertise behind the French bread as an integral part of human culture.
UNESCO -- the UN's cultural body -- defines intangible cultural heritage as "traditions or living expressions inherited from our ancestors and passed on to our descendants."
The baguette joins other foods and culinary cultures on UNESCO's list of Intangible Cultural Heritage, including the making of Neapolitan pizza, kimchi, Belgian beer culture, the "Mediterranean diet", and Arabic coffee.
While sites from the US, including the Statue of Liberty, Yellowstone National Park and Philadelphia's Independence Hall are recognized by UNESCO as World Heritage Sites, nothing from the US is currently listed on the organization's Intangible Cultural Heritage of Humanity list.
'''
x=text.translate(str.maketrans('' ,'',string.punctuation))
print(x)