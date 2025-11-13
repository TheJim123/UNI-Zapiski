import java.util.*;
public class Tocka {

	String ime;
	double x, y;
	Set<Tocka> sosedi;
	static int stevec = 0;
	
	//static Graf g;            Kako bi naredili staticen graf z neko tocko? Uporabimo staticni konstruktor.
	//static {
	//	g = new Graf();
	//	g.dodajTocko();
	//}
	
	public Tocka(String ime) {
		this.ime = ime;
		sosedi = new HashSet<Tocka>();
		x = y = 0;
		++stevec;
	}
	
	public int stopnja() {
		return sosedi.size();
	}
	
	public String toString() {
		return ime;
	}
}
