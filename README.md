## ToxVec

Venom is a mixture of substances produced by a venomous organism aiming at preying, defending, or intraspecific competing resulting in certain unwanted conditions for the target organism. Venom sequences are interesting  protein sequences that have evolved independently multiple times throughout the tree of life, making their machine learning-based and BLAST-based identification challenging. Prominent applications in drug discovery and healthcare, while having scarcity of annotations in the protein databases, made automatic identification of venom an important protein informatics task. Most of the existing machine learning approaches rely on engineered features, where the predictive model is trained on top of those manually designed features. Recently, transfer learning and representation learning resulted in significant advancements in many machine learning problem settings by automatically learning the essential features. This paper proposes an approach, called ToxVec, for automatic representation learning of protein sequences for the task of venom identification. We show that pre-trained language model-based representation outperforms the existing approaches in terms of the F1 score of both positive and negative classes achieving the macro-F1 of 0.89. We also show that an ensemble classifier trained over multiple training sets constructed from multiple down-samplings of the negative class instances can substantially improve the macro-F1 score to 0.93, which is 7 percent higher than the state-of-the-art performance.

<image src='toxvec.png'/>


### Installation

'''
pip install -r installation/requirements.txt
''''



### Example Running

'''
python3 toxvec.py --in example_input/input.fasta --out example_input/input_annaotated_by_toxvec.fasta
'''

### Benchmarking

See the benchmarking notebook at:

'''
benchmarkingfiles/
'''
