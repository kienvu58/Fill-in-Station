import heapq
import effective_branching_factor as ebf


class PriorityQueue:
    """
    Implements a priority queue data structure. Each inserted item
    has a priority associated with it and the client is usually interested
    in quick retrieval of the lowest-priority item in the queue. This
    data structure allows O(1) access to the lowest-priority item.

    Note that this PriorityQueue does not allow you to change the priority
    of an item.  However, you may insert the same item multiple times with
    different priorities.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


class FillinStationProblem:
    """
    A problem defines the state space, start state, goal test, successor
    function. This search problem can be used to find a solution for fill-in
    station words puzzle.

    An assignment sets a values into the variable.
    State is a set of assignments.
    Goal state is a complete set of assignments that satisfies all contraints.
    """

    def __init__(self, domain, dictionary, bigram_freq):
        """
        Constructs a FIS problem. It defines variables, domain and constraints
        for search problem. Initial state is an empty assignment.
            domain: input letters need to fill in
            dictionary: a dictionary of 3 letters word
            bigram_freq: bigram frequencies to calculate heuristic
        """
        self.variables = range(9)
        self.domain = domain
        self.dictionary = dictionary
        self.bigram_freq = bigram_freq
        self.constraints = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))
        self.start_state = {}
        self.count = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        return self.start_state

    def is_goal_state(self, state):
        """
            state: current state
        Returns True if and only if the set of assignments is complete and
        satisfies all constraints.
        """
        return len(state) == 9 and self.check_contraints(state)

    def get_next_states(self, state, heuristic_fn):
        """
            state: current state
        Returns priority queue of next states
        """
        next_states = PriorityQueue()
        next_var = len(state)
        curr_domain = self.domain[:]
        for key in state.keys():
            curr_domain.remove(state[key])
        for value in curr_domain:
            heuristic = heuristic_fn(
                self.bigram_freq, self.variables, state, next_var, value)

            if heuristic == 0:  # bigram never happens
                continue

            next_state = state.copy()
            next_state.update({self.variables[next_var]: value})

            if self.check_contraints(next_state):
                next_states.push(next_state, heuristic)
                self.count += 1

        return next_states

    def check_contraints(self, state):
        """
            state: current state
        Return True iff current state satisfies all constraints
        """
        for constraint in self.constraints:
            if all(key in state.keys() for key in constraint):
                word = "".join(state[key] for key in constraint)
                if word not in self.dictionary:
                    return False

        return True


def trivial_heuristic(bigram_freq, variables, state, next_var, next_value):
    """
    This is a trivial heuristic, it always returns constant value.
    """
    return 1


def normal_heuristic(bigram_freq, variables, state, next_var, next_value):
    """
        state: current state
        next_var: next variable in matrix
        next_value: value of next variable need to calculate heuristic
    Returns heuristic value for assigning next variable from current state.
    This is a simple heuristic function.
    """
    heuristic = 1
    if next_var in (0, 3, 6):
        heuristic *= bigram_freq[('$', next_value)]
    else:
        prev_value = state[variables[next_var - 1]]
        heuristic *= bigram_freq[(prev_value, next_value)]

    return - heuristic


def advanced_heuristic(bigram_freq, variables, state, next_var, next_value):
    """
        state: current state
        next_var: next variable in matrix
        next_value: value of next variable need to calculate heuristic
    Returns heuristic value for assigning next variable from current state.
    This is an advanced heuristic function.
    """
    heuristic = 1
    # horizontal
    if next_var in (0, 3, 6):
        heuristic *= bigram_freq[('$', next_value)]
    else:
        prev_value = state[variables[next_var - 1]]
        heuristic *= bigram_freq[(prev_value, next_value)]

    # vertical
    if next_var in (0, 1, 2):
        heuristic *= bigram_freq[('$', next_value)]
    else:
        prev_value = state[variables[next_var - 3]]
        heuristic *= bigram_freq[prev_value, next_value]

    # main diagonal
    if next_var in (4, 8):
        prev_value = state[variables[next_var - 4]]
        heuristic *= bigram_freq[prev_value, next_value]

    # anti diagonal
    if next_var in (4, 6):
        prev_value = state[variables[next_var - 2]]
        heuristic *= bigram_freq[prev_value, next_value]

    return - heuristic


def backtracking_search(problem, heuristic_fn, trace):
    """
        trace: True turn on traces, False turn off traces
    Returns a solution for fill-in station problem.
    Use heuristic to choose which value goes first.
    """
    def recursive_backtracking(state, problem, heuristic_fn, trace):
        if problem.is_goal_state(state):
            return state

        next_states = problem.get_next_states(state, heuristic_fn)
        children = next_states.heap[:]

        if trace:
            print_trace(state, children)

        while not next_states.isEmpty():
            next_state = next_states.pop()
            result = recursive_backtracking(
                next_state, problem, heuristic_fn, trace)

            if result is not None:
                return result

        return None

    def print_trace(parent, children):
        print "======================================="
        print "Current state, depth %i:" % len(parent)
        print_matrix(parent)
        if children:
            count = 0
            for child in children:
                count += 1
                print "Child %i, heuristic = %0.18f:" % (count, child[0])
                print_matrix(child[2])
        else:
            print "No child!"
    func = {'advanced_heuristic': advanced_heuristic,
            'normal_heuristic': normal_heuristic,
            'trivial_heuristic': trivial_heuristic}
    return recursive_backtracking({}, problem, func[heuristic_fn], trace)


def get_dictionary(filename):
    """
        filename: name of dictionary file
    Returns a set contains 3-letters words.
    """
    dictionary = set()
    with open(filename, 'r') as f:
        for line in f:
            dictionary.add(line.strip())
    return dictionary


def get_bigram_freq(filename):
    """
        filename: name of frequencies file
    Returns a set contains bigram frequencies.
    """
    bigram_freq = {}
    with open(filename, 'r') as f:
        for line in f:
            first, second, freq = line.split()
            bigram_freq[(first, second)] = float(freq)
    return bigram_freq


def print_matrix(state):
    """
        state: current state
    Prints a matrix from current state.
    """
    matrix = ((0, 1, 2),
              (3, 4, 5),
              (6, 7, 8))
    for row in matrix:
        word = ""
        for col in row:
            if col in state.keys():
                word += state[col]
            else:
                word += "*"
        print word
    print ""


def read_command():
    """
    Processes the command used to run fill_in_station from CLI.
    """
    import argparse
    parser = argparse.ArgumentParser(description='Fill-in Station')

    parser.add_argument('input', action='store')
    parser.add_argument('dict', action='store')
    parser.add_argument('freq', action='store')
    parser.add_argument('fn', action='store')
    parser.add_argument('-trace', action='store_true', default=False)
    return vars(parser.parse_args())


def solve_problem(input, dict, freq, fn, trace, ebf=False, disp=True):
    """
        input: input file
        dict: dictionary file
        freq: bigram frequence list
        fn: heuristic function
        trace: trace mode
        ebf: False - not calculate effective branching factor
        disp: True - display result
    Solves fill-in station problem with given args.
    Returns average time & ebf.
    """
    import time
    dict = get_dictionary(dict)
    bigram_freq = get_bigram_freq(freq)
    domains = []
    with open(input, 'r') as f:
        for line in f:
            domains.append(line.strip().split())
    count = 0
    total_time = 0
    total_ebf = 0

    for dom in domains:
        count += 1
        problem = FillinStationProblem(dom, dict, bigram_freq)
        start_time = time.time()
        result = backtracking_search(problem, fn, trace)
        elapsed_time = time.time() - start_time

        if result is not None:
            total_time += elapsed_time
            total_ebf += ebf.effective_branching_factor(problem.count, 9)

        if disp:
            print "***************************************"
            print "Problem %d:" % count
            if result is not None:
                print "Found a solution:"
                print_matrix(result)
            else:
                print "Cannot find any solution"

            print "Finished in %f seconds!" % elapsed_time
            print "Expanded %d nodes\n" % problem.count

    return total_time/count, total_ebf/count


if __name__ == "__main__":
    args = read_command()
    solve_problem(**args)
