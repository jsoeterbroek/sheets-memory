import pygsheets
from ddict import ddict

gc = pygsheets.authorize()

# Open spreadsheet and then worksheet
sh = gc.open_by_key('1HO9s7VNA_zBQfu8qLemwAORczdoiA1OUAvt7wRutjOQ')
template_wks = sh.sheet1
sheetname = ddict['sheetname']

try:
    exists = sh.worksheet_by_title(sheetname)
except:
    res = sh.add_worksheet(sheetname, src_worksheet=template_wks)

wks = sh.worksheet_by_title(sheetname)

# Update cells with values
for k,v in ddict.iteritems():
    if not k == 'sheetname':
        wks.update_cell(k, v)
