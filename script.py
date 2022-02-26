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
    def __init__(self, name, body_area, weights = False, timed = False, sets = 2, reps = 10, kg = 5, mins = 1):
        self.name = name
        self.body_area = body_area
        self.sets = sets
        self.reps = reps
        self.weights = weights
        self.kg = kg
        self.timed = timed
        self.mins = mins
    
    def __repr__(self):
       part_1 = '{name}: these are a {bodyarea} excecise - '.format(name=self.name, bodyarea=self.body_area)
       if self.timed == True:
           return part_1 + 'set to {sets} for {mins} mins each.'.format(sets=self.sets, mins=self.mins)
       else:
            if self.weights == True:
                return part_1 + 'set to {sets} sets of {reps} reps with weights at {kg}kg.'.format(sets=self.sets, reps=self.reps, kg=self.kg)
            else:
                return part_1 + 'set to {sets} sets of {reps} reps'.format(sets=self.sets, reps=self.reps) 

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
# upper body with weights:
bicep_curls = Exercise('Bicep Curls', 'upper', True)
overhead_tricep_curls = Exercise('Over-head Tricpe extensions', 'upper', True)
standing_press = Exercise('Standing Press', 'upper', True)        

# upper body without weights:
pushups = Exercise('Pushups', 'upper')
tricep_dips = Exercise('Tricep Dips', 'upper')
shadow_box = Exercise('Shadow Box', 'upper', False, True)

#core with weights:
side_bends = Exercise('Side Bends', 'core', True)
twist = Exercise('Twist', 'core', True)

#core without weights:
leg_lifts = Exercise('Leg Lifts', 'core')
crunches = Exercise('Crunches', 'core')
plank = Exercise('Plank', 'core', False, True, 2, 0, 0, 1)

#cardio
climbers = Exercise('Climbers', 'cardio', False, True, 3, 0, 0, 1)
burpees = Exercise('Burpees', 'cardio', False, True, 3, 0, 0, 1)
skipping = Exercise('Skipping', 'cardio', False, True, 3, 0, 0, 5)


#lower with weights
goblin_squat = Exercise('Goblin Squat', 'legs', True)
lunges = Exercise('Lunges', 'legs', True)
dead_lift = Exercise('Dead Lift', 'legs', True)

#lower without weights
squats = Exercise('Squats', 'legs')
wall_sit = Exercise('Wall Sit', 'legs', False, True)



name = input('what is your name?').title()
level = input('how strong are you?')
workout = input('what kind of workout do you want?')

you = Profile(name, level, workout)

print(you)
print(pushups)
print(bicep_curls)