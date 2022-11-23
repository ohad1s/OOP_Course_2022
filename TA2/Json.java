package TA2;

import com.google.gson.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Json {

    static String star = "********************************";
    static boolean print = true;

    /**
     * method that serialize a TA2.student object to json file
     * @return the string of the json we got
     */
    private static String Serialize(){
        if(print)System.out.println(star+"Serialize"+star+"\n");
        student a = new student("Ploni", "Almoni", 111111111, 21, "Ariel", "Math");
//        Gson gson = new Gson();
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String jsonS = gson.toJson(a);
        try {
            FileWriter fw=new FileWriter("ploni.json");
            fw.write(gson.toJson(a));
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if(print)System.out.println(jsonS);
        return jsonS;
    }

    /**
     * method that DeSerialize a json file to a TA2.student object
     */
    private static void DeSerialization(){
                Gson gson = new Gson();
        if(print)System.out.println(star+"DeSerialization"+star+"\n");
        try{
            FileReader FR = new FileReader("src\\TA2\\student.json");
            BufferedReader BR = new BufferedReader(FR);
            student ohad_student= gson.fromJson(BR, student.class);
            System.out.println(ohad_student);
        }
        catch (Exception err){
            err.printStackTrace();
        }
    }

    public static  void main(String[]args){
//        Serialize();
        DeSerialization();
    }
}
