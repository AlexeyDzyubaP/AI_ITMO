import numpy as np
import math
import glob
from pathlib import Path
import os

def zernIndex(j):
    """
    Find the [n,m] list giving the radial order n and azimuthal order
    of the Zernike polynomial of Noll index j.

    Parameters:
        j (int): The Noll index for Zernike polynomials

    Returns:
        list: n, m values
    """
    n = int((-1.+np.sqrt(8*(j-1)+1))/2.)
    p = (j-(n*(n+1))/2.)
    k = n%2
    m = int((p+k)/2.)*2 - k

    if m!=0:
        if j%2==0:
            s=1
        else:
            s=-1
        m *= s

    return [n, m]
#########################

f = open('csvfile.csv','w')

## Python will convert \n to os.linesep


#rootdir = '/home/p/Documents/Rodin-Khonina-Seraphimovich-Popov-rev/2021Paper/mail1/code/dataset _ two Zernike/data'
#rootdir = './testdata'
rootdir = './dataset _ two Zernike/data'

for subdir in glob.glob(rootdir+'/*'):
    #print(subdir)
    subdir2csv = subdir.split(os.sep)[3]
    #print(subdir2csv)
    filesList = glob.glob(subdir+'/*')
    for i, fileName in enumerate(filesList):
        filesList[i] = Path(fileName).stem
    filesList = sorted(filesList)
    filesList = filesList[1::2]
    #print(filesList)
    
    for i, fileName in enumerate(filesList):
        labelArr = np.zeros(8)
        fileNameSplit = fileName.split('_')
        for j in range(1,3):
            #print(fileNameSplit[j])
            sum1 = fileNameSplit[j]
            n = int(sum1[1])
            m = int(sum1[3])
            #print(n, '   ', m)
            for j in range(1,16):
                n_, m_ = zernIndex(j)
                if (n == n_) and (m == m_):
                    break
            #print(j)
            alf = float(sum1[-4:])
            #print(alf)
            if j < 11:
                caseInd = 'a'
            else:
                caseInd = 'c'
            if j == 11:
                caseInd = 'b'
            #print(caseInd)
            jArr = {
                'a': lambda j: j/2 - 1,
                'b': lambda j: 5,
                'c': lambda j: j/2
            }[caseInd](j)
            #print(jArr)
            labelArr[int(jArr)] = alf
    
        line2csv = subdir2csv + os.sep + fileName + '.png' + ','
        line2csv += ','.join(str(x) for x in labelArr)
        f.write(line2csv + '\n') #Give your csv text here.


f.close()

#print(fileNames)

