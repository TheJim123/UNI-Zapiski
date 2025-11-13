function je = JeMagicniKvadrat(A)
[m, n] = size(A);
if m ~= n
    je = false;
elseif ~isequal(unique(A)', (1:n^2))
        je = false;
else
    S = sum(A, 1);
    if any(S ~= S(1))
        je = false;
    else
        if any(sum(A, 2) ~= S(1))
            je = false;
        elseif sum(diag(A)) ~= S(1)
                je = false;
        elseif sum(diag(A(:, n:-1:1))) ~= S(1)
                je = false;
        else
            je = true;
        end
    end
end


