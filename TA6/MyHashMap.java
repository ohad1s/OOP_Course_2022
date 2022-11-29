package TA6;
import java.util.HashMap; // import the HashMap class
public class MyHashMap {
    public static void main(String[]args){
        HashMap<String, Integer> WorldCupScore = new HashMap<String, Integer>();
        // Add keys and values (Country, City)
        WorldCupScore.put("England", 4);
        WorldCupScore.put("Germany", 1);
        WorldCupScore.put("Spain", 4);
        WorldCupScore.put("USA", 1);
        WorldCupScore.put("Brazil", 6);

        System.out.println(WorldCupScore);

        System.out.println(WorldCupScore.get("Spain"));

        System.out.println(WorldCupScore.remove("USA"));

        for (String NationalTeam: WorldCupScore.keySet()) {
            System.out.println(NationalTeam);
        }

        for (Integer score : WorldCupScore.values()) {
            System.out.println(score);
        }
    }

}
