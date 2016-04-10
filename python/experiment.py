from fill_in_station import *


if __name__ == "__main__":
    result_1 = solve_problem('input', '3_letters_dictionary',
                             'bigram_frequence_list', 'normal_heuristic',
                             False, True, False)
    result_2 = solve_problem('input', '3_letters_dictionary',
                             'bigram_frequence_list', 'advanced_heuristic',
                             False, True, False)

    print "+---------------------+---------------------+--------------------+"
    print "| Heuristic           | Average Time        | Average EBF        |"
    print "+---------------------+---------------------+--------------------+"
    print "| Normal Heuristic    | %10f          | %10f         |" % result_1
    print "+---------------------+---------------------+--------------------+"
    print "| Advanced Heuristic  | %10f          | %10f         |" % result_2
    print "+---------------------+---------------------+--------------------+"
