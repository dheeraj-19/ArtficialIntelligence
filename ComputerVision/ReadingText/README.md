# Reading text

Recognize the text in an image 

– e.g., we have an image that has letters “It is so ordered.” goal is to recognize that this image says “It is so ordered.” 

But the images are noisy, so any particular letter may be difficult to recognize. 
However, if we make the assumption that these images have English words and sentences, we can use statistical properties of the language to resolve ambiguities.

### Assumptions:

    - All the text in our images has the same fixed-width font of the same size. 
      In particular, each letter fits in a box that’s 16 pixels wide and 25 pixels tall
    - Our documents only have the following:
      . 26 uppercase latin characters
      . 26 lowercase characters
      . 10 digits
      . spaces
      . 7 punctuation symbols: (),.-!?’"
      
Suppose we’re trying to recognize a text string with n characters, so we have the following:
- n observed variables (the subimage corresponding to each letter) O1, ..., On 
- n hidden variables, l1..., ln, which are the letters we want to recognize. 

We’re thus interested in P (l1, ..., ln|O1, ..., On)

Using Bayes’ Law, estimate P (Oi|li) and P (li|li−1) from training data, then use probabilistic inference to estimate the posterior, in order to recognize letters.

Program can be run like this:

    python3 ./image2text.py train-image-file.png train-text.txt test-image-file.png

