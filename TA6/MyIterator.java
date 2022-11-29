package TA6;

import java.util.ArrayList;
import java.util.Iterator;

public class MyIterator {

    public static void main(String[] args) {

        ArrayList<String> countries = new ArrayList<String>();
        countries.add("Argentina");
        countries.add("Brazil");
        countries.add("Spain");
        countries.add("Germany");
        countries.add("Portugal");
        countries.add("France");
        countries.add("Serbia");
        countries.add("Cameroon");

        Iterator<String> it = countries.iterator();
        System.out.println("--- only first element ----");
        System.out.println(it.next());
        System.out.println("--- while has next... ----");
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        System.out.println("--- remove items from collection by iterator ----");
        Iterator<String> it2 = countries.iterator();
        while (it2.hasNext()) {
            String country = it2.next();
            if (country.startsWith("S")) {
                System.out.println(country+" deleted!");
                it2.remove();
            }
        }
        System.out.println(countries);
    }
}

