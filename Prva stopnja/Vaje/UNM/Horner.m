function p = Horner(Polinom, x)
% Na danem polinomu izvede Hornerjev postopek za izračun vrednosti polinoma
% v točki x. Za x predpostavimo, da je predstavljivo število. V vsakem
% koraku rezultat zaokroži na najbližje predstavljivo število v dvojiški
% bazi z mantiso dolžine 5. Polinom je seznam koeficientov od n-tega do
% zadnjega.
l = length(Polinom);
b = zeros(l, 1);
    function fl2 = fl(y) % Zaokroži dano število na najbližje predstavljivo
    [d, e] = log2(y);    % število v dvojiški bazi z mantiso dolžine 5
    fl2 = pow2(round(pow2(d, 5)), e-5);
    end
b(1) = fl(Polinom(1));
for i = 2:l
    b(i) = fl(Polinom(i) + fl(b(i-1)*x));
end
p = b(end);
end
