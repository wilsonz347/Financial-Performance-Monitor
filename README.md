# Financial-Performance-Monitor (2007-2024)
Financial Performance Monitor (FPM) is an interactive dashboard designed to analyze the U.S. economy over time.

## 📊 Data Sources
This project analyzes economic indicators (GDP, Inflation, and Unemployment) from **2007 to 2024**, obtained from official U.S. government sources:

1. **Gross Domestic Product (GDP)**
   - **Source:** U.S. Bureau of Economic Analysis (BEA)
   - **URL:** [https://www.bea.gov/data/gdp/gross-domestic-product](https://www.bea.gov/data/gdp/gross-domestic-product)
   - **Dataset:** Real GDP (Chained 2017 Dollars)  
   - **Download Method:** BEA interactive data tool → Table 1.1.6  

2. **Inflation Rate (Consumer Price Index - CPI)**
   - **Source:** U.S. Bureau of Labor Statistics (BLS)
   - **URL:** [https://www.bls.gov/cpi/](https://www.bls.gov/cpi/)
   - **Dataset:** CPI-U (All Urban Consumers)
   - **Download Method:** BLS data tool → CPI database  

3. **Unemployment Rate (Total & by Race)**
   - **Source:** U.S. Bureau of Labor Statistics (BLS)
   - **URL:** [https://www.bls.gov/data/](https://www.bls.gov/data/)
   - **Datasets:**
     - Overall Unemployment Rate (LNS14000000)
     - White Unemployment (LNU04000003)
     - Black or African American Unemployment (LNU04000006)
     - Asian Unemployment (LNU04032183)
     - Hispanic or Latino Unemployment (LNU04000009)
   - **Download Method:** BLS "Top Picks" → Labor Force Statistics  

## 📂 Data Preprocessing
The datasets have been preprocessed as follows:

1. **Gross Domestic Product (GDP)**
   - **Cleaning Method:**  
     - Manually cleaned in Microsoft Excel to address formatting issues (e.g., missing values, inconsistencies).  
     - Further cleaned using **pandas** to ensure proper formatting and alignment with other datasets.

2. **Inflation Rate (Consumer Price Index - CPI)** && **Unemployment Rate (Total & by Race)**
   - **Cleaning Method:**  
     - Cleaned manually in Microsoft Excel to fix formatting issues.  
     - Converted to CSV format for merging with other datasets.

3. **Merging Datasets**
   - After cleaning, the datasets (GDP, Inflation, and Unemployment) will be merged based on the time period (2007-2024) for comprehensive analysis.

## 🛠 How to Use
