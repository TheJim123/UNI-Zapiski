function [A, B, C] = Druga (m, n)
% Sestavi naključno celoštevilsko matriko A, izračuna njen kvadrat kot
% matriko B in sestavi matriko C, katere elementi so kvadrati istoležečih
% elementov iz A.
A = randi(m, n);
B = A*A;
C = zeros(n);
for i = 1:n
    for j = 1:n
        C(i, j) = A(i, j) * A(i, j);
    end
end

end