# Audio to text

from transformers import Pipeline

cls = Pipeline('automatic-speech-recognition')
res=cls('testaudio1.m4a')
print(res)