class Profile:
    def __init__(self, name, level, workout, time = 30, weights = False):
        self.name = name
        self.level = level
        self.workout = workout
        self.time = time
        self.weights = weights

    def __repr__(self):
        return 'your name is {name} and you are {level} level.'.format(name=self.name, level=self.level)


class Exercise:
    def __init__(self, name, body_area, weights = False, sets = 2, reps = 10, kg = 5):
        self.name = name
        self.body_area = body_area
        self.sets = sets
        self.reps = reps
        self.weights = weights
        self.kg = kg
    
    def __repr__(self):
       part_1 = '{name}: these are a {bodyarea} excecise. set to {sets} sets of {reps} reps '.format(name=self.name, bodyarea=self.body_area, sets=self.sets, reps=self.reps)
       if self.weights == False:
           return part_1 + 'and requires no weights.'
       else:
           return part_1 + 'with weights at {kg}kg.'.format(kg=self.kg)

    # method that increase the sets, reps or weight depending on strength.       

    def reps_sets_increase(self):
        if self.weights == True:
            if self.reps < 12 and self.sets <= 4:
                self.reps += 1
            elif self.reps == 12 and self.sets < 4:
                self.sets += 1
                self.reps = 8
            elif self.reps == 12 and self.sets == 4:
                self.reps = 8
                self.kg += 1
        else:
            if self.reps < 20 and self.sets <= 4:
                self.reps += 2
            elif self.reps == 20 and self.sets < 4:
                self.sets += 1
                self.reps = 10
            else:
                self.reps += 2

# now to create a bunch of excersises
pushups = Exercise('Pushups', 'upper', False, 3, 8)
bicep_curls = Exercise('Bicep Curls', 'upper', True)        




name = input('what is your name?').title()
level = input('how strong are you?')
workout = input('what kind of workout do you want?')

you = Profile(name, level, workout)

print(you)
print(pushups)
print(bicep_curls)