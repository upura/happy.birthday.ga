import string
import random


USER_NAME = 'upura'
OBJECTIVE_SENTENCE = 'happy birthday' + ' ' + USER_NAME

def get_string_candidate():
    string_candidate = [chr(i) for i in range(97, 97 + 26)]
    string_candidate.append(' ')
    return string_candidate

def get_sentence(string_candidate):
    created_sentence = random.choices(string_candidate, k = len(OBJECTIVE_SENTENCE))
    print(''.join(created_sentence))
    return created_sentence

def evaluation_function(sentence):
    judgment = [True if i == j else False for i, j in zip(OBJECTIVE_SENTENCE, sentence)]
    evaluation = sum(judgment) / len(judgment)
    return evaluation

if __name__ == '__main__':
    string_candidate = get_string_candidate()
    sentence = get_sentence(string_candidate)
    print(evaluation_function(sentence))