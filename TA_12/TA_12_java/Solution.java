package TA_12_java;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    interface PaymentStrategy {
        public void pay(int amount);
    }

    static class CreditCardStrategy implements PaymentStrategy {
        private String name;
        private String cardNumber;
        private String cvv;
        private String dateOfExpiry;

        public CreditCardStrategy(String nm, String ccNum, String cvv, String expiryDate) {
            this.name = nm;
            this.cardNumber = ccNum;
            this.cvv = cvv;
            this.dateOfExpiry = expiryDate;
        }

        @Override
        public void pay(int amount) {
            System.out.println(amount + " paid with credit/debit card");
        }
    }

    static class PaypalStrategy implements PaymentStrategy {
        private String emailId;
        private String password;

        public PaypalStrategy(String email, String pwd) {
            this.emailId = email;
            this.password = pwd;
        }

        @Override
        public void pay(int amount) {
            System.out.println(amount + " paid using Paypal.");
        }
    }

    static class ShoppingCart2 {
        List<Item> items;

        public ShoppingCart2() {
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

        public void pay(PaymentStrategy paymentMethod) {
            int amount = calculateTotal();
            paymentMethod.pay(amount);
        }
    }

    public static void main(String[] args) {
        ShoppingCart2 cart = new ShoppingCart2();

        Item item1 = new Item("1234",10);
        Item item2 = new Item("5678",40);

        cart.addItem(item1);
        cart.addItem(item2);

        cart.pay(new PaypalStrategy("myemail@example.com", "mypwd"));

        cart.pay(new CreditCardStrategy("Ohad Shirazi", "1234567890123456", "786", "11/23"));

    }
}
