/*
 * Arrays.java
 *
 */

/**
 *
 * @author aharris
 */
public class Arrays {

    public static void main(String args[]){
        String[] games = {
            "Super Mario Bros.",
            "Legend of Zelda",
            "Tetris",
            "Civilization II",
            "Super Mario 64",
            "Pirates!",
            "StarCraft",
            "Street Fighter II",
            "Star Wars TIE Fighter",
            "Super Metroid"
        };
        System.out.println(games[3]);
        
        for (int i = 0; i < games.length; i++){
            //System.out.printf("%d) %s\n", i+1, games[i]);
        	System.out.println((i + 1) + ") " + games[i]);
        } // end for

        //creating an empty array
        String[] gameSeries = new String[3];
        gameSeries[0] = "Rogue";
        gameSeries[1] = "Civilization";
        gameSeries[2] = "Command and Conquer";

        for (int i = 0; i < gameSeries.length; i++){
          System.out.println(gameSeries[i]);
        } // end for loop

        
    } // end main
    
    
}
