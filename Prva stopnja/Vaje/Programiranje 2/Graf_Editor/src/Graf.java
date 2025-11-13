import java.util.*;
import java.io.*;
public class Graf {
	int stevec;
	Map<String, Tocka> tocke;
	
	public Graf() {
		stevec = 0;
		tocke = new HashMap<String, Tocka>();
	}
	
	public Tocka toèka(String ime) {
		return tocke.get(ime);
	}
	
	public boolean povezava(Tocka t1, Tocka t2) {
		
		return t1.sosedi.contains(t2);
	}
	
	public Tocka dodajTocko(String ime) {
		Tocka v = toèka(ime);
		if (v == null) {
			v = new Tocka(ime);
			tocke.put(ime, v);
		}
		return v;
	}
	
	public Tocka dodajTocko() {
		while (true) {
			String n_ime = Integer.toString(++stevec);
			Tocka v = toèka(n_ime);
			if (v != null) continue;
			v = new Tocka(n_ime);
			tocke.put(n_ime, v);
			return v;
		}
	}
	
	public void dodajPovezavo(Tocka t1, Tocka t2) {
		if (t1 == t2) return;
		t1.sosedi.add(t2);
		t2.sosedi.add(t1);
	}
	
	public void odstraniPovezavo(Tocka t1, Tocka t2) {
		t1.sosedi.remove(t2);
		t2.sosedi.remove(t1);
	}
	
	public void odstraniTocko(Tocka t) {
		for (Tocka v : t.sosedi) odstraniPovezavo(t, v); //Uporabljam funkcijo, da je bolj oèitno, kaj se dogaja. Sicer bi lahko: v.sosedi.remove(t)
		tocke.remove(t.ime);
	}
	
	private Tocka[] dodajTocke(int n) {
		Tocka[] tab = new Tocka[n];
		for (int i = 0; i < n; i++) tab[i] = dodajTocko();
		return tab;
	}
	
	public static Graf prazen(int n) {
		Graf nov = new Graf();
		nov.dodajTocke(n);
		return nov;
	}
	
	public static Graf cikel(int n) {
		Graf graf = new Graf();
		Tocka[] tab = graf.dodajTocke(n);
		for (int i = 0; i < n; i++) {
			graf.dodajPovezavo(tab[i], tab[(i+1) % n]); // Pri (i+1) uporabljamo modulo n, saj nam za števila manjša od n vrne to število, èe sluèajno pridemo do indeksa n, pa nas vrne na 0.
		}
		return graf;
	}
	
	public static Graf poln(int n) {
		Graf graf = new Graf();
		Tocka[] tab = graf.dodajTocke(n);
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				graf.dodajPovezavo(tab[i], tab[j]);
			}	
		}
		return graf;
	}
	
	public static Graf polnDvodelen(int n, int m) {
		Graf graf = new Graf();
		Tocka[] tab1 = graf.dodajTocke(n);
		Tocka[] tab2 = graf.dodajTocke(m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				graf.dodajPovezavo(tab1[i], tab2[j]);
			}	
		}
		return graf;
	}
	
	public void izpis() {
		for (Tocka t : tocke.values()) {
			System.out.print(t + ":");
			for (Tocka v : t.sosedi) {
				System.out.print(" " + v);
			}
			System.out.println();
		}
	}
	
	public void razporedi (double x, double y, double r) {
		int n = tocke.size();
		int i = 0;
		for (Tocka t : tocke.values()) {
			double kot = 2 * i * Math.PI / n;
			t.x = x + r * Math.cos(kot);
			t.y = y + r * Math.sin(kot);
			i++;
		}
	}
	
	
	public void shrani(String ime) {
		try{
			PrintWriter dat = new PrintWriter(new FileWriter(ime));
			for (Tocka t : tocke.values()) {
				dat.println(t + ": " + t.x + " " + t.y);
			}
			dat.println("***");
			for (Tocka t : tocke.values()) {
				dat.print(t + ":");
				for (Tocka u : t.sosedi) {
					
					dat.print(" " + u);
				}
				dat.println();
			}
			dat.close();
		}
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	public static Graf odpri(String ime) {
		Graf graf = new Graf();
		try{
			BufferedReader dat = new BufferedReader(new FileReader(ime));
			
			int blok = 1;
			while (dat.ready()) {
				String vrstica = dat.readLine().trim();
				if (vrstica.equals(" ")) continue;
				if (vrstica.equals("***")) blok = 2;
				else if (blok == 1) {
					String[] podatki = vrstica.split("[ :]+");
					Tocka v = graf.dodajTocko(podatki[0]);
					v.x = Double.parseDouble(podatki[1]);
					v.y = Double.parseDouble(podatki[2]);
				}
				
				else if (blok == 2) {
					String[] podatki = vrstica.split("[ :]+");
					Tocka v = graf.toèka(podatki[0]);
					if (v == null) {
						v = graf.dodajTocko(podatki[0]);
					}
					else {
						for (int i = 1; i < podatki.length; ++i) {
							Tocka u = graf.toèka(podatki[i]);
							if (u == null) u = graf.dodajTocko(podatki[i]);
							graf.dodajPovezavo(v, u);
						}
					}
				}
			}
			
			dat.close();
		}
		
		catch (IOException e) {
			e.printStackTrace();
			return null;
		}
		return graf;
	}
	
}
