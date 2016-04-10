import random


def generate_fill_in_station_input(n_inputs, dict_fn, input_fn):
    """
        n_inputs: number of inputs needs to generate
        dict_fn: dictionary of meaning words filename
        input_fn: input filename
        Writes all inputs to given input file.
    """

    dictionary = set()
    with open(dict_fn, 'r') as f:
        for line in f:
            dictionary.add(line.strip())

    with open(input_fn, 'w') as f:
        for word_1 in dictionary:
            for word_2 in dictionary:
                if word_1 == word_2:
                    continue
                for word_3 in dictionary:
                    if word_2 == word_3 or word_1 == word_3:
                        continue
                    seq = word_1 + word_2 + word_3

                    if check_constraints(seq, dictionary):
                        seq = ' '.join(random.sample(seq, len(seq)))
                        f.write(seq + '\n')
                        n_inputs -= 1

                    if n_inputs == 0:
                        return


def check_constraints(seq, dict):
    constraints = ((0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for constraint in constraints:
        word = "".join(seq[key] for key in constraint)
        if word not in dict:
            return False
    return True


if __name__ == "__main__":
    generate_fill_in_station_input(100, '3_letters_dictionary', 'input')
