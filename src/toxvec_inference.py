import random
import os
import os.path
from os import path
import codecs
import numpy as np
import fasttext
import tqdm
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import itertools

class ToxVec(object):
    '''
        ToxVec Inference code
    '''
    def __init__(self, path = './models/'):
        # Loading models
        self.model = dict()
        for model_idx in tqdm.tqdm(range(1,11)):
            self.model[model_idx] = fasttext.load_model(F"{path}/toxvec_model_{model_idx}.bin")
    
    def predict(self, sequence):
        '''
            returns the label and the score to be venom
        '''
        three_instances=ToxVec.generate_kmer_seqs(sequence,3)
        score = np.sum([1 if list(itertools.chain(*self.model[model_idx].predict(three_instances)[0])).count('__label__1') > 1 else 0 for model_idx in range(1,11)])
        if score==10:
            return ('Venom', 1)
        else:
            return ('Non-Venom', score/10)
    
    def predict_fasta(self, fasta_file_in, fasta_file_out):
        result_fasta = []
        with open(fasta_file_in, "rU") as handle:
            for record in tqdm.tqdm(SeqIO.parse(handle, "fasta")):
                sequence = str(record.seq)
                class_v, score = self.predict(sequence)
                seq_ID = record.id
                seq_description = F"{record.description} toxvec_pred={class_v} toxvec_venom_score={score} "
                result_fasta.append(SeqRecord(Seq(sequence), id=seq_ID, description=seq_description))
        SeqIO.write(result_fasta, fasta_file_out, "fasta")

    def predict_list(self, sequences):
        return [self.predict(seq) for seq in sequences]
        
    @staticmethod
    def generate_kmer_seqs(sequence, k):
        '''
        :param sentence: sentence t
        :param n: n of n-gram
        :param padding: to pad whitespaces before and after sentence
        :param cookie_cut: generate all ways or only overlapping
        :return:
        '''
        sequence = '##'+sequence.lower() +'@@'
        # generate all ways of n-gram sequences
        sequence = [(sequence[i:i + k]) for i in range(len(sequence) - k + 1)]
        return [' '.join(sequence[i::k]) for i in range(k)]        
            
    @staticmethod
    def save_list(filename, list_names):
        f = codecs.open(filename, 'w', 'utf-8')
        for x in list_names:
            f.write(x + '\n')
        f.close()

    @staticmethod
    def load_list(filename):
        return [line.strip() for line in codecs.open(filename, 'r', 'utf-8').readlines()]
    
    