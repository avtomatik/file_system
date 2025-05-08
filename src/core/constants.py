import datetime

LATIN_SUBSTITUTION = '''a,b,v,g,d,e,zh,z,i,y,k,l,m,n,o,p,r,s,t,u,f,kh,ts,ch,sh,shch,,y,,e,yu,ya,,yo'''


MAP_CYRILLIC_TO_LATIN = {
    chr(_): latin for _, latin in enumerate(LATIN_SUBSTITUTION.split(','), start=1072)
}


PREFIXES = ('.', '_', '~')


FILE_NAMES = ['test.py']
FILE_NAMES = [
    'incompleteDFT.py',
    'incompleteDataFusionUSACostIndex.py',
    'incompleteUSABLSV.py'
    'incompletedataFetchCAN.py',
]
FILE_NAMES = ['datafetch.py', 'project.py', 'test.py', 'tools.py']
FILE_NAMES = [
    'Reference EN Cobb C.W., Douglas P.H. A Theory of Production.pdf',
    'Reference EN Douglas P.H. The Theory of Wages.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2246.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2249.pdf',
    'Reference RU Brown M. 0597_088.pdf',
    'Reference RU Brown M. 0597_099.pdf',
    'Reference RU Kurenkov Yu.V. Proizvodstvennye moshchnost v promyshlennosti glavnykh kapitalisticheskikh stran.pdf'
]
FILE_NAMES = [
    'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_en.pdf',
    'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_en.tex',
    'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_ru.pdf',
    'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_ru.tex',
    'reference_en_samuelson_p_a_paul_douglas_s_measurement.pdf',
    'reference_en_samuelson_p_a_paul_douglas_s_measurement.tex',
]


FILE_NAME_L = 'file_names_d.txt'
FILE_NAME_R = 'file_names_e.txt'

FILE_NAME_LOG = f'log_{datetime.datetime.today()}.txt'.replace(' ', '_')
