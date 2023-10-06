
def calcula_media(v):   
    # v e' uma variavel local
    print("dentro - antes")
    print(v)
    v=10
    print("dentro - depois")
    print(v)
    

# main
if __name__ == '__main__':
    v = 4
    calcula_media(v)
    print(v)
