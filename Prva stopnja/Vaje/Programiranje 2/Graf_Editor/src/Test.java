
public class Test {

	public static void main(String[] args) {
		// Komentar zavoljo komentarja
		Graf g = Graf.cikel(66);
		g.razporedi(300, 300, 200);
		g.izpis();
		
		Okno okno = new Okno();
		okno.pack();
		okno.setVisible(true);
		okno.platno.narisi(g);
	}

}