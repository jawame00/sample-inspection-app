import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def process_csv(samples_path, standards_path, output_path="result.csv"):
    samples = pd.read_csv(samples_path)
    standards = pd.read_csv(standards_path)

    merged = samples.merge(standards, on="law", how="left")
    merged["is_exceeded"] = merged["value"] > merged["standard"]

    merged.to_csv(output_path, index=False)

def select_samples():
    path = filedialog.askopenfilename(
        title="検体CSVを選択",
        filetypes=[("CSV files", "*.csv")]
    )
    samples_var.set(path)

def select_standards():
    path = filedialog.askopenfilename(
        title="基準値CSVを選択",
        filetypes=[("CSV files", "*.csv")]
    )
    standards_var.set(path)

def run_process():
    samples_path = samples_var.get()
    standards_path = standards_var.get()

    if not samples_path or not standards_path:
        messagebox.showerror("エラー", "CSVを両方選択してください")
        return

    try:
        process_csv(samples_path, standards_path)
        messagebox.showinfo("完了", "判定が完了しました\nresult.csv を確認してください")
    except Exception as e:
        messagebox.showerror("エラー", str(e))

root = tk.Tk()
root.title("分析判定アプリ（CSV版）")

samples_var = tk.StringVar()
standards_var = tk.StringVar()

tk.Label(root, text="検体CSV").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=samples_var, width=40).grid(row=0, column=1)
tk.Button(root, text="選択", command=select_samples).grid(row=0, column=2)

tk.Label(root, text="基準値CSV").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=standards_var, width=40).grid(row=1, column=1)
tk.Button(root, text="選択", command=select_standards).grid(row=1, column=2)

tk.Button(root, text="判定実行", command=run_process, width=20).grid(row=2, column=1, pady=10)

root.mainloop()