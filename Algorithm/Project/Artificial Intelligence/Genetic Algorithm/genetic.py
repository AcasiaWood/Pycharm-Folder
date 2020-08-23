# set password

import random
import string

# random password generation function

def generate_word(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, k=length))

# initial population generation function

def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        length = i % (max_len - min_len + 1) + min_len
        population.append(generate_word(length))
    return population

# object fitness evaluation function

def fitness(original_word, test_word):
    score = 0

    # if the length is different, the genetic evaluation score is 0
    if len(original_word) != len(test_word):
        return score

    # if the length is the same, add 0.5 points to the length
    len_score = 0.5
    score += len_score

    # add 1 point if the string is the same for each digit
    for i in range(len(original_word)):
        if original_word[i] == test_word[i]:
            score += 1

    # converted to 100 points and returned
    return (score / (len(original_word) + len_score)) * 100

# a function that evaluates goodness of fit for all objects and adds scores to the list

def compute_performance(original_word, population):
    performance_list = []
    predict_len = 0

    for word in population:
        score = fitness(original_word, word)

        # if the score is not 0, the length of the original password is found.
        if score != 0:
            predict_len = len(word)

        performance_list.append([word, score])

    population_sorted = sorted(performance_list, key=lambda x: x[1], reverse=True)

    return population_sorted, predict_len

# a function that creates a survival group with a good score among all individuals

def select_survivors(population_sorted, best_sample_size, lucky_sample_size, password_len):
    next_generation = []

    # insert good factor into list
    for i in range(best_sample_size):
        if population_sorted[i][1] > 0:
            next_generation.append(population_sorted[i][0])

    # insert survivors from the list
    lucky_survivors = random.sample(population_sorted, k=lucky_sample_size)
    for survivor in lucky_survivors:
        next_generation.append(survivor[0])

    # add a random password if the length of the next_generation is smaller than the best_sample_size and lucky_sample_size combined
    while len(next_generation) < best_sample_size + lucky_sample_size:
        next_generation.append(generate_word(password_len))

    random.shuffle(next_generation)

    return next_generation

# a function that creates new objects by crossing two objects

def create_child(mom, dad):
    # receive two objects and create children by mixing one character of mom and dad with 50% probability based on the small object
    child = ''
    min_len = min(len(mom), len(dad))

    for i in range(min_len):
        point = random.randint(1, 2)
        if point == 1:
            child += mom[i]
        else:
            child += dad[i]

    return child


# a function that selects two of the survivors as children and returns a list
# if the initial population was 100 and the survivor is 40, the number_child should be set to 5 to make the next group 100.

def mating(survivors, number_child):
    next_population = []

    for i in range(int(len(survivors)/2)):
        for j in range(number_child):
            next_population.append(create_child(survivors[i], survivors[len(survivors) - i - 1]))

    return next_population

# function to create mutant objects

def mutate_word(word):
    index = random.randint(0, len(word)-1)
    change_char = random.choice(string.ascii_letters + string.digits)
    if index == 0:
        word = change_char + word[1:]
    else:
        word = word[:index] + change_char + word[index+1:]
    return word

# function to generate mutant individuals with a certain probability in the population

def mutate_population(population, mutate_percent):
    for i in range(len(population)):
        if random.randint(0, 100) < mutate_percent:
            population[i] = mutate_word(population[i])
    return population
