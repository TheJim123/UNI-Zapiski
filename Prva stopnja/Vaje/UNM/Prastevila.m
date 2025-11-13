function [m, prastevila] = Prastevila(n)
stevila = 1:n-1;
so_prastevila = isprime(stevila);
prastevila = stevila(so_prastevila);
m = length(prastevila);
