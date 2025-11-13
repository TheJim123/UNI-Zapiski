% Primer razcepa Choleskega

A = [4 6 2 -4; 6 18 0 3; 2 0 3 -4; -4 3 -4 23];
V = chol(A)';

disp('Matrika:');
disp(A);

disp('Faktor Choleskega matrike:');
disp(V);

a = [2; -6; 3; 3];
alpha = 100;
B = [A a; a' alpha];
b = V\a;
U = [V zeros(4,1); b' sqrt(alpha - norm(b)^2)];

disp('Razsirjena matrika:');
disp(B);

disp('Razcep Choleskega razsirjene matrike:');
disp(U);
fprintf([ ...
    'Norma razlike med faktorjem Choleskega, izracunim na podlagi\n' ...
    'faktorja Choleskega prvotne matrike, in faktorjem Choleskega,\n' ...
    'izracunanim z vgrajeno metodo: %d\n' ...
    ], ...
    norm(chol(B)'-U));
