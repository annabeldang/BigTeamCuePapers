import os

folders = [
    (
        r"/Users/beheo/Desktop/GitHub/BigTeamCuePapers/BT_NT_PDFs",
        "abstract_",
        1
    ),
    (
        r"/Users/beheo/Desktop/GitHub/BigTeamCuePapers/ST_NT_PDFs",
        "abstract_",
        51
    ),
    (
        r"/Users/beheo/Desktop/GitHub/BigTeamCuePapers/BT_TS_PDFs",
        "abstract_",
        101
    ),
    (
        r"/Users/beheo/Desktop/GitHub/BigTeamCuePapers/ST_TS_PDFs",
        "abstract_",
        151
    ),
]

for folder, new_prefix, start_num in folders:

    print(f"\n--- {folder} ---")

    files = sorted([
        f for f in os.listdir(folder)
        if f.lower().endswith(".pdf")
    ])

    if not files:
        print("No PDF files found.")
        continue

    rename_pairs = []

    for i, old_name in enumerate(files):

        new_number = start_num + i
        new_name = f"{new_prefix}{new_number:03d}.pdf"

        rename_pairs.append((old_name, new_name))

        print(f"  {old_name}  ->  {new_name}")

    confirm = input("\nProceed? (yes/no): ").strip().lower()

    if confirm == "yes":

        for old_name, new_name in rename_pairs:

            old_path = os.path.join(folder, old_name)
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)

        print("Done!")

    else:
        print("Cancelled — no files were changed.")