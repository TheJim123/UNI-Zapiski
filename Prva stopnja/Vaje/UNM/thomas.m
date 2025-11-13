function [x,l,u] = thomas(a,b,c,z)
% Opis:
%  thomas resi sistem s tridiagonalno matriko z LU razcepom brez
%  pivotiranja.
%
% Definicija:
%  [x,l,u] = thomas(a,b,c,z)
%
% Vhodni podatki:
%  a    glavna diagonala matrike,
%  b    diagonala nad glavno diagonalo matrike,
%  c    diagonala pod glavno diagonalo matrike,
%  z    stolpec, ki predstavlja desno stran sistema.
%
% Izhodni podatki:
%  x    resitev sistema A x = z, kjer je matrika A dolocena z diagonalami
%       a, b, c,
%  l    diagonala pod glavno diagonalo enic matrike L v LU razcepu A
%       (ostali elementi L so enaki 0),
%  u    glavna diagonala matrike U v LU razcepu matrike A (diagonala nad
%       glavno diagonalo je enaka b, vsi ostali elementi U so enaki 0).

n = length(a);
u = zeros(n,1);
l = zeros(n-1,1);

% LU razcep (3n-3 operacij)
u(1) = a(1);
for k = 1:n-1
    l(k) = c(k)/u(k);
    u(k+1) = a(k+1) - l(k)*b(k);
end

% prema substitucija (2n-2 operacij)
y = z;
for k = 2:n
    y(k) = z(k) - l(k-1)*y(k-1);
end

% obratna substitucija (3n-2 operacij)
x = y;
x(n) = y(n)/u(n);
for k = n-1:-1:1
    x(k) = (y(k) - b(k)*x(k+1))/u(k);
end

end
