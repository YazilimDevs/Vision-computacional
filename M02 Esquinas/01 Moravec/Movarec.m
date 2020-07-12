img = rgb2gray(imread('https://i1.wp.com/duochess.es/wp-content/uploads/2019/06/22-TABLERO-POPULAR-50-CM.jpg?fit=800%2C800&ssl=1'));
img_moravec= feature_detect(img)
imshow(img_moravec)
 