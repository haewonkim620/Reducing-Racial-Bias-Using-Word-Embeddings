# **Overview**

This project was created in collaboration by Alejandro Lopez, Junie Hae Won Kim, and Monae McKinney.  
It was based off of the work from [Reducing Gender Bias in Word-Level Language Models with a Gender-Equalizing Loss Function](https://www.aclweb.org/anthology/P19-2031/).  
This projecs allows for: 
> \- Data set preprocessing  
> \- Data set augmentation  
> \- Word embedding training and evaluation  

## Prerequisites
Have Python version 3.6+ installed as well as jupyter notebook.  

## Getting Started
Start by importing your names in csv format, and placing them in `./names/spreadsheets/`. There should be 4 files titled `1wfn` (for white first names), `2bfn` (for black first names), `3wln` (for white last names), and `4bln` (for black last names). The first column for each file should be labeled `Name`, and the second column should be labeled `Count`. The `Count` column corresponds to the frequency of that name given that race.  

Next, import your list of occupations as a txt file, placing them in `./occupations/`, and with each occupation on a new line.  

## Running the code
Start by running `python3 preprocessing.py` in your terminal. This file will strip the corpus of unwanted symbols, make the corpus and occupations lowercase, and create the txt files from the `names` spreadsheets that will be used in the word embeddings. This file also grabs the intersections between the `names` files, finds the proportion of each names frequency by the total frequency of all the names in its file, and allocate those names to the file with the higher frequency for that name.  

Next run `python3 data_augmentation.py` in your terminal. This file will parse through the corpus, and it will swap every instance of a name with a random name from the opposite races name list, e.g. if it comes across the name "John" (typically in the `1wfn`), it will swap it with a random name from `2bfn`, and vice versa. The same is true for the list of last names.  

Finally, open `jupyter notebook training.ipynb` in your terminal, and run all. This will train the word embeddings model, and plot the top 50 occupations found in the corpus against the average of all the cosine similarities of each name with the occupattion for each race.

## File Structure
> * `corpus` - **Ths folder holds both the unaugmented and augmented corpus that is to be trained on**  
>     *  `full` - **This folder contains all of the 20 Mb slices of the full corpus**  
>     * `training_set` - **This folder holds the unaugmented corpus**  
>         * `slice##.txt` - **Each of these numbered slice files are a 20 Mb portion of the full corpus**  
>     * `swapped_training_set` - **This folder holds the augmented corpus**  
>         * `slice##_swapped.txt` - **Each of these numbered slice files are a 20 Mb portion of the full corpus after swapping the names in the respective slice file in `training_set`**  
>     * `enwiki9` - **The full text corpus before being broken up into 20 Mb slices**  
> * `names` - **This folder holds all the text and excel files that store the names that will be swapped**  
>     * `docs` - **This folder holds all the names in txt format**  
>         * `1wfn.txt` - **This file contains all of the white first names in txt format**  
>         * `2bfn.txt` - **This file contains all of the black first names in txt format**  
>         * `3wln.txt` - **This file contains all of the white last names in txt format**  
>         * `4bln.txt` - **This file contians all of the black last names in txt format**  
>     * `spreadsheets` - **This folder holds all the names in csv format**  
>         * `1wfn.csv` - **This file contains all of the white first names in csv format**  
>         * `2bfn.csv` - **This file contains all of the black first names in csv format**  
>         * `3wln.csv` - **This file contains all of the white last names in csv format**  
>         * `4bln.csv` - **This file contains all of the black last names in csv format**  
> * `occupations` - **This folder holds all of the occupations to be trained on**  
>     * `occupations.txt` - **This file holds all the names in txt format**  
> * `README` - **This file**  
> * `data_augmentation.py` - **This performs all of the name swapping in the corpus**  
> * `preprocessing.py` - **This performs all of the tokenization, unwanted symbol stripping, and removal of duplicates throughout the occupations and names files**  
> * `README.md` - **This file**  
> * `training.ipynb` - **This performs al of the word embedding training and evaluation**  

## References
Link to the original paper: <https://www.aclweb.org/anthology/P19-2031/>  
Link to the first billion characters from Wikipedia: <http://mattmahoney.net/dc/textdata.html>