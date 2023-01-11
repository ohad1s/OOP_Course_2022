package TA_12_java;

import java.util.ArrayList;
import java.util.List;


public class ShoppingCart {
    List<Item> items;

    public ShoppingCart() {
        this.items = new ArrayList<Item>();
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

    public void removeItem(Item item) {
        this.items.remove(item);
    }

    public int calculateTotal() {
        int sum = 0;
        for (Item item : items) {
            sum += item.getPrice();
        }
        return sum;
    }

    public void payByPaypal(String emailId, String password) {
        int amount = calculateTotal();
        System.out.println(amount + " paid using Paypal.");
    }

    public void payByCreditCard(String name, String cardNumber, String cvv, String dateOfExpiry) {
        int amount = calculateTotal();
        System.out.println(amount + " paid with credit/debit card");
    }

    public static void main(String[]args){
//        מה יקרה כאשר נרצה להוסיף כעת עוד דרך תשלום למשל גוגל פיי? וכו'
//        איך נפתור את הבעיה?
//        אילו עקרונות SOLID באים לידי ביטוי לרעה וכיצד ניתן לפתור אותם?
//
    }
}

