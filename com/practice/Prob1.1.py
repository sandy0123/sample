
'''
Created on Feb 6, 2014

@author: parsa12
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
    test1="Sandeep"
    unique(test1)
    
    test1 = 'Sandy'
    unique(test1)
    
    test1=" Sand  ep "
    unique(test1)
    
