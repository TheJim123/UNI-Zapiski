function [x,X,k] = iteracija(g,x0,tol,N)
% Funkcija izvede navadno iteracijo.
% 
% Vhodni podatki:
% g     iteracijska funkcija
% x0    zacetni priblizek
% tol   toleranca absolutne razlike med zaporednima priblizkoma
% N     maksimalno stevilo korakov
%
% Izhodni podatki:
%  x    koncni priblizek
%  X    seznam vseh priblizkov
%  k    stevilo opravljenih korakov

X = x0;
for k = 1:N
    X(k+1) = g(X(k));
    if abs(X(k+1)-X(k)) < tol
        break;
    end
end
x = X(k+1);

end
