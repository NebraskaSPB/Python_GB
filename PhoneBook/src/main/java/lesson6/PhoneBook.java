package lesson6;

import java.util.*;

public class PhoneBook {

    public static HashMap<String, ArrayList<Integer>> bookPhone = new HashMap<>();
    // Метод, который добавляет номера в книгу
    public static void addNumber(String name, int value, Map<String, ArrayList<Integer>> number){
        if (number.containsKey(name)) {
            number.get(name).add(value);
        } else {
            ArrayList<Integer> list = new ArrayList<>();
            list.add(value);
            number.put(name, list);
        }
    }
    // Метод, который печатает список контактов
    public static void printBook(){
        ArrayList<Map.Entry<String, ArrayList>> list = new ArrayList(bookPhone.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<String, ArrayList>>() {
            @Override
            public int compare(Map.Entry<String, ArrayList> o1, Map.Entry<String, ArrayList> o2) {
                return o2.getValue().size()-o1.getValue().size();
            }
        });
        for (Map.Entry<String, ArrayList> entry: list) {
            System.out.printf("\n" + entry.getKey()+": "+ entry.getValue());
        }
    }
    public static void main(String[] args) {

        addNumber("Ivanov", 123, bookPhone);
        addNumber("Ivanov", 1234, bookPhone);
        addNumber("Petrov", 546585, bookPhone);
        addNumber("Sidorov", 8956477, bookPhone);
        addNumber("Ivanov", 12356233, bookPhone);
        addNumber("Petrov", 787897, bookPhone);

        printBook();
    }
}
