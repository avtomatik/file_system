from datetime import datetime

CYRILLIC_TO_LATIN = (
    'a,b,v,g,d,e,zh,z,i,y,k,l,m,n,o,p,r,s,t,u,f,kh,ts,ch,sh,shch,,y,,e,yu,ya,'
    ',yo'
)

PREFIXES = {'.', '_', '~'}

RESERVED = {'FOUND.000', 'System Volume Information'}

FILE_NAME_SRC = 'file_names_d.txt'

FILE_NAME_DST = 'file_names_e.txt'


MAP_CYRILLIC_TO_LATIN = {
    chr(idx): latin
    for idx, latin in enumerate(CYRILLIC_TO_LATIN.split(','), start=1072)
}

FILE_NAME_LOG = f'log_{datetime.now():%Y-%m-%d_%H-%M-%S}.txt'
