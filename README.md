TextMining

.
├── code/
|   ├── model/
|   |   ├── sentiment_analysis/         <- models for sentiment analysis (vader, textblob and flair)
|   |   |   ├── flair_model.py
|   |   |   ├── textblob.py
|   |   |   └── vader.py
|   |   ├── topic_modelling/            <- models for topic modelling (BERT-based and LDA)
|   |   |   ├── bertopic.py
|   |   |   └── LDA.ipynb
|   |   └── __init__.py
|   ├── preprocessing/          
|   |   ├── __init__.py
|   |   └── preprocessing.py
|   ├── scraping/
|   |   ├── __init__.py
|   |   ├── skytrax_scraping.py
|   |   └── tripadvisor_scraping.py     
|   ├── main.py
|   └── postprocessing.ipynb
├── data/                               
├── docs/
├── chromedriver.exe
├── README.md
└── requirements.txt
