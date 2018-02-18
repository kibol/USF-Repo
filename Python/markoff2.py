import doctest
import string
import math
import numpy as np
from matrices import*

nt_columns = {'A':0, 'C':1, 'T':2, 'G':3}
state_ref = {0:"S1", 1:"S2", 2:"S3"}

def cleanword(word):
    new_word = ""
    for i in range(len(word)):
        if word[i].isalpha():
           new_word += word[i]
    return new_word

def clean_string():
    """
     The clean_string function is set up to received any FASTA format file
     and clean it and return a DNA or RNA sequence in uppercase
    :return:
    """"""
   dna_sequence_reading = open("fasta.txt",'r')
   dna_sequence = dna_sequence_reading.read().replace('\n','').upper()
   dna_sequence = dna_sequence.split()
   dna_sequence = "".join(dna_sequence)
   dna_sequence = cleanword(dna_sequence)
   return dna_sequence

##def set_matrix was taken from "How to think like a computer
##This function is deviced to create a structure for my vitergi
##aligorithm table. MxN matrix with M is the length of the states
##and N is the length of DNA sequence.
------------------------------------------------------------------------------------------
"""

def set_matrix(rows, columns): 
    matrix = []
    for i in range(rows):
        matrix+= [[0] * columns]
    return matrix



def hmmarkov(seq, matrix, state):
    """
     This fucntion will iniitalize the hidden markov model aligorithm using initial probably and populate
     the rest of the table by using transition, emission and the max probability of the last
     column.  It is also set up to generate.
     ----------------------------------------------------------------------------------------
    :param seq:
    :param matrix:
    :param state:
    :return:
    """
    
    # Initial column of the viterbi
    viterbi = matrix
    j= 0
    while j == 0:
      for i in range(len(matrix)):
        nt = seq[j]
        #print nt
        viterbi[i][j]= initial_prob[i]*emis_prob[i][nt_columns[nt]]
      j+= 1
     
    j = 1
    while j < len(seq):
      for i in range(len(matrix)):
         prev_max = -99
         max_k = 0
         for k in range(len(matrix)):
           col_max = trans_prob[k][i]*viterbi[k][j-1]
           if col_max > prev_max:
             prev_max = col_max
             max_k = k
             nt = seq[j]
         viterbi[i][j]= prev_max*emis_prob[i][nt_columns[nt]]
         state [i][j] = max_k
      j+= 1
    return viterbi, state 


def max_col_index(mat, index_tab, strand):
    # """
    # :param mat:
    # :param index_tab:
    # :param strand:
    # :return:
    
     """
        new_list = []
        state_string= ""
        for i in range(len(mat)):
           new_list +=[mat[i][-1]]
        max_index = 0
        #state_string= ""
        for j in range(len(new_list)):
          #print j  
          if new_list[j] > new_list[max_index]:
            max_index = j
            #print max_index   
        state_string += state_ref[max_index]
        i= max_index
        for k in range(len(strand)-1, 0, -1):
            state_pos = index_tab[i][k]
            state_string = state_ref[state_pos] + state_string
            i= state_pos
            print "????", k
##                print "----", i 
##                print "!!!!", state_string
        return max_index, state_string    

dna_sequence_reading= "CCT"
###dna_sequence_reading = clean_string()
#initial_prob = [.25,.5,.25]
initial_prob1 = [4,8,16]
initial_prob = [ ]
print initial_prob

for elem in initial_prob1:
   initial_prob += [np.log2(elem)]
   print initial_prob[0], initial_prob

##initial_prob = [.3,.2,.5]
#initial_prob = change_to_log (initial_prob)
#print initial_prob
##trans_prob = [[.5,0,.5], [.25,.5,.25],[.1,.4,.5]]
trans_prob = [[.25,.5,.25], [.25,.25,.5],[.5,.0,0]]
##emis_prob = [[.3,.1,.4,.2],[.1,.5,.1,.3],[.25,.25,.25,.25]]
emis_prob = [[1,0,0,0],[.25,.5,0,.25],[.25,.25,.25,.25]]

placeholder_matrix  = set_matrix(len(trans_prob),len(dna_sequence_reading))
max_state = set_matrix(len(trans_prob),len(dna_sequence_reading))
table, max_state = hmmarkov(dna_sequence_reading, placeholder_matrix, max_state)

print table,'\n'
print max_state

print max_col_index(table, max_state, dna_sequence_reading)
"""
"""
Find max of the last column in table(this is the end state) 
store as last state in output string. 
and from now on you are in the max_state
from find the state where it came from 
parallel cell to the winning shows which row it came from. 
go to previous to the previous column of that row and it came from.

[0, 0, 1, 0]
[0, 2, 1, 2]
[0, 2, 2, 0]

[[0.0, 0.0, 0.0]
[0.25, 0.03125, 0.0]
[0.0625, 0.03125, 0.00390625]] "s3"

S2, S2, S3 
"""


    




