import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets['Sandbox']
    if sheet['A1'].value == 'Hello XLWings!':
        sheet['A1'].value = 'Bye XLWings!'
    else:
        sheet['A1'].value = 'Hello XLWings!'
    sheet.autofit()


@xw.func
def hello(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    xw.Book('EloXL.xlsm').set_mock_caller()
    main()
