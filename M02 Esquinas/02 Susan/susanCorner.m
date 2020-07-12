function [ map r c ] = susanCorner( img )


maskSz = [7 7];
fun = @(img) susanFun(img);
map = nlfilter(img,maskSz,fun);
[r c] = find(map);

end

function res = susanFun(img)
%Mascara de radio fijo
mask = [...
	0 0 1 1 1 0 0
	0 1 1 1 1 1 0
	1 1 1 1 1 1 1
	1 1 1 1 1 1 1
	1 1 1 1 1 1 1
	0 1 1 1 1 1 0
	0 0 1 1 1 0 0];

%Umbrales
thGeo = (nnz(mask)-1)*.2;
thGeo1 = (nnz(mask)-1)*.4;
thGeo2 = (nnz(mask)-1)*.4;
thT = .07;
thT1 = .04;

sz = size(img,1);
% Se compara los pixeles y  se gnera el area USAN 
usan = ones(sz)*img(round(sz/2),round(sz/2));

similar = (abs(usan-img)<thT);
similar = similar.*mask;
res = sum(similar(:));

%si las localizaciones donde el número de pixeles en el área USAN alcanza
%un mínimo local y por debajo del umbral se considera como esquina
if res < thGeo
	dark = nnz((img-usan<-thT1).*mask);
	bright = nnz((img-usan>thT1).*mask);
	res = min(dark,bright)<thGeo1 && max(dark,bright)>thGeo2;

else
	res = 0;
end

end