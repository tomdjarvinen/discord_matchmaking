import numpy as np
import unittest

def hungarian_algorithm(S,T,E):
    """
    Assigned to: Beining Ouyang

    Implementation of the Bipartite Graph Formulation of the hungarian algorithm:
    https://en.wikipedia.org/wiki/Hungarian_algorithm#Bipartite_graph_formulation
    :param S: "Worker" List w/ lenth n
    :param T: "Job" List w/ length n
    :param E: Transitions costs matrix; n x n numpy array.
        Position i x j in the matrix defines the transition cost between worker S[i] and job T[j]
        Assumption: E is strictly positive
    :return: List of tuples where each tuple contains a worker from S and a job from T.
        This list should constitute the perfect matching for S, T, and E
    """
    pass

def generate_cost_matrix(S,T,cost_function):
    """
    Given a cost function and a set of workers and jobs, populate a cost matrix
    :param S:
    :param T:
    :param cost_function:
    :return:
    """
    costs = np.zeros([len(S),len(T)])
    for i in range(len(S)):
        for j in range(len(T)):
            costs[i,j] = cost_function(S[i],T[j])
    return costs

class Test_bipartite_graph(unittest.TestCase):

    def test_hungarian_algorithm(self):
        """
        Test hungarian algorithm using example given in:
        https://en.wikipedia.org/wiki/Hungarian_algorithm#Example
        :return:
        """
        workers = ["Paul", "Dave", "Chris"]
        jobs = ["Clean bathroom", "Sweep floors", "Wash windows"]
        pay_rates = np.array([[2,3,3],[3,2,3],[3,3,2]])
        hungarian_solution = hungarian_algorithm(workers,jobs,pay_rates)

        actual_solution = [("Paul","Clean bathroom"),
                           ("Dave","Sweep floors"),
                           ("Chris","Wash windows")]
        self.assertEqual(type(hungarian_solution),list)
        self.assertEqual(len(hungarian_solution),len(actual_solution))
        # Don't care about ordering, so sort solutions
        sort_key = lambda x: x[0]
        hungarian_solution.sort(key=sort_key)
        actual_solution.sort(key=sort_key)
        for i in range(3):
            for j in range(2):
                self.assertEqual(hungarian_solution[i][j],actual_solution[i][j])





if __name__ == '__main__':
    unittest.main()