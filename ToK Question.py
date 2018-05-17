import random

way_of_knowing = ["Language ", "Emotion ", "Perception ", "Reason "]
randomizerW = random.choice(way_of_knowing)

fill_one = "in "
fill_two = "affect "

area_of_knowledge = ["Natural sciences", "Mathematics", "Ethics", "the Arts", \
                    "Human Sciences", "History"]
randomizerA = random.choice(area_of_knowledge)

question_starters = ["To what extent does ", "How does ", "What is the role of " \
                    ,"Evaluate the strengths and weaknesses of ", "Compare and contrast " \
                    ,"How can " + randomizerW + "be used to justify " \
                    ,"How can " + randomizerW + "be used to explain " \
                    ,"What is the validity of " + randomizerW + "to justify "]

knowledge_bank_Q1 = question_starters[0:1]
randomizerQ1 = random.choice(knowledge_bank_Q1)
knowledge_question1 = randomizerQ1 + randomizerW + fill_two + randomizerA

knowledge_bank_Q2 = question_starters[2:4]
randomizerQ2 = random.choice(knowledge_bank_Q2)
knowledge_question2 = randomizerQ2 + randomizerW + fill_one + randomizerA

knowledge_bank_Q3 = question_starters[5:7]
randomizerW3 = random.choice(way_of_knowing)
randomizerQ3 = random.choice(knowledge_bank_Q3)
knowledge_question3 = randomizerQ3 + randomizerW3 + fill_one + randomizerA

final_random_question_bank = [knowledge_question1, knowledge_question2, knowledge_question3]
final_random_question = random.choice(final_random_question_bank)

print final_random_question
