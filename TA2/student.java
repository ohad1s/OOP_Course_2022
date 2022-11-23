package TA2;

public class student {
    public String first;     // first name
    public String last;      // last name
    public int id;
    public int age;
    public String University;
    public String degree;

    public student(String first, String last, int id, int age, String university, String degree) {
        this.first = first;
        this.last = last;
        this.id = id;
        this.age = age;
        this.University = university;
        this.degree = degree;
    }

    @Override
    public String toString() {
        return "TA2.student-----" +
                "first='" + first + '\'' +
                ", last='" + last + '\'' +
                ", id=" + id +
                ", age=" + age +
                ", University='" + University + '\'' +
                ", degree='" + degree + '\'' +
                "********";
    }
}
