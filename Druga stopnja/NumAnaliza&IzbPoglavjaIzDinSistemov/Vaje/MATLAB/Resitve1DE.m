F = @(t, x) x(1).*[2, 2, 1] + x(2).*[3, 1, 2] + x(3).*[1, -3, 3];
%
[T1, Z1] = SDEeuler(F, 0, 1, [-2.7, 2.8, 2.1], 20);
[T2, Z2] = SDErk4(F, 0, 1, [-2.7, 2.8, 2.1], 20);
 plot(T1, Z1(:, 1), 'DisplayName','xEuler')
 hold on
 plot(T2, Z2(:, 1), 'DisplayName','xRK4')
 hold on
 plot(T1, Z1(:, 2), 'DisplayName', 'yEuler')
 %
 hold on
 %
 plot(T2, Z2(:, 2), 'DisplayName', 'yRK4')
 hold on
 plot(T1, Z1(:, 3), 'DisplayName', 'zEuler')
 hold on
 plot(T2, Z2(:, 3), 'DisplayName', 'zRK4')
legend()
%