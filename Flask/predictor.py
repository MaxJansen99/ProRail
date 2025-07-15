from datetime import datetime
import pandas as pd
from joblib import load


class Predictor:
    def __init__(self):
        # Laad vooraf getrainde modellen (lineaire regressie & random forest classifier)
        self.linear_regression_model = load("../Models/LinearRegressionModel.joblib")
        self.random_forest_model = load(
            "../Models/RandomForest.joblib"
        )  # Zorg dat dit een classifier is

    def predict(self, data: dict):
        """
        Voorspelt herstelklasse op basis van invoerdata.

        Parameters:
            data: dict – een woordenboek met invoervelden

        Retourneert:
            Een tuple met (lineaire regressie voorspelling, random forest voorspelling)
        """

        # omzetten naar dag van de jaar
        date_obj = datetime.strptime(data["stm_sap_melddatum"], "%Y-%m-%d")
        day_of_year = date_obj.timetuple().tm_yday

        # om
        time_obj = datetime.strptime(data["stm_sap_meldtijd"], "%H:%M")
        stm_sap_meldtijd = time_obj.hour * 60 + time_obj.minute

        time_obj = datetime.strptime(data["stm_aanntpl_tijd"], "%H:%M")
        stm_aanntpl_tijd = time_obj.hour * 60 + time_obj.minute

        # Bepaal tijdvakken (15 minuten)
        bin_size = 15
        meldtijd_bin = (day_of_year // bin_size) * bin_size
        aanntpl_tijd_bin = (stm_sap_meldtijd // bin_size) * bin_size
        progfh_in_duur_bin = (stm_aanntpl_tijd // bin_size) * bin_size

        # Bereken tijdsverschil en spitsuur-indicator
        tijd_verschil_meld_aanntpl = stm_aanntpl_tijd - stm_sap_meldtijd
        uur_van_dag = stm_sap_meldtijd // 60
        is_spitsuur = int((7 <= uur_van_dag <= 9) or (17 <= uur_van_dag <= 19))

        # Maak een DataFrame voor lineaire regressie met kolomnamen
        lr_data = pd.DataFrame(
            [
                {
                    "stm_sap_meldtijd": stm_sap_meldtijd,
                    "stm_sap_melddatum": day_of_year,
                    "stm_aanntpl_tijd": stm_aanntpl_tijd,
                    "stm_progfh_in_duur": data["stm_progfh_in_duur"],
                }
            ]
        )

        # Maak een DataFrame voor random forest met correcte kolomnamen
        rf_data = pd.DataFrame(
            [
                {
                    "stm_sap_melddatum": day_of_year,
                    "meldtijd_bin": meldtijd_bin,
                    "aanntpl_tijd_bin": aanntpl_tijd_bin,
                    "progfh_in_duur_bin": progfh_in_duur_bin,
                    "stm_prioriteit": data["stm_prioriteit"],
                    "stm_oorz_code": data["stm_oorz_code"],
                    "stm_contractgeb_mld": data["stm_contractgeb_mld"],
                    "stm_techn_mld_encoded": data["stm_techn_mld_encoded"],
                    "tijd_verschil_meld_aanntpl": tijd_verschil_meld_aanntpl,
                    "is_spitsuur": is_spitsuur,
                }
            ]
        )

        # Voer voorspellingen uit
        lr_predict = self.linear_regression_model.predict(lr_data)[0]
        rf_predict = self.random_forest_model.predict(rf_data)[0]

        # Retourneer afgeronde regressiewaarde en klasse-voorspelling
        return round(float(lr_predict), 2), int(rf_predict) * 15


if __name__ == "__main__":
    # Voorbeeld invoerdata
    data = {
        "stm_sap_melddatum": "2006-02-01",
        "stm_sap_meldtijd": "09:00",
        "stm_aanntpl_tijd": "11:00",
        "stm_progfh_in_duur": 52,
        "stm_prioriteit": 2,
        "stm_oorz_code": 218,
        "stm_contractgeb_mld": 4,
        "stm_techn_mld_encoded": 10,  # Zorg dat dit een numerieke waarde is (geen string zoals 'S')
    }

    predictor = Predictor()
    lr_pred, rf_pred = predictor.predict(data)

    print(f"Lineaire regressie voorspelling: {lr_pred}")
    print(f"Random forest voorspelling (herstelklasse): {rf_pred} tot {rf_pred + 15}")
