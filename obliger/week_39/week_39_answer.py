import pandas as pd
from pathlib import Path
from datetime import datetime


def organize_psa_data(csv_path, project_root="psa_project"):
    # Sorts PSA data by study/patient and saves files.
    df = pd.read_csv(csv_path)

    root = Path(project_root)
    root.mkdir(exist_ok=True)


    df["unique_id"] = df["study_id"] + "_" + df["patient_id"].astype(str).str.zfill(4)

    df["surgery_date"] = pd.to_datetime(df["surgery_date"])
    df["psa_date"] = pd.to_datetime(df["psa_date"])

    for study, study_df in df.groupby("study_id"):
        study_folder = root / study
        study_folder.mkdir(exist_ok=True)

        summary_rows = []

        for uid, patient_df in study_df.groupby("unique_id"):
            patient_folder = study_folder / uid
            patient_folder.mkdir(exist_ok=True)

            patient_df_sorted = patient_df.sort_values("psa_date")
            patient_df_sorted.to_csv(patient_folder / f"{uid}_records.csv", index=False)

            dob = patient_df["date_of_birth"].iloc[0]
            surgery = patient_df["surgery_date"].iloc[0]
            follow_up_days = (patient_df["psa_date"].max() - surgery).days
            n_psa = len(patient_df)

            summary_rows.append({
                "unique_id": uid,
                "date_of_birth": dob,
                "surgery_date": surgery.date(),
                "follow_up_days": follow_up_days,
                "number_of_psa_measurements": n_psa,
                "patient_folder_path": str(patient_folder.relative_to(root))
            })

        pd.DataFrame(summary_rows).to_csv(study_folder / f"{study}_summary.csv", index=False)


#oppgave 2


def build_sequencing_manifest(seq_folder, project_root="psa_project"):
    # Extracts study/patient IDs from VCF headers and saves a manifest.
    seq_folder = Path(seq_folder)
    root = Path(project_root)

    manifest = []

    for file in seq_folder.glob("*.vcf"):
        study_id = None
        patient_id = None

        # Les kun header-linjer
        with file.open() as f:
            for line in f:
                if not line.startswith("##"):
                    break
                if line.startswith("##study_id="):
                    study_id = line.strip().split("=")[1]
                if line.startswith("##patient_id="):
                    patient_id = line.strip().split("=")[1]

        if study_id and patient_id:
            uid = f"{study_id}_{str(patient_id).zfill(4)}"
            manifest.append({
                "unique_id": uid,
                "study_id": study_id,
                "patient_id": patient_id,
                "sequencing_file_path": str(file.relative_to(root))
            })

    pd.DataFrame(manifest).to_csv(root / "sequencing_manifest.csv", index=False)