## ToxVec

Venom is a mixture of substances produced by a venomous organism aiming at preying, defending, or intraspecific competing resulting in certain unwanted conditions for the target organism. Venom sequences are a highly divergent class of proteins making their machine learning-based and homology-based identification challenging. Prominent applications in drug discovery and healthcare, while having scarcity of annotations in the protein databases, made automatic identification of venom an important protein informatics task. Most of the existing machine learning approaches rely on engineered features, where the predictive model is trained on top of those manually designed features. Recently, transfer learning and representation learning resulted in significant advancements in many machine learning problem settings by automatically learning the essential features. This paper proposes an approach, called ToxVec, for automatic representation learning of protein sequences for the task of venom identification. We show that pre-trained language model-based representation outperforms the existing approaches in terms of the F1 score of both positive and negative classes achieving a  macro-F1 of 0.89. We also show that an ensemble classifier trained over multiple training sets constructed from multiple down-samplings of the negative class instances can substantially improve a macro-F1 score to 0.93, which is 7 percent higher than the state-of-the-art performance.


<image src='toxvec.png'/>


## Installation

Please use python 3.x.x to run ToxVec. The requirement for using ToxVec can be installed using the following `pip` command:

```
pip install -r installation/requirements.txt
```

### Download the model files

Besfor running the script you need to download the model files from the following URL and copy them to the models directory

Replace `YYY` with numbers from 1 to 10 to dowload 10 ToxVec models
```
 http://7xr.ir:5000/static/toxvec_model_YYY.bin
```

#### Download Script in Linux
or if you are using a linux\mac os machine call the following scripts to download the models:

```
For Linux:

bash dowload_linux.sh

For Mac OS:

bash dowload_macos.sh

```


## Example Running

```
python3 toxvec.py --in example_input/input.fasta --out example_input/input_annaotated_by_toxvec.fasta
```

The file `example_input/input_annaotated_by_toxvec.fasta` is an example output of ToxVec where the ToxVec has annottated the fatsa.
We used the benchmarking dataset as an example where the `actual_label` is the variable showing the ground truth.
`toxvec_pred` shows the ToxVec prediction.
`toxvec_venom_score` is the portion of models classify this peptide as venom. A peptide is classifed as Venom if and only if this score is 1.
