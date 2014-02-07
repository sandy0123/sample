'''
'''

def unique(str):
    if str is None:
        return True
    elif str.strip() is "":
        return True
    else:
        for i in range(0,len(str)):
            if str[i] == " ":
                continue
            else:
                for j in range(i+1,len(str)):
                    if str[i] == str[j]:
                         print("Not unique :"+str[i])
                         return False
            
    return True

if __name__ == '__main__':
    test1="Aakash"
    unique(test1)
    
    test1 = 'Bansal'
    unique(test1)
    
    test1=" Aa kas sh "
    unique(test1)
    
