import heapq


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
        self.variables = ('11', '12', '13',
                          '21', '22', '23',
                          '31', '32', '33')
        self.domain = domain
        self.dictionary = dictionary
        self.bigram_freq = bigram_freq
        self.constraints = (
            ('11', '12', '13'), ('21', '22', '23'), ('31', '32', '33'),
            ('11', '21', '31'), ('12', '22', '32'), ('13', '23', '33'),
            ('11', '22', '33'), ('13', '22', '31'))
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

    def get_successors(self, state):
        """
            state: current state
        Returns priority queue of next states
        """
        successors = PriorityQueue()
        next_var_index = len(state)
        curr_domain = self.domain[:]
        for key in state.keys():
            curr_domain.remove(state[key])
        for value in curr_domain:
            heuristic = self.get_heuristic(state, next_var_index, value)
            if heuristic == 0:  # bigram never happens
                continue
            next_state = state.copy()
            next_state.update({self.variables[next_var_index]: value})
            if self.check_contraints(next_state):
                successors.push(next_state, heuristic)

        return successors

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

    def get_heuristic(self, state, next_var_index, next_value):
        """
            state: current state
            next_var_index: next variable position in matrix
            next_value: value of next variable need to calculate heuristic
        Returns heuristic value for assigning next variable from current
        state.
        """
        heuristic = 1
        if next_var_index in (0, 3, 6):
            heuristic *= self.bigram_freq[('$', next_value)]
        else:
            prev_value = state[self.variables[next_var_index - 1]]
            heuristic *= self.bigram_freq[(prev_value, next_value)]

        return - heuristic


def backtracking_search(problem, trace_fn=None):
    """
        trace_fn: name of trace file, None means no trace
    Returns a solution for fill-in station problem.
    Use heuristic to choose which value goes first.
    """
    def recursive_backtracking(state, problem, trace_fn):
        if problem.is_goal_state(state):
            return state

        successors = problem.get_successors(state)
        children = successors.heap[:]

        while not successors.isEmpty():
            next_state = successors.pop()
            result = recursive_backtracking(next_state, problem, trace_fn)
            if result is not None:
                return result
        problem.count += 1
        if trace_fn is not None:
            print_trace(trace_fn, state, children, problem.count)

        return None

    def print_trace(trace_fn, parent, children, n_nodes):
        f = open(trace_fn, 'a')
        f.write(str(n_nodes))

    return recursive_backtracking({}, problem, trace_fn)


def get_dictionary(filename):
    """
        filename: name of dictionary file
    Returns a set contains 3-letters words
    """
    dictionary = set()
    for line in open(filename, 'r'):
        dictionary.add(line.strip())
    return dictionary


def get_bigram_freq(filename):
    """
        filename: name of frequencies file
    Returns a set contains bigram frequencies
    """
    bigram_freq = {}
    for line in open(filename, 'r'):
        first, second, freq = line.split()
        bigram_freq[(first, second)] = float(freq)
    return bigram_freq


def print_matrix(state):
    """
        state: current state
    Prints a matrix from current state
    """
    matrix = (('11', '12', '13'),
              ('21', '22', '23'),
              ('31', '32', '33'))
    for row in matrix:
        word = ""
        for col in row:
            if col in state.keys():
                word += state[col]
            else:
                word += "*"
        print word
    print ""

if __name__ == "__main__":
    dom1 = ['A', 'E', 'O',
            'P', 'R', 'R',
            'S', 'W', 'Y']
    dom2 = ['A', 'E', 'E',
            'I', 'K', 'L',
            'L', 'P', 'Y']
    dict = get_dictionary('3_letters_dictionary')
    bigram_freq = get_bigram_freq('bigram_frequence_list')
    problem = FillinStationProblem(dom1, dict, bigram_freq)
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
    # print problem.check_contraints(right_assignment)
    # print problem.check_contraints(incomplete_assignment)
    # print problem.check_contraints(wrong_assignment)
    # print problem.check_contraints(wrong_incomplete)

    result = backtracking_search(problem)
    if result is not None:
        print_matrix(result)
    else:
        print "Cannot find any solution!"
    print problem.count
