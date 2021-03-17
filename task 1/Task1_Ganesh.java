import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

/*
 * Should not use 
 * javax.xml.* or 
 * org.w3c.* or 
 * org.jsoup.* or 
 * java.util.stream.* or 
 * java.util.regex.* or
 * html dom element libraries or
 * Pattern, matcher or any
 * other such libraries 
 * You should find the logic from scratch
 */

public class Task1_Ganesh {

	public static ArrayList<String> arraylist(String s) {

		StringBuffer sb = new StringBuffer(s);
		ArrayList<String> s1 = new ArrayList<String>();

		int i = 0;
		while (true) {
			String d = sb.substring(sb.indexOf("<"), sb.indexOf(">") + 1);
			s1.add(d);
			// s.replace(d," ");
			sb.delete(sb.indexOf("<"), sb.indexOf(">") + 1);
			i++;
			if (sb.length() == 0) {
				break;
			}
		}

		return s1;
	}

	public static int[] oc(int id, String s) {
		int open = 1, close = 0, si = 0, ei = 0;

		ArrayList<String> s1 = arraylist(s);

		for (String z : s1) {
			if (z.contains(String.format("\"%d", id))) {
				if (!z.contains("/>")) {
					si = s1.indexOf(z);
					break;
				}
			}
		}
		// System.out.println(si);

		for (int j = si + 1; true; j++) {
			if (s1.get(j).contains("id") && !s1.get(j).contains("/>")) {
				open += 1;
			}
			if (s1.get(j).contains("</")) {
				close += 1;
			}
			if (open == close) {
				ei += j;
				break;
			}

		}
		// System.out.println(ei);
		int[] arr = { si, ei };
		return arr;

	}

	public static int oc(int id, String s, boolean b) {
		int si = 0;

		ArrayList<String> s1 = arraylist(s);
		if (b) {
			for (String z : s1) {
				if (z.contains(String.format("\"%d", id))) {
					if (z.contains("/>")) {
						si = s1.indexOf(z);
						break;
					}
				}
			}
		}
		return si;
	}

	public static void main(String[] args) throws IOException {

		String givenString = new String(Files.readAllBytes(Paths.get("htmlFile.txt")));
		givenString = givenString.replaceAll("\\t", "");
		givenString = givenString.replaceAll("\\r", "");
		givenString = givenString.replaceAll("\\n", "");

		System.out.println("Given String:");
		System.out.println(givenString);

		System.out.println("\nOutput for append:");
		System.out.println(append(givenString, "6", "<img id=\"appendSample2\" />"));

		System.out.println("\nOutput for prepend:");
		System.out.println(prepend(givenString, "10", "<br id=\"prependSample2\" />"));

		System.out.println("\nOutput for after:");
		System.out.println(after(givenString, "7", "<div id=\"afterSample2\"><div>"));

		System.out.println("\nOutput for before:");
		System.out.println(before(givenString, "13", "<span id=\"beforeSample2\"><span>"));

		// System.out.println(before(givenString,"9","*****"));
	}

	public static String append(String givenString, String id, String stringToAdd) {

		String outputString = "";
		int Id = Integer.valueOf(id);

		ArrayList<String> arrlist = arraylist(givenString);
		int[] arr = oc(Id, givenString);

		int start = arr[0];
		int end = arr[1];

		boolean single = false;

		for (String s : arrlist) {
			if (s.contains(String.format("\"%d", Id)) && s.contains("/>")) {
				single = true;
				outputString += "No Output";
				return outputString;
			}
		}
		if (!single) {
			for (int i = 0; i < arrlist.size(); i++) {
				if (i != end) {
					outputString += arrlist.get(i);
				}
				if (i == end) {
					outputString += stringToAdd;
					outputString += arrlist.get(i);
				}
			}
		}
		return outputString;
	}

	public static String prepend(String givenString, String id, String stringToAdd) {

		String outputString = "";
		int Id = Integer.valueOf(id);

		ArrayList<String> arrlist = arraylist(givenString);
		int[] arr = oc(Id, givenString);

		int start = arr[0];
		int end = arr[1];
		boolean single = false;

		for (String s : arrlist) {
			if (s.contains(String.format("\"%d", Id)) && s.contains("/>")) {
				single = true;
				outputString += "No Output";
				return outputString;

			}
		}

		if (!single) {
			for (int i = 0; i < arrlist.size(); i++) {
				if (i != start) {
					outputString += arrlist.get(i);
				}
				if (i == start) {
					outputString += arrlist.get(i);
					outputString += stringToAdd;
				}
			}
		}
		return outputString;
	}

	public static String after(String givenString, String id, String stringToAdd) {

		String outputString = "";
		int Id = Integer.valueOf(id);

		ArrayList<String> arrlist = arraylist(givenString);

		boolean single = false;

		for (String s : arrlist) {
			if (s.contains(String.format("\"%d", Id)) && s.contains("/>")) {
				single = true;
				break;
			}
		}

		if (single) {
			int index = oc(Id, givenString, single);
			for (int i = 0; i < arrlist.size(); i++) {
				if (i != index) {
					outputString += arrlist.get(i);
				}
				if (i == index) {
					outputString += arrlist.get(i);
					outputString += stringToAdd;
				}
			}
			return outputString;
		} else {
			int[] arr = oc(Id, givenString);

			int end = arr[1];

			for (int i = 0; i < arrlist.size(); i++) {
				if (i != end) {
					outputString += arrlist.get(i);
				}
				if (i == end) {
					outputString += arrlist.get(i);
					outputString += stringToAdd;
				}
			}

			return outputString;
		}
	}

	public static String before(String givenString, String id, String stringToAdd) {

		String outputString = "";
		int Id = Integer.valueOf(id);

		ArrayList<String> arrlist = arraylist(givenString);

		boolean single = false;

		for (String s : arrlist) {
			if (s.contains(String.format("\"%d", Id)) && s.contains("/>")) {
				single = true;
				break;
			}
		}

		if (single) {
			int index = oc(Id, givenString, single);
			for (int i = 0; i < arrlist.size(); i++) {
				if (i != index) {
					outputString += arrlist.get(i);
				}
				if (i == index) {
					outputString += stringToAdd;
					outputString += arrlist.get(i);
				}
			}
			return outputString;
		} else {
			int[] arr = oc(Id, givenString);

			int start = arr[0];

			for (int i = 0; i < arrlist.size(); i++) {
				if (i != start) {
					outputString += arrlist.get(i);
				}
				if (i == start) {
					outputString += stringToAdd;
					outputString += arrlist.get(i);
				}
			}

			return outputString;
		}
	}
}