

from lib import delete_files, move_files, rename_files

PATH_HOME = '/Users/alexandermikhailov/Documents'
PATH_STICK0 = '/Volumes/NO NAME'
PATH_STICK1 = '/Volumes/NO NAME 1'

FILE_NAMES_IN = ('test.py')
FILE_NAMES_UT = ('project.py', 'datafetch.py', 'tools.py', 'test.py')
FILE_NAMES_UT = (
    'incompleteDataFusionUSACostIndex.py',
    'incompletedataFetchCAN.py',
    'incompleteDFT.py',
    'incompleteUSABLSV.py'
)


delete_files(FILE_NAMES_IN)
rename_files(FILE_NAMES_IN, FILE_NAMES_UT)
move_files(FILE_NAMES_UT)
