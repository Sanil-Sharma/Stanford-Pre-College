import json

with open(r"C:\My-Projects\Stanford-Pre-College\Notebook3_SSharma - Copy.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find the %%time cell
for i, cell in enumerate(nb["cells"]):
    if cell["source"] and cell["source"][0].strip() == "%%time":
        print(f"Found %%time cell at index {i}")
        print("Current last 3 lines:", cell["source"][-3:])
        # Remove any trailing lines that are just triple-quotes
        cell["source"] = [line for line in cell["source"] if line.strip() != '"""']
        print("Fixed last 3 lines:", cell["source"][-3:])
        break

with open(r"C:\My-Projects\Stanford-Pre-College\Notebook3_SSharma - Copy.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Done.")
