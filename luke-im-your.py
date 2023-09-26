names = {"Darth Vader":"father", "Leia":"sister", "Han":"brother in law","R2D2":"droid"}
relation_to_luke = lambda n:"Luke, I am your "+names[n]+"."
print(relation_to_luke("Leia"))

