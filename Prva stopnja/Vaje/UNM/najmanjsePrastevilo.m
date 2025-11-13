function p = najmanjsePrastevilo(n)
% vrne najmanjse prastevilo, ki je vecje od n

p = n+1;
while ~isprime(p)    
    p = p+1;
end

end
