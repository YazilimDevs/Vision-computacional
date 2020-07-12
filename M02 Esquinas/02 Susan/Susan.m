img = rgb2gray(im2double(imread('https://i1.wp.com/duochess.es/wp-content/uploads/2019/06/22-TABLERO-POPULAR-50-CM.jpg?fit=800%2C800&ssl=1')));
[map, r, c] = susanCorner(img);
figure,imshow(img),hold on
plot(c,r,'o')