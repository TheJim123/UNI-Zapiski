function A = Tretja (x, y)
% S pomočjo vektorjev x in y sestavi matriko A
n = length(x);
m = length(y);
A = zeros(n, m);
for i = 1:n
    for j = 1:m
        if y(j) == 0
            A(i, j) = x(i);
        else
            A(i, j) = x(i) / y(j);
        end
    end
end
end