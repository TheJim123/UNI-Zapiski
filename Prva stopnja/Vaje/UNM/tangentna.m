function [x,X,k] = tangentna(f,df,x0,tol,N)

g = @(x) x - f(x)/df(x);
[x,X,k] = iteracija(g,x0,tol,N);

end
