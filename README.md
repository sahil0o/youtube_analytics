# Project Setup Instructions

1) **YouTube Data API Key:**
   This project uses the YouTube Data API. To obtain your API key:
   - Create an account on [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project, then go to **APIs & Services** and search for **YouTube Data API v3**.
   - Enable the API and generate your credentials (API key).

2) **Create a `config.py` file:**
   In the project directory, create a `config.py` file with the following content:
   ```python
   from googleapiclient.discovery import build

   api_key = 'insert your API key here'
   youtube = build('youtube', 'v3', developerKey=api_key)
You will not be able to run the code without creating this file and inserting your API key. 

3) **Functions:**
   The necessary functions for the project are located in the `functions` folder. The `creator_analytics.ipynb` file includes inline documentation explaining the role of each function.
   
4) **Analysis Notebook:**
   Go through the `creator_analytics.ipynb` notebook to understand the analysis that can be performed. Please be aware that the API has a limited quota, so use it wisely.
   - You can check your daily quota on the [Google Cloud Console home page](https://console.cloud.google.com/).
   - The quota costs for various requests can be found [here](https://developers.google.com/youtube/v3/determine_quota_cost).

   For further analysis and more endpoints, visit the YouTube Data API references page:  
   [YouTube Data API Documentation](https://developers.google.com/youtube/v3).

5) **Clone the repository:**
   To get started, clone this repository using:
   ```bash
   git clone <repository-url>

Make sure to replace `<repository-url>` with the actual URL of your repository when you use it!

6) 6) **Install dependencies:**
   After cloning the repository, install the necessary packages by running:
   ```bash
   pip install -r requirements.txt

