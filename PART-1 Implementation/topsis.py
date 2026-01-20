import numpy as np
import pandas as pd
import sys
import os


def error(msg):
    print("Error:", msg)
    sys.exit(1)

def convert_excel_to_csv(input_file):
    try:
        df = pd.read_excel(input_file)
        csv_file = input_file.rsplit('.', 1)[0] + ".csv"
        df.to_csv(csv_file, index=False)
        print(f"Converted {input_file} to {csv_file}")
        return csv_file
    except Exception as e:
        error("Failed to convert Excel file to CSV.")



def main():
    if len(sys.argv) != 5:
        error("Incorrect number of parameters.\n""Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        error("Input file not found.")

    file_ext = os.path.splitext(input_file)[1].lower()

    if file_ext == ".csv":
        df = pd.read_csv(input_file)

    elif file_ext in [".xlsx", ".xls"]:
        input_file = convert_excel_to_csv(input_file)
        df = pd.read_csv(input_file)

    else:
        error("Unsupported file format. Only .csv, .xlsx, .xls allowed.")

    

    if df.shape[1] < 3:
        error("Input file must contain at least three columns.")

    data = df.iloc[:,1:]

    try:
        data = data.astype(float)
    except ValueError:
        error("From 2nd to last columns must contain numeric values only.")

    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        error("Number of weights, impacts and columns must be same.")
    
    try:
        weights = np.array([float(w) for w in weights])
    except ValueError:
        error("Weights must be numeric values only.")
    
    for imp in impacts:
        if imp not in ['+', '-']:
            error("Impacts must be either '+' or '-'.")

    norm_data = data / np.sqrt((data ** 2).sum())

    weighted_data = norm_data * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_data.iloc[:, i].max())
            ideal_worst.append(weighted_data.iloc[:, i].min())
        else:
            ideal_best.append(weighted_data.iloc[:, i].min())
            ideal_worst.append(weighted_data.iloc[:, i].max())
    

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    S_plus = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    S_minus = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    topsis_score = S_minus / (S_minus + S_plus)

    df['Topsis Score'] = topsis_score
    df['Rank'] = df['Topsis Score'].rank(ascending=False, method='dense').astype(int)


    df.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully.")
    print("Result saved to:", output_file)

if __name__ == "__main__":
    main()