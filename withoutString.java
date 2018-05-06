// codingbat.com/prob/p192570

// https://stackoverflow.com/questions/5054995/how-to-replace-case-insensitive-literal-substrings-in-java?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


public String withoutString(String base, String remove) {
  String pattern = "(?i)" + remove;
  String s = base.replaceAll(pattern, "");
  return s;
}
