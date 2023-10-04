import gspread

gc = gspread.service_account(filename='credentials.json')
# de link naar de google sheet
sh = gc.open_by_key('14IU8y8tmB7-w3oAp59FXh_57VJ7F-K3xwzhUD0lY_RU')
# zorgt dat i de eerste sheet pakt
worksheet = sh.sheet1

# res = worksheet.get_all_records()
res = worksheet.get_all_values()

data = ["Frankrijk", "Lyon"]
# worksheet.insert_row(data, 4)
# worksheet.append_row(data)
# worksheet.update_cell(4,2, "Paris")
worksheet.delete_rows(6)
print(res)