function y = f(x)
if x < 6
    y = 2;
elseif (6 <= x && x <= 20)
    y = x - 4;
else
    y = -x;
end