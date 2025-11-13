function A = mat(n)

A = diag(n-(1:n-1),1) - 2*diag(1:n) + diag(n-(1:n-1),-1);

end
