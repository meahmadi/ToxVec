#!/bin/bash
for i in {1..10}
do
   curl -o ./models/toxvec_model_$i.bin http://7xr.ir:5000/static/toxvec_model_$i.bin
done

