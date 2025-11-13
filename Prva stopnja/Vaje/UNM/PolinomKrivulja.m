t = linspace(0, 1, 1000);
x = polyval([-17, 52, -48, 8, 0], t);
z1 = polyval(polyder([-17, 52, -48, 8, 0]), t);
z2 = polyval(polyder(polyder([-17, 52, -48, 8, 0])), t);
y = polyval([-19.5, 64, -60, 16, 0], t);
w1 = polyval(polyder([-19.5, 64, -60, 16, 0]), t);
w2 = polyval(polyder(polyder([-19.5, 64, -60, 16, 0])), t);
for i = 1:1000
    if ~( 0.5 <= (x(i)^2 + y(i)^2) && (x(i)^2 + y(i)^2) <= 1)
            x(i) = 0;
            y(i) = 0;
    end
end
xi = x > 0;
yi = y > 0;
plot(x(xi),y(yi));

% Ukrivljenost:
% ukrivljenost (x, y) = 
% abs(polyder(x)*polyder(polyder(y)) - polyder(y)*polyder(polyder(x))) /
% / (polyder(x)^2 + polyder(y)^2)^(1.5)
