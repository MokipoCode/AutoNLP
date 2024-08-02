import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('austinreese/craigslist-carstrucks-data', path='data/', unzip=True)