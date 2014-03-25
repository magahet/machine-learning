import csv


key = [
    [],
    [' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov', ' Local-gov', ' ?', ' Self-emp-inc', ' Without-pay', ' Never-worked'],
    [],
    [' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th', ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th', ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th', ' Preschool', ' 12th'],
    [],
    [' Never-married', ' Married-civ-spouse', ' Divorced', ' Married-spouse-absent', ' Separated', ' Married-AF-spouse', ' Widowed'],
    [' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty', ' Other-service', ' Sales', ' Craft-repair', ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct', ' Tech-support', ' ?', ' Protective-serv', ' Armed-Forces', ' Priv-house-serv'],
    [' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried', ' Other-relative'],
    [' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo', ' Other'],
    [' Male', ' Female'],
    [],
    [],
    [],
    [' United-States', ' Cuba', ' Jamaica', ' India', ' ?', ' Mexico', ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada', ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland', ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos', ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic', ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan', ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland', ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong', ' Ireland', ' Hungary', ' Holand-Netherlands'],
    [' <=50K', ' >50K'],
]


with open('adult.data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in reader:
        for col in range(len(row)):
            if col in [10, 11]:
                try:
                    row[col] = row[col] // 1000
                except TypeError:
                    pass
            try:
                row[col] = key[col].index(row[col])
            except ValueError:
                pass
        print ','.join([str(i) for i in row])
