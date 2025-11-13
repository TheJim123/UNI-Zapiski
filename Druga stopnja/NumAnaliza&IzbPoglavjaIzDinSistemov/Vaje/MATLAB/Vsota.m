function [S, s] = Vsota(x)
l = length(x);
s= zeros(1, l);
s(1) = x(1);
for i = 2:l
    s(i)= x(i) + s(i-1);
end
S = s(l)