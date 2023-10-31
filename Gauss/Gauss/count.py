def count(X1,X2,X3,Y1,Y2,Y3,Z1,Z2,Z3,F1,F2,F3):
        #Вычисления
        #Приводим А11 к 1 или -1
        if (X1 != 1 or X1 != -1):
            if (X2 == 1 or X2 == -1):
                X,Y,Z,F = X1,Y1,Z1,F1
                X1,Y1,Z1,F1 = X2,Y2,Z2,F2
                X2,Y2,Z2,F2 = X,Y,Z,F
            elif (X3 == 1 or X3 == -1):
                X,Y,Z,F = X1,Y1,Z1,F1
                X1,Y1,Z1,F1 = X3,Y3,Z3,F3
                X3,Y3,Z3,F3 = X,Y,Z,F
            elif (Y1%X1==0 and Z1%X1==0 and F1%X1==0):
                X1,Y1,Z1,F1 = X1/X1,Y1/X1,Z1/X1,F1/X1
            else:
                i=1
                while(True):
                    if (X1+X2*i==1 or X1+X2*i==-1):
                        X1 = X1+X2*i
                        Y1 = Y1+Y2*i
                        Z1 = Z1+Z2*i
                        F1 = F1+F2*i
                        break
                    elif (X1-X2*i==1 or X1-X2*i==-1):
                        X1 = X1-X2*i
                        Y1 = Y1-Y2*i
                        Z1 = Z1-Z2*i
                        F1 = F1-F2*i
                        break
                    elif (X1+X3*i==1 or X1+X3*i==-1):
                        X1 = X1+X3*i
                        Y1 = Y1+Y3*i
                        Z1 = Z1+Z3*i
                        F1 = F1+F3*i
                        break
                    elif (X1-X3*i==1 or X1-X3*i==-1):
                        X1 = X1-X3*i
                        Y1 = Y1-Y3*i
                        Z1 = Z1-Z3*i
                        F1 = F1-F3*i
                        break
                    i+=1
        
        #Приводим А21 и А23 к 0
        if (X2 != 0):
            i=1
            while(True):
                if (X2+X1*i==0):
                    X2 = X2+X1*i
                    Y2 = Y2+Y1*i
                    Z2 = Z2+Z1*i
                    F2 = F2+F1*i
                    break
                elif (X2-X1*i==0):
                    X2 = X2-X1*i
                    Y2 = Y2-Y1*i
                    Z2 = Z2-Z1*i
                    F2 = F2-F1*i
                    break
                elif (X2+X3*i==0):
                    X2 = X2+X3*i
                    Y2 = Y2+Y3*i
                    Z2 = Z2+Z3*i
                    F2 = F2+F3*i
                    break
                elif (X2-X3*i==0):
                    X2 = X2-X3*i
                    Y2 = Y2-Y3*i
                    Z2 = Z2-Z3*i
                    F2 = F2-F3*i
                    break
                i+=1
        if (X3 != 0):
            i=1
            while(True):
                if (X3+X1*i==0):
                    X3 = X3+X1*i
                    Y3 = Y3+Y1*i
                    Z3 = Z3+Z1*i
                    F3 = F3+F1*i
                    break
                elif (X3-X1*i==0):
                    X3 = X3-X1*i
                    Y3 = Y3-Y1*i
                    Z3 = Z3-Z1*i
                    F3 = F3-F1*i
                    break
                elif (X3+X2*i==0):
                    X3 = X3+X2*i
                    Y3 = Y3+Y2*i
                    Z3 = Z3+Z2*i
                    F3 = F3+F2*i
                    break
                elif (X3-X2*i==0):
                    X3 = X3-X2*i
                    Y3 = Y3-Y2*i
                    Z3 = Z3-Z2*i
                    F3 = F3-F2*i
                    break
                i+=1
        if (Y2==0):
            X,Y,Z,F = X2,Y2,Z2,F2
            X2,Y2,Z2,F2 = X3,Y3,Z3,F3
            X3,Y3,Z3,F3 = X,Y,Z,F
        if (Z3==0):
            X,Y,Z,F = X3,Y3,Z3,F3
            X3,Y3,Z3,F3 = X2,Y2,Z2,F2
            X2,Y2,Z2,F2 = X,Y,Z,F
        
        #Приводим А22 к 1 или -1
        if (Y2 != 1 or Y2 != -1):
            if (Z2%Y2==0 and F2%Y2==0):
                Y2,Z2,F2 = Y2/Y2,Z2/Y2,F2/Y2
            else:
                i=1
                while(True):
                    if (Y2+Y3*i==1 or Y2+Y3*i==-1):
                        Y2 = Y2+Y3*i
                        Z2 = Z2+Z3*i
                        F2 = F2+F3*i
                        break
                    elif (Y2-Y3*i==1 or Y2-Y3*i==-1):
                        Y2 = Y2-Y3*i
                        Z2 = Z2-Z3*i
                        F2 = F2-F3*i
                        break
                    i+=1

        #Приводим А32 к 0
        if (Y3 != 0):
            i=1
            while(True):
                if (Y3+Y2*i==0):
                    Y3 = Y3+Y2*i
                    Z3 = Z3+Z2*i
                    F3 = F3+F2*i
                    break
                elif (Y3-Y2*i==0):
                    Y3 = Y3-Y2*i
                    Z3 = Z3-Z2*i
                    F3 = F3-F2*i
                    break
                i+=1
        
        #Приводим А33 к 1 или -1
        if (Z3 != 1 or Z3 != -1):
            if (F3%Z3==0):
                Z3,F3 = Z3/Z3,F3/Z3

        if (X1==-1):
            X1,Y1,Z1,F1 = X1*(-1),Y1*(-1),Z1*(-1),F1*(-1)
        if (Y2==-1):
            Y2,Z2,F2 = Y2*(-1),Z2*(-1),F2*(-1)
        if (Z3==-1):
            Z2,F2 = Z2*(-1),F2*(-1)
        Z = F3/Z3
        Y = F2 - (Z2*Z)
        X = F1 - (Y1*Y) - (Z1*Z)
        return X,Y,Z

