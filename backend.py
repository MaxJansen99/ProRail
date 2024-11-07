import pandas as pd
from joblib import load
df = pd.read_csv("datamodel.csv")
data= pd.read_csv("Validatieset 2024-2025 Excel.csv")
model = load("LinearRegressionModel.joblib")

def similar_data(oorz_code,geo_mld,stm_techn_mld):
    if len(df.loc[(df['stm_oorz_code'] == oorz_code) & (df['stm_geo_mld'] == geo_mld) & (df['stm_techn_mld'] == stm_techn_mld)]) != 0:
        data=df.loc[(df['stm_oorz_code'] == oorz_code) & (df['stm_geo_mld'] == geo_mld) & (df['stm_techn_mld'] == stm_techn_mld)]
        print(f"gegevens met  oorzaak code:{oorz_code},	Geo code: {geo_mld} en techniekveld: {stm_techn_mld}")
        return len(data),data['targetherstel'].mean(),data['targetherstel'].max(),data['targetherstel'].min()
    elif len(df.loc[(df['stm_oorz_code'] == oorz_code) & (df['stm_geo_mld'] == geo_mld) ]) != 0:
        data = df.loc[(df['stm_oorz_code'] == oorz_code) & (df['stm_geo_mld'] == geo_mld) ]
        print(f"gegevens met  oorzaak code:{oorz_code},	Geo code: {geo_mld}")
        return data['targetherstel'].mean(), data['targetherstel'].max(), data['targetherstel'].min()
    else:
        data = df.loc[(df['stm_oorz_code'] == oorz_code)]
        print(f"gegevens met  oorzaak code:{oorz_code}")
        return data['targetherstel'].mean(), data['targetherstel'].max(), data['targetherstel'].min()

def model(stm_oorz_code,stm_sap_melddatum,stm_sap_meldtijd,stm_aanntpl_tijd,stm_geo_mld,stm_techn_mld, stm_prioriteit):
    d = {'stm_oorz_code': stm_oorz_code, 'stm_sap_melddatum': stm_sap_melddatum,'stm_sap_meldtijd': stm_sap_meldtijd,
         'stm_geo_mld' : stm_geo_mld,'stm_aanntpl_tijd' : stm_aanntpl_tijd,'stm_techn_mld':stm_techn_mld,'stm_prioriteit':stm_prioriteit}

    dataframe = pd.DataFrame(d)

    dataframe['stm_sap_meldtijd'] = pd.to_datetime(dataframe['stm_sap_meldtijd'], format='%H:%M:%S', errors='coerce')
    dataframe['stm_sap_meldtijd'] = dataframe['stm_sap_meldtijd'].apply(lambda x: x.hour * 60 + x.minute)

    dataframe['stm_aanntpl_tijd'] = pd.to_datetime(dataframe['stm_aanntpl_tijd'], format='%H:%M:%S', errors='coerce')
    dataframe['stm_aanntpl_tijd'] = dataframe['stm_aanntpl_tijd'].apply(lambda x: x.hour * 60 + x.minute)

    dataframe['stm_sap_melddatum'] = pd.to_datetime(dataframe['stm_sap_melddatum'], format='%d/%m/%Y')

    dataframe['stm_sap_melddatum'] = dataframe['stm_sap_melddatum'].dt.dayofyear
    dataframe['stm_oorz_code'] = dataframe['stm_oorz_code'].astype('int32')
    dataframe['stm_prioriteit'] = dataframe['stm_prioriteit'].astype('int32')

    dataframe = pd.concat([dataframe, pd.get_dummies(dataframe['stm_oorz_code']).astype(int)], axis=1)
    dataframe = pd.concat([dataframe, pd.get_dummies(dataframe['stm_techn_mld']).astype(int)], axis=1)
    dataframe = pd.concat([dataframe, pd.get_dummies(dataframe['stm_prioriteit']).astype(int)], axis=1)
    dataframe = pd.concat([dataframe, pd.get_dummies(dataframe['stm_geo_mld']).astype(int)], axis=1)

    model = load('LinearRegressionModel.joblib')
    predictions = model.predict(dataframe)
    print(predictions)

pd.set_option('display.max_columns', None)
data=data.loc[[0]]
model(data['stm_oorz_code'],data['stm_sap_melddatum'],data['stm_sap_meldtijd'],data['stm_aanntpl_tijd'],data['stm_geo_mld'],data['stm_techn_mld'],data['stm_prioriteit'])


