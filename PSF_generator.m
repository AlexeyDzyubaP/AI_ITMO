%%
clear
clc
%%



x = -2:0.0134:2;
[X,Y] = meshgrid(x,x);
[theta,r] = cart2pol(X,Y);
idx = r<=1;
z = zeros(size(X));
z1 = zeros(size(X));



no_of_aberrations = 8;
nm_matrix = [1 1; 2 0; 2 2; 3 1; 3 3; 4 0; 4 2; 4 4]; 
alf_1 = 0:0.01:0.5; % (alf_1*2*pi = c1; (0.5-alf_1(idx_alf))*2*pi = c2) (c1*zernfun_1 + c2*zernfun_2 - ????)
alf = 40;  


for idx_1 = 1:no_of_aberrations
    for idx_2 = 1:no_of_aberrations
        for idx_alf = 1:50
            %?????? ???? 
            z(idx) = (alf_1(idx_alf)*2*pi)*zernfun(nm_matrix(idx_1,1),nm_matrix(idx_1,2),r(idx),theta(idx))+((0.5-alf_1(idx_alf))*2*pi)*zernfun(nm_matrix(idx_2,1),nm_matrix(idx_2,2), r(idx),theta(idx));
            
            %
            z1(idx) = (abs(exp(i*alf*r(idx).*cos(theta(idx))) + exp(i*z(idx)))).^2;
          
            %????? ??????
            seq = "n" + nm_matrix(idx_1,1) + "m" + nm_matrix(idx_1,2) + "\" + "_n" + nm_matrix(idx_1,1) + "m" + nm_matrix(idx_1,2) + "a" + (alf_1(idx_alf)) + "_" + "n" + nm_matrix(idx_2,1) + "m" + nm_matrix(idx_2,2) + "a" + ((0.5-alf_1(idx_alf))) + "_z500_intens.png";
            filename = "C:\Users\Alex\matlab funcs\Interfer_2x\" + seq;
            imwrite(mat2gray(z1), filename)

            


        end
        
    end
    
end