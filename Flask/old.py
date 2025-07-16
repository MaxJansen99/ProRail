import pandas as pd

class Old:
    def __init__(self, csv_path):
        """
        Initialiseer de DataFilter-class.

        Parameters:
            csv_path (str): De pad naar het CSV-bestand met de gegevens.
        """
        self.csv_path = csv_path
        self.data = pd.read_csv(csv_path)

    @staticmethod
    def minutes_to_time_str(m):
        """
        Converteer minuten naar een tijdstring in HH:MM-formaat.

        Parameters:
            m (int): Aantal minuten.

        Retourneert:
            str: Tijdstring in HH:MM-formaat.
        """
        hour = m // 60
        minute = m % 60
        return f"{hour:02d}:{minute:02d}"

    def filter_data(self, stm_oorz_code=None, stm_contractgeb_mld=None, stm_techn_mld=None, stm_prioriteit=None):
        """
        Filter de gegevens op basis van de opgegeven parameters.

        Parameters:
            stm_oorz_code (int, optional): Code van de storingsoorzaak.
            stm_contractgeb_mld (int, optional): Contractgebied meldcode.
            stm_techn_mld (str, optional): Technisch meldcode.
            stm_prioriteit (int, optional): Prioriteitscode van de storing.

        Retourneert:
            pd.DataFrame: Gefilterde gegevens.
        """
        filtered_data = self.data

        if stm_oorz_code is not None:
            filtered_data = filtered_data[filtered_data['stm_oorz_code'] == stm_oorz_code]
        if stm_contractgeb_mld is not None:
            filtered_data = filtered_data[filtered_data['stm_contractgeb_mld'] == stm_contractgeb_mld]
        if stm_techn_mld is not None:
            filtered_data = filtered_data[filtered_data['stm_techn_mld'] == stm_techn_mld]
        if stm_prioriteit is not None:
            filtered_data = filtered_data[filtered_data['stm_prioriteit'] == stm_prioriteit]

        # Selecteer de relevante kolommen
        filtered_data = filtered_data[
            [
                # 'stm_sap_melddatum',
                'stm_sap_meldtijd',
                'stm_aanntpl_tijd',
                'stm_progfh_in_tijd',
                'stm_progfh_in_duur',
                'stm_prioriteit',
                'stm_oorz_code',
                'stm_contractgeb_mld',
                'stm_techn_mld',
                'stm_fh_tijd',
                'targetherstel'
            ]
        ]

        # Converteer tijdweergave
        filtered_data['stm_sap_meldtijd'] = filtered_data['stm_sap_meldtijd'].apply(self.minutes_to_time_str)
        filtered_data['stm_aanntpl_tijd'] = filtered_data['stm_aanntpl_tijd'].apply(self.minutes_to_time_str)

        return filtered_data.head(10).to_dict(orient="records")


if __name__ == "__main__":
    # Voorbeeldgebruik
    data_filter = Old('../Data/sap_storing_data_hu_filtered.csv')
    filtered_data = data_filter.filter_data(
        stm_oorz_code=215,
        stm_contractgeb_mld=26,
        stm_techn_mld='S',
        stm_prioriteit=2
    )

    print(filtered_data)