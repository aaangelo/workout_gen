test = input('do you have weights? yes or no?')

if test == 'yes':
    print('3 x 10 curls')
elif test == 'no':
    print('don 3 x 10 pushups')

class Profile:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'your name is {name} and you are {level} level.'.format(name=self.name, level=self.level)

name = input('what is your name?').title()
level = input('how strong are you?')


you = Profile(name, level)

print(you)