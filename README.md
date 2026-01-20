## Project Overview

This project provides a complete Python implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method, a widely used multi-criteria decision-making technique for ranking alternatives based on their closeness to an ideal solution.

The TOPSIS algorithm has been packaged as a **Python library** and published on **PyPI**, allowing users to easily install and execute it using a **command-line interface (CLI)**. The package supports CSV and Excel input files, validates weights and impacts, and generates an output file containing TOPSIS scores and ranks.

In addition, a **web-based application** was developed to demonstrate TOPSIS as a web service. The web interface allows users to upload input files, specify weights and impacts, and obtain the result file through a user-friendly webpage, showcasing real-world deployment of the algorithm.


## Input Requirements

- Input file must contain **three or more columns**
- **First column** must contain alternative names (non-numeric)
- **Second to last columns** must contain **numeric values only**
- Number of **weights**, **impacts**, and **criteria columns** must be equal
- Impacts must be:
  - `+` for benefit criteria
  - `-` for cost criteria
- Weights and impacts must be **comma-separated**
- Weights need not be normalized (handled internally)

---

## Input File Format (data.csv)

Each row represents an alternative, and each column (except the first) represents
a decision criterion such as Correlation, R², RMSE, Accuracy, etc.

Example:

| Model | Corr | Rseq | RMSE | Accuracy |
|------:|-----:|-----:|-----:|---------:|
| M1 | 0.79 | 0.62 | 1.25 | 60.89 |
| M2 | 0.66 | 0.44 | 2.89 | 63.07 |
| M3 | 0.56 | 0.31 | 1.57 | 62.87 |
| M4 | 0.82 | 0.67 | 2.68 | 70.19 |
| M5 | 0.75 | 0.56 | 1.30 | 80.39 |


---

## Output File Format (result.csv)

For weights "1,2,1,1" and impacts "+,-,-,+", the output file will contain two
additional columns: **Topsis Score** and **Rank**.

## Example Output

| Model | Corr | Rseq | RMSE | Accuracy | Topsis Score | Rank |
|------:|-----:|-----:|-----:|---------:|-------------:|-----:|
| M1 | 0.79 | 0.62 | 1.25 | 60.89 | 0.423744391359611 | 4 |
| M2 | 0.66 | 0.44 | 2.89 | 63.07 | 0.467426368298297 | 3 |
| M3 | 0.56 | 0.31 | 1.57 | 62.87 | 0.760230957034903 | 1 |
| M4 | 0.82 | 0.67 | 2.68 | 70.19 | 0.207772533881566 | 5 |
| M5 | 0.75 | 0.56 | 1.30 | 80.39 | 0.504864457803718 | 2 |


---

## Description of Output

- **Topsis Score**: Relative closeness of the alternative to the ideal solution  
- **Rank**: Rank based on TOPSIS score (1 = best alternative)

---

## License

This project is developed for academic purposes.
