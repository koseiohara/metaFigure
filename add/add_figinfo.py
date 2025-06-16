from add_pdfinfo import add_pdfinfo
from add_pnginfo import add_pnginfo

def add_figinfo(target, key, text):

    if (target[-4:].lower() == '.pdf'):
        add_pdfinfo(target, key, text)
    elif (target[-4:].lower() == '.png'):
        add_pnginfo(target, key, text)
    else:
        print('Unsupported Format : ' + target)
        print('error stop')
        exit(1)


add_figinfo('DIFF_1990_2020_VINT_qe_ANLFILTER.pdf', 'hoge1', 'fuga')
add_figinfo('JRA3Q_MIM_st_1970_2022_DJF.png', 'hoge1', 'fuga')
    
