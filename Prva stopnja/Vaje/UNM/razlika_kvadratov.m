% razlika kvadratov

% racunanje v dvojni natancnosti
dx = 2^-1 + 2^-13 + 2^-24;
dy = 2^-1 + 2^-13;
dz = dx^2 - dy^2;

% racunanje v enojni natancnosti
x = single(dx);
y = single(dy);
z1 = x*x - y*y;
z2 = (x-y)*(x+y);

e1 = abs(dz-double(z1))/abs(dz);
e2 = abs(dz-double(z2))/abs(dz);

fprintf('Napaka pri racunanju x*x - y*y:     %g\n', e1);
fprintf('Napaka pri racunanju (x-y) * (x+y): %g\n', e2);
