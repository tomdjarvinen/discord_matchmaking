import numpy as np

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