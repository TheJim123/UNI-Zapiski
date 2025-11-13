X = (0:5)'/5;
VX = fliplr(vander(X));
s = svd(VX);
fprintf('Spektralna obcutljivost matrike V: %g \n', cond(VX));
fprintf('Kvocient najvecje in najmanjse singularne vrednosti V: %g \n', max(s)/min(s));

fprintf('\n');

N = 10;
kappa = zeros(1,N);
for n = 1:N
    Xn = (0:n)'/n;
    VXn = fliplr(vander(Xn));
    kappa(n) = cond(VXn);
    fprintf('Spektralna obcutljivost matrike V_%d: %g \n', n, kappa(n));
end
semilogy(1:N,kappa);
title('Rast obcutljivosti Vandermondovih matrik v logaritemski skali');

fprintf('\n');

p = ones(6,1);
a = VX\polyval(p,X);
fprintf('Norma napake za vektor koeficientov pri racunanju polinoma: %g \n', norm(a-p));

fprintf('\n');

Y = exp(2*pi*(0:N)'*1i/(N+1));
VY = fliplr(vander(Y));
fprintf('Spektralna obcutljivost Vandermondove matrike na tockah, ki ustrezajo korenom enote za n = %d: %g \n', N, cond(VY));
