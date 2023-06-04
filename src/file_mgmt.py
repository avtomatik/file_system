

import os

from lib import delete_files, move_files, rename_files

FILE_NAMES = ('test.py')
FILE_NAMES = (
    'incompleteDataFusionUSACostIndex.py', 'incompletedataFetchCAN.py', 'incompleteDFT.py', 'incompleteUSABLSV.py'
)

PATH_SRC = '/Users/alexandermikhailov/Documents'
delete_files(FILE_NAMES, PATH_SRC)
PATH_SRC = '/Volumes/NO NAME'
delete_files(FILE_NAMES, PATH_SRC)
PATH_SRC = '/Volumes/NO NAME 1'
delete_files(FILE_NAMES, PATH_SRC)


PATH_SRC = '/Users/alexandermikhailov/Documents'
rename_files(FILE_NAMES, PATH_SRC)
PATH_SRC = '/Volumes/NO NAME 1'
rename_files(FILE_NAMES, PATH_SRC)
PATH_SRC = '/Volumes/NO NAME'
rename_files(FILE_NAMES, PATH_SRC)


FILE_NAMES = ('project.py', 'datafetch.py', 'tools.py', 'test.py')
move_files(FILE_NAMES)

PATH_SRC = '/Users/alexandermikhailov/Documents'
FILE_NAMES = (
    'Reference EN Cobb C.W., Douglas P.H. A Theory of Production.pdf',
    'Reference EN Douglas P.H. The Theory of Wages.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2246.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2249.pdf',
    'Reference RU Brown M. 0597_088.pdf',
    'Reference RU Brown M. 0597_099.pdf',
    'Reference RU Kurenkov Yu.V. Proizvodstvennye moshchnost v promyshlennosti glavnykh kapitalisticheskikh stran.pdf'
)

if os.getcwd() == PATH_SRC:
    for file_name in FILE_NAMES:
        os.unlink(file_name)
