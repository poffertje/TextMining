# Yelp Reviews

Repository for the Text Mining course at VU Amsterdam 2022

### Environment Setup
```
conda create -n text_mining python=3.7.7
activate text_mining
pip install -r requirements.txt
```

### How to run 


### Structure
```
.
├── application/
|   ├── scraping/
|   |   ├── 
|   |   ├── 
|   |   └──  
├── code/
|   ├── fake_classifier/  
|   |   ├──   
|   |   ├── 
|   |   ├──
|   ├── sentiment_analysis/        
|   |   ├── BERT.ipynb
|   ├── topic_modelling/
|   |   ├── BERTopic.ipynb
|   |   ├── LDA.ipynb
|   ├── preprocessing.ipynb        
├── datasets/
|   ├── YelpZip/
|   |   ├── YelpZip.zip                         <-- unzip the file into the existing folder (supported using git LFS for convinience of the reader)
|   ├── production_set.csv
|   ├── sample_production_set.csv
|   ├── sentiment_sample_25_75.csv              <-- not included because can be obtained from preprocessing notebook (too large to push)
|   ├── sentiment_sample_50_50.csv              <-- not included because can be obtained from preprocessing notebook (too large to push)
├── report/
|   ├── report.pdf
├── README.md
└── requirements.txt
```
