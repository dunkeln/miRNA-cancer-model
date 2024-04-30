# Cancer Prognosis from tumor cells @TCGA


### Selection

*from tumor tissue of alive patients*

experimental strategy: miRNA-Seq
data type: miRNA expression classification
data category: transcription profiling
workflow: BCGSC miRNA profiling

### df info

genes: 1881
after log normalization: 548


### picked siamese net

**why?**
+ one-shot learning
+ can learn on newly introduced miRNAs for other types of cancers



### References
+ [inception-v2 paper](inceptionv2)
+ [siamese-network](siamese-one-shot)


[inceptionv2]: https://arxiv.org/abs/1502.03167v3
[siamese-network]: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf 
