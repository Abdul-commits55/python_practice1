import os

# List of folders you want to include
folders_to_scan = ["chapter1", "chapter2", "chapter3", "chapter4"]

# Output file name
output_file_name = "merged_code.py"

with open(output_file_name, "w", encoding="utf-8") as outfile:
    for folder in folders_to_scan:
        if os.path.isdir(folder):
            for root, _, files in os.walk(folder):
                for file_name in files:
                    # merge all .py files (change to 'example.py' if you want exactly that file)
                    if file_name.endswith(".py"):
                        full_path = os.path.join(root, file_name)
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as infile:
                            outfile.write(f"\n# ----- Start of {full_path} -----\n")
                            outfile.write(infile.read())
                            outfile.write(f"\n# ----- End of {full_path} -----\n")

print("✅ Done!  Code copied into", output_file_name)
