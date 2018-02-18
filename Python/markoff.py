####from wordtools import*
####import string
import math
import numpy
####from matrices import*
##
nt_columns = {'A':0, 'C':1, 'T':2, 'G':3}
##
##trp ={(0, 0): .5, (0, 1): 0,(0, 2):.5,
##      (1, 0): .25,(1, 1):.5,(1, 2):.25,
##      (2, 0): .1, (2, 1):.4,(2, 2):.5}
##
#### The clean_string function is set up to received any FASTA format file
#### and clean it and return a DNA or RNA sequence in uppercase
####def clean_string( ):
####    #dna_sequence_reading = open("fasta.txt",'r')
####    dna_sequence = dna_sequence_reading.read().replace('\n','').upper()
####    dna_sequence = dna_sequence.split()
####    dna_sequence = "".join(dna_sequence)
####    dna_sequence = cleanword(dna_sequence)
####    return dna_sequence
##
#### def set_matrix was taken from "How to think like a computer
#### This function is deviced to create a structure for my vitergi
#### aligorithm table. MxN matrix with M is the length of the states
#### and N is the length of DNA sequence.


def set_matrix(rows, columns): 
    matrix = []
    for i in range(rows):
        matrix+= [[0] * columns]
    return matrix
##

def hmmarkov(seq, matrix):
    viterbi = matrix
    j= 0
    while j == 0:
     for i in range(len(matrix)):
       #print seq[j]
       nt = seq[j]
       viterbi[i][j]= initial_prob[i]*emis_prob[i][nt_columns[nt]]
     j+= 1   
     print viterbi 
    
    j= 1
    while j < len(seq):
     max_table = []
     for i in range(len(matrix)):
         prev_max = -99
         max_k = []
         for k in range(len(matrix)):
           col_max = trans_prob[k][i]*viterbi[k][j-1]
           #print col_max
           if col_max > prev_max:
             prev_max = col_max
             max_k = k
             #print seq[j]
             #print j
             nt = seq[j]
             print nt
             viterbi[i][j]= prev_max*trans_prob[i][k]*emis_prob[i][nt_columns[nt]]
             max_table += (prev_max, max_k)
     j+= 1
    print viterbi,'\n'
    print max_table,'\n'
    return max_table


##def max_index(tup_list):
##    max_ref = []
##    for i in tup_list:
##       max_ref = tup_list[i][1]
##    return max_ref
##      


##def change_to_log(listing):
##    ip = []
##    for i in listing and j in :
##        for j in listing[i]:
##         ip = [math.log(listing[i][j])]
##    return ip



dna_sequence_reading= "ACTG"
#initial_prob = [.3,.2,.5]
initial_prob = [.25, .5, .25]
#trans_prob = [[.5,0,.5], [.25,.5,.25],[.1,.4,.5]]
trans_prob = [[.25,.5,.25], [.25,.25,.5],[.5,.0,0]]
##log = change_to_log([[2,4,5,7], [4,3,2,5]])
#emis_prob = [[.3,.1,.4,.2],[.1,.5,.1,.3],[.25,.25,.25,.25]]
emis_prob = [[1,0,0,0],[.25,.5,0,.25],[.25,.25,.25,.25]]
placeholder_matrix  = set_matrix(len(trans_prob),len(dna_sequence_reading))
#print placeholder_matrix
table = hmmarkov(dna_sequence_reading, placeholder_matrix)
print table
##tuple_list = max_index(table)
##print tuple_list
##print log

##The for every iteration get the max of the i-1 of the current i and use it
### in the max(vertibi[i-1])*trans_prob*
##prev_max = 0
##max_col = max(viterbi[i][j])
##if max_col > prev_max
##prev_max = max_col
