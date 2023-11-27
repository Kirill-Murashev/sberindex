import pandas as pd

translation_mapping = {
    'Санкт-Петербург': ['St. Petersburg', '圣彼得堡'],
    'Ленинградская область': ['Leningrad Oblast', '列宁格勒州'],
    'Москва': ['Moscow', '莫斯科'],
    'Московская область': ['Moscow Oblast', '莫斯科州'],
    'Краснодарский край': ['Krasnodar Krai', '克拉斯诺达尔边疆区'],
    'Республика Калмыкия': ['Republic of Kalmykia', '卡尔梅克共和国'],
    'Волгоградская область': ['Volgograd Oblast', '伏尔加格勒州'],
    'Республика Северная Осетия — Алания': ['Republic of North Ossetia–Alania', '北奥塞梯-阿兰共和国'],
    'Ростовская область': ['Rostov Oblast', '罗斯托夫州'],
    'Ямало-Ненецкий автономный округ': ['Yamalo-Nenets Autonomous Okrug', '亚马尔-涅涅茨自治区'],
    'Республика Башкортостан': ['Republic of Bashkortostan', '巴什科尔托斯坦共和国'],
    'Астраханская область': ['Astrakhan Oblast', '阿斯特拉罕州'],
    'Приморский край': ['Primorsky Krai', '滨海边疆区'],
    'Республика Татарстан': ['Republic of Tatarstan', '鞑靼斯坦共和国'],
    'Ульяновская область': ['Ulyanovsk Oblast', '乌里扬诺夫斯克州'],
    'Амурская область': ['Amur Oblast', '阿穆尔州'],
    'Калининградская область': ['Kaliningrad Oblast', '加里宁格勒州'],
    'Липецкая область': ['Lipetsk Oblast', '利佩茨克州'],
    'Иркутская область': ['Irkutsk Oblast', '伊尔库茨克州'],
    'Камчатский край': ['Kamchatka Krai', '堪察加边疆区'],
    'Кабардино-Балкарская Республика': ['Kabardino-Balkar Republic', '卡巴尔达-巴尔卡尔共和国'],
    'Еврейская автономная область': ['Jewish Autonomous Oblast', '犹太自治州'],
    'Удмуртская Республика': ['Udmurt Republic', '乌德穆尔特共和国'],
    'Белгородская область': ['Belgorod Oblast', '别尔哥罗德州'],
    'Ярославская область': ['Yaroslavl Oblast', '雅罗斯拉夫尔州'],
    'Нижегородская область': ['Nizhny Novgorod Oblast', '下诺夫哥罗德州'],
    'Калужская область': ['Kaluga Oblast', '卡卢加州'],
    'Кировская область': ['Kirov Oblast', '基洛夫州'],
    'Республика Мордовия': ['Republic of Mordovia', '莫尔多瓦共和国'],
    'Саратовская область': ['Saratov Oblast', '萨拉托夫州'],
    'Забайкальский край': ['Zabaykalsky Krai', '外贝加尔边疆区'],
    'Тверская область': ['Tver Oblast', '特维尔州'],
    'Тюменская область': ['Tyumen Oblast', '秋明州'],
    'Архангельская область': ['Arkhangelsk Oblast', '阿尔汉格尔斯克州'],
    'Республика Бурятия': ['Republic of Buryatia', '布里亚特共和国'],
    'Республика Ингушетия': ['Republic of Ingushetia', '印古什共和国'],
    'Республика Тыва': ['Tuva Republic', '图瓦共和国'],
    'Республика Коми': ['Komi Republic', '科米共和国'],
    'Республика Дагестан': ['Republic of Dagestan', '达吉斯坦共和国'],
    'Красноярский край': ['Krasnoyarsk Krai', '克拉斯诺亚尔斯克边疆区'],
    'Республика Карелия': ['Republic of Karelia', '卡累利阿共和国'],
    'Орловская область': ['Oryol Oblast', '奥廖尔州'],
    'Брянская область': ['Bryansk Oblast', '布良斯克州'],
    'Челябинская область': ['Chelyabinsk Oblast', '车里雅宾斯克州'],
    'Кемеровская область': ['Kemerovo Oblast', '克麦罗沃州'],
    'Хабаровский край': ['Khabarovsk Krai', '哈巴罗夫斯克边疆区'],
    'Курская область': ['Kursk Oblast', '库尔斯克州'],
    'Пензенская область': ['Penza Oblast', '彭萨州'],
    'Костромская область': ['Kostroma Oblast', '科斯特罗马州'],
    'Рязанская область': ['Ryazan Oblast', '梁赞州'],
    'Республика Саха (Якутия)': ['Sakha Republic (Yakutia)', '萨哈（雅库特）共和国'],
    'Курганская область': ['Kurgan Oblast', '库尔干州'],
    'Владимирская область': ['Vladimir Oblast', '弗拉基米尔州'],
    'Магаданская область': ['Magadan Oblast', '马加丹州'],
    'Ставропольский край': ['Stavropol Krai', '斯塔夫罗波尔边疆区'],
    'Тамбовская область': ['Tambov Oblast', '坦波夫州'],
    'Карачаево-Черкесская Республика': ['Karachay-Cherkess Republic', '卡拉恰伊-切尔克斯共和国'],
    'Псковская область': ['Pskov Oblast', '普斯科夫州'],
    'Тульская область': ['Tula Oblast', '图拉州'],
    'Республика Марий Эл': ['Mari El Republic', '马里埃尔共和国'],
    'Алтайский край': ['Altai Krai', '阿尔泰边疆区'],
    'Россия': ['Russia', '俄罗斯'],
    'Самарская область': ['Samara Oblast', '萨马拉州'],
    'Свердловская область': ['Sverdlovsk Oblast', '斯维尔德洛夫斯克州'],
    'Республика Алтай': ['Altai Republic', '阿尔泰共和国'],
    'Сахалинская область': ['Sakhalin Oblast', '萨哈林州'],
    'Вологодская область': ['Vologda Oblast', '沃洛格达州'],
    'Ханты-Мансийский автономный округ — Югра': ['Khanty-Mansi Autonomous Okrug – Yugra', '汉特-曼西自治区 - 尤格拉'],
    'Пермский край': ['Perm Krai', '彼尔姆边疆区'],
    'Ненецкий автономный округ': ['Nenets Autonomous Okrug', '涅涅茨自治区'],
    'Новгородская область': ['Novgorod Oblast', '诺夫哥罗德州'],
    'Республика Адыгея': ['Republic of Adygea', '阿迪格共和国'],
    'Ивановская область': ['Ivanovo Oblast', '伊万诺沃州'],
    'Новосибирская область': ['Novosibirsk Oblast', '新西伯利亚州'],
    'Томская область': ['Tomsk Oblast', '托木斯克州'],
    'Чувашская Республика': ['Chuvash Republic', '楚瓦什共和国'],
    'Смоленская область': ['Smolensk Oblast', '斯摩棱斯克州'],
    'Чукотский автономный округ': ['Chukotka Autonomous Okrug', '楚科奇自治区'],
    'Воронежская область': ['Voronezh Oblast', '沃罗涅日州'],
    'Омская область': ['Omsk Oblast', '鄂木斯克州'],
    'Оренбургская область': ['Orenburg Oblast', '奥伦堡州'],
    'Республика Хакасия': ['Republic of Khakassia', '哈卡斯共和国'],
    'Чеченская Республика': ['Chechen Republic', '车臣共和国'],
    'Мурманская область': ['Murmansk Oblast', '摩尔曼斯克州']
}


def translate_region(region, translation_mapping):
    """Concatenate the original region name with its English and Chinese translations."""
    if region in translation_mapping:
        # Concatenate the names with commas
        return f"{region}, {translation_mapping[region][0]}, {translation_mapping[region][1]}"
    return region

def update_csv_file(file_path, translation_mapping):
    try:
        df = pd.read_csv(file_path, delimiter=';')
        df['region'] = df['region'].apply(lambda x: translate_region(x, translation_mapping))
        df.to_csv(file_path, index=False, sep=';')  # Save with the same delimiter
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


# List of your CSV file paths
file_paths = [
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_real_estate_deals_primary_market.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_srednyaya-stoimost-kvadratnogo-metra-pervichnyi-rynok.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_kolichestvo-predlozhenii-o-prodazhe-pervichki.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_real_estate_deals_secondary_market.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_srednyaya-stoimost-kvadratnogo-metra-vtorichnyi-rynok.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_kolichestvo-predlozhenii-vtorichki.csv',
    '/home/kaarlahti/PycharmProjects/sberindex/data/utf8_srok-ekspozicii-vtorichki.csv'
]

for file_path in file_paths:
    update_csv_file(file_path, translation_mapping)
