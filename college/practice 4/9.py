def simple_interest(P,R,T):
    S_I = P*R*T/100
    return S_I

P = int(input("Enter the principle amount : "))
R = int(input("Enter the Rate at which the amount is provided : "))
T = int(input("Enter the time span(in years) : "))
print(simple_interest(P,R,T))
