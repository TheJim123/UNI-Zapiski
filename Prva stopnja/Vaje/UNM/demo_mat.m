n = 1000;
A = mat(n);

tic; a1 = norm(A,1); ta1 = toc;
tic; a2 = norm(A,2); ta2 = toc;
tic; aInf = norm(A,Inf); taInf = toc;
tic; aFro = norm(A,'fro'); taFro = toc;
tic; amax = max(max(abs(A))); tamax = toc;

fprintf('1-norma: %g (cas izracuna: %g s)\n', a1, ta1);
fprintf('2-norma: %g (cas izracuna: %g s)\n', a2, ta2);
fprintf('Inf-norma: %g (cas izracuna: %g s)\n', aInf, taInf);
fprintf('Frobeniusova norma: %g (cas izracuna: %g s)\n', aFro, taFro);
fprintf('N_Inf: %g (cas izracuna: %f s)\n', amax, tamax);

sqn = sqrt(n);
a2m = max([aFro/sqn a1/sqn aInf/sqn amax]);
a2M = min([aFro sqn*a1 sqn*aInf 10*amax sqrt(a1*aInf)]);
fprintf('Spodnja meja za 2-normo: %g\n', a2m);
fprintf('Zgornja meja za 2-normo: %g\n', a2M);
