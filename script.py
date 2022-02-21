class Profile:
    def __init__(self, name, level, workout, time, weights = False):
        self.name = name
        self.level = level
        self.workout = workout
        self.time = time
        self.weights = weights

    def __repr__(self):
        return 'your name is {name} and you are {level} level.'.format(name=self.name, level=self.level)


class Exercise:
    def __init__(self, name, body_area, sets = 3, reps = 10, weights = False, kg = 5):
        self.name = name
        self.body_area = body_area
        self.sets = sets
        self.reps = reps
        self.weights = weights
        self.kg = kg
    
    def __repr__(self):
       part_1 = '{name}: these are a {bodyarea} excecise. set to {sets} sets and {reps} reps'.format(name=self.name, bodyarea=self.body_area, sets=self.sets, reps=self.reps)
       if self.weights == False:
           return part_1 + 'and requires no weights.'
       else:
           return part_1 + 'with weights at {kg}kg.'.format(kg=self.kg)




name = input('what is your name?').title()
level = input('how strong are you?')

pushups = Exercise('pushups', 'chest & arms')

you = Profile(name, level)

print(you)
print(pushups)