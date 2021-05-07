

import xlrd

excel_projet = xlrd.open_workbook('../Crypto.xlsx')

excel_t_proj_sheet = excel_projet.sheet_names()

for v in range(0, len(excel_t_proj_sheet)):
    t_proj = excel_projet.sheet_by_index(v)

    for x in range(1, t_proj.nrows):
        proj_coin_url = t_proj.cell(x, 1).value

        proj_description = t_proj.cell(x, 3).value

        proj_forage_possible = t_proj.cell(x, 5).value