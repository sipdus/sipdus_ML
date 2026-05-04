def get_label(df, subject_id):
    row = df[df["ID"] == subject_id]
    
    if row.empty:
        print(f"ID {subject_id} não encontrado")
        return None
    
    return row.iloc[0]