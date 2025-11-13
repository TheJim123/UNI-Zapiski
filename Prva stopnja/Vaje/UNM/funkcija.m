function [m,prastevila] = funkcija(n)
% to je funkcija, ki poisce vsa prastevila, ki so manjsa od n, in vrne
% njihovo stevilo ter seznam, ki jih vsebuje

stevila = 1:n-1;
soprastevila = isprime(stevila);
prastevila = stevila(soprastevila);
m = length(prastevila);

end
