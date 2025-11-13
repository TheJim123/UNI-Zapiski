function [T, Z] = SDEeuler(F, a, b, Za, k)
	% Vhodni podatki:
	% F je SDE, zapisan kot niz 'F'
	% a in b sta krajisci intervala
	% Za = [x1(a), ..., xn(a)] zacetni pogoji
	% k je stevilo korakov metode
	% Izhodni podatki:
	% T vektor, ki vsebuje tk - vektor korakov
	% Z matrika, v kateri je na koordinati (i, j) priblizek vrednosti funkcije xj v tocki t(i+1)
	h = (b-a)/k; % Dolocimo velikost koraka
	n = length(Za); % Stevilo funkcij oz. enacb v sistemu
	%T = zeros(1, k+1); % Pripravimo vektor za korake
	Z = zeros(k+1, n); % Pripravimo matriko Z
	T=a:h:b; % a:h:b: je seznam stevil od a do b, s korakom h
	Z(1, :) = Za; % Prvo vrstico matrike Z napolnimo z zacetnimi pogoji
	
    for j = 1:k
		Z(j+1, :) = Z(j, :) + h*feval(F, T(j), Z(j, :)); % Poracunamo (j+1)-to vrstico matrike Z
    end