import xlwings as xw
import numpy as np
import pandas as pd

import json


class ReadJSON:

    def __init__(self):
        self.file = 'fbd.json'
        with open(self.file, encoding='utf-8') as json_file:
            self.data = json.load(json_file)
        self.wb = xw.Book.caller()

    def write_leagues(self):
        league_keys = list(self.data.keys())
        sheet = self.wb.sheets['Leagues']
        sheet['A1'].value = 'LgID'
        sheet['A2'].options(transpose=True).value = league_keys
        sheet.autofit()

        headers = ['TmID', 'name', 'shortName', 'tla', 'eloNow']
        for lg in league_keys:
            lg_sht = self.wb.sheets[lg]
            lg_sht.clear_contents()
            tm_ids = list(self.data[lg]['data'].keys())
            lg_sht['A1'].value = headers
            lg_sht['A2'].options(transpose=True).value = tm_ids

            for row, tm in enumerate(tm_ids):
                tm_data = self.data[lg]['data'][tm]
                wr_cell = 'B' + str(row + 2)
                lg_sht[wr_cell].value = [tm_data[headers[1:][i]] for i in range(len(headers[1:]))]

            xw.Range('E2').expand('down').number_format = '0'
            lg_sht.autofit()

    def write_test(self):
        sheet = self.wb.sheets['Sandbox']
        if sheet['A1'].value == 'Hello EloXL!':
            sheet['A1'].value = 'Bye EloXL!'
        else:
            sheet['A1'].value = 'Hello EloXL!'
        sheet.autofit()

    def __str__(self):
        return '[Reading from {0} to Excel file {1}]'.format(self.file, self.wb)

    def __repr__(self):
        return str(self)


@xw.func
def hello(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    xw.Book('EloXL.xlsm').set_mock_caller()
    rj = ReadJSON()
    print(rj)
    rj.write_leagues()