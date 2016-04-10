def sum(results, n_nodes, depth):
    sum = 0
    for index in range(1, depth + 1):
        sum += results**index
    return sum - n_nodes


def effective_branching_factor(n_nodes, depth):
    """
        Returns effective_branching_factor given number of expanded node and
        solution depth.
    """
    error = 0.001
    results = n_nodes ** (1 / depth)
    if(abs(sum(results, n_nodes, depth)) < error):
        print(results)
        return results
    _results = 0
    while True:
        middle = (results + _results) / 2
        if abs(sum(middle, n_nodes, depth)) < error:
            middle = middle.__round__(3)
            print(middle)
            return middle
            break
        elif sum(middle, n_nodes, depth) * sum(results, n_nodes, depth) > 0:
            results = middle
        else:
            _results = middle


if __name__ == "__main__":
    effective_branching_factor(52, 9)
