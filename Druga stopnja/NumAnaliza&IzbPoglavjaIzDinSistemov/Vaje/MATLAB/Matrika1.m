function [M, t] = Matrika1 (n, m)
% Zgradi matriko reda n x m z elementi M(i, j) = i * j / (i + j)
if ~exist("m","var")
    m = n;
end

M = ones(n, m);
t = 1;
for i = 1:n 
    for j = 1:m
        M(i, j) = (i * j) / (i + j);
        t = t * M(1, j);
    end
end
