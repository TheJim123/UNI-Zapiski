function A = Prva (n)
% Generira nxn matriko, ki ima za poddiagonalo same -1, za diagonalo
% števila od 1 do n, nad diagonalo pa same 2.
A = triu(-1 * ones(n), -1);
for i = 1:n;
    A(i,i) = i;
    A(i, i+1:n) = 2;
end

end

