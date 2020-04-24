import math
from decimal import *

class Solution :
    def main(self):
        try:
            getcontext().prec = 4
            T = int(input()) 
            for t in range(T):
                result = 0.0
                W,H,L,U,R,D = map(int, input().split())

                if (U == 1 and D == H) or (L == 1 and R == W):
                    result = 0.0
                else:

                    if L > 1 and D < H:
                        dist = D-1
                        pt = -D
                        result += math.pow(2, pt)
                        for j in range(1,L-1):
                            l = dist + j
                            pt += math.log2(l/j)
                            result += math.pow(2, pt-j)
                    
                    if R < W and U > 1:
                        dist = R-1
                        pt = -R
                        result += math.pow(2, pt) 
                        for j in range(1,U-1):
                            l = dist + j
                            pt += math.log2(l/j)
                            result += math.pow(2, pt-j)    
                print("Case #{}: {}".format(str(t+1),float(Decimal(result))))    
        except:
           stop = 0

if __name__=="__main__":
    sl = Solution()
    sl.main()