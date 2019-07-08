import java.io.*;
import java.util.*;

public class PorownajZbiory {



        public static void main(String[] args) {

            String nazwaPlikuEB;
            String nazwaPlikuMB;
            BufferedReader w = new BufferedReader(new InputStreamReader(System.in));

            try{
                System.out.print("Podaj nazwe pliku z imionami EB:");
                nazwaPlikuEB = w.readLine() + ".txt";
                Scanner sc1 = new Scanner(new File(nazwaPlikuEB));
                List<String> namesEB = new ArrayList<String>();

                while (sc1.hasNext()) {
                    namesEB.add(sc1.next());
                }
                sc1.close();

                System.out.print("Podaj nazwe pliku z imionami MB:");
                nazwaPlikuMB = w.readLine() + ".txt";
                Scanner sc2 = new Scanner(new File(nazwaPlikuMB));
                List<String> namesM = new ArrayList<String>();

                while (sc2.hasNext()) {
                    namesM.add(sc2.next());
                }
                sc2.close();
				
				List<String> namesEBUpper = namesEB.stream().map(String::toUpperCase).collect(toList());

                Set<String> zbior1 = new HashSet<String>(namesEBUpper);

                Set<String> zbior2 = new HashSet<String>(namesM);

                Set<String> zbior3 = new HashSet<String>(zbior1);

                zbior3.removeAll(zbior2);
				
				

                // wypisanie imion do analizy

                System.out.println("Brak imion w słowniku MB " + zbior3);


                PrintWriter zapis = new PrintWriter("listaImionDoAnalizy.txt");
                zapis.print(zbior3);
                zapis.close();

            } catch(Exception e) {System.out.println("Blad"+e.getMessage());}
        }
}
