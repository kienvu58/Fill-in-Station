class Problem:
    def __init__(self, dom, dict):
        self.variables = ['11', '12', '13',
                          '21', '22', '23',
                          '31', '32', '33']
        self.domain = dom
        self.start_state = {}
        self.dictionary = dict
        self.count = 0

    def check_contraints(self, assignment):
        isConsistent = True
        contraints = (('11', '12', '13'), ('21', '22', '23'), ('31', '32', '33'),
                      ('11', '21', '31'), ('12', '22', '32'), ('13', '23', '33'),
                      ('11', '22', '33'), ('13', '22', '31'))

        for contraint in contraints:
            if all(key in assignment.keys() for key in contraint):
                word = "".join(assignment[key] for key in contraint)
                if word not in self.dictionary:
                    isConsistent = False

        return isConsistent

    def is_goal_state(self, state):
        return len(state) == 9

    def select_unassigned_variable(self, assignment):
        unassigned_variable = [var for var in self.variables 
                                    if var not in assignment.keys()]
        var = unassigned_variable.pop()
        return var


def get_dictionary(filename):
    dictionary = set()
    for line in open(filename, 'r'):
        dictionary.add(line.strip())
    return dictionary

def backtracking_search(problem):
    return recursive_backtracking({}, problem)

def recursive_backtracking(assignment, problem):

    if problem.is_goal_state(assignment):
        return assignment
    var = problem.select_unassigned_variable(assignment)
    for value in problem.domain:
        assignment[var] = value
        if problem.check_contraints(assignment):
            backup_domain = problem.domain
            index = problem.domain.index(value)
            problem.domain.pop(i)
            result = recursive_backtracking(assignment, problem)
            if result is not None:
                return result
            problem.domain.insert(index, value)
        del assignment[var] 
    return None

if __name__ == "__main__":
    dom = ['A', 'E', 'O',
           'P', 'R', 'R',
           'S', 'W', 'Y']
    dict = get_dictionary('3_letters_dictionary')
    problem = Problem(dom, dict)
    right_assignment = {'11': 'S', '12': 'O', '13': 'P',
                        '21': 'E', '22': 'A', '23': 'R',
                        '31': 'W', '32': 'R', '33': 'Y'}
    incomplete_assignment = {'11': 'S', '12': 'O', '13': 'P',
                             '21': 'E', '22': 'A', '23': 'R',
                             '31': 'W', '32': 'R'}
    wrong_assignment = {'11': 'S', '12': 'O', '13': 'R',
                        '21': 'E', '22': 'A', '23': 'P',
                        '31': 'W', '32': 'R', '33': 'Y'} 
    wrong_incomplete = {'32': 'R', '31': 'W', '33': 'Y',
                        '11': 'S', '12': 'O', '13': 'P'}
    print problem.check_contraints(right_assignment)
    print problem.check_contraints(incomplete_assignment)
    print problem.check_contraints(wrong_assignment)
    print problem.check_contraints(wrong_incomplete)

    print backtracking_search(problem)