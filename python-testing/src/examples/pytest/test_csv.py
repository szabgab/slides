import csv


def test_csv():
    filename = '../../examples/csv/process_csv_file_newline.csv'
    with open(filename) as fh:
        rd = csv.reader(fh, delimiter=';')
        assert rd.__next__() == ['Tudor', 'Vidor', '10', 'Hapci']
        assert rd.__next__() == ['Szundi', 'Morgo', '7', 'Szende']
        assert rd.__next__() == ['Kuka', 'Hofeherke; \nalma', '100', 'Kiralyno']
        assert rd.__next__() == ['Boszorkany', 'Herceg', '9', 'Meselo']
