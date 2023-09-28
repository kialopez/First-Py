# Programmed by: KURT IVAN A. LOPEZ BSCS1-B

# Input WEIGHT IN POUNDS
pounds = float(input("Enter weight in pounds: "))

# Convert LBS TO KG
kilograms = pounds * 0.453592

# OUTPUTE HERE
print("Weight in pounds: ",pounds,"lbs" )

print("Weight in kilograms: ",kilograms,"kg")

print("============================================")

# Input MILES
miles = float(input("Enter distance in miles: "))

# Convert LBS TO KG
kilometers = miles * 1.60934

# OUTPUTE HERE
print("Distance in Miles: ",miles,"mi" )

print("Distance in Kilometers: ",kilometers,"km")

print("============================================")

# Input FAHRENHEIT
fahrenheit = float(input("Enter temperature in fahrenheit: "))

# Convert F TO C
celcius = (fahrenheit - 32) * 5/9.

# OUTPUTE HERE
print("Temperature in Fahrenheit: ",fahrenheit,"°F" )

print("Temperature in Celcius: ",celcius,"°C")

print("============================================")

ages = []

# GET AGES OF STUDENTS
for i in range(10):
    while True:
        try:
            age = int(input(f"Enter the age of student {i + 1}: "))
            if age >= 0:
                ages.append(age)
                break
            else:
                print("ENTER A VALID AGE.")
        except ValueError:
            print("ENTER A VALID AGE.")

# CALCULATE THE AVERAGE AGE
average_age = sum(ages) / len(ages)

# DISPLAY
print(f"\nAverage Age of all the Students: {average_age:.2f} years")

print("============================================")

# NAMES
hero = "Kurt"
kontrabida = "Malik"
heropet = "Nuggets"
wizards = "Cordillera"
love = "Belle"

# POWER
heropower = "Sagada Shadowmeld"
kontrabidapower = "Dark Sorcery"
petpower = "Darkness  Bark"
wizardpower = "Wisdom of the Mountains"
lovelook = "Beauty"

# ARMAS
heroarmas = "Sword of Radiance"
kontrabidaarmas = "Wizard Staff"
petarmas = "Crescent Shield"
wizardarmas = "Mountain's Dagger"
loveitem = "Heart necklace"

story = f"""In the magical city of Baguio, known for its misty mountains and cool breeze, lived a brave hero named {hero}. His extraordinary ability, {heropower}, brought light to the darkest corners of the city.

Yet, beneath the shadows, a evil villain named {kontrabida} wielded the power of {kontrabidapower}, spreading chaos across Baguio. 

Alongside {hero} on his quest was his loyal dog companion, {heropet}, who possessed the power of {petpower} and a trusty {petarmas}. Together, they embarked on a historic mission to defeat the forces of evil.

Guiding their steps was the wise wizard, {wizards}, whose mastery of {wizardpower} provided invaluable knowledge. He taught {hero} the secrets of his abilities and the path to victory.

Amidst their battles, {hero} found love in the heart of {love}, a woman blessed with {lovelook}. The {loveitem} symbolized his affection for her.

Will the forces of good prevail over the darkness in the heart of Baguio?"""

print(story)
