if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = input()
        b = []
        c = 1
        for j in range(len(a) - 1):
            if a[j] == a[j + 1]:
                c = c + 1
            else:
                b.append(a[j])
                b.append(str(c))
                c = 1
        b.append(a[-1])
        b.append(str(c))
        if len(''.join(b)) < len(a):
            print("YES")
        else:
            print("NO")