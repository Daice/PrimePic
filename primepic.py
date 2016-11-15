#!/usr/bin/python

from PIL import Image
import cv2

pp={0:[0,0],\
    2:[0,2],\
    4:[2,2],\
    6:[3,3],\
    8:[3,5],\
    10:[3,7],\
    12:[5,7],\
    14:[3,11],\
    16:[3,13],\
    18:[5,13],\
    20:[3,17],\
    22:[3,19],\
    24:[5,19],\
    26:[3,23],\
    28:[5,23],\
    30:[7,23],\
    32:[3,29],\
    34:[3,31],\
    36:[5,31],\
    38:[7,31],\
    40:[3,37],\
    42:[5,37],\
    44:[3,41],\
    46:[3,43],\
    48:[5,43],\
    50:[3,47],\
    52:[5,47],\
    54:[7,47],\
    56:[3,53],\
    58:[5,53],\
    60:[7,53],\
    62:[3,59],\
    64:[3,61],\
    66:[5,61],\
    68:[7,61],\
    70:[3,67],\
    72:[5,67],\
    74:[3,71],\
    76:[3,73],\
    78:[5,73],\
    80:[7,73],\
    82:[3,79],\
    84:[5,79],\
    86:[3,83],\
    88:[5,83],\
    90:[7,83],\
    92:[3,89],\
    94:[5,89],\
    96:[7,89],\
    98:[19,79],\
    100:[3,97],\
    102:[5,97],\
    104:[3,101],\
    106:[3,103],\
    108:[5,103],\
    110:[3,107],\
    112:[3,109],\
    114:[5,109],\
    116:[3,113],\
    118:[5,113],\
    120:[7,113],\
    122:[13,109],\
    124:[11,113],\
    126:[13,113],\
    128:[17,101],\
    130:[3,127],\
    132:[5,127],\
    134:[3,131],\
    136:[5,131],\
    138:[7,131],\
    140:[3,137],\
    142:[3,139],\
    144:[5,139],\
    146:[7,139],\
    148:[11,137],\
    150:[11,139],\
    152:[3,149],\
    154:[3,151],\
    156:[5,151],\
    158:[7,151],\
    160:[3,157],\
    162:[5,157],\
    164:[7,157],\
    166:[3,163],\
    168:[5,163],\
    170:[3,167],\
    172:[5,167],\
    174:[11,163],\
    176:[3,173],\
    178:[5,173],\
    180:[7,173],\
    182:[3,179],\
    184:[3,181],\
    186:[5,181],\
    188:[7,181],\
    190:[11,179],\
    192:[11,181],\
    194:[3,191],\
    196:[3,193],\
    198:[5,193],\
    200:[3,197],\
    202:[3,199],\
    204:[5,199],\
    206:[7,199],\
    208:[11,197],\
    210:[11,199],\
    212:[13,199],\
    214:[3,211],\
    216:[5,211],\
    218:[7,211],\
    220:[23,197],\
    222:[11,211],\
    224:[13,211],\
    226:[3,223],\
    228:[5,233],\
    230:[3,227],\
    232:[3,229],\
    234:[5,229],\
    236:[3,233],\
    238:[5,233],\
    240:[7,233],\
    242:[3,239],\
    244:[3,241],\
    246:[5,241],\
    248:[7,241],\
    250:[11,239],\
    252:[11,241],\
    254:[3,251]
    }
picstr=raw_input("Please enter picture name:")
img=cv2.imread(picstr)
size=img.shape
for i in range(size[0]):
    for j in range(size[1]):
        t=[]
        for k in range(size[2]):
            if img[i,j,k]==0 or img[i,j,k]==255:
                t.append(img[i,j,k])
            elif img[i,j,k]%2==0:
                t.append(pp[img[i,j,k]][0])
            else:
                t.append(pp[img[i,j,k]+1][0])
        img[i,j]=t

cv2.imwrite("pre"+picstr,img)
