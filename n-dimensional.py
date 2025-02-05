if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    
    coordinates = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:  
                    coordinates.append([i, j, k])

    print(coordinates)
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    sonuc = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    sonuc.append([i, j, k])
                    print(sonuc) #burda sonuç her seferinde döner 
                        [[0, 0, 0]]
                        [[0, 0, 0], [0, 0, 1]]
                        [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
                        biz direkt sonucu istediğimiz için printi döngüden önce yazdırırız.

'''
