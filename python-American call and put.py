
import numpy as np

def Binomial(n, s0, K, r, σ,δ,t, PutCall):
    h=t/n
    z=(r-δ)*h
    q=σ*np.sqrt(h)
    u=np.exp(z+q)
    d=np.exp(z-q)
    a=np.exp(-r*h)
    pu=a*((np.exp(z)-d)/(u-d))
    pd=a*((u-np.exp(z))/(u-d))
 

    #Stock price
    s = np.zeros((n+1,n+1))
    s[0,0] = s0
    for i in range(1,n+1):
        s[i,0] = s[i-1,0]*u
        for j in range(1,i+1):
            s[i,j] = s[i-1,j-1]*d
    
    #option value at final node   
    v = np.zeros((n+1,n+1))
    for j in range(n+1):
        if PutCall=="C": # Call
            v[n,j] = max(0, s[n,j]-K)
        elif PutCall=="P": #Put
            v[n,j] = max(0, K-s[n,j])
    
    #backward calculation for option price    
    for i in range(n-1,-1,-1):
        for j in range(i+1):
                if PutCall=="P":
                    v[i,j] = max(K-s[i,j], pu*v[i+1,j]+pd*v[i+1,j+1])
                elif PutCall=="C":
                    v[i,j] = max(s[i,j]-K, pu*v[i+1,j]+pd*v[i+1,j+1])
    return v
if __name__ == "__main__":
    print("American option price:")
    option_price = Binomial(1000, 41, 40, 0.08, 0.3, 0,1, PutCall="P")
    print(option_price)
    