import string
import random
import numpy as np
import sys


try:
    USER_NAME = sys.argv[1]
except:
    USER_NAME = 'upura'

OBJECTIVE_SENTENCE = 'Happy birthday, ' + USER_NAME + '!'
AGENT_NUM = 1000
GENETIC_OPERATORS = []
CROSSOVER_PROB = 0.1
MUTATION_PROB = 0.1
GENETIC_OPERATORS = ['CROSSOVER', 'MUTATION', 'REPRODUCTION']
GENETIC_OPERATORS_WEIGHT = \
    [CROSSOVER_PROB, MUTATION_PROB, 1 - (CROSSOVER_PROB + MUTATION_PROB)]

def get_string_candidate():
    string_candidate = \
        [chr(i) for i in range(97, 97 + 26)] + [chr(i) for i in range(65, 65 + 26)]    
    string_candidate.append(' ')
    string_candidate.append(',')
    string_candidate.append('!')
    return string_candidate

def get_sentence(string_candidate, sentence_length):
    created_sentence = random.choices(string_candidate, k = sentence_length)
    return created_sentence

def get_fitness(sentence):
    judgment = [i == j for i, j in zip(OBJECTIVE_SENTENCE, sentence)]
    evaluation = sum(judgment) / len(judgment)
    return evaluation

def decide_genetic_operator():
    return np.random.choice(GENETIC_OPERATORS, p = GENETIC_OPERATORS_WEIGHT)

def fitness_proportionate_selection(agents, evaluations):
    weight = np.array(evaluations) / sum(evaluations)
    index = np.arange(AGENT_NUM)
    return agents[np.random.choice(index, p = weight)]

def crossover(agents, evaluations):
    father_agent = fitness_proportionate_selection(agents, evaluations)
    mother_agent = fitness_proportionate_selection(agents, evaluations)
    crossover_points = random.sample(list(np.arange(len(OBJECTIVE_SENTENCE) - 1)), 2)
    next_agent = father_agent[:min(crossover_points)] \
        + mother_agent[min(crossover_points):max(crossover_points)] \
        + father_agent[max(crossover_points):]
    return next_agent

def mutation(agents, evaluations, string_candidate):
    selectd_agent = fitness_proportionate_selection(agents, evaluations)
    next_agent = [i if random.random() > 0.1 else \
        get_sentence(string_candidate, 1)[0] for i in selectd_agent]
    return next_agent

def reproduction(agents, evaluations):
    return fitness_proportionate_selection(agents, evaluations)

def create_one_next_agent(agents, evaluations, string_candidate):
    genetic_operator = decide_genetic_operator()
    if genetic_operator == GENETIC_OPERATORS[0]:
        next_agent = crossover(agents, evaluations)
    elif genetic_operator == GENETIC_OPERATORS[1]:
        next_agent = mutation(agents, evaluations, string_candidate)
    else:
        next_agent = reproduction(agents, evaluations)
    return next_agent

def create_next_generation(agents, evaluations, string_candidate):
    next_agents = [create_one_next_agent(agents, evaluations, string_candidate) for i in range(AGENT_NUM)]
    return next_agents

if __name__ == '__main__':
    string_candidate = get_string_candidate()
    agents = [get_sentence(string_candidate, len(OBJECTIVE_SENTENCE)) for i in range(AGENT_NUM)]
    evaluations = [get_fitness(agents[i]) for i in range(AGENT_NUM)]
    generation_id = 0

    while max(evaluations) < 1:
        generation_id += 1
        agents = create_next_generation(agents, evaluations, string_candidate)
        evaluations = [get_fitness(agents[i]) for i in range(AGENT_NUM)]
        print('===GENERATION ' + str(generation_id) + '===')
        print(''.join(agents[np.argmax(evaluations)]))
        print('max_fitness: ' + str(max(evaluations)))
