num = [0, 1]


def truthtable(n):
    p = []
    return nextnum(n, p)


def nextnum(n, p):
    if(len(p) == n):
        print(p)
        return
    for i in num:
        p.append(i)
        nextnum(n, p)
        p.pop()


truthtable(3)

''' 
以truthtable(3)為例
程式先call truthtane(3)
此時n=3 p=[] 傳入 nextnum(n, p)
若p的長度 = n (此例為3)時回到上層
接下來先拿到[0] call nextnum 獲得 [0,0] 再call nextnum 獲得[0,0,0] (三層nexnum)
因長度 = n 回到上層 然後pop 得[0,0] 繼續跑完第三層nextnum的for 也就是 append(1) 得到 [0, 0, 1]
跑第二層 nextnum的for 得 [0,1]再跑第三層的for得[0,1,0] [0,1,1] 跑第一層nextnum 得[1]後重放前述動作


      0           1            
     /  \        /  \
    0    1      0    1
  /  \  / \    / \  /  \
0     1 0  1   0  1 0   1

'''
