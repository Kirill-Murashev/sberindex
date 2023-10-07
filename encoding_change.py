import os

folder_path = "/home/kaarlahti/PycharmProjects/sberindex/data/"

files = [
    "srok-ekspozicii-vtorichki.csv",
    "srednyaya-stoimost-kvadratnogo-metra-vtorichnyi-rynok.csv",
    "srednyaya-stoimost-kvadratnogo-metra-pervichnyi-rynok.csv",
    "real_estate_deals_secondary_market.csv",
    "real_estate_deals_primary_market.csv",
    "kolichestvo-predlozhenii-vtorichki.csv",
    "kolichestvo-predlozhenii-o-prodazhe-pervichki.csv"
]

for file_name in files:
    input_path = os.path.join(folder_path, file_name)
    output_path = os.path.join(folder_path, "utf8_" + file_name)

    with open(input_path, "r", encoding="windows-1251") as source_file:
        with open(output_path, "w", encoding="utf-8") as target_file:
            for line in source_file:
                target_file.write(line)
