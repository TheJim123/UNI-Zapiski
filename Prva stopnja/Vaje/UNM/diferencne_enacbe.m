% diferencne enacbe

a = [1 1/2 zeros(1,49)];
for n = 3:51
    a(n) = 5/2*a(n-1) - a(n-2);
end
subplot(3,1,1);
semilogy(0:50,a,'o');
title('Seznam a');

b = [1 1/3 zeros(1,49)];
for n = 3:51
    b(n) = 10/3*b(n-1) - b(n-2);
end
subplot(3,1,2);
semilogy(0:50,b,'o');
title('Seznam b');

rb = [zeros(1,49) 1 0];
for n = 49:-1:1
    rb(n) = 10/3*rb(n+1) - rb(n+2);
end
rb = rb/rb(1);
subplot(3,1,3);
semilogy(0:50,rb,'o');
title('Seznam b v obratnem vrstnem redu');

disp('Maksimalna absolutna napaka pri racunanju clenov b v obratnem vrstnem redu:');
disp(max(abs(rb - (1/3).^(0:50))));
