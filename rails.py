n,m  = [int(i) for i in ''.split()]
railindex = [i for i in range(m*n)]
rail1 = [0,0,0,1,2,2,2,1,1]
rail2 = [0,1,2,2,2,1,0,0,1]
def rail_maker(n,m) :
    #rail1 = [0,0,0,1,2,2,2,1,1] координаты i, или row
    #max = m-1
    #длина равна n*m
    #rail2 = [0,1,2,2,2,1,0,0,1] координаты j, или col
    #max = n-1

    rail1 = [0 for i in range(m * n)]  # индекс строки
    rail2 = [0 for i in range(m * n)]  # индекс столбца
    # создаем два массива макимальной длины, куда будем заносить координаты

    rail1 =


    print(rail1)
    print()
    print(rail2)

    #return rail1, rail2

rail_maker(n,m)