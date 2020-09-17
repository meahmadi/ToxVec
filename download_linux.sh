#!/bin/bash
for i in {1..10}
do
   wget http://7xr.ir:5000/static/toxvec_model_$i.bin -P ./models/
done

