

import os

from lib import delete_files, move_files, rename_files

FILE_NAMES = ('test.py')
FILE_NAMES = (
    'incompleteDataFusionUSACostIndex.py', 'incompletedataFetchCAN.py', 'incompleteDFT.py', 'incompleteUSABLSV.py'
)

PATH = '/Users/alexandermikhailov/Documents'
delete_files(FILE_NAMES, PATH)
PATH = '/Volumes/NO NAME'
delete_files(FILE_NAMES, PATH)
PATH = '/Volumes/NO NAME 1'
delete_files(FILE_NAMES, PATH)


PATH = '/Users/alexandermikhailov/Documents'
rename_files(FILE_NAMES, PATH)
PATH = '/Volumes/NO NAME 1'
rename_files(FILE_NAMES, PATH)
PATH = '/Volumes/NO NAME'
rename_files(FILE_NAMES, PATH)


FILE_NAMES = ('project.py', 'datafetch.py', 'tools.py', 'test.py')
move_files(FILE_NAMES)

PATH = '/Users/alexandermikhailov/Documents'
FILE_NAMES = (
    'Reference EN Cobb C.W., Douglas P.H. A Theory of Production.pdf',
    'Reference EN Douglas P.H. The Theory of Wages.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2246.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2249.pdf',
    'Reference RU Brown M. 0597_088.pdf',
    'Reference RU Brown M. 0597_099.pdf',
    'Reference RU Kurenkov Yu.V. Proizvodstvennye moshchnost v promyshlennosti glavnykh kapitalisticheskikh stran.pdf'
)

if os.getcwd() == PATH:
    for file_name in FILE_NAMES:
        os.unlink(file_name)
