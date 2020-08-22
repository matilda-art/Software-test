package com.bit.java_image_server.dao;

import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;

// 单元测试-白盒测试
public class ImageDaoTest {

    @Test
    public void insert() {
        Image image=new Image();
        image.setImageName("15&16&30");
        image.setUploadTime("20-08-07 19:57:23");
        image.setSize(1200818);
        image.setMd5("2553a6426fc4c5b10a20f4de5a110421");
        image.setContentType("image/jpeg");
        image.setPath("C:\\Users\\18591\\image1\\photo\\2553a6426fc4c5b10a20f4de5a110421");
        ImageDao  imageDao = new ImageDao();
        imageDao.insert(image);

    }

    @Test
    public void selectAll() {
        ImageDao imageDao = new ImageDao();
        ArrayList<Image>  lists=imageDao.selectAll();
        System.out.println("size  = "+lists.size());
    }

    @Test
    public void selectOne() {
        ImageDao imageDao = new ImageDao();
        Image iamge = imageDao.selectOne(3432);
        System.out.println("imageName ="+iamge.getImageName());
    }

    @Test
    public void delete() {
        //创建实例
        ImageDao imageDao = new ImageDao();
        boolean flag = imageDao.delete(2626);
        System.out.println(flag);

    }

    @Test
    public void selectByMD5() {

    }

    @Test
    public void testInsert() {
    }

    @Test
    public void testSelectAll() {
    }

    @Test
    public void testSelectOne() {
    }

    @Test
    public void testDelete() {
    }

    @Test
    public void testSelectByMD5() {
    }

    @Test
    public void main() {
    }
}