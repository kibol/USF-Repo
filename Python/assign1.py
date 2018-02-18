from wordtools import*
import string
import numpy

condon_to_protein = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'#', 'TAG':'#',
    'TGC':'C', 'TGT':'C', 'TGA':'#', 'TGG':'W',
    }


def fasta_to_sequence( ):
    dna_sequence_reading = open("fasta.txt",'r')
    dna_sequence = dna_sequence_reading.read().replace('\n','').upper()
    dna_sequence = dna_sequence.split()
    dna_sequence = "".join(dna_sequence)
    dna_sequence = cleanword(dna_sequence)
    return dna_sequence


def sequence_to_protein(dna):
    reading_frame = 1
    protein =""
    while reading_frame <= 3:
     if reading_frame == 1:
      start = 0
      end = start+3
     if reading_frame == 2:
      start = 1
      end = start+3
     if reading_frame == 3:
      start = 2
      end = start+3
     for i in range(len(dna)):
         if dna[start:end] not in condon_to_protein:
            pass                 
         else:
            protein += condon_to_protein[dna[start:end]]
            start += 3
            end += 3
     reading_frame += 1
    return protein


def complement_strand(f_strand):
    comp_strand="" 
    for n in f_strand:
      if n == "T":
        comp_strand +="A"
      elif n == "C":
        comp_strand+="G"
      elif n == "A":
        comp_strand+="T"
      elif n == "G":
        comp_strand += "C"
    return comp_strand

def rev_sequence_to_protein (rev_dna):
    rev_dna = rev_dna[::-1]
    reversed_read_protein = sequence_to_protein(rev_dna)
    return reversed_read_protein

DNA = fasta_to_sequence()
print "Protein From First 3 Reading Frames" '\n'
print sequence_to_protein(DNA), '\n' 
print "Protein From Reversed 3 Reading Frames" '\n'
comp = complement_strand(DNA)
print rev_sequence_to_protein(comp), '\n'
