import numpy
#import pygame
import math, time, sys
import pandas as pd


if __name__ == "__main__":
    out_file = 'out1.obj'
    in_file = 'cube.pov' 
    
    with open(in_file,'r') as fi:
        lines = fi.readlines()
    vert_startnum = -100
    vert_count = -100
    vt_startnum = -100
    vt_count = -100
    vn_startnum = -100
    vn_count = -100
    f_startnum = -100
    f_count = -100
    nindice_startnum = -100
    nindice_count = -100   
    uvindice_startnum = -100
    uvindice_count = -100       
    for ii,line in enumerate(lines):
            if line.strip().startswith('vertex_vectors'):
                vert_startnum = ii
            if ii == vert_startnum+1:
                vert_count = int(line.strip())
            if line.strip().startswith('normal_vectors'):
                vn_startnum = ii
            if ii == vn_startnum+1:
                vn_count = int(line.strip())
            if line.strip().startswith('uv_vectors'):
                vt_startnum = ii
            if ii == vt_startnum+1:
                vt_count = int(line.strip())
            if line.strip().startswith('face_indices'):
                f_startnum = ii
            if ii == f_startnum+1:
                f_count = int(line.strip())
            if line.strip().startswith('normal_indices'):
                nindice_startnum = ii
            if ii == nindice_startnum+1:
                nindice_count = int(line.strip())
            if line.strip().startswith('uv_indices'):
                uvindice_startnum = ii
            if ii == uvindice_startnum+1:
                uvindice_count = int(line.strip())
    print(    vert_startnum ,vert_count ,vt_startnum,vt_count,vn_startnum,vn_count,f_startnum,f_count)
    print(    nindice_startnum ,nindice_count ,uvindice_startnum,uvindice_count)
    list1 = []
    list2 = []
    list3 = []
    width = 1024
    height = 1024
    with open(out_file,'w') as outfile:
        outfile.write('mtllib cube.mtl\n')
        for ii,line in enumerate(lines):

            if ii > vert_startnum +1 and ii<=vert_startnum+1+vert_count:
                temp = line.strip().split(',')
                vx = temp[0].split('<')[1]
                vy = temp[1]
                vz = temp[2].split('>')[0]
                mystr = 'v '+vx + vy + vz+'\n'
                outfile.write(mystr)

            if ii > vn_startnum +1 and ii<=vn_startnum+1+vn_count:
                temp = line.strip().split(',')
                vx = temp[0].split('<')[1]
                vy = temp[1].strip()
                vz = temp[2].strip().split('>')[0]
                mystr = 'vn '+ vx +' '+ vy+' ' +vz+' ' +'\n'
                outfile.write(mystr)
                
            if ii > vt_startnum +1 and ii<=vt_startnum+1+vt_count:
                temp = line.strip().split(',')
                
                vx = temp[0].split('<')[1]
                vy = temp[1].split('>')[0]
                mystr = 'vt '+vx + vy +'\n'
                outfile.write(mystr)
            if ii > f_startnum +1 and ii<=f_startnum+1+f_count:
                temp = line.strip().split(',')
                vx = str(int(temp[0].split('<')[1])+1)
                vy = str(int(temp[1].strip())+1)
                vz = str(int(temp[2].strip().split('>')[0])+1)
                list1.append(vx)
                list1.append(vy)
                list1.append(vz)
            if ii > nindice_startnum +1 and ii<=nindice_startnum+1+nindice_count:
                temp = line.strip().split(',')
                vx = str(int(temp[0].split('<')[1])+1)
                vy = str(int(temp[1].strip())+1)
                vz = str(int(temp[2].strip().split('>')[0])+1)
                list3.append(vx)
                list3.append(vy)
                list3.append(vz)
            if ii > uvindice_startnum +1 and ii<=uvindice_startnum+1+uvindice_count:
                temp = line.strip().split(',')
                vx = str(int(temp[0].split('<')[1])+1)
                vy = str(int(temp[1].strip())+1)
                vz = str(int(temp[2].strip().split('>')[0])+1)
                list2.append(vx)
                list2.append(vy)
                list2.append(vz)
        mystr = 'usemtl optical'+'\n'
        outfile.write(mystr)
        for ii in range(1,uvindice_count):
            str = 'f '+list1[3*(ii-1)]+'/'+list2[3*(ii-1)]+'/'+list3[3*(ii-1)]
            str = str+ ' '+list1[3*(ii-1)+1]+'/'+list2[3*(ii-1)+1]+'/'+list3[3*(ii-1)+1]
            str = str+ ' '+list1[3*(ii-1)+2]+'/'+list2[3*(ii-1)+2]+'/'+list3[3*(ii-1)+2]
            outfile.write(str+'\n')







