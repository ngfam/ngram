# N-gram language model

The implementation of N-gram language model using Kneser-Ney smoothing. 
I did not figure out how to deal with the 0s of C(prefix, word), therefore Laplace Smoothing was also applied. 

The average number of characters in an English word is 4.3 so I made a guess that using Trie Data Structure would give a better performance than using map() (red black tree based) on large to very large corpuses.

## Usage

As far as I know, Smoothing solutions are mostly used for evaluating models. This project was implemented to estimate the perplexity of Kneser-Ney and Laplace smoothing solutions only.

Put the training set corpus in ```training_set.txt``` and testing set corpus in ```testing_set.txt```. 
You are all set at this point, run this command in terminal to get the result:

```bash
python model.py
```
