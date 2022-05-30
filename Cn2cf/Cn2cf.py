ys = {'氢': 'H', '氦': 'He', '锂': 'Li', '铍': 'Be', '硼': 'B', '碳': 'C', '氮': 'N', '氧': 'O', '氟': 'F', '氖': 'Ne', '钠': 'Na', '镁': 'Mg', '铝': 'Al', '硅': 'Si', '磷': 'P', '硫': 'S', '氯': 'Cl', '氩': 'Ar', '钾': 'K', '钙': 'Ca', '钪': 'Sc', '钛': 'Ti', '钒': 'V', '铬': 'Cr', '锰': 'Mn', '铁': 'Fe', '钴': 'Co', '镍': 'Ni', '铜': 'Cu', '锌': 'Zn', '镓': 'Ga', '锗': 'Ge', '砷': 'As', '硒': 'Se', '溴': 'Br', '氪': 'Kr', '铷': 'Rb', '锶': 'Sr', '钇': 'Y', '锆': 'Zr', '铌': 'Nb', '钼': 'Mo', '锝': 'Tc', '钌': 'Ru', '铑': 'Rh', '钯': 'Pd', '银': 'Ag', '镉': 'Cd', '铟': 'In', '锡': 'Sn', '锑': 'Sb', '碲': 'Te',
      '碘': 'I', '氙': 'Xe', '铯': 'Cs', '钡': 'Ba', '镧': 'La', '铈': 'Ce', '镨': 'Pr', '钕': 'Nd', '钷': 'Pm', '钐': 'Sm', '铕': 'Eu', '钆': 'Gd', '铽': 'Tb', '镝': 'Dy', '钬': 'Ho', '铒': 'Er', '铥': 'Tm', '镱': 'Yb', '镥': 'Lu', '铪': 'Hf', '钽': 'Ta', '钨': 'W', '铼': 'Re', '锇': 'Os', '铱': 'Ir', '铂': 'Pt', '金': 'Au', '汞': 'Hg', '铊': 'Tl', '铅': 'Pb', '铋': 'Bi', '钋': 'Po', '砹': 'At', '氡': 'Rn', '钫': 'Fr', '镭': 'Ra', '锕': 'Ac', '钍': 'Th', '镤': 'Pa', '铀': 'U', '镎': 'Np', '钚': 'Pu', '镅': 'Am', '锔': 'Cm', '锫': 'Bk', '锎': 'Cm', '锿': 'Es', '镄': 'Fm', '钔': 'Md', '锘': 'No', '铹': 'Lr'}
sz = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
      '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}


def get(ChemicalName):
    if '化' in ChemicalName:
        cname = ChemicalName.split('化')
        for x in range(2):
            if len(cname[x]) < 2:
                cname[x] = ['', cname[x]]
            for y in sz.keys():
                if y in cname[x]:
                    cname[x] = [sz[y], cname[x].split(y)[1]]
        cname[0] = ys[cname[0][1]]+str(cname[0][0])
        cname[1] = ys[cname[1][1]]+str(cname[1][0])
        return cname[1] + cname[0]
