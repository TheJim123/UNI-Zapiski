% Primer Thomasovega postopka

n = 1e4;

a = rand(n,1) + 2;
b = rand(n-1,1);
c = rand(n-1,1);

z = rand(n,1);

tic; x1 = thomas(a,b,c,z); t1 = toc;
fprintf('Resevanje sistema s Thomasovim postopkom: %g sekund\n', t1);

A = diag(a) + diag(b,1) + diag(c,-1);
tic; x2 = A\z; t2 = toc;
fprintf('Resevanje sistema z vgrajeno metodo: %g sekund\n', t2);

As = spdiags([[c; 0] a [0; b]],[-1 0 1],n,n);
tic; x3 = As\z; t3 = toc;
fprintf('Resevanje sistema z vgrajeno metodo v razprseni obliki: %g sekund\n', t3);
