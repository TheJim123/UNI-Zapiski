function x = lusolve(A,b)
% Opis:
%  lusolve izracuna resitev sistema Ax = b z uporabo LU razcepa ter premih
%  in obratnih substitucij
%
% Definicija:
%  x = lusolve(A,b)
%
% Vhodna podatka:
%  A    matrika sistema,
%  b    vektor sistema
%
% Izhodni podatek:
%  x    vektor, ki je resitev sistema Ax = b

n = size(A,1);

% LU razcep z delnim pivotiranjem
[L,U,P] = lu(A);

% prema substitucija
y = P*b;
for i = 2:n
    for k = 1:i-1
        y(i) = y(i) - L(i,k)*y(k);
    end
end

% obratna substitucija
x = y;
for i = n:-1:1
    for k = i+1:n
        x(i) = x(i) - U(i,k)*x(k);
    end
    x(i) = x(i)/U(i,i);
end

end
