# SpaceX Falcon 9 First Stage Landing Prediction

A comprehensive data science project that predicts the success of SpaceX Falcon 9 first-stage landings using machine learning. This prediction has profound economic implications, as each successful landing can save approximately $28 million in launch costs.

## 🚀 Project Overview

SpaceX advertises Falcon 9 rocket launches at $62 million, significantly undercutting competitors who charge upwards of $165 million. This cost advantage stems from SpaceX's ability to reuse the first stage of their rockets. By predicting landing success, we can estimate launch costs and help alternative companies compete more effectively in the commercial space industry.

This project explores the economics of reusable rockets by building predictive models that achieve **83.3% accuracy** in determining whether a Falcon 9 first stage will successfully land.

## 📊 Key Results

- **Accuracy**: 83.3% prediction accuracy across multiple ML models
- **Data Processed**: 90+ SpaceX launch records from API and web scraping
- **Economic Impact**: $28M potential cost savings per successful landing prediction
- **Launch Sites Analyzed**: 4 different launch sites with 100+ launch records
- **Payload Range**: 0-15,600 kg analyzed for correlation with landing success

## 🎯 Objectives

1. Collect comprehensive SpaceX launch data through API requests and web scraping
2. Perform exploratory data analysis to identify factors affecting landing success
3. Create interactive visualizations to understand launch patterns
4. Build and compare multiple classification models
5. Optimize models to achieve the highest prediction accuracy

## 📁 Project Structure

```
SpaceX-Falcon-9-first-stage-Landing-Prediction/
├── Complete the Data Collection API Lab.ipynb
├── Complete the Data Collection with Web Scraping lab.ipynb
├── Data Wrangling.ipynb
├── Complete the EDA with SQL.ipynb
├── EDA with Visualization Lab.ipynb
├── Interactive Visual Analytics with Folium lab.ipynb
├── Complete the Machine Learning Prediction lab.ipynb
├── Building Plotly Dashboard/
│   └── spacex-dash-app.py
├── Spacex.csv
├── ds-capstone-ppt-coursera.pdf
└── README.md
```

## 🛠️ Technologies Used

### Programming & Data Science
- **Python 3.8+** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning models and preprocessing

### Data Collection
- **Requests** - API data collection from SpaceX API
- **BeautifulSoup** - Web scraping for additional launch data

### Visualization
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive charts and dashboards
- **Folium** - Interactive geospatial maps
- **Dash** - Web-based dashboard application

### Database & Analysis
- **SQLite** - SQL-based exploratory data analysis

### Machine Learning Models
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree Classifier**
- **K-Nearest Neighbors (KNN)**

## 📈 Methodology

### 1. Data Collection
- **API Collection**: Retrieved launch data from SpaceX REST API
- **Web Scraping**: Scraped additional historical launch data from Wikipedia
- **Data Sources**: Combined multiple sources for comprehensive dataset

### 2. Data Wrangling
- Handled missing values and data inconsistencies
- Feature engineering and data transformation
- Achieved 94% dataset completeness across 17 features
- Created binary classification target (successful vs unsuccessful landing)

### 3. Exploratory Data Analysis (EDA)
- **SQL Analysis**: Queried 100+ launch records across 4 launch sites
- **Statistical Analysis**: Identified correlations between payload mass and landing success
- **Visualization**: Created 12+ statistical visualizations to understand patterns
- Analyzed temporal trends in landing success rates

### 4. Interactive Visual Analytics
- Built interactive Folium maps showing launch site locations
- Visualized proximity to geographical features
- Created marker clusters for launch outcomes
- Generated Plotly dashboard for dynamic data exploration

### 5. Machine Learning Modeling
- Trained and compared 4 classification algorithms
- Performed hyperparameter tuning using GridSearchCV
- Cross-validation to ensure model reliability
- Evaluated models using accuracy, precision, recall, and F1-score

## 🎓 Key Insights

1. **Payload Mass Correlation**: Launch success rates show correlation with payload mass in the 0-15,600 kg range
2. **Launch Site Performance**: Different launch sites show varying success rates
3. **Temporal Trends**: Landing success has improved significantly over time as SpaceX refined their technology
4. **Orbit Type Impact**: Certain orbit types have higher landing success rates
5. **Model Performance**: All models achieved similar accuracy (~83%), with SVM and Decision Trees performing slightly better

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package installer)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SindhuraShankeshi/SpaceX-Falcon-9-first-stage-Landing-Prediction.git
cd SpaceX-Falcon-9-first-stage-Landing-Prediction
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

### Usage

#### Run Jupyter Notebooks
```bash
jupyter notebook
```

Navigate through the notebooks in order:
1. Data Collection (API & Web Scraping)
2. Data Wrangling
3. EDA with SQL
4. EDA with Visualization
5. Interactive Visual Analytics
6. Machine Learning Prediction

#### Run Plotly Dashboard
```bash
cd "Building Plotly Dashboard"
python spacex-dash-app.py
```
Then open your browser to `http://127.0.0.1:8050/`

## 📊 Dashboard Features

The interactive Plotly dashboard includes:
- **Launch Site Selection**: Dropdown to filter by launch site
- **Payload Range Slider**: Interactive payload mass range selection
- **Success Rate Pie Chart**: Visual breakdown of success vs failure
- **Scatter Plot**: Correlation between payload mass and launch outcome
- **Color-coded Results**: Visual distinction between successful and failed launches

## 🔍 Model Performance

| Model | Accuracy | Notes |
|-------|----------|-------|
| Logistic Regression | 83.3% | Good baseline performance |
| SVM | 83.3% | Robust with optimal hyperparameters |
| Decision Tree | 83.3% | Best interpretability |
| KNN | 83.3% | Competitive performance |

All models were evaluated using:
- Confusion Matrix
- Classification Report (Precision, Recall, F1-Score)
- Cross-validation scores

## 📝 Requirements

Create a `requirements.txt` file with:
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
requests>=2.26.0
beautifulsoup4>=4.9.0
folium>=0.12.0
plotly>=5.0.0
dash>=2.0.0
sqlalchemy>=1.4.0
jupyter>=1.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Sindhura Patel Shankeshi**
- Email: sindhuraa05@gmail.com
- LinkedIn: [linkedin.com/in/sindhura05](https://linkedin.com/in/sindhura05)
- GitHub: [github.com/SindhuraShankeshi](https://github.com/SindhuraShankeshi)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **SpaceX** for providing public API access to launch data
- **IBM Data Science Professional Certificate** for project guidance
- **Coursera** for the capstone project framework
- Open source community for the amazing tools and libraries

## 📚 References

- [SpaceX REST API](https://api.spacexdata.com)
- [SpaceX Wikipedia](https://en.wikipedia.org/wiki/SpaceX)
- [Falcon 9 Wikipedia](https://en.wikipedia.org/wiki/Falcon_9)

---

⭐ **Star this repository** if you found it helpful!

🚀 **Happy Coding!**
