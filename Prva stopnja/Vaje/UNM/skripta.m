% to je skripta, ki izpise vsa prastevila, ki so manjsa od 100
n = 100;
stevila = 1:n-1;
soprastevila = isprime(stevila);
prastevila = stevila(soprastevila);
disp(prastevila);
