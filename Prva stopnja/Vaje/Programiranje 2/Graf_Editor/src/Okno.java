import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

@SuppressWarnings("serial")
public class Okno extends JFrame implements ActionListener {
	
	Platno platno;
	
	JMenuItem menuOdpri, menuShrani, menuKoncaj;
	JMenuItem menuPrazen, menuCikel, menuPoln, menuPolnDvodelen;
	JMenuItem menuBarvaPovezave, menuBarvaTocke, menuBarvaAktivneTocke, menuBarvaIzbraneTocke, menuBarvaRoba;
	JMenuItem menuDebelinaPovezave, menuDebelinaRoba, menuPolmer;
	
	public Okno() {
		super();
		setTitle("Urejevalnik grafov");
		platno = new Platno(600, 600);
		add(platno);
		
		JMenuBar menubar = new JMenuBar();
		
		JMenu menuDatoteka = new JMenu("Datoteka");
		JMenu menuGraf = new JMenu("Graf");
		JMenu menuNastavitve = new JMenu("Nastavitve");
		
		JMenuItem menuOdpri = new JMenuItem("Odpri ...");
		JMenuItem menuShrani = new JMenuItem("Shrani ...");
		JMenuItem menuKoncaj = new JMenuItem("Koncaj ...");
		
		JMenuItem menuPrazen = new JMenuItem("Prazen ...");
		JMenuItem menuCikel = new JMenuItem("Cikel ...");
		JMenuItem menuPoln = new JMenuItem("Poln ...");
		JMenuItem menuPolnDvodelen = new JMenuItem("Poln Dvodelen ...");
		
		JMenuItem menuBarvaPovezave = new JMenuItem("Barva Povezave ...");
		JMenuItem menuBarvaTocke = new JMenuItem("Barva Tocke ...");
		JMenuItem menuBarvaAktivneTocke = new JMenuItem("Barva Aktivne Tocke ...");
		JMenuItem menuBarvaIzbraneTocke = new JMenuItem("Barva Izbrane Tocke ...");
		JMenuItem menuBarvaRoba = new JMenuItem("Barva Roba ...");
		
		JMenuItem menuDebelinaPovezave = new JMenuItem("Debelina Povezave ...");
		JMenuItem menuDebelinaRoba = new JMenuItem("Debelina Roba ...");
		JMenuItem menuPolmer = new JMenuItem("Polmer toèke ...");
		
		menuDatoteka.add(menuOdpri);
		menuDatoteka.add(menuShrani);
		menuDatoteka.addSeparator();
		menuDatoteka.add(menuKoncaj);
		
		menuGraf.add(menuPrazen);
		menuGraf.add(menuCikel);
		menuGraf.add(menuPoln);
		menuGraf.add(menuPolnDvodelen);
		
		menuNastavitve.add(menuBarvaPovezave);
		menuNastavitve.add(menuBarvaTocke);
		menuNastavitve.add(menuBarvaAktivneTocke);
		menuNastavitve.add(menuBarvaIzbraneTocke);
		menuNastavitve.add(menuBarvaRoba);
		menuNastavitve.addSeparator();
		menuNastavitve.add(menuDebelinaPovezave);
		menuNastavitve.add(menuDebelinaRoba);
		menuNastavitve.addSeparator();
		menuNastavitve.add(menuPolmer);
		
		menubar.add(menuDatoteka);
		menubar.add(menuGraf);
		menubar.add(menuNastavitve);
		
		menuOdpri.addActionListener(this);
		menuShrani.addActionListener(this);
		menuKoncaj.addActionListener(this);
		menuPrazen.addActionListener(this);
		menuCikel.addActionListener(this);
		menuPoln.addActionListener(this);
		menuPolnDvodelen.addActionListener(this);
		menuBarvaPovezave.addActionListener(this);
		menuBarvaTocke.addActionListener(this);
		menuBarvaAktivneTocke.addActionListener(this);
		menuBarvaIzbraneTocke.addActionListener(this);
		menuBarvaRoba.addActionListener(this);
		menuDebelinaPovezave.addActionListener(this);
		menuDebelinaRoba.addActionListener(this);
		menuPolmer.addActionListener(this);
		
		setJMenuBar(menubar);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		if (source == menuOdpri) {
			JFileChooser chooser = new JFileChooser ();
			int gumb = chooser.showOpenDialog(this);
			if (gumb == JFileChooser.APPROVE_OPTION) {
				String ime = chooser.getSelectedFile().getPath(); 
				Graf graf = Graf.odpri(ime);
				platno.narisi(graf);
			}
		}
		else if (source == menuShrani) {
			JFileChooser chooser = new JFileChooser ();
			int gumb = chooser.showOpenDialog(this);
			if (gumb == JFileChooser.APPROVE_OPTION) {
				String ime = chooser.getSelectedFile().getPath(); 
				platno.graf.shrani(ime);
			}
		}
		else if (source == menuKoncaj) {
			
		}
		else if (source == menuPrazen) {
			
		}
		else if (source == menuCikel) {
			
		}
		else if (source == menuPoln) {
			
		}
		else if (source == menuPolnDvodelen) {
			
		}
		else if (source == menuBarvaPovezave) {
			
		}
		else if (source == menuBarvaTocke) {
			
		}
		else if (source == menuBarvaAktivneTocke) {
			
		}
		else if (source == menuBarvaIzbraneTocke) {
			
		}
		else if (source == menuBarvaRoba) {
			
		}
		else if (source == menuDebelinaPovezave) {
			
		}
		else if (source == menuDebelinaRoba) {
			
		}
		else if (source == menuPolmer) {
			
		}
		
	}
}
