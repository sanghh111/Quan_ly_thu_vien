def timKiem_String(sach,stt,gia_tri,dau_ra) ->list:
    if sach == []:
        return sach
    else:
        i = sach.pop()
        # print('i: ', i)
        if(gia_tri in i[stt]):
            dau_ra.append(i)
            # print('dau_ra: ', dau_ra)
        timKiem_String(sach,stt,gia_tri,dau_ra)

def timKiem_Int(sach,stt,gia_tri,state,dau_ra):
    if sach == []:
        return sach
    else:
        i = sach.pop()
    if state == 0:
        if(i[stt] == gia_tri):
            dau_ra.append(i)
    elif state == 1:
        if(i[stt] > gia_tri):
            dau_ra.append(i)
    elif state == 2:
        if(i[stt] < gia_tri):
            dau_ra.append(i)
    timKiem_Int(sach,stt,gia_tri,state,dau_ra)


def partition_tl(tl,sach, low, high):
    i = (low-1)
    print('high: ', high)
    pivot = tl[high][1]
  
    for j in range(low, high):
        if tl[j][1] <= pivot:
            i = i+1
            tl[i], tl[j] = tl[j], tl[i]
            sach[i],sach[j] = sach[j],sach[i]
        
    tl[i+1], tl[high] = tl[high], tl[i+1]
    sach[i+1], sach[high] = sach[high], sach[i+1]
    return (i+1)
  
  
  
def quickSort_tl(tl,sach, low, high):   
    if len(tl) == 1:
        return tl
    if low < high:
        pi = partition_tl(tl,sach, low, high)
        quickSort_tl(tl,sach, low, pi-1)
        quickSort_tl(tl,sach, pi+1, high)

def partition_s(sach,stt, low, high):
    i = (low-1)
    print('high: ', high)
    if(stt == 1):
        print('sach: ', sach)
        pivot = sach[high]
        print('pivot: ', pivot)
        pivot = pivot[2]
    elif(stt == 2):
        pivot = sach[high][3]
    elif stt == 3 :
        pivot = sach[high][4]
    elif stt == 4 :
        pivot = sach[high][5]
  
    for j in range(low, high):
        if(stt == 1):
            if sach[j][2] <= pivot:
                i = i+1
                sach[i],sach[j] = sach[j],sach[i]
        elif(stt == 2):
            if sach[j][3] <= pivot:
                i = i+1
                sach[i],sach[j] = sach[j],sach[i]
        elif stt == 3 :
            if sach[j][4] <= pivot:
                i = i+1
                sach[i],sach[j] = sach[j],sach[i]
        elif stt == 4 :
            if sach[j][5] <= pivot:
                i = i+1
                sach[i],sach[j] = sach[j],sach[i]
        
    sach[i+1], sach[high] = sach[high], sach[i+1]
    return (i+1)
  
  
  
def quickSort_s(sach,stt, low, high):   
    if len(sach) == 1:
        return sach
    if low < high:
        pi = partition_s(sach,stt, low, high)
        quickSort_s(sach,stt, low, pi-1)
        quickSort_s(sach,stt, pi+1, high)


# a =   [("123",),("12345",),("231321",)]
# c = []
# b = timKiem_String(a.copy(),0,"3",c)
# print(c)
# print("12" in "131112")