G = @(t, x) [x(2), 6*cos(t) - x(1)];
f = @(t) 2.*cos(t) + 3.*sin(t) + 3.*t.*sin(t);
%
[T1, Z1] = SDEeuler(G, 0, 1, [2, 3], 20);
[T2, Z2] = SDErk4(G, 0, 1, [2, 3], 20);
F = f(T1);
%
plot(T1, Z1(:, 1), 'DisplayName','xEuler')
hold on
plot(T2, Z2(:, 1), 'DisplayName','xRK4')
hold on
%
%plot(T1, Z1(:, 2), 'DisplayName', 'yEuler')
%hold on
%plot(T2, Z2(:, 2), 'DisplayName', 'yRK4')
%hold on
%
plot(T1, F, 'DisplayName', 'xAnaliticna')
legend()
%