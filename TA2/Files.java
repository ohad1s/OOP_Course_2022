package TA2;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Files {
    public static void create_file(String path){
        try{
            File my_file= new File(path);
            if (my_file.createNewFile()){
                System.out.println("Created: "+ my_file.getName());
            }
            else {
                System.out.println("File already exists");
            }
        }
        catch (IOException e){
            System.out.println("error");
            e.printStackTrace();
        }
    }

    public static void wrire_to_file(String path, String str){
        try{
            FileWriter fw= new FileWriter(path);
//            fw.write(str);
//            fw.append(str);
            fw.append(str);
            fw.close();
            System.out.println("Ciii");
        }
        catch (IOException e){
            System.out.println("error");
            e.printStackTrace();
        }
    }


    public static void main(String[]args){
//        create_file("ohad.txt");
        wrire_to_file("ohad.txt", "Ohad Shirazi");
        wrire_to_file("ohad.txt","gdgeqgqetghqet");

    }
}
