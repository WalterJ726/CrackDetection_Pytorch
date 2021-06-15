clear all;
clc;
file_path1 ='E:\������\����ͼ����\image\image1\test\';
img_path_list1 = dir(strcat(file_path1,'*.jpg'));
Len= length(img_path_list1);                                            % ��ȡͼ�������� (����ͼƬ�ļ�����ͼƬ����һ��)
for k=0:Len
    Img = imread([file_path1,num2str(k),'.jpg']);
    adjImg=imadjust(Img,[0.1,0.30],[0,1]);

    se=strel('disk',5);
    imbImg=imbothat(adjImg,se);

    H = fspecial('gaussian',3,3);
    filImg = imfilter(imbImg,H,'replicate');

    bwImgSmall=im2bw(filImg,20/255);

    recImg=bwareaopen(bwImgSmall,100);
    
    filename=['E:\������\����ͼ����\image\image2\',num2str(k),'.jpg'];
    imwrite(recImg,filename);
end