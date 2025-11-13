n = 1000;
A = mats(n);

a1 = norm(A,1);
a2 = normest(A);
aInf = norm(A,Inf);
aFro = norm(A,'fro');
amax = full(max(max(abs(A))));

fprintf('1-norma: %g \n', a1);
fprintf('Ocena za 2-normo: %g \n', a2);
fprintf('Inf-norma: %g\n', aInf);
fprintf('Frobeniusova norma: %g \n', aFro);
fprintf('N_Inf: %g \n', amax);

sqn = sqrt(n);
a2m = max([aFro/sqn a1/sqn aInf/sqn amax]);
a2M = min([aFro sqn*a1 sqn*aInf 10*amax sqrt(a1*aInf)]);
fprintf('Spodnja meja za 2-normo: %g\n', a2m);
fprintf('Zgornja meja za 2-normo: %g\n', a2M);
