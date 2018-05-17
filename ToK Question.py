import random

way_of_knowing = ["Language ", "Emotion ", "Perception ", "Reason "]
randomizerW = random.choice(way_of_knowing)

fill_one = "in "
fill_two = "affect "

area_of_knowledge = ["Natural sciences", "Mathematics", "Ethics", "the Arts", \
                    "Human Sciences", "History"]
randomizerA = random.choice(area_of_knowledge)

question_starters = ["To what extent does ", "How does " + randomizerW + fill_two \
                    ,"What is the role of " \
                    ,"Evaluate the strengths and weaknesses of ", "Compare and contrast " \
                    ,"How can " + randomizerW + "be used to justify " \
                    ,"How can " + randomizerW + "be used to explain " \
                    ,"What is the validity of " + randomizerW + "to justify "]

randomizerQ = random.choice(question_starters)

##repeat = [s for s in question_starters if randomizerW in s]

knowledge_question = randomizerQ + randomizerW + fill_one + randomizerA

print knowledge_question
