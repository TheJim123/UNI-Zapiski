function p = najvecjePrastevilo(n)
% vrne najvecje prastevilo, ki je manjse od n

for p = n-1:-1:2
    if isprime(p)
        break;
    elseif mod(p,2) == 0
        fprintf('%d je sodo stevilo\n',p);
    else
        fprintf('%d je liho stevilo\n',p);
    end
end

end
