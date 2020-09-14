import argparse
import os
import os.path
import sys
from src.toxvec_inference import ToxVec

def checkArgs(args):
    err = "";
    # Using the argument parser in case of -h or wrong usage the correct argument usage
    # will be prompted
    parser = argparse.ArgumentParser()

    def file_choices(choices,fname):
        ext = os.path.splitext(fname)[1][1:]
        if ext not in choices:
            parser.error("file doesn't end with one of {}".format(choices))
        return fname


    # input file #################################################################################################
    parser.add_argument('--in', action='store', dest='input_fasta', type=lambda s:file_choices(("txt","fasta"),s),
                        help='input fasta file of the protein sequences .txt or .fasta')

    # output file #######################################################################################################
    parser.add_argument('--out', action='store', dest='output_fasta', type=lambda s:file_choices(("txt","fasta"),s),
                        help='output fasta file of the protein sequences .txt or .fasta')

    parsedArgs = parser.parse_args()

    if (not os.access(parsedArgs.input_fasta, os.F_OK)):
        err = err + "\nError: Permission denied or could not find the input fasta file!"
        return err
    try:
        print('Loading the models..')
        toxvec = ToxVec('./models/')
        print('Predicting the given fasta')
    except:
        print ('error occured')
    toxvec.predict_fasta(parsedArgs.input_fasta, parsedArgs.output_fasta)
    

if __name__ == '__main__':
    err = checkArgs(sys.argv)
    if err:
        print(err)
        exit()

    