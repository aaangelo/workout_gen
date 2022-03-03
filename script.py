class Profile:
    def __init__(self, name, level, workout_area, time, weights = False):
        self.name = name
        self.level = int(level) * 2
        self.workout_area = workout_area
        self.time = int(time)
        self.weights = weights

    def __repr__(self):
        return 'your name is {name} and you are {level} level.'.format(name=self.name, level=int(self.level)/2)

    def workout_gen(self, workouts_list):
        workout_time = 0
        personal_workout_list = []
        difficulty = 0
        #creates list depending on body are and weights, excluding cardio for weights
        for workout in workouts_list:
            if self.workout_area == workout.body_area:
                if workout.body_area == 'cardio':
                    personal_workout_list.append(workout)
                elif self.weights == workout.weights:
                    personal_workout_list.append(workout)
        #increase difficulty for level
        while difficulty < int(self.level):
            for workout in personal_workout_list:
                workout.reps_sets_increase()
            difficulty += 1
        #adds time of all workouts           
        for exercise in personal_workout_list:
            workout_time += (exercise.mins * exercise.sets)
        # adds excercsies until its the right amount of time
        if workout_time < self.time:
            print('too short')
               

        # prints exercise list plus time.  
        print('your exercise list is:')
        for thing in personal_workout_list:
            print(thing)
        print( 'it will take ' + str(workout_time) + ' mins to complete.')



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
        if self.timed == True:
            self.mins += 0.25
        elif self.weights == True:
            if self.reps < 12 and self.sets <= 4:
                self.reps += 2
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
plank = Exercise('Plank', 'core', False, True, 2, 0, 0, 2)

#cardio
climbers = Exercise('Climbers', 'cardio', False, True, 3, 0, 0, 2)
burpees = Exercise('Burpees', 'cardio', False, True, 3, 0, 0, 0.5)
skipping = Exercise('Skipping', 'cardio', False, True, 3, 0, 0, 2)


#lower with weights
goblin_squat = Exercise('Goblin Squat', 'legs', True)
lunges = Exercise('Lunges', 'legs', True)
dead_lift = Exercise('Dead Lift', 'legs', True)

#lower without weights
squats = Exercise('Squats', 'legs')
wall_sit = Exercise('Wall Sit', 'legs', False, True)

workouts_list = [bicep_curls, overhead_tricep_curls,standing_press, pushups, tricep_dips, shadow_box, side_bends, twist, leg_lifts, crunches, plank, climbers, burpees, skipping, goblin_squat, lunges, dead_lift, squats, wall_sit]



name = input('what is your name?').title()
level = input('how strong are you?')
workout = input('what kind of workout do you want?')
time = input('how long do you want your workout to be?(in mins)')
weights_test = input('do you have weights? yes or no.')
if weights_test == 'yes':
    has_weights = True
else:
    has_weights = False
you = Profile(name, level, workout, time, has_weights)

print(you)
you.workout_gen(workouts_list)
