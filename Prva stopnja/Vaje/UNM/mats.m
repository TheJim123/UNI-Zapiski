function A = mats(n)

A = spdiags([n-(1:n)' -2*(1:n)' n-(0:n-1)'], [-1 0 1], n, n);

end
