import pandas as pd


def fetchDataset(loc, Model, db):
    csv_reader = pd.read_csv(loc)
    for i in csv_reader.values.tolist():
        db.session.add(Model(*i))
        db.session.commit()
