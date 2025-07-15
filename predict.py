WieIsMax.nl
wieismax.nl
Online

WieIsMax.nl — 08-07-2025, 11:54
Of staat dat allemaal in de notebook
En is die gepushed?
Yujian — 08-07-2025, 11:57
nog niet
'stm_sap_melddatum','stm_geo_mld','stm_aanntpl_tijd','stm_fh_dd','stm_fh_tijd','stm_techn_mld','stm_prioriteit','stm_progfh_in_tijd','stm_contractgeb_mld'
WieIsMax.nl — 09-07-2025, 09:59
https://teams.microsoft.com/meet/3504594619456?p=MMxS5b9IUwDmkgwWrR
Microsoft Teams
Join meeting on Teams
Afbeelding
Afbeelding
Yujian — 09-07-2025, 11:25
ik heb gepust
mis nog wel wat uitleg
WieIsMax.nl — 09-07-2025, 11:29
Top
analyse_en_model.ipynb

Is dit de notebook?
Yujian — 09-07-2025, 11:32
ja
csv is te groot
ik kan nergens sturen
moet je misschien bij canvas even kijken
WieIsMax.nl
 heeft een gesprek gestart dat 6 minuten duurde. — 10-07-2025, 10:01
Yujian — 10-07-2025, 12:25
ik heb nu een aparte jupyternotebook gepushed
waar ik filter aangepast en linearregressie model bij gezet heb.
WieIsMax.nl — 10-07-2025, 17:11
data[['stm_sap_meldtijd', 'stm_aanntpl_tijd', 'stm_fh_tijd','stm_fh_duur']]


Dit worden de uiteindelijke features toch?
Yujian — 10-07-2025, 17:32
dat is voor linearregressie
Andere features dat ik dummie maakt kun je ook gebruiken
WieIsMax.nl — 10-07-2025, 17:35
data=df[[
    'stm_oorz_code', 'stm_sap_melddatum', 'stm_sap_meldtijd', 'stm_geo_mld',
    'stm_aanntpl_tijd', 'stm_fh_tijd', 'stm_techn_mld', 'stm_prioriteit',
    'stm_contractgeb_mld', 'stm_fh_duur', 'stm_progfh_in_duur', 'stm_progfh_in_tijd'
]]

Ah oke dus dan moet ik opnieuw kijken vanuit deze
Yujian — 10-07-2025, 17:37
ja
letop dat stm_fh_duur en stm_fh_tijd niet moet gebruiken
WieIsMax.nl — 10-07-2025, 17:40
Nee dat worden de targets toch
de stm_fh_duur in ieder geval 
Yujian — 10-07-2025, 18:03
target is iets ander
Je kunt bij kopje target zien
WieIsMax.nl — 10-07-2025, 19:25
Oh ja ik zie het
Yujian — 12-07-2025, 21:49
ik had iets verkeerd gepushed en wilde terug naar ouwe versie zetten. naar heeft nu een verkeerde versie gepakt
Afbeelding
ik kan de nieuwste versie niet meer terug vinden, ik heb mijn gedeelte van de code nog
Yujian — gisteren om 08:37
hoelaat spreken we af？
WieIsMax.nl — gisteren om 08:40
11 of 12?
Yujian — gisteren om 08:40
op school？
WieIsMax.nl — gisteren om 08:40
En heb trouwens ook nog wat van de notebooks dus we kunnen zo wel kijken wat we terug kunnen krijgen
WieIsMax.nl — gisteren om 08:40
Ja lijkt mij nu wel handig
Alles samenvoegen
En adviesrapport
Yujian — gisteren om 08:41
ok
dan 11 bij school？
WieIsMax.nl — gisteren om 08:41
Is goed
Yujian — gisteren om 08:42
tot straks
WieIsMax.nl — gisteren om 08:46
Tot straks
WieIsMax.nl — gisteren om 10:54
Zullen we zo op de 1e verdieping bij de grote trap zitten boven?
Yujian — gisteren om 10:57
Prima, ik ben er bijna
Yujian — gisteren om 12:07
'tijd_verschil_meld_aanntpl', 'is_werkdag',
                        'uur_van_dag', 'is_spitsuur','stm_oorz_code', 'stm_geo_mld', 'stm_techn_mld', 'stm_contractgeb_mld'
WieIsMax.nl — gisteren om 12:07
tijd_verschil_meld_aanntpl','is_werkdag',
                        'uur_van_dag', 'is_spitsuur','stm_oorz_code', 'stm_geo_mld', 'stm_techn_mld', 'stm_contractgeb_mld'
WieIsMax.nl — gisteren om 20:43
Ik heb wat van het adviesrapport gepushed. Ik heb alles tot en met het business understanding deel verbeterd.
Yujian — 10:21
ik heb mijn bus niet gehaalt ben wat later
WieIsMax.nl — 10:41
Is goed
Yujian — 11:52
data = {
        'stm_sap_melddatum': 131,
        'stm_sap_meldtijd': 561,
        'stm_aanntpl_tijd': 608,
        'stm_progfh_in_duur': 52,
        'stm_prioriteit': 2,
        'stm_oorz_code': 218,
        'stm_contractgeb_mld': 4,
        'stm_techn_mld_encoded': 10  # Zorg dat dit een numerieke waarde is (geen string zoals 'S')
    }
Yujian — 13:27
2.2.2
vaak zijn er hoge vreemde data, ook zijn er gebrekte data waar Nan's staan.
Yujian — 14:07
{'A': 0, 'B': 1, 'E': 2, 'G': 3, 'I': 4, 'K': 5, 'M': 6, 'O': 7, 'P': 8, 'S': 9, 'T': 10, 'X': 11, nan: 12}
{'stm_prioriteit': <IntegerArray>
 [2, 4, 5, 1]
 Length: 4, dtype: Int64,
 'stm_oorz_code': <IntegerArray>
 [215, 225, 143, 221, 218, 133, 145, 226, 235, 219, 147, 214, 240, 203, 213,
  132, 228, 184, 140, 222, 149, 154, 230, 299, 212, 207, 201, 223, 151, 135,
  209, 298, 146, 241, 227, 210, 208, 183, 185, 186,   0, 148, 211, 220, 144,
  204, 181, 182, 150, 187, 142, 224, 294, 234, 229, 188, 242, 134, 231, 250,
  131, 206, 141, 136, 189, 239, 205, 130, 202, 999, 233,  33, 180]
 Length: 73, dtype: Int64,
 'stm_contractgeb_mld': <IntegerArray>
 [ 0, 26, 25,  5,  2, 24, 18, 20, 27,  1, 19,  8, 30, 34, 10, 11, 32, 23,  6,
   9,  3, 29, 36,  4, 31, 21, 12, 35, 16,  7, 81, 33, 14, 37, 13, 22, 28, 15,
  71, 56, 99, 62, 60, 64, 17, 61, 58, 52, 53, 59, 63, 51, 54, 55, 83, 70]
 Length: 56, dtype: Int64}
Yujian — 15:08
from datetime import datetime
import pandas as pd
from joblib import load

class Predictor:
    def __init__(self):
Uitvouwen
message.txt
4 KB
wst
Yujian
yueying7911
 
from datetime import datetime
import pandas as pd
from joblib import load

class Predictor:
    def __init__(self):
        # Laad vooraf getrainde modellen (lineaire regressie & random forest classifier)
        self.linear_regression_model = load('LinearRegressionModel.joblib')
        self.random_forest_model = load('RandomForest.joblib')  # Zorg dat dit een classifier is

    def predict(self, data: dict):
        """
        Voorspelt herstelklasse op basis van invoerdata.

        Parameters:
            data: dict – een woordenboek met invoervelden

        Retourneert:
            Een tuple met (lineaire regressie voorspelling, random forest voorspelling)
        """

        # omzetten naar dag van de jaar
        date_obj = datetime.strptime(data['stm_sap_melddatum'], '%Y/%m/%d')
        day_of_year = date_obj.timetuple().tm_yday

        # om
        time_obj = datetime.strptime(data['stm_sap_meldtijd'], '%H:%M')
        stm_sap_meldtijd = time_obj.hour * 60 + time_obj.minute

        time_obj = datetime.strptime(data['stm_aanntpl_tijd'], '%H:%M')
        stm_aanntpl_tijd = time_obj.hour * 60 + time_obj.minute

        # Bepaal tijdvakken (15 minuten)
        bin_size = 15
        meldtijd_bin = (day_of_year// bin_size) * bin_size
        aanntpl_tijd_bin = (stm_sap_meldtijd// bin_size) * bin_size
        progfh_in_duur_bin = (stm_aanntpl_tijd // bin_size) * bin_size

        # Bereken tijdsverschil en spitsuur-indicator
        tijd_verschil_meld_aanntpl = stm_aanntpl_tijd - stm_sap_meldtijd
        uur_van_dag = (stm_sap_meldtijd // 60)
        is_spitsuur = int((7 <= uur_van_dag <= 9) or (17 <= uur_van_dag <= 19))

        # Maak een DataFrame voor lineaire regressie met kolomnamen
        lr_data = pd.DataFrame([{
            'stm_sap_meldtijd': stm_sap_meldtijd,
            'stm_sap_melddatum': day_of_year,
            'stm_aanntpl_tijd': stm_aanntpl_tijd,
            'stm_progfh_in_duur': data['stm_progfh_in_duur']
        }])

        # Maak een DataFrame voor random forest met correcte kolomnamen
        rf_data = pd.DataFrame([{
            'stm_sap_melddatum': day_of_year,
            'meldtijd_bin': meldtijd_bin,
            'aanntpl_tijd_bin': aanntpl_tijd_bin,
            'progfh_in_duur_bin': progfh_in_duur_bin,
            'stm_prioriteit': data['stm_prioriteit'],
            'stm_oorz_code': data['stm_oorz_code'],
            'stm_contractgeb_mld': data['stm_contractgeb_mld'],
            'stm_techn_mld_encoded': data['stm_techn_mld_encoded'],
            'tijd_verschil_meld_aanntpl': tijd_verschil_meld_aanntpl,
            'is_spitsuur': is_spitsuur
        }])

        # Voer voorspellingen uit
        lr_predict = self.linear_regression_model.predict(lr_data)[0]
        rf_predict = self.random_forest_model.predict(rf_data)[0]

        # Retourneer afgeronde regressiewaarde en klasse-voorspelling
        return round(float(lr_predict), 2), int(rf_predict)*15


if __name__ == '__main__':
    # Voorbeeld invoerdata
    data = {
        'stm_sap_melddatum': '2006/02/01',
        'stm_sap_meldtijd': '09:00',
        'stm_aanntpl_tijd': '11:00',
        'stm_progfh_in_duur': 52,
        'stm_prioriteit': 2,
        'stm_oorz_code': 218,
        'stm_contractgeb_mld': 4,
        'stm_techn_mld_encoded': 10  # Zorg dat dit een numerieke waarde is (geen string zoals 'S')
    }

    predictor = Predictor()
    lr_pred, rf_pred = predictor.predict(data)

    print(f"Lineaire regressie voorspelling: {lr_pred}")
    print(f"Random forest voorspelling (herstelklasse): {rf_pred} tot {rf_pred+15}")
