function [xt, yt] = Tezisce(A)
[m, n] = size(A);
M = sum(sum(A));
xt = (1:n)*sum(A,1)'/M;
yt = (1:m)*sum(A,2)/M;
