"""
Demba Sissoko
Hidden Markov Model
"""
from wordtools import *
import numpy as np

nt_columns={'A': 0, 'C': 1, 'T': 2, 'G': 3}
state_ref = {0: "S1", 1: "S2", 2: "S3"}

def clean_string():
    """
     The clean_string function is set up to received any FASTA format file
     and clean it and return a DNA or RNA sequence in uppercase
    :return: A string of nucleotides with all white spaces, numeric value and special characters removed.
     At the end, the function will return a dna or rna sequence in uppercase.

    """
    seq_reading = open("fasta.txt", 'r')
    dna_sequence = seq_reading.read().replace('\n', '').upper()
    dna_sequence = dna_sequence.split()
    dna_sequence = "".join(dna_sequence)
    dna_sequence = cleanword(dna_sequence)
    return dna_sequence

def set_matrix(rows, columns):
    """
    This function will create a placeholder matrix filled with zeros.  Those values will be overwritten with the
    probabilities values obtained from processing thd hidden markov model algorithm.
    :param rows: the number of states.
    :param columns: the length of the sequence to be processed
    :return: a matrix whose dimension depends on the the length of sequence and the number
     of states(length of the transition probability table)
    """
    matrix = []
    for i in range(rows):
        matrix += [[0] * columns]
    return matrix


def hmmarkov(seq, matrix, state):
    """
     This function will initialize the hidden markov model algorithm using some initial probabilities and populate
     the rest of the table by using transition, emission and the max probability of the last
     column.  It is also set up to generate a probability table of the best path and states reference table.
     ----------------------------------------------------------------------------------------
    :param seq: the sequence of protein or nucleotide provided.
    :param matrix: an array with with dimensions determined by the length of the sequence and the
    number of states.
    :param state: the three states that each character can take on.
    :return: will return a array of the best probabilities of the sequence and the state
    """
    viterbi = matrix
    j = 0
    while j == 0:
        for i in range(len(matrix)):
            nt = seq[j]
            # print nt
            viterbi[i][j] = initial_prob[i] + emis_prob[i][nt_columns[nt]]
        j += 1
    j = 1
    while j < len(seq):
        k= 0
        for i in range(len(matrix)):
            prev_max = trans_prob[0][i] + viterbi[k][j-1]
            max_k = 0
            for k in range(len(matrix)):
                col_max = trans_prob[k][i] + viterbi[k][j - 1]
                if col_max > prev_max:
                    prev_max = col_max
                    max_k = k
                    nt = seq[j]
            viterbi[i][j] = prev_max + emis_prob[i][nt_columns[nt]]
            state[i][j] = max_k
            print max_k
        j += 1
    return viterbi, state


def max_col_index(mat, index_tab, strand):
    """
    :param mat:a matrix.  dimension = length of sequence provided, and the number of states(S1, S2, S3)
    :param index_tab: a matrix containing the indices of the best probabilities
    for each state.
    :param strand: the dna or rna sequence provided. data type= string.
    :return: will return the maximum probability generated from the entire iteration through the nucleotide sequence,
     and the best path sequence of the states(based on the best probability of hidden state for each nucleotide.)
    """
    new_list = []
    state_string = ""
    for i in range(len(mat)):
        new_list += [mat[i][-1]]
    max_index = 0  # state_string= ""
    for j in range(len(new_list)):
        # print j
        if new_list[j] > new_list[max_index]:
            max_index = j
            new_list[max_index]
            # print max_index
    state_string += state_ref[max_index]
    i = max_index
    for k in range(len(strand) - 1, 0, -1):
        state_pos = index_tab[i][k]
        state_string = state_ref[state_pos] + state_string
        i = state_pos
    return new_list[max_index], state_string

seq_reading = clean_string()
initial_prob = [.3, .2, .5]
initial_prob = np.log(initial_prob)
trans_prob = [[.5, 0, .5], [.25, .5, .25], [.1, .4, .5]]
trans_prob = np.log(trans_prob)
emis_prob = [[.3, .1, .4, .2], [.1, .5, .1, .3], [.25, .25, .25, .25]]
emis_prob = np.log(emis_prob)
placeholder_matrix = set_matrix(len(trans_prob),len(seq_reading))
max_state = set_matrix(len(trans_prob),len(seq_reading))
table, max_state = hmmarkov(seq_reading, placeholder_matrix, max_state)
best_probability, traceback_seq = max_col_index(table, max_state, seq_reading)

print max_state, '\n'
print best_probability, '\n'
print traceback_seq

