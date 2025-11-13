% primeri navadne iteracije

g1 = @(x) x^2 - 2;
g2 = @(x) sqrt(x+2);
g3 = @(x) 1 + 2/x;
g4 = @(x) (x^2+2)/(2*x-1);
g = g4;

tol = 1e-8;
N = 100;

d = 601;
X0 = linspace(-2,4,d);
K = zeros(1,d);
M = zeros(1,d);

for i = 1:d
    x0 = X0(i);
    [x,~,k] = iteracija(g,x0,tol,N);
    K(i) = k;
    if abs(x-2) < tol
        M(i) = 1;
    elseif abs(x+1) < tol
        M(i) = 2;
    else
        M(i) = 3;
    end
end

plot(X0(M==1),K(M==1),'ro', X0(M==2),K(M==2),'bo', X0(M==3),K(M==3),'go');
legend('Konvergenca k 2', 'Konvergenca k -1', 'Konvergenca ?');
