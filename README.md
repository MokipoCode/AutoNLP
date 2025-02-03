# AutoNLP
This project serves as a portfolio to showcase what I know/like to do

## Project Structure
TBD

## Data Source

The data used in this project is sourced from Kaggle:

- **Used Car Dataset**: [Kaggle - Vehicles listings from Craigslist.org from Austin Reese](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)

## Features

- **Data Fetching**: Fetch data from APIs or databases.
- **Data Exploration**: Explore the data to understand its structure and content.
- **Data Cleaning**: Clean the data to make it usable.
- **Data Visualization**: Visualize the data for better understanding.
- **NLP Exploration**: Use NLP techniques to analyze textual data.
- **Conversational Assistant**: Create a conversational assistant capable of answering questions about the data using Transformers.

## Installation

```bash
git clone https://github.com/MokipoCode/tmp_projet.git
python -m venv [yourvenvname]
activate venv 
pip install -r requirements.txt
```


## Usage
- Download to [data folder](data/) the file from the [dataset](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) or use [data_fetching](src/data_fetching.py)
- Use [data_processing](src/data_processing.py)


## To-Do List

1. **Data Fetching**
   - ✔️ Find a data source
   - ✔️ Get the data

2. **Data Exploration**
   - ✔️ Write [data_explo notebook](notebooks\data_explo.ipynb) to explore the data
      - `ongoing` Explore the data
      - ✔️ Find some interesting questions to answer
      - ✔️ Write functions to correct/delete unwanted data

3. **Data Cleaning**
   - ✔️ Write [data_processing script](src\data_processing.py)

4. **Data Visualization**
   - `next step` Some visualizations to illustrate the cleaned data in [data_visu notebook](notebooks\data_visu.ipynb)
      - ✔️ Basic questions and charts
      - ✔️ Correlations
      - [ ] NER exploration (available in [NER notebook](notebooks\NER.ipynb))

6. **Conversational Assistant**
   - [ ] Think about how to create it
   - [ ] Write and test it

8. **Documentation**
   - [ ] Create detailed documentation in the `docs/` directory.
   - [ ] Document the overall project structure and usage.

<!-- Note: venv_project\Scripts\activate -->
