# Part-of-speech tagging

A basic problem in Natural Language Processing is part-of-speech tagging, in which the goal is to mark every word in a sentence with its part of speech (noun, verb, adjective, etc.)

Sometimes this is easy: a sentence like “Blueberries are blue” clearly consists of a noun, verb, and adjective, since each of these words has only one possible part of speech (e.g., “blueberries” is a noun but can’t be a verb)

But in general, one has to look at all he words in a sentence to figure out the part of speech of any individual word. For example, consider the — grammatically correct! — sentence: “Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.” To figure out what it means, we can parse its parts of speech:

     Buffalo  buffalo  Buffalo  buffalo buffalo buffalo  Buffalo  buffalo
    Adjective   Noun  Adjective   Noun    Verb   Verb   Adjective   Noun
    
(In other words: the buffalo living in Buffalo, NY that are buffaloed (intimidated) by buffalo living in Buffalo, NY buffalo (intimidate) buffalo living in Buffalo, NY.)

That’s an extreme example, obviously. Here’s a more mundane sentence:

    Her position covers  a  number  of  daily  tasks common  to any social director
    DET   NOUN    VERB  DET  NOUN   ADP  ADJ   NOUN    ADJ  ADP DET   ADJ    NOUN
    
where DET stands for a determiner, ADP is an adposition, ADJ is an adjective, and ADV is an adverb

Many of these words can be different parts of speech: “position” and “covers” can both be nouns or verbs, for example, and the only way to resolve the ambiguity is to look at the surrounding words. Labeling parts of speech thus involves an understanding of the intended meaning of the words in the sentence, as well as the relationships between the words.

Fortunately, statistical models work amazingly well for NLP problems.

Consider a simple Bayes net:

This Bayes net has random variables 

    S = {S1,...,SN} and W = {W1,...,WN}. The W’s represent observed words in a sentence. The S’s represent part of speech tags, so Si ∈ {VERB, NOUN, . . .}
    
## Data

    Here we have a large corpus of labeled training and testing data. 
    Each line consists of a sentence, and each word is followed by one of 12 part-of-speech tags: 
    - ADJ (adjective)
    - ADV (adverb)
    - ADP (adposition)
    - CONJ (conjunction)
    - DET (determiner)
    - NOUN
    - NUM (number)
    - PRON (pronoun)
    - PRT (particle)
    - VERB
    - X (foreign word)
    - . (punctuation mark)

## Goal

#### 1. Consider the simplified Bayes net
    
    To perform part-of-speech tagging, we estimate the most-probable tag s∗i for each word Wi  

    s∗i = arg max P(Si = si|W)
    
#### 2. Consider a richer Bayes net

    This incorporates dependencies between words
    Implement Viterbi to find the maximum a posteriori (MAP) labeling for the sentence
    
    (s∗1,...,s∗N) = arg max P(Si = si|W)
 
#### 3. Consider an even richer Bayes Net

    This incorporates richer dependencies between words. But it’s not an HMM, so we can’t use Viterbi.
    We use Gibbs Sampling to sample from the posterior distribution P(S|W). 
    Then estimate the best labeling for each word (by picking the maximum marginal for each word, s∗i = arg max P (Si = si |W ) 
    (To do this, just generate thousands of samples and, for each individual word, check which part of speech occurred most often.)
    
    
    
    
    
    
